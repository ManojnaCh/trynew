import nltk
sentence = "Jim bought 300 shares of Acme Corp. in 2006. He is studying in VIT University."
tokens = nltk.word_tokenize(sentence)
print tokens
tagged = nltk.pos_tag(tokens)
print tagged[0:6]
entities = nltk.chunk.ne_chunk(tagged)
print entities
#from nltk.corpus import treebank
#t = treebank.parsed_sents('wsj_0001.mrg')[0]
entities.draw()

