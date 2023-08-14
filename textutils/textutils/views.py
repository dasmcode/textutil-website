from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    dj_text = request.GET.get('text', 'NIL')
    if_removepunc = request.GET.get('removepunc', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    punctuations = '''!()-[]}{;:'"\,<>./?@#$%^&*_~'''
    analyzed = ''
    if if_removepunc == 'on' and len(dj_text) != 0:
        for i in dj_text:
            if i not in punctuations:
                analyzed += i
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if newlineremove == 'on' and len(dj_text) != 0:
        for i in dj_text:
            analyzed += i
        analyzed = analyzed.replace('\r\n', '')
        params = {'purpose': 'New Lines removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if capitalize == 'on' and len(dj_text) != 0:
        for i in dj_text:
            analyzed += i.upper()

        params = {'purpose': 'All letters capitalized',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if spaceremove == 'on' and len(dj_text) != 0:
        for i in dj_text:
            if i != ' ':
                analyzed += i
        params = {'purpose': 'Spaces removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    if charcount == 'on' and len(dj_text) != 0:
        counter = 0
        for i in dj_text:
            if i != '\r':
                counter += 1
        analyzed = f'The no. of characters in the string are {counter}'
        params = {'purpose': 'Characters in entered text',
                  'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        analyzed = dj_text
        params = {'purpose': 'No text entered/No option selected',
                  'analyzed_text': analyzed}
        return render(request, 'analyzenotext.html', params)


def contact(request):
    return render(request, 'contact.html')
