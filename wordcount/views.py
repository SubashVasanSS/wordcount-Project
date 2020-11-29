from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request,'home.html')

def countMe(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    worddict={}

    for words in wordlist:
        if words in worddict:
            worddict[words]+=1
        else:
            worddict[words]=1
    sortedwords=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
    return render(request,'about.html')