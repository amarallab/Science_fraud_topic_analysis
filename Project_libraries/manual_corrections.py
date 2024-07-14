__author__ = "Amaral LAN"
__copyright__ = "Copyright 2024 Amaral LAN"
__credits__ = ["Amaral LAN"]
__version__ = "1.0"
__maintainer__ = "Amaral LAN"
__email__ = "amaral@northwestern.edu"
__status__ = "Production"


#########################################################################
def brca2( articles ):
    """
    Manual corrections for brca2 articles.
    """
    i = 265
    articles[i]['abstract'] = 'Breast conservation surgery is safe in selected women when combined with adjuvant therapy'
    articles[i]['other_ids'] = 'DOI: 10.1136/bmj.39114.354248.80 PMCID: PMC1808129 PMID: 17332541 [Indexed for MEDLINE]'

    i = 364
    articles[i]['other_ids'] = 'DOI: 10.7705/biomedica.5663 PMCID: PMC8768485 PMID: 34936260 [Indexed for MEDLINE]'

    i = 442
    articles[i]['abstract'] = 'Breast surgeons recommend against the procedure unless cancer risk is increased.'
    articles[i]['other_ids'] = 'DOI: 10.1097/01.NAJ.0000505576.27516.9d PMID: 27787313 [Indexed for MEDLINE]'

    i = 1662
    articles[i]['abstract'] = 'A collaborative assessment of options and trade-offs-perhaps using visual decision aids-can help.'
    articles[i]['other_ids'] = 'PMID: 32555753 [Indexed for MEDLINE]'

    i = 2453
    articles[i]['other_ids'] = 'PMID: 25191729 [Indexed for MEDLINE]'

    i = 4116
    articles[i]['other_ids'] = 'DOI: 10.33145/2304-8336-2019-24-455-464 PMID: 31841487 [Indexed for MEDLINE]'

    i = 5952
    articles[i]['other_ids'] = 'PMID: 26695891'
    
    i = 6389
    articles[i]['other_ids'] = 'DOI: 10.1001/jamanetworkopen.2021.7728 PMCID: PMC8105747 PMID: 33961040 [Indexed for MEDLINE]'

    i = 6567
    articles[i]['other_ids'] = 'DOI: 10.1038/sj.onc.1209153 PMID: 16205630 [Indexed for MEDLINE]'

    i = 6627
    articles[i]['abstract'] = 'Clinical genomics is poised for a rapid expansion but more work must be done to build a supporting ethical infrastructure.'
    articles[i]['other_ids'] = 'DOI: 10.1371/journal.pbio.1001663 PMCID: PMC3782420 PMID: 24086107 [Indexed for MEDLINE]'

    i = 6628
    articles[i]['comment'] = articles[i]['comment'].replace('Juni', 'Jun')

    i = 7382
    articles[i]['date'] = articles[i]['date'].replace('Juni', 'Jun')
    articles[i]['comment'] = articles[i]['comment'].replace('Juni', 'Jun')

    i = 6875
    articles[i]['abstract'] = 'A lupus causing anti-DNA antibody penetrates living cells and targets DNA repair for therapeutic advantage in human cancer cells.'
    articles[i]['other_ids'] = 'DOI: 10.1126/scitranslmed.3004955 PMID: 23100623 [Indexed for MEDLINE]'

    i = 7033
    articles[i]['abstract'] = "A report of the Keystone Symposium 'DNA Replication and Recombination' held in Keystone, USA, 27 February to 4 March 2011."
    articles[i]['copyright'] = '© 2011 BioMed Central Ltd'
    articles[i]['other_ids'] = 'DOI: 10.1186/gb-2011-12-4-304 PMCID: PMC3218856 PMID: 21554750 [Indexed for MEDLINE]'

    i = 7576
    articles[i]['other_ids'] = 'DOI: 10.1024/1661-8157/a001489 PMID: 24280604 [Indexed for MEDLINE]' 
    
    i = 8248
    articles[i]['abstract'] = '[Image: see text]'
    articles[i]['other_ids'] = 'DOI: 10.15252/embr.201744508 PMCID: PMC5494498 PMID: 28673926'

    i = 10152

    articles[i]['copyright'] = '(c) 2002 Elsevier Science (USA).'
    articles[i]['other_ids'] = 'DOI: 10.1006/gyno.2002.6615 PMID: 11972384 [Indexed for MEDLINE]'
    
    i = 11037
    articles[i]['comment'] = 'Republished in Maturitas. 2008 Sep-Oct;61(1-2):203-13; discussion 213.'
    articles[i]['abstract'] = ( 'In North America and Northern Europe, breast cancer incidence rates begin' +
    ' increasing in the early reproductive years and continue climbing into the late' +
    ' seventies, whereas rates plateau after menopause in japan and less developed' +
    ' countries. Female gender, age and country of birth are the strongest' +
    ' determinants of disease risk. Family history and mutations in the BRCA1 and' +
    ' BRCA2 genes are important correlates of lifetime risk. Genetic polymorphisms' +
    ' associated with estrogen synthesis and metabolism are currently under study.' +
    ' Atypical hyperplasia and molecular alterations in benign breast lesions appear' +
    ' to be involved in the pathogenesis of invasive carcinoma. In postmenopausal' +
    ' women, increased breast density on mammograms increases risk. Bone density and' +
    ' breast cancer are associated, presumably through the mechanism of endogenous' +
    ' estrogen levels. Serum estrogen levels are higher in breast cancer cases than' +
    ' controls. Many established risk factors for breast cancer may function through' +
    ' and endocrine mechanism. Current use of oral contraceptives and prolonged,' +
    ' current or recent use of hormone replacement therapy moderately increase risk.' +
    ' Tamoxifen and possibly other selective estrogen receptor modulators reduce' +
    ' breast cancer risk in high risk women. Relationships between various dietary' +
    ' micro and macronutrients and breast cancer have been suggested but require' +
    ' evaluation in clinical trials. Whereas alcohol consumption is associated with' +
    ' increased risk, most environmental factors, including polychlorinated compounds' +
    ' and electromagnetic fields, are not.' +
    ' CONCLUSION: Breast cancer etiology is becoming clearer through the study of' +
    ' molecular alterations in germline and somatic cell genes, and the interaction of' +
    ' these genes with steroid hormones and relevant growth factors. This knowledge' +
    ' should be useful for breast cancer prevention.' )
    articles[i]['other_ids'] = 'DOI: 10.1016/s0378-5122(00)00196-1 PMID: 11311599 [Indexed for MEDLINE]'

    i = 11178
    articles[i]['abstract'] = 'A case study in the kinds of problems to expect from this increasingly popular marketing tactic.'
    articles[i]['other_ids'] = 'PMCID: PMC4809519 PMID: 11478123 [Indexed for MEDLINE]'
    
    i = 11377
    articles[i]['comment'] = 'Republished in Maturitas. 2008 Sep-Oct;61(1-2):141-50.'
    articles[i]['abstract'] = ('Cancer is a genetic disease. Breast cancer tumorigenesis can be described as a' +
    ' multi-step process in which each step is thought to correlate with one or more' +
    ' distinct mutations in major regulatory genes. The question addressed is how far' +
    ' a multi-step progression model for sporadic breast cancer would differ from that' +
    ' for hereditary breast cancer. Hereditary breast cancer is characterized by an' +
    ' inherited susceptibility to breast cancer on basis of an identified germline' +
    ' mutation in one allele of a high penetrance susceptibility gene (such as BRCA1,' +
    ' BRCA2, CHEK 2, TP53 or PTEN). Inactivation of the second allele of these tumour' +
    ' suppressor genes would be an early event in this oncogenic pathway (Knudsons' +
    ' "two-hit" model). Sporadic breast cancers result from a serial stepwise' +
    ' accumulation of acquired and uncorrected mutations in somatic genes, without any' +
    ' germline mutation playing a role. Mutational activation of oncogenes, often' +
    ' coupled with non-mutational inactivation of tumour suppressor genes, is probably' +
    ' an early event in sporadic tumours, followed by more, independent mutations in' +
    ' at least four or five other genes, the chronological order of which is likely' +
    ' less important. Oncogenes that have been reported to play an early role in' +
    ' sporadic breast cancer are MYC, CCND1 (Cyclin D1) and ERBB2 (HER2/neu). In' +
    ' sporadic breast cancer, mutational inactivation of BRCA1/2 is rare, as' +
    ' inactivation requires both gene copies to be mutated or totally deleted.' +
    ' However, non-mutational functional suppression could result from various' +
    ' mechanisms, such as hypermethylation of the BRCA1 promoter or binding of BRCA2' +
    ' by EMSY. In sporadic breast tumorigenesis, at least three different' +
    ' pathway-specific mechanisms of tumour progression are recognizable, with breast' +
    ' carcinogenesis being different in ductal versus lobular carcinoma, and in well' +
    ' differentiated versus poorly differentiated ductal cancers. Thus, different' +
    ' breast cancer pathways emerge early in the process of carcinogenesis, ultimately' +
    ' leading to clinically different tumour types. As mutations acquired early during' +
    ' tumorigenesis will be present in all later stages, large-scale gene expression' +
    ' profiling using DNA microarray analysis techniques can help to classify breast' +
    ' cancers into clinically relevant subtypes.')
    articles[i]['other_ids'] = 'DOI: 10.1016/j.maturitas.2004.06.005 PMID: 15351094 [Indexed for MEDLINE]'

    i = 11751
    articles[i]['copyright'] = '(c) 2002 Elsevier Science (USA).'
    articles[i]['other_ids'] = 'DOI: 10.1016/s0006-291x(02)00624-1 PMID: 12083779 [Indexed for MEDLINE]'
    
    i = 11911
    articles[i]['copyright'] = 'International Cancer Imaging Society.'
    articles[i]['other_ids'] = 'DOI: 10.1102/1470-7330.2005.0040 PMCID: PMC1665313 PMID: 16361123 [Indexed for MEDLINE]'

    return


#########################################################################
def chest_imaging( articles ):
    """
    Manual corrections for chest imaging pneumonia articles.
    """
    i = 20
    articles[i]['abstract'] = 'Online supplemental material is available for this article.'
    articles[i]['other_ids'] = 'DOI: 10.1148/radiol.212902 PMCID: PMC9131172 PMID: 34935512 [Indexed for MEDLINE]'
    
    i = 132
    articles[i]['copyright'] = 'Sociedad Argentina de Pediatría.'
    articles[i]['other_ids'] = 'DOI: 10.5546/aap.2022.eng.e246 PMID: 36374061 [Indexed for MEDLINE]'

    i = 703
    articles[i]['copyright'] = None
    articles[i]['other_ids'] = 'DOI: 10.1024/1661-8157/a001437 PMID: 24129296 [Indexed for MEDLINE]'

    i = 857
    articles[i]['comment'] = 'Republished in Intensive Crit Care Nurs. 2003 Feb;19(1):41, 42.'
    articles[i]['other_ids'] = 'PMID: 12592773 [Indexed for MEDLINE]'

    i = 862
    articles[i]['copyright'] = '(c) 2023 The authors; licensee World Health Organization.'
    articles[i]['other_ids'] = 'DOI: 10.2471/BLT.22.288801 PMCID: PMC9948502 PMID: 36865598 [Indexed for MEDLINE]'

    i = 1914
    articles[i]['copyright'] = 'Croatian Society of Medical Biochemistry and Laboratory Medicine.'
    articles[i]['other_ids'] = 'DOI: 10.11613/BM.2020.030402 PMCID: PMC7394256 PMID: 32774118 [Indexed for MEDLINE]'

    i = 1916
    articles[i]['other_ids'] = 'DOI: 10.1024/1661-8157/a001680 PMID: 24894612 [Indexed for MEDLINE]'

    i = 2111
    articles[i]['other_ids'] = 'DOI: 10.36660/abc.20200724 PMCID: PMC8528369 PMID: 34231797 [Indexed for MEDLINE]'

    i = 2524
    articles[i]['abstract'] = 'Chest CT is not a suitable screening tool to rule out COVID-19 in children https://bit.ly/2SBGzQm. \n It is difficult to identify children infected with coronavirus disease 2019 (COVID-19) who have little or no respiratory symptoms. For routine clinical care in different circumstances, it is relevant to assess the COVID-19 status of patients. Routine PCR is recognised as the gold standard but can be falsely negative due to sampling errors. For diagnosing and monitoring adult COVID-19 patients, characteristic radiological lesions have been recognised [1, 2] and to assess the possibility of COVID-19 infection in adults scheduled for surgery in whom a PCR test is negative or missing, a non-enhanced chest computed tomography (CT) scan has been proposed as an option in the Netherlands [3] because: 1) patients may be pre-symptomatic in the incubation period of COVID-19 infection and subsequently develop symptoms post-operatively, implying a greater risk for adverse post-operative outcomes; and 2) patients may be asymptomatic or mildly symptomatic carriers and shedders of COVID-19, and place hospital workers and other patients at risk.'
    articles[i]['other_ids'] = 'DOI: 10.1183/13993003.01241-2020 PMCID: PMC7236836 PMID: 32398302 [Indexed for MEDLINE]'

    i = 2266
    articles[i]['copyright'] = 'Sociedad Argentina de Investigación Odontológica.'
    articles[i]['other_ids'] = 'DOI: 10.5546/aap.2019.e150 PMID: 30869495 [Indexed for MEDLINE]'

    i = 3082
    articles[i]['other_ids'] = 'DOI: 10.2471/BLT.09.068239 PMCID: PMC2814482 PMID: 20428371 [Indexed for MEDLINE]'

    i = 3537
    articles[i]['copyright'] = 'Revista de la Facultad de Ciencias Médicas de Córdoba'
    articles[i]['other_ids'] = 'DOI: 10.31053/1853.0605.v75.n4.20356 PMID: 30734710 [Indexed for MEDLINE]'

    i = 3998
    articles[i]['abstract'] = '[Image: see text]'
    articles[i]['other_ids'] = 'DOI: 10.1111/eci.13908 PMCID: PMC10078553 PMID: 36377261 [Indexed for MEDLINE]'

    i = 4284
    articles[i]['abstract'] = 'Schulze-Hagen M, Hübel C, Meier-Schroers M, et al. Low-dose chest CT for the diagnosis of COVID-19. Dtsch Arztebl Int. 2020;117:389-95. 32762834.'
    articles[i]['other_ids'] = 'DOI: 10.7326/ACPJ202012150-068 PMID: 33316180 [Indexed for MEDLINE]'

    i = 4377
    articles[i]['copyright'] = 'Thieme. All rights reserved.'
    articles[i]['other_ids'] = 'DOI: 10.1055/a-1740-4310 PMID: 35211925 [Indexed for MEDLINE]'

    i = 4398
    articles[i]['other_ids'] = 'DOI: 10.36660/abc.20220287 PMCID: PMC9833213 PMID: 36629604 [Indexed for MEDLINE]'

    i = 4419
    articles[i]['other_ids'] = 'DOI: 10.36660/abc.20220642 PMCID: PMC10263399 PMID: 37255182 [Indexed for MEDLINE]'

    i = 5405
    articles[i]['abstract'] += ( ' ' + 'Update of Cochrane Database Syst Rev. 2020 Sep 30;9:CD013639.'
                             + 'BACKGROUND: The respiratory illness caused by SARS-CoV-2 infection continues to present diagnostic challenges. Early research showed thoracic (chest) imaging to ' )
    articles[i]['other_ids'] = 'DOI: 10.1002/14651858.CD013639.pub3 PMID: 33242342 [Indexed for MEDLINE]'

    i = 5522
    articles[i]['other_ids'] = 'DOI: 10.1024/1661-8157/a001606 PMID: 24686759 [Indexed for MEDLINE]'

    i = 5541
    articles[i]['other_ids'] = 'DOI: 10.1161/CIRCIMAGING.121.013661 PMCID: PMC8772050 PMID: 34961327 [Indexed for MEDLINE]'

    i = 5561
    articles[i]['copyright'] = 'Sestre Milosrdnice University Hospital.'
    articles[i]['other_ids'] = 'DOI: 10.20471/acc.2022.61.04.21 PMCID: PMC10588378 PMID: 37868166 [Indexed for MEDLINE]'

    i = 5608
    articles[i]['abstract'] += 'Update of Cochrane Database Syst Rev. 2020 Nov 26;11:CD013639.\n BACKGROUND: The respiratory illness caused by SARS-CoV-2 infection continues to present diagnostic challenges. Our 2020 edition of this review showed thoracic...'
    articles[i]['copyright'] = 'Copyright © 2021 The Authors. Cochrane Database of Systematic Reviews published by John Wiley & Sons, Ltd. on behalf of The Cochrane Collaboration.'
    articles[i]['other_ids'] = 'DOI: 10.1002/14651858.CD013639.pub4 PMCID: PMC8078565 PMID: 33724443 [Indexed for MEDLINE]'

    i = 5611
    articles[i]['other_ids'] = 'DOI: 10.1148/radiol.2020203776 PMCID: PMC7903987 PMID: 33399508 [Indexed for MEDLINE]'

    i = 5930
    articles[i]['other_ids'] = 'DOI: 10.1590/1984-0462/;2019;37;1;00009 PMCID: PMC6362377 PMID: 30183802 [Indexed for MEDLINE]'

    i = 6265
    articles[i]['other_ids'] = 'DOI: 10.26633/RPSP.2022.20 PMCID: PMC8942285 PMID: 35350452'

    i = 7235
    articles[i]['abstract'] = 'This article discusses the importance and essentials of clinical evaluation and keys to an accurate diagnosis of interstitial lung disease.'
    articles[i]['other_ids'] = 'DOI: 10.1016/j.ccm.2004.05.007 PMID: 15331183 [Indexed for MEDLINE]'

    i = 7371
    articles[i]['other_ids'] = 'DOI: 10.1177/000992280504400905 PMID: 16327964 [Indexed for MEDLINE]'

    i = 7607
    articles[i]['other_ids'] = 'DOI: 10.26633/RPSP.2020.59 PMCID: PMC7241574 PMID: 32454808'

    i = 7653
    articles[i]['copyright'] = 'Sociedad Argentina de Pediatría.'
    articles[i]['other_ids'] = 'DOI: 10.5546/aap.2018.e455 PMID: 29756723 [Indexed for MEDLINE]'
    
    return


#########################################################################
def deep_learning( articles ):
    """
    Manual corrections for deep learning tumor articles.
    """
    i = 117
    articles[i]['abstract'] = '5 TECHNICAL EFFICACY: Stage 1 J. Magn. Reson. Imaging 2020;52:1237-1238.'
    articles[i]['copyright'] = '© 2020 International Society for Magnetic Resonance in Medicine.'
    articles[i]['other_ids'] = 'DOI: 10.1002/jmri.27131 PMID: 32154967 [Indexed for MEDLINE]'

    i = 417
    articles[i]['abstract'] = 'Dataset use reported in doi: 10.1038/s41591-018-0156-x.\nCurrently, approximately 150 different brain tumour types are defined by the WHO. Recent endeavours to exploit machine learning and deep learning methods for supporting more precise diagnostics based on the histological tumour appearance have been hampered by the relative paucity of accessible digital histopathological datasets. While freely available datasets are relatively common in many medical specialties such as radiology and genomic medicine, there is still an unmet need regarding histopathological data. Thus, we digitized a significant portion of a large dedicated brain tumour bank based at the Division of Neuropathology and Neurochemistry of the Medical University of Vienna, covering brain tumour cases from 1995-2019. A total of 3,115 slides of 126 brain tumour types (including 47 control tissue slides) have been scanned. Additionally, complementary clinical annotations have been collected for each case. In the present manuscript, we thoroughly discuss this unique dataset and make it publicly available for potential use cases in machine learning and digital image analysis, teaching and as a reference for external validation.'
    articles[i]['copyright'] = '© 2022. The Author(s).'
    articles[i]['other_ids'] = 'DOI: 10.1038/s41597-022-01157-0 PMCID: PMC8847577 PMID: 35169150 [Indexed for MEDLINE]'
    
    i = 1134
    articles[i]['comment'] = articles[i]['authors']
    articles[i]['authors'] = '[No authors listed]'
    articles[i]['abstract'] = 'Algorithms matching the performance of expert pathologists in prostate cancer diagnosis were designed.'
    articles[i]['copyright'] = '©2020 American Association for Cancer Research.'
    articles[i]['other_ids'] = 'DOI: 10.1158/2159-8290.CD-RW2020-012 PMID: 31953243 [Indexed for MEDLINE]'

    i = 2280
    articles[i]['comment'] = 'Comment in Neuro Oncol. 2020 Mar 5;22(3):311-312.'
    articles[i]['abstract'] = 'BACKGROUND: Isocitrate dehydrogenase (IDH) mutation status has emerged as an important prognostic marker in gliomas. Currently, reliable IDH mutation determination requires invasive surgical procedures. The purpose of this study was to develop a highly accurate, MRI-based, voxelwise deep-learning IDH classification network using T2-weighted (T2w) MR images and compare its performance to a multicontrast network.\nMETHODS: Multiparametric brain MRI data and corresponding genomic information were obtained for 214 subjects (94 IDH-mutated, 120 IDH wild-type) from The Cancer Imaging Archive and The Cancer Genome Atlas. Two separate networks were developed, including a T2w image-only network (T2-net) and a multicontrast (T2w, fluid attenuated inversion recovery, and T1 postcontrast) network (TS-net) to perform IDH classification and simultaneous single label tumor segmentation. The networks were trained using 3D Dense-UNets. Three-fold cross-validation was performed to generalize the networks performance. Receiver operating characteristic analysis was also performed. Dice scores were computed to determine tumor segmentation accuracy.\nRESULTS: T2-net demonstrated a mean cross-validation accuracy of 97.14% ± 0.04 in predicting IDH mutation status, with a sensitivity of 0.97 ± 0.03, specificity of 0.98 ± 0.01, and an area under the curve (AUC) of 0.98 ± 0.01. TS-net achieved a mean cross-validation accuracy of 97.12% ± 0.09, with a sensitivity of 0.98 ± 0.02, specificity of 0.97 ± 0.001, and an AUC of 0.99 ± 0.01. The mean whole tumor segmentation Dice scores were 0.85 ± 0.009 for T2-net and 0.89 ± 0.006 for TS-net.\nCONCLUSION: We demonstrate high IDH classification accuracy using only T2-weighted MR images. This represents an important milestone toward clinical translation.'
    articles[i]['copyright'] = '© The Author(s) 2019. Published by Oxford University Press on behalf of the Society for Neuro-Oncology. All rights reserved. For permissions, please e-mail: journals.permissions@oup.com.'
    articles[i]['other_ids'] = 'DOI: 10.1093/neuonc/noz199 PMCID: PMC7442388 PMID: 31637430 [Indexed for MEDLINE]'
     
    i = 3711
    articles[i]['other_ids'] = 'DOI: 10.1631/jzus.B2300363 PMCID: PMC10758209 PMID: 38163668 [Indexed for MEDLINE]'

    i = 4727
    articles[i]['copyright'] = '(2018) COPYRIGHT Society of Photo-Optical Instrumentation Engineers (SPIE).'
    articles[i]['other_ids'] = 'DOI: 10.1117/1.JBO.23.6.066002 PMID: 29900705 [Indexed for MEDLINE]'

    i = 4953
    articles[i]['copyright'] = '(2017) COPYRIGHT Society of Photo-Optical Instrumentation Engineers (SPIE).'
    articles[i]['other_ids'] = 'DOI: 10.1117/1.JBO.22.10.106017 PMCID: PMC5661703 PMID: 29086544 [Indexed for MEDLINE]'

    i = 5244
    articles[i]['copyright'] = '© 2023 The Authors. Veterinary Dermatology published by John Wiley & Sons Ltd on behalf of ESVD and ACVD.'
    articles[i]['other_ids'] = 'DOI: 10.1111/vde.13221 PMID: 38057947 [Indexed for MEDLINE]'
    
    
    i = 6093
    articles[i]['copyright'] = None
    articles[i]['other_ids'] = 'DOI: 10.11817/j.issn.1672-7347.2021.200999 PMCID: PMC10930230 PMID: 34911846 [Indexed for MEDLINE]'
    
    i = 6490
    articles[i]['copyright'] = '© 2023. The Author(s).'
    articles[i]['other_ids'] = 'DOI: 10.1186/s12911-023-02404-z PMCID: PMC10759705 PMID: 38166852 [Indexed for MEDLINE]'
    
    i = 6495
    articles[i]['copyright'] = None
    articles[i]['other_ids'] = 'DOI: 10.11817/j.issn.1672-7347.2022.210645 PMCID: PMC10950116 PMID: 36097766 [Indexed for MEDLINE]'

    i = 7756
    articles[i]['copyright'] = None
    articles[i]['other_ids'] = 'DOI: 10.11817/j.issn.1672-7347.2022.220101 PMCID: PMC10950118 PMID: 36097773 [Indexed for MEDLINE]'

    i = 9188
    articles[i]['abstract'] = articles[i]['other_ids'] + '\nAutomatic segmentation of vestibular schwannomas (VS) from magnetic resonance imaging (MRI) could significantly improve clinical workflow and assist patient management. We have previously developed a novel artificial intelligence framework based on a 2.5D convolutional neural network achieving excellent results equivalent to those achieved by an independent human annotator. Here, we provide the first publicly-available annotated imaging dataset of VS by releasing the data and annotations used in our prior work. This collection contains a labelled dataset of 484 MR images collected on 242 consecutive patients with a VS undergoing Gamma Knife Stereotactic Radiosurgery at a single institution. Data includes all segmentations and contours used in treatment planning and details of the administered dose. Implementation of our automated segmentation algorithm uses MONAI, a freely-available open-source framework for deep learning in healthcare imaging. These data will facilitate the development and validation of automated segmentation frameworks for VS and may also be used to develop other multi-modal algorithmic models.'
    articles[i]['copyright'] = '© 2021. The Author(s).'
    articles[i]['other_ids'] = 'DOI: 10.1038/s41597-021-01064-w PMCID: PMC8553833 PMID: 34711849 [Indexed for MEDLINE]'
        
    i = 9523
    articles[i]['abstract'] = articles[i]['other_ids']
    articles[i]['other_ids'] = 'DOI: 10.3390/cancers15082237 PMCID: PMC10136532 PMID: 37190334'
    
    return
    
    
#########################################################################
def green_synthesis( articles ):
    """
    Manual corrections for green synthesis of silver nanoparticles articles.
    """
    i = 2116
    articles[i]['abstract'] = '[Formula: see text].'
    articles[i]['other_ids'] = 'DOI: 10.1177/15347346221133627 PMID: 36325727'

    return


#########################################################################
def rnai_cancer( articles ):
    """
    Manual corrections for skind wound healing articles.
    """
    i = 105
    articles[i]['other_ids'] = 'DOI: 10.1038/sj.gt.3302694 PMID: 16341059 [Indexed for MEDLINE]'

    i = 136
    articles[i]['other_ids'] = 'DOI: 10.3779/j.issn.1009-3419.2013.02.08 PMCID: PMC6000388 PMID: 23425903 [Indexed for MEDLINE]'

    i = 2106
    articles[i]['other_ids'] = 'DOI: 10.1111/j.1349-7006.2006.00174.x PMID: 16630124 [Indexed for MEDLINE]'

    i = 3477
    articles[i]['other_ids'] = 'DOI: 10.1038/sj.onc.1209153 PMID: 16205630 [Indexed for MEDLINE]'
    
    i = 3671
    articles[i]['copyright'] = articles[i]['other_ids']   
    articles[i]['other_ids'] = 'DOI: 10.1002/jmv.20466 PMID: 16173017 [Indexed for MEDLINE]'
    
    i = 4311
    articles[i]['copyright'] = articles[i]['other_ids']   
    articles[i]['other_ids'] = 'DOI: 10.1016/j.canlet.2009.04.014 PMID: 19457608 [Indexed for MEDLINE]'
    
    i = 4742
    articles[i]['other_ids'] = 'DOI: 10.1038/sj.onc.1208852 PMID: 16170380 [Indexed for MEDLINE]'
     
    i = 5243
    articles[i]['comment'] = articles[i]['other_ids']  
    articles[i]['abstract'] = '1. RNA interference (RNAi) is a robust method of post-transcriptional silencing of genes using double-stranded RNA (dsRNA) with sequence homology driven specificity. The dsRNA can be between 21 and 23 nucleotides long: this is converted to small interfering RNA (siRNA), which then mediates gene silencing by degradation/blocking of translation of the target mRNA. 2. RNA interference provides a simple, fast and cost-effective alternative to existing gene targeting approaches both in vitro and in vivo. The discovery of siRNAs that cause RNAi in mammalian cells opened the door to the therapeutic use of siRNAs. Highly intense research efforts are now aimed at developing siRNAs for therapeutic purposes. 3. Recent advances in the design and delivery of targeting molecules now allow efficient and highly specific gene silencing in mammalian systems. Synthetic siRNA libraries targeting thousands of mammalian genes are publicly available for high-throughput genetic screens for target discovery and validation. Recent studies have demonstrated the clinical potential of aptly designed siRNAs in various types of viral infections, cancer and renal and neurodegenerative disorders. 4. The present review provides insight into the novel therapeutic strategies of siRNA technology, which is the latest development in nucleic acid-based tools for knocking down gene expression, and its potential for silencing genes associated with various human diseases.'
    articles[i]['other_ids'] = 'DOI: 10.1111/j.1440-1681.2006.04399.x PMID: 16700886 [Indexed for MEDLINE]'
    
    i = 5255
    articles[i]['abstract'] = articles[i]['other_ids']   
    articles[i]['other_ids'] = 'DOI: 10.1186/gb-2004-5-9-342 PMCID: PMC522865 PMID: 15345042 [Indexed for MEDLINE]'
    
    i = 5304
    articles[i]['copyright'] = articles[i]['other_ids']   
    articles[i]['other_ids'] = 'DOI: 10.1073/pnas.1702370114 PMCID: PMC5692527 PMID: 29078269 [Indexed for MEDLINE]'
    
    i = 6233
    articles[i]['other_ids'] = 'DOI: 10.1177/2472555219883621 PMCID: PMC7036479 PMID: 31658850 [Indexed for MEDLINE]'
    
    i = 6262
    articles[i]['copyright'] = articles[i]['other_ids']   
    articles[i]['other_ids'] = 'DOI: 10.1089/1043034041648462 PMID: 15319038 [Indexed for MEDLINE]'
    
    i = 6287
    articles[i]['copyright'] = articles[i]['other_ids']   
    articles[i]['other_ids'] = 'DOI: 10.1073/pnas.1711310114 PMCID: PMC5676921 PMID: 29078358 [Indexed for MEDLINE]'
    
    return
    
#########################################################################
def wound_healing( articles ):
    """
    Manual corrections for skind wound healing articles.
    """
    i = 402
    articles[i]['abstract'] = 'A correction to this article has been published and is linked from the HTML and PDF versions of this paper. The error has not been fixed in the paper.'
    articles[i]['other_ids'] = 'DOI: 10.1038/s41598-018-33558-w PMCID: PMC6198006 PMID: 30349056'

    i = 599
    articles[i]['abstract'] = 'Wound healing is a complex biological process [...].'
    articles[i]['other_ids'] = 'DOI: 10.3390/pharmaceutics14061291 PMCID: PMC9231209 PMID: 35745862'
    
    i = 606
    articles[i]['abstract'] = 'The authors are sorry to report that some of the HPLC data reported in their recently published paper [...]..'
    articles[i]['other_ids'] = 'DOI: 10.3390/ijms20174178 PMCID: PMC6747146 PMID: 31454990'
    
    i = 702
    articles[i]['abstract'] = articles[i]['comment']
    articles[i]['comment'] = None
    
    i = 2121
    articles[i]['other_ids'] = 'DOI: 10.1631/jzus.B2200447 PMCID: PMC10264175 PMID: 37309042 [Indexed for MEDLINE]'
    
    return
