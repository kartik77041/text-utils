
# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    a = 0
    purpose = ''
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = 'Removed Punctuations'
        djtext = analyzed
        a = 1

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        if a == 1:
            purpose = purpose + ", "
        purpose = purpose + 'Changed to Uppercase'
        djtext = analyzed
        a = 1

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        if a == 1:
            purpose = purpose + ", "
        purpose = purpose + 'Removed extra spaces'
        djtext = analyzed
        a = 1

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        if a == 1:
            purpose = purpose + ", "
        purpose = purpose + 'Removed NewLines'
        a = 1
    if(removepunc != "on" and fullcaps!="on" and newlineremover != "on" and extraspaceremover!="on"):
        return HttpResponse("Error")
    else:

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)