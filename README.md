# Investigation of scientific fraud across research topics

This project aims to investigate large-scale the patterns of potential scientific fraud at the level of single topics.

Our starting point is the retrieval bibliometric information on specific research topics from `PubMed`.  Our initial analysis includes the following 4 topics:

* Studies of *Brac2* gene (which is implicated in breast cancer)
* Studies of penumonia using chest imaging
* Studies green synthesis of silver nanoparticles
* Studies of skin wound healing

For each of those research topics, we downloaded blibliometric information of the publications listed in PubMed.  Of particular interest, we obtain title, abstract, journal,
and year of publication. This analysis is conducted using the notebooks titled `process_data.ipynb` included in the topic folder.  On of the steps in the analysis aims to determine
whether the article:

* is a review, 
* is a comment,
* was commented on by another article commented on it,
* had an erratum published,
* has been retracted.

The pre-processing step produces a file titled `articles_clean.json` that is available for further analysis.

Because of the important role played by predatory publishers, the notebook titled `compile_publisher_info.ipynb` uses a search to the NLM catalogue and/or a manual determination 
to assign a publisher to a journal.

Finally, the notebook `publication_patterns_by_topic.ipynb` conducts some simple analysis relating to the relative occurrence of certain characteristics (retracted, review, etc) 
for all articles retrieved in a topic, for all articles published in a given journal, and for all article published by a given publisher. 

The results of the analysis are saved a file named `time_series.png` (for all publications) or in folders named *Journals* and *Publishers* within each of the topic folders.

I have attempted to summarize results for some of those topics is files named `Report_{topic name}.ipynb`.
