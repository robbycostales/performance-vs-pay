# -*- coding: UTF-8 -*-
import unidecode

with open('manual/17stats.csv', 'r') as myfile:
    data=myfile.read()

#convert plain text to utf-8
u = unicode(data, "utf-8")
#convert utf-8 to normal text
x = unidecode.unidecode(u)

with open('accent-free/17stats.csv','wb') as myfile:
    myfile.write(x)

# print(x)
