# Investigation of scientific fraud across research topics

This project aims to investigate large-scale the patterns of potential scientific fraud at the level of single topics.

Our starting point is the retrieval bibliometric information on specific research topics from `PubMed`. Each topic is associated with a data folder in the repo.  

For each of those research topics, we downloaded blibliometric information of the publications listed in PubMed.  Of particular interest, we obtain title, abstract, journal,
and year of publication. This analysis is conducted using the notebook titled `process_data.ipynb` and the functions for manual correction developed for each topic.  On of the steps in the analysis aims to determine
whether the article:

* is a review, 
* is a comment,
* was commented on by another article commented on it,
* had an erratum published,
* has been retracted.

The pre-processing step produces a file titled `articles_clean.json` that is available for further analysis.

The notebook titled `compile_publisher_info.ipynb` uses a search to the NLM catalogue and/or a manual determination 
to assign a publisher to a journal.

Finally, the notebook `publication_patterns_by_topic.ipynb` conducts some simple analysis relating to the relative occurrence of certain characteristics (retracted, review, etc) 
for all articles retrieved in a topic, for all articles published in a given journal, and for all article published by a given publisher. 

The results of the analysis are saved a file named `time_series.png` (for all publications) or in folders named *Journals* and *Publishers* within each of the topic folders.

The results for some of those topics iare summarized in files named `Report_{topic name}.ipynb`.
