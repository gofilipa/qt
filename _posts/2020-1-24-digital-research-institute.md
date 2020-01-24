---
layout: post
title: Data & Abstraction, reflections from GCDRI
categories: [methods, text-analysis, distant reading] 
--- 


The past few days we have been running our annual [Digital Research
Institute](https://gcdri.commons.gc.cuny.edu/) at the Graduate Center
Digital Initiatives. I've taught three sessions of python, and
supported sessions on Text Analysis, as well as helping out in Command
Line, Git/Github, and attended Mapping.

What I've found, or realized once again, is how much my approach
toward data and method informs my interest in DH. 

As I watched the Text Analysis workshop unfold, the most striking
realization was the preconceptions and biases we bring into our
inferences. We might make certain assumptions about the analysis in
Natural Language Toolkit's (NLTK) `similar()` method, which measures
what words are similar to any other word. In the analysis below, we
see what words are associated to "love" across two different texts,
*Moby Dick* (text1) and *Sense And Sensibility* (text2).

![Finding words that are similar to "love" in *Moby Dick* and *Sense
and Sensibility*](../images/love-similar.jpg)

For Melville, love is associated with the strong natural forces,
having to do with or brought on by nature ("sea," "whale," "fear") and
men, male bodies ("head," "hand," "him," "me"). In Austen, the word
love has associations with domestic life, family and specific people
("sister," "mother," "elinor," "marianne"). Both Melville and Austen
share "head" and "him," though Austen also has "heart" (rather than
"hand") and "her." The affect associated with love in Austen is
"affection," while in Melville, it's "fear."

I wonder how our analysis changes if the text is written by a
woman. What kinds of conclusions can we draw? Presumably, that love
for Austen is associated with family affection, and for Melville, with
awe of nature. 

- We do not do text analysis to answer a question. We do text analysis
to arrive at the question. 

- "text analysis is just playing with lists" (rafa)

- The idea that stopwords have no meaning, so we remove them. of
  course they have meaning. They are moments of flight! from one
  resting place (noun) to the next. They should be called "go" words. 

- Lemmatize, remove stopwords: the more and more you simplify and
  regularize your data, the easier it is to see the relationships
  between them. Moretti: distance as a condition of knowledge. 


