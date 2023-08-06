#Py-Levenshtien

Python levenshtein project used to calculate the difference between two strings

Download from command prompt using:
pip install git+git://github.com/Redstomite/py-levenshtein#egg=py-levenshtein
(pip needs to be installed first)
or
pip install py-levenshtein

How to use it:
import py-levenschtein as pylev

word1 = ""
word2 = ""

distance = pylev.distc(word1, word2)

print(distance)

https://pypi.org/project/py-levenshtein/1.0/

Algorithm:
https://en.wikipedia.org/wiki/Levenshtein_distance
