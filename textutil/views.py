
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
# def paswordg(requeat):
#     passorwd=request.POST.get('text','default')
def analyze(request):
    txt=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capson=request.POST.get('capson','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charctercounter=request.POST.get('charctercounter','off')

    # print(removepunc)
    # print(txt)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed+char
        parameters = {'Purpose': 'Removed Punctuations', 'analyzedText': analyzed}
        return render(request, 'analyze.html', parameters)
    elif capson=="on":
        analyzed = ""
        for char in txt:
            analyzed=analyzed+char.upper()
        parameters = {'Purpose': 'Converted To Uppercase', 'analyzedText': analyzed}
        return render(request, 'analyze.html', parameters)
    elif newlineremover=="on":
        analyzed = ""
        for char in txt:
            if char!="\n" and char!="\r":
              analyzed = analyzed + char
        parameters = {'Purpose': 'New Lines Are Removed', 'analyzedText': analyzed}
        return render(request, 'analyze.html', parameters)
    elif extraspaceremover=="on":
        analyzed = ""
        for index,char in enumerate(txt):
            if not(txt[index]==" " and txt[index+1]==" "):
                analyzed = analyzed + char
        parameters = {'Purpose': 'Extra Spaces Are Removed', 'analyzedText': analyzed}
        return render(request, 'analyze.html', parameters)
    elif charctercounter == "on":
        analyzed=len(txt)
        parameters = {'Purpose': 'Total Character in your String is', 'analyzedText': analyzed}
        return render(request, 'analyze.html', parameters)


    else:
        return HttpResponse ("error")



