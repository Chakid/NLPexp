# T21

from nltk.book import *
word_li = [w for w in text5 if len(w)==4]
fdist = FreqDist(word_li)
sorted_word_li = sorted(fdist.keys(),key=lambda x:fdist[x],reverse=True)
for w in sorted_word_li:
    print ("%s\t%d; "%(w,fdist[w]))
