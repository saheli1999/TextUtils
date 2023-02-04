from django.http import HttpResponse
from django.shortcuts import render

#  use template


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # removepunc
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'Analyze_text': analyzed}
        djtext = analyzed

    #  fullcaps
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to UpperCase', 'Analyze_text': analyzed}
        djtext = analyzed

        # newlineremove
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()

        params = {'purpose': 'Removed Newline', 'Analyze_text': analyzed}
        djtext = analyzed

        # extraspaceremove
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'Analyze_text': analyzed}
        djtext = analyzed

        # charcount
    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            analyzed = analyzed+1

        params = {'purpose': 'Number of Characters', 'Analyze_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please Select any Operation and Try again!")
    return render(request, 'analyze.html', params)
