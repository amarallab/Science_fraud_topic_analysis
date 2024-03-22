__author__ = "Amaral LAN"
__copyright__ = "Copyright 2024, Amaral LAN"
__credits__ = ["Amaral LAN"]
__version__ = "1.0"
__maintainer__ = "Amaral LAN"
__email__ = "amaral@northwestern.edu"
__status__ = "Production"

#########################################################################
import requests
import re

import pandas as pd

from collections import Counter
from bs4 import BeautifulSoup
from datetime import datetime
from numpy import arange, array, isnan, nan
from string import whitespace, punctuation

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep

from Project_libraries.my_stats import ( half_frame, place_commas )


#########################################################################
def get_articles_start_line( abstracts_files ):
    """
    This file takes a list of Posix Paths to data files and 
    returns a list of integers with start line of the 
    individual articles and a list of lines from the files.
    
    inputs:
        abstracts_files -- list of Posic Paths
    
    returns:
        articles_start -- list of int
        data -- list of str
    """
    data = []
    file_switches = []
    for data_file in abstracts_files:
        with open(data_file, 'r', encoding = 'utf-8') as f_abs:
            data.extend( f_abs.readlines() )
            data.extend( ['\n']*2 )
            print(f"Finished reading {place_commas(len(data))} lines.")
            file_switches.append( len(data) )

    # Identify starting line of each article
    #
    pattern = '\d{1,4}[.] '

    articles_start = []
    k0 = 0
    k = 0
    while True:

        # Account for restart of potential_index at new file
        if k == file_switches[0]:
            file_switches.pop(0)
            k0 = len( articles_start )

        # Start of record  
        #
        potential_match = re.match(pattern, data[k])
        if potential_match:
            potential_index = int( data[k][potential_match.start(): 
                                           potential_match.end()-2] ) + k0


            if potential_index - 1 == len(articles_start):
#                 if not potential_index % 100: print(potential_index)
                articles_start.append( k )

        k += 1
        if k == len(data):
            break

    print(f"\n----> There are {place_commas(len(articles_start))} articles listed in file.\n\n" )

    # Need to add last line of file so all articles are checked later
    articles_start.append( len(data) )
    
    return (articles_start, data)


#########################################################################
def count_articles_by_journal( articles, n ):
    """
    Takes a set of articles and returns a list with the n most common 
    journals in the set.
    
    inpouts:
        articles -- list of dict
        n -- int
        
    returns:
        counter.most_common -- list
    
    """
    journals = []
    for article in articles:
        journals.append( article['journal'] )
        
    counter = Counter(journals)
    
    return counter.most_common( n )


#########################################################################
def get_articles_by_publisher( articles, publisher ):
    """
    Takes a list of articles and a publisher name and returns a list 
    with the subset of articles from that publisher.
    
    inpouts:
        articles -- list of dict
        publisher -- str
        
    returns:
        new_articles -- list of dict
    
    """    
    new_articles = []
    for article in articles:
        if article['publisher'] == publisher:
            new_articles.append( article )

    return new_articles


#########################################################################
def search_for_journal_match( browser, journal, match_url ):
    """
    This function takes a soup object that returned a list of 
    journals instead of info on a specific journal and tries to 
    identify the url to the correct webpage.
    
    inputs:
        browser -- selenium webdriver object
        journal -- str 
        match_url -- str with url of NLM page
        
    returns:
        table -- soup item 
        
    """
    browser.get(match_url)            
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # Find number of items and pages
    final_item = soup.find('h3', {'class': 'result_count left'})
    if final_item is None:
        return None
    
    final_page = soup.find('h3', {'class': 'page'})
    if final_page is None:
        final_page = 1
    else:
        final_page = int( final_page.text.split()[-1] )
        
    print(f"There are {final_page} pages of results.\n")
    if final_page > 10:
        print('Too many pages of results.\n')
        return None

    for page in range(final_page):
        print(f"-----------{page}-----------")
        pane = soup.find('div', {'class': 'content'})
        results = list(pane.children)[9]

        # Search single page
        #
        for i, item in enumerate( results.children ):
            if not item.text.strip():
                return None 

            title = item.find('p', {'class': 'title'})
            title = title.text
            aux = item.find('span', {'class': 'nlmcat_aux_title'})
            if aux is None:
                continue

            # This is how many items are in the soup before the one I want <- This may fail!!!
            title_abbrev = aux.next.next
            title_abbrev = title_abbrev.text
            
            # Compare title to journal name
            if title_abbrev == journal:   
                nlm_id = item.find('div', {'class': 'aux'}).text
                match_url = ( 'https://www.ncbi.nlm.nih.gov/nlmcatalog/' + 
                              nlm_id.lstrip('NLM ID: ').rstrip('[Serial]').strip() )

                soup = BeautifulSoup(requests.get(match_url).text, 'html.parser')
                table = soup.find('dl', {'class': 'nlmcat_dl'})

                return table

        # If you reach here, the search in the page failed
        #
        if final_page > 1 and (page + 2) <= final_page:
            elem = browser.find_element(By.ID, 'pageno')
            elem.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + str(page + 2) + Keys.ENTER)
            sleep(4)

            browser.refresh() 
            soup = BeautifulSoup(browser.page_source, 'html.parser')
        
    return None


#########################################################################
def classify_articles( articles, label ):
    """
    This function takes a list of articles and classifies them into 
    four non-exclusive categories
    
    inputs:
        label -- str to add info to printout
        articles -- list of dict
        
    returns:
        no_abstract_articles -- list of dict 
        retracted_articles -- list of dict
        erratum_articles -- list of dict
        commented_articles -- list of dict
        
    """
    retracted_articles = []
    erratum_articles = []
    commented_articles = []
    no_abstract_articles = []
    
    for article in articles:
        if not article['abstract']:
            no_abstract_articles.append(article)

        if article['retraction']:
            retracted_articles.append(article)

        if article['erratum']:
            erratum_articles.append(article)

        if article['comment'] and 'Received comment! ' == article['comment'][:18]:
            commented_articles.append(article)

    print(f"There are {len(articles)} articles in the {label} set; "
          f"{len(no_abstract_articles)} have no abstract; \n"
          f"{len(retracted_articles)} have been retracted; "
          f"{len(erratum_articles)} have had errata published; and \n"
          f"{len(commented_articles)} have had comments written about them.\n\n")

    return ( no_abstract_articles, retracted_articles, erratum_articles,
             commented_articles )


#########################################################################
def extract_publication_date( article ):
    """
    This funnction takes a dictionary as an input with information
    about an article and returns a datetime object with a publication 
    date if both 'year' and 'date' keys are present. Otherwise it
    returns None.
    
    inputs:
        article -- dict
        
    returns:
        date_focus -- datetime.date object
        
    """
    if 'date' not in article.keys():
        return None
    
    my_date = article['date'].replace(' - ', '-')
    
    if '-' in my_date:
        my_date = my_date.split('-')[0]
        
    if my_date.strip().lower() in ['spring', 'summer', 'fall', 'autumn', 'winter']:
        my_date = ''
    
    str_focus = ' '.join([str(article['year']), my_date.strip()]).strip()
    print(str_focus, type(str_focus), len(str_focus) )
    
    if len(my_date) == 0:
        date_focus = datetime.strptime(str_focus, '%Y')
    elif len(my_date.split()) == 2:
        date_focus = datetime.strptime(str_focus, '%Y %b %d')
    elif len(my_date.split()) == 1:
        date_focus = datetime.strptime(str_focus, '%Y %b')
    
    return date_focus
    
    
#########################################################################
def concatenate_lines(info):
    """
    Concatenates lines that are not empty and removes empty lines.
    
    inputs:
        info -- list of str
        
    returns:
        new_info -- list of str
        
    """
    k = 0
    new_info = []
    while k < len(info) and info[k]:
        if info[k] != '\n':
            if info[k][:5] == '[This':
                new_info[-1] += ' ' + info[k].strip()
            else:
                new_info.append(info[k].strip())
            
            k += 1
            while k < len(info) and info[k] != '\n':
                new_info[-1] += ' ' + info[k].strip()
                k += 1
            
        k += 1
#         if k == len(info):
#             break
            
    return new_info


#########################################################################
def consensus_publisher(publisher1, publisher2, publisher3):
    """
    This function takes 3 strings with potential publisher assignments
    in order to a final publisher assignment. It considers different
    possibilities in decreasing order of trust. 
    
    inputs:
        publisher1 -- str
        publisher2 -- str
        publisher4 -- str
       
    returns:
        publisher -- str
    """
    publisher = None
#     print(publisher1, publisher2, publisher3)

    if publisher1:
        publisher = publisher1
        
    if publisher2 and not publisher:
        publisher = publisher2
        
    if publisher3 and not publisher:
        publisher = publisher3
    
    return publisher



#########################################################################
def get_time_series(df, year0, year1):
    """
    """
    if df.empty:
        return array( [nan]*(year1-year0) )
    
    n_papers = []
    for i in range(year0, year1):
        n_papers.append( len( df[df.year == i] ) )

    return array(n_papers)    


#########################################################################
def plot_time_series(ax, df, key, delta, label, color, band_color):
    """
    
    """
    if 'ratio' in key:
        ylabel = 'Percentage'
        mean = 100 * df[key].rolling(delta, min_periods = 1, center = True).mean()
        sem = 100 * df[key].rolling(delta, min_periods = 1, center = True).sem()
        my_text = f"{label}"
        my_fontsize = 20
        my_factor = 3.5

    elif 'Case' == label[:4]:
        ylabel = 'Publications'
        mean = df[key].rolling(delta, min_periods = 1, center = True).mean()
        sem = df[key].rolling(delta, min_periods = 1, center = True).sem()
        my_text = f"Topic: {label[5:].title()}"
        my_fontsize = 20
        my_factor = 3.5
        
    else:
        ylabel = 'Publications'
        mean = df[key].rolling(delta, min_periods = 1, center = True).mean()
        sem = df[key].rolling(delta, min_periods = 1, center = True).sem()
        my_text = f"{label}"
        my_fontsize = 18
        my_factor = 3.1
        
     
    step = sem.iloc[mean.idxmax()]
    if isnan(step):
        step = 0

    ymax = mean.max() + step

    half_frame(ax, 'Year', ylabel, font_size = 15)    
    ax.plot(df.Year, mean, color, lw = 3)
    
    ax.fill_between( df.Year,
                     mean - 1.0 * sem,
                     mean + 1. * sem,
                     color = band_color, zorder = 1 )
    
    ax.set_xlim( df.Year.min(), df.Year.max()+1 )
    ax.set_xticks(arange(df.Year.min(), df.Year.max()+1, 4))
    ax.set_ylim(0, ymax)
    
    # Guide lines
    n = len( str( int(ymax) ) )
    ystep = 10**(n-2) * int( ymax / (4. * 10**(n-2)) + 0.5 )
    if ystep == 0:
        ystep = 0.1
    ax.set_yticks(arange(0, 5*ystep, ystep))
    ax.hlines( arange(0, 5*ystep, ystep), df.Year.min(), df.Year.max()+1, '0.2',
               zorder = -10 )
    
    # Text
    ax.text( df.Year.min() + 1, my_factor*ystep, my_text, fontsize = my_fontsize, 
             color = color, zorder = 2 )
    
    return


#########################################################################
def get_article_data(info):
    """
    
    """
    # Now get article metadata
    #
    article = {}
    flag = None
    info = concatenate_lines( info )
    
    # Check that it is not retracted article
    #
    article['retraction'] = None
    aux = info[0].split('.')
    if aux[1].strip() == 'RETRACTED ARTICLE':
        print( f"-----> {info.pop(0)}\n" )
        info[0] = '. '.join([aux[0], info[0]])  # Create standard first line      
        flag = 'retracted'
    
    # Typical first line
    #  _index_. _Journal_. _Date_; _volume_(_issue_):_article_. doi: _doi_
    #
    # Attention: doi might not exist!!
    #
    aux = info[0].split('.')
    article['journal'] = aux[1].strip()
    date_string =  aux[2].split(';')[0].strip()
    article['year'] = int( date_string[:4] )
    article['date'] = date_string[4:]

    # Check for volume and pages:
    if ';' in info[0]:
        aux = info[0].split(';')[1].split(':')
        article['volume'] = aux[0]
        article['pages'] = aux[1].split('.')[0]
    else:
        article['volume'] = None
        article['pages'] = None
    
    # Check for doi
    if len(aux) > 2:
        article['doi'] = aux[2].split()[0].strip('.')
    else:
        article['doi'] = None

    # Check for title
    article['title'] = info[1].strip(whitespace)
    if info[2][0] == '[':
        article['title'] += ' ' + info.pop(2)
        
    # Check that is not publication announcing retraction
    if 'retraction' == article['title'][:10].lower():
        article['retraction'] = 'Retraction Notice: '
        flag = 'retraction notice'
        
    # check for Erratum or authors
    if 'Erratum' in info[2]:
        info.insert(2, 'Authors')
        article['authors'] = None
    else:
        article['authors'] = info[2].strip(whitespace + '.')
        
        if 'Collaborators:' == info[3][:14]:
            article['authors'] += '. ' + info.pop(3).strip(whitespace)
        
    # Check for affiliations
    if 'Author information:' == info[3][:19]:
        article['affiliations'] = info[3].strip(punctuation + whitespace)
    else: 
        info.insert(3, 'Author information:')
        article['affiliations'] = None

    # Check for Erratum info
    if 'erratum' in info[4].lower():
        article['erratum'] = info.pop(4).strip(whitespace)
    else:
        article['erratum'] = None
        
    if 'This corrects the article' in info[4]:
        article['erratum'] += ' ' + info.pop(4).strip(whitespace)
    elif 'An amendment to this paper' in info[4]:
        article['erratum'] += ' ' + info.pop(4).strip(whitespace)
    elif 'A Correction to this paper' in info[4]:
        article['erratum'] += ' ' + info.pop(4).strip(whitespace)
    elif 'After publication of the original article' in info[4]:
        article['erratum'] += ' ' + info.pop(4).strip(whitespace)
    elif 'The original version of this article' in info[4]:
        article['erratum'] += ' ' + info.pop(4).strip(whitespace)
    elif 'In the original publication of the article' in info[4]:
        article['erratum'] += ' ' + info.pop(4).strip(whitespace)
        
    # Check for Comment info
    if 'Original report in' in info[4]:
        article['comment'] = info.pop(4).strip(whitespace) + ' '
    else:
        article['comment'] = ''
        
    # Look for comment in beginning of string, so you do not look for
    # it in abstract -- It will not take care of all cases!!!
    if 'comment ' in info[4][:150].lower():
        article['comment'] += info.pop(4).strip(whitespace)
        
        if 'comment ' in info[4][:200].lower():
            article['comment'] += ' ' + info.pop(4).strip(whitespace)
    elif article['comment'] == '':
        article['comment'] = None

    # Check for Retraction or Expression of concern info
    if 'Expression of concern in' in info[4]:
        if article['retraction']:
            article['retraction'] += ' ' + info.pop(4).strip(whitespace)
        else:
            article['retraction'] = info.pop(4).strip(whitespace)
            flag = 'retracted'
        
    if 'Retraction in' in info[4]:
        if article['retraction']:
            article['retraction'] += ' ' + info.pop(4).strip(whitespace)
        else:
            article['retraction'] = info.pop(4).strip(whitespace)
            flag = 'retracted'
    
    if 'Retraction of' in info[4]: 
        if article['retraction']:
            article['retraction'] += info.pop(4).strip(whitespace)
        else:
            article['retraction'] = 'Retraction Notice: ' + info.pop(4).strip(whitespace)
            flag = 'retraction notice'

    # Check for abstract
    if 'Republished from' in info[4]:
        return None, None
    
    article['abstract'] = ''
    if 'Update of' in info[4]:
        article['abstract'] += info.pop(4).strip(whitespace) + ' '
    if 'Update in' in info[4]:
        article['abstract'] += info.pop(4).strip(whitespace) + ' '
    
    if info[:4] != 'DOI:' and len(info[4]) > 150:
        article['abstract'] += info[4].strip(whitespace)  
    else:
        info.insert(4, 'Abstract:')
        article['abstract'] += ''
        
    if 'Plain Language Summary:' in info[5]:
        article['abstract'] += ' ' + info.pop(5).strip(whitespace)
        if 'Summary for patients'  in info[5]:
            article['abstract'] += ' ' + info.pop(5).strip(whitespace)
            
    elif 'Summary for patients'  in info[5]:
        article['abstract'] += ' ' + info.pop(5).strip(whitespace)
        if 'Plain Language Summary:' in info[5]:
            article['abstract'] += ' ' + info.pop(5).strip(whitespace)
        
    # Check for copyright
    if ( '©' in info[5] or 'Copyright' in info[5]  
         or 'All rights reserved' in info[5] 
         or 'Published by' in info[5] 
         or 'Verlag KG' in info[5] 
         or 'Wiley-Liss, Inc.' in info[5] 
         or 'John Wiley & Sons' in info[5] 
         or 'Wiley Periodicals, Inc' in info[5]
         or 'wileyonlinelibrary.com/journal/jgc4' in info[5]
         or 'Thieme' in info[5] 
         or 'Thieme Medical Publishers' in info[5] 
         or '(Cancer Epidemiol Biomarkers Prev' in info[5]
         or 'American Cancer Society' in info[5] 
         or 'Massachusetts Medical Society' in info[5]
         or 'BMJ Publishing Group Ltd' in info[5]
         or 'Celsius' in info[5]
         or 'Karger AG' in info[5] 
         or 'APA' in info[5] 
         or 'RSNA' in info[5]
         or 'AACR' in info[5] 
         or 'Multimed Inc' in info[5]
         or 'in the public domain' in info[5]
         or 'Creative Commons Attribution' in info[5]
         or 'Radiological Society of North America, Inc' in info[5]
         or 'American Institute of Chemical Engineers Biotechnol' in info[5] 
         or 'American Academy of Family Physicians'  in info[5] ):
        article['copyright'] = info[5].strip(punctuation + whitespace)
        article['other_ids'] = info[6]
        m = 6
    else:
        article['copyright'] = None
        article['other_ids'] = info[5]
        m = 5
        
    # Check for error due to abstract in foreign language
    if article['other_ids'][:10] == 'Publisher:' or len(article['other_ids']) > 300:
        if article['abstract']:
            article['abstract'] += ' ' + article['other_ids']
        else:
            article['abstract'] = article['other_ids']
            
        if ( '©' in info[m+1] or 'Copyright' in info[m+1]  
             or 'All rights reserved' in info[m+1] 
             or 'Published by' in info[m+1] 
             or 'Verlag KG' in info[m+1] 
             or 'Wiley-Liss, Inc.' in info[m+1] 
             or 'John Wiley & Sons' in info[m+1] 
             or 'Wiley Periodicals, Inc' in info[m+1]
             or 'wileyonlinelibrary.com/journal/jgc4' in info[m+1]
             or 'Thieme' in info[m+1]
             or 'Thieme Medical Publishers' in info[m+1]
             or '(Cancer Epidemiol Biomarkers Prev' in info[m+1]
             or 'American Cancer Society' in info[m+1]
             or 'Massachusetts Medical Society' in info[m+1]
             or 'BMJ Publishing Group Ltd' in info[m+1]
             or 'Celsius' in info[m+1]
             or 'Karger AG' in info[m+1] 
             or 'APA' in info[m+1]
             or 'RSNA' in info[m+1]
             or 'AACR' in info[m+1]
             or 'Multimed Inc' in info[m+1]
             or 'in the public domain' in info[m+1]
             or 'Creative Commons Attribution License' in info[m+1]
             or 'Radiological Society of North America, Inc' in info[m+1]
             or 'American Institute of Chemical Engineers Biotechnol' in info[m+1] 
             or 'American Academy of Family Physicians'  in info[m+1] ):
            article['copyright'] = info[m+1].strip(punctuation + whitespace)
            article['other_ids'] = info[m+2]
        else:
            article['copyright'] = None
            article['other_ids'] = info[m+1]

    if article['abstract'] == '':
        article['abstract'] = None
    
    return flag, article


#########################################################################
def manual_assignment_of_publisher( journal ):
    """
    This function takes a string with a NLM journal title abbreviations
    and matches to a curated list of publishers. Returns None if no match 
    is found.
    
    inputs:
        journal -- str
        
    returns:
        publisher -- str or None
    """
    publisher = None
    
    if journal in ['Science']: 
        publisher = 'AAAS'
        
    elif journal in ['Cancer Prev Res (Phila)']: 
        publisher = 'American Association for Cancer Research'
    
    elif journal in ['J Immunol']:
        publisher = 'American Association of Immunologists'
        
    elif journal in ['Gene', 'Lancet', 'Methods', 'Nanomedicine', 
                     'Talanta', 'Toxicology', 'Urology', 'Vaccine']: 
        publisher = 'Elsevier'
        
    elif journal in ['Front Endocrinol (Lausanne)', 'Front Med (Lausanne)']:
        publisher = 'Frontiers'
        
    elif journal in ['Clin Sci (Lond)', 'Nanomedicine (Lond)', 'Womens Health (Lond)']:
        publisher = 'Future Science Group'
                
    elif journal in ['Aging (Albany NY)']: 
        publisher = 'Impact Journals'
                    
    elif journal in ['Intern Med']:
        publisher = 'Japanese Society of Internal Medicine'
    
    elif journal in ['Oncology (Williston Park)']: 
        publisher = 'Karger'
        
    elif journal in ['Adv Wound Care (New Rochelle)']:
        publisher = 'Mary Ann Liebert'

    elif journal in ['Biomolecules', 'Life (Basel)']:
        publisher = 'MDPI'             
        
    elif journal in ['G3 (Bethesda)']:
        publisher = 'Oxford University Press'

    elif journal in ['Cancer']: 
        publisher = 'Wiley'

    elif journal in ['Medicine (Baltimore)']:
        publisher = 'Wolters Kluwer'
    
    return publisher


#########################################################################
def assign_publisher( line ):
    """
    This function takes a string and search for a match in order to guess
    the publisher of the journal
    
    inputs:
        line -- str
        
    returns:
        publisher -- str
    """
    if line is None:
        return None
    elif type(line) != str:
        return None
    elif not line.strip():
        return None
    
    if 'Academia Brasileira De Ciencias' in line:
        publisher = 'Academia Brasileira De Ciencias'
        
    elif 'American Academy of Family Physicians' in line:
        publisher = 'American Academy of Family Physicians'
    
    elif 'American Academy of Forensic Sciences' in line:
        publisher = 'American Academy of Forensic Sciences'
        
    elif ( 'American Association for the Advancement of Science' in line
           or 'AAAS' in line ):
        publisher = 'AAAS'
        
    elif 'American Association for Anatomy' in line:
        publisher = 'American Association for Anatomy'
        
    elif 'American Association for Cancer Research' in line:
        publisher = 'American Association for Cancer Research'
        
    elif 'American Association of Immunologists' in line:
        publisher = 'The American Association of Immunologists'
        
    elif 'American Association for Laboratory Animal Science' in line:
        publisher = 'American Association for Laboratory Animal Science'
        
    elif ( 'American Chemical Society' in line or 'ACS' in line
           or 'Easton, Pa. [etc.]' in line ):
        publisher = 'American Chemical Society'
        
    elif 'American College of Physicians' in line:
        publisher = 'American College of Physicians'
        
    elif ( 'American Institute of Chemical Engineers' in line 
           or 'AICHE' in line ):
        publisher = 'American Institute of Chemical Engineers'
    
    elif ( 'College of American Pathologists' in line
           or 'American Medical Ass' in line):
        publisher = 'American Medical Association'
        
    elif ( 'American Medical Informatics Association' in line
            or 'AMIA' in line ):
        publisher = 'American Medical Informatics Association'
        
    elif 'American Medical Pub' in line:
        publisher = 'American Medical Pub'
        
    elif ( 'American Physical Society' in line
           or 'Society for Applied Spectroscopy' in line
           or 'Optical Society of America' in line
           or 'AVS' in line or 'American Vacuum Society' in line 
           or 'American Institute of Physics' in line 
           or 'Melville, NY : AIP Publishing' in line ):
        publisher = 'AIP Publ'
          
    elif 'American Physiological Society' in line:
        publisher = 'American Physiological Society'
        
    elif 'American Public Health Association' in line:
        publisher = 'American Public Health Association'
        
    elif 'American Scientific Publishers' in line or 'ASP' in line:
        publisher = 'American Scientific Publishers'
        
    elif 'American Society of Clinical Oncology' in line:
        publisher = 'American Society of Clinical Oncology'
        
    elif 'American Society of Hematology' in line:
        publisher = 'American Society of Hematology'
        
    elif 'American Society for Microbiology' in line:
        publisher = 'American Society for Microbiology'
        
    elif 'American Society of Photobiology' in line:
        publisher = 'American Society of Photobiology'
        
    elif 'American Statistical Association' in line:
        publisher = 'American Statistical Association'
    
    elif 'American Veterinary Medical Ass' in line:
        publisher = 'American Veterinary Medical Ass'

    elif ( 'AME Publishing Company' in line or 
           'Pioneer Bioscience' in line ):
        publisher = 'AME Publishing'
        
    elif 'Annual Reviews' in line:
        publisher = 'Annual Reviews'
        
    elif 'Baishideng Pub' in line:
        publisher = 'Baishideng Publishing Group'

# B
    elif 'Bentham' in line:
        publisher = 'Bentham'
        
    elif ( 'Biochemical Society' in line
           or 'Portland Press' in line ):
        publisher = 'Biochemical Society'
        
    elif 'Bio-protocol LLC' in line:
        publisher = 'Bio-protocol'
        
    elif 'Brill Academic' in line or 'VSP' in line:
        publisher = 'Brill Academic Publ' 
        
    elif 'British Institute of Radiology' in line:
        publisher = 'British Institute of Radiology'
        
    elif ( 'British Medical Journal' in line 
           or 'Published by BMJ' in line
           or 'BMJ Publishing Group' in line
           or 'British Medical Ass' in line ):
        publisher = 'British Medical Association'
        
    elif 'British Pharmacological Society' in line:
        publisher = 'British Pharmacological Society'

# C
    elif 'Cambridge University Press' in line:
        publisher = 'Cambridge University Press'
        
    elif 'Canadian Medical Ass' in line:
        publisher = 'Canadian Medical Association'
    
    elif 'Cell Press' in line:
        publisher = 'Cell Press'
        
    elif 'Science China Press' in line:
        publisher = 'Chinese Academy of Sciences'

    elif 'Chinese Anti-Cancer Ass' in line:
        publisher = 'Chinese Anti-Cancer Association'
        
    elif ( 'Chinese Medical Ass' in line or 
           'Zhongguo yi xue ke xue yuan' in line ):
        publisher = 'Chinese Medical Association'
          
    elif ( 'Cold Spring Harbor Laboratory Press' in line or 
           'CSHL Press' in line ):
        publisher = 'Cold Spring Harbor Laboratory Press'
        
    elif 'Company of Biologists' in line:
        publisher = 'Company of Biologists'
        
    elif ( 'Croatian Academy Of Medical Sciences' in line or
           'Hrvatska akademija medicinskih znanosti' in line ):
        publisher = 'Croatian Academy Of Medical Sciences'

    elif ( 'CRC' in line 
           or 'Routledge' in line
           or 'Chapman & Hall' in line
           or 'Chapman and Hall' in line
           or 'Dekker' in line ):
        publisher = 'CRC Press'

# D
    elif 'Dō Gakkai' in line or 'do gakkai' in line.lower():
        publisher = 'Do Gakkai'
        
    elif ( 'De Gruyter' in line 
           or 'de Gruyter' in line
           or 'Berkeley Electronic Press' in line
           or 'Versita' in line 
           or 'Birkhäuser' in line 
           or 'Birkhauser' in line ):
        publisher = 'De Gruyter'

# E
    elif 'e-Century Pub' in line:
        publisher = 'e-Century Pub'
        
    elif 'eLife Sciences Pub' in line:
        publisher = 'eLife Sciences Pub'
        
    elif ( 'Elsevier' in line 
           or 'Applied Science Publishers' in line 
           or 'Masson' in line 
           or 'Bristol, Eng., Wright' in line
           or 'Orlando : Academic Press' in line
           or 'Orlando Fl : Academic Press' in line
           or 'Urban & Fischer Verlag' in line
           or 'New York, Academic Press' in line
           or 'New York: Academic Press' in line
           or 'New York, Ny : Academic Press' in line
           or 'New York, London, Academic Press' in line 
           or 'London : Current Biology' in line 
           or 'Polish Society for Biology of Reproduction' in line 
           or 'Pergamon Press' in line
           or 'North-Holland Pub' in line ):
        publisher = 'Elsevier'
        
    elif 'European Academy of Dermatology and Venereology' in line:
        publisher = 'European Academy of Dermatology and Venereology'
        
# F
    elif ( 'FASEB' in line or 
           'Federation of American Societies for Experimental Biology' in line ):
        publisher = 'FASEB'

    elif 'Federation of European Biochemical Societies' in line:
        publisher = 'Federation of European Biochemical Societies'
        
    elif 'Frontiers' in line:
        publisher = 'Frontiers'
    
    elif ( 'Future Science' in line or 'Future Medicine' in line ):
        publisher = 'Future Science'
        
# H
    elif ( 'Hindawi' in line 
           or 'Pulsus Group' in line 
           or 'Austin, TX  : Landes Bioscience' in line ):
        publisher = 'Hindawi'
    
# I 
    elif 'Impact Journals' in line:
        publisher = 'Impact Journals'
        
    elif 'IMR Press' in line:
        publisher = 'IMR Press'
        
    elif 'IOP Pub' in line or 'Institute of Physics Pub' in line:
        publisher = 'IOP Publishing'
        
    elif 'IOS Press' in line:
        publisher = 'IOS Press'
        
    elif ( 'Institute of Electrical and Electronics Engineers' in line
           or 'IEEE' in line ):
        publisher = 'IEEE'
        
    elif ( 'International Association of Physical Chemists' in line 
            or 'IAPC' in line ):
        publisher = 'International Association of Physical Chemists'
        
    elif 'International Federation for Cell Biology' in line:
        publisher = 'International Federation for Cell Biology'
        
    elif 'International Institute of Anticancer Research' in line:
        publisher = 'International Institute of Anticancer Research'
        
    elif 'International Scientific Literature' in line:
        publisher = 'International Scientific Literature'
        
    elif 'International Society of Dermatology' in line:
        publisher = 'International Society of Dermatology'
    
    elif 'International Society on Thrombosis and Haemostasis' in line:
        publisher = 'International Society on Thrombosis and Haemostasis'
        
# J
    elif 'Japan Endocrine Society' in line:
        publisher = 'Japan Endocrine Society'
        
    elif 'Japanese Society of Developmental Biologists' in line:
        publisher = 'Japanese Society of Developmental Biologists'
    
# K
    elif 'Karger' in line:
        publisher = 'Karger'
     
    elif 'Korean Association of Anatomists' in line:
        publisher = 'Korean Association of Anatomists'
        
    elif 'Korean Association of Hepato-Biliary-Pancreatic Surgery' in line:
        publisher = 'Korean Association of Hepato-Biliary-Pancreatic Surgery'
       
    elif 'Korean Breast Cancer Society' in line:
        publisher = 'Korean Breast Cancer Society'
        
    elif 'Korean Dermatological Association' in line:
        publisher = 'Korean Dermatological Association'

    elif 'Korean Diabetes Association' in line:
        publisher = 'Korean Diabetes Association'
        
    elif 'Korean Society of Developmental Biology' in line:
        publisher = 'Korean Society of Developmental Biology'

    elif 'Korean Society for Laboratory Medicine' in line:
        publisher = 'Korean Society for Laboratory Medicine'
        
    elif 'Korean Surgical Society' in line:
        publisher = 'Korean Surgical Society'

# L
    elif 'Lancet' in line:
        publisher = 'Lancet'
# M
    elif 'Mary Ann Liebert' in line or 'M.A. Liebert' in line:
        publisher = 'Mary Ann Liebert'
        
    elif ('Izdatelstvo Meditsina' in line
           or 'Meditsina' in line ):
        publisher = 'Meditsina'
        
    elif ( 'Molecular Diversity Preservation International' in line
           or 'MDPI' in line
           or 'Caister Academic Press' in line ):
        publisher = 'MDPI'

# N
    elif ( 'National Academy of Sciences' in line):
        publisher = 'National Academy of Sciences'
        
    elif 'National Research Council of Canada' in line:
        publisher = 'National Research Council of Canada'

# O
    elif 'OMICS Pub' in line:
        publisher = 'OMICS'

    elif ( 'Orlando, FL : Academic Press' in line
           or 'AOAC International' in line
           or 'Oxford University Press' in line ):
        publisher = 'Oxford University Press'

# P
    elif 'Pharmaceutical Society of Korea' in line:
        publisher = 'Pharmaceutical Society of Korea'
        
    elif 'Pharmaceutical Society of Japan' in line:
        publisher = 'Pharmaceutical Society of Japan'
        
    elif ( 'plos' in line.lower() 
           or 'Public Library of Science' in line ):
        publisher = 'PLoS'      
     
    elif 'Polski Towarzystwo Farmaceutyczne' in line:
        publisher = 'Polski Towarzystwo Farmaceutyczne'
        
    elif ( 'Princeton Scientific Pub' in line
           or 'Princeton University Press' in line):
        publisher = 'Princeton University Press'
    
# R
    elif 'Royal Australian College of General Practitioners' in line:
        publisher = 'Royal Australian College of General Practitioners'
        
    elif 'Royal College of Surgeons of England' in line:
        publisher = 'Royal College of Surgeons of England'
    
    elif ( 'Royal Pharmaceutical Society' in line ):# or 'RPS' in line:
        publisher = 'Royal Pharmaceutical Society'
        
    elif 'Royal Society Pub' in line:
        publisher = 'Royal Society'
          
    elif 'Royal Society of Chemistry' in line or 'RSC' in line:
        publisher = 'Royal Society of Chemistry'

# S
    elif ( 'Sage' in line
           or 'SAGE' in line
           or 'Natural Product Communications' in line 
           or 'Bangalore : Phcog.Net' in line ):
        publisher = 'Sage'

    elif 'Shared Science Publishers' in line:
        publisher = 'Shared Science Publ'
        
    elif 'Slovenian Chemical Society' in line:
        publisher = 'Slovenian Chemical Society'
        
    elif ( 'Slovak Academic Press' in line
           or 'Slovenská akadémia vied' in line ):
        publisher = 'Slovak Academic Press'
        
    elif ( 'Society for Endocrinology' in line
           or 'BioScientifica' in line 
           or 'Bioscientifica' in line ):
        publisher = 'Society for Endocrinology'
        
    elif 'Spandidos' in line:
        publisher = 'Spandidos'
        
    elif ( 'International Society for Optical Engineering' in line 
           or 'SPIE' in line ):
        publisher = 'SPIE'
        
    elif ( 'Demos Medical Publishing' in line ):
        publisher = 'Springer Publishing Company'
          
    elif ( 'Springer-Verlag' in line 
           or 'Springer Verlag' in line 
           or 'Springer Science' in line
           or 'Springer Wien' in line
           or 'Springer India' in line
           or 'Springer Netherlands' in line
           or 'Heidelberg : Springer' in line
           or 'Springer Singapore' in line
           or 'New York : Springer' in line
           or 'New York, NY : Springer' in line
           or 'New York, NY. : Springer' in line 
           or 'Barcelona, Spain : Springer' in line
           or 'Springer Berlin' in line
           or 'SpringerPlus' in line 
           or 'Springer Nature' in line
           or 'Springer International' in line 
           or 'Berlin : Springer' in line
           or 'BertelsmannSpringer' in line
           or 'Current Medicine Group' in line
           or 'ADIS' in line or 'Adis' in line
           or 'Kluwer Academic' in line
           or 'Humana Press' in line
           or 'Plenum Press' in line
           or 'Cureus' in line
           or 'Steinkopff' in line 
           or 'Tissue Culture Association' in line
           or ('Dordrecht' in line and 'Springer' in line)
           or ('Dordrecht' in line and 'Boston' in line and 'Reidel' in line)
           or 'Nature Pub' in line 
           or 'BMC' in line or 'BioMed Central' in line 
           or 'Biomed Central' in line ):
        publisher = 'Springer Nature'

# T
    elif ( 'Taylor & Francis' in line 
           or 'Taylor and Francis' in line 
           or 'Informa Healthcare' in line 
           or 'Swets & Zeitlinger' in line
           or 'dove medical press' in line.lower()
           or 'dove press' in line.lower() ):
        publisher = 'Taylor & Francis'
        
    elif ( 'Termedia Pub' in line 
          or 'Termedia & Banach' in line ):
        publisher = 'Termedia'
        
    elif 'Thieme' in line:
        publisher = 'Thieme Group'
    
# U
    elif 'United States and Canadian Academy of Pathology' in line:
        publisher = 'United States and Canadian Academy of Pathology'

# V
    elif 'Verduci' in line:
        publisher = 'Verduci'
    
# W
    elif ( 'Wiley' in line or 'WILEY' in line 
           or 'VCH' in line
           or 'San Diego : Academic Press' in line
           or 'Alexandria, VA : The Federation' in line 
           or 'International Union of Biochemistry and Molecular Biology' in line
           or 'Blackwell' in line 
           or 'Berlin : Akademie-Verlag' in line ):
        publisher = 'Wiley'
          
    elif 'Wound Healing Society' in line:
        publisher = 'Wound Healing Society'
          
    elif ( 'Wolters Kluwer' in line
           or 'Lippincott' in  line 
           or 'Williams & Wilkins' in line
           or 'Medknow Pub' in line ):
        publisher = 'Wolters Kluwer'

# Z
    elif ('Zhonghua yi xue hui' in line or 'zhonghua yixuehui' in line.lower()):
        publisher = 'Zhonghua yi xue hui'

        
    else:
        publisher = None
        
    return publisher

