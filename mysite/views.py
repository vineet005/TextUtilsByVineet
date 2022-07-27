#created file
# 'django-admin' command to know the fuctions of djnago.
# 'django-admin startproject Project_name' to make the project in directory you are working.
# 'python manage.py runserver' to start the project and make it run on inbuilt server of django.
# to add templates go to settings.py->templates fn->DIRS and write " 'templates' " in [].(templates will be a folder)

'''Code for django project comes here'''
from django.http import HttpResponse#takes string as arguments
from django.shortcuts import render#takes request and files from templates as arguments

def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')  # for backend print->look in the terminal. it will return text u have written otherwise the default value.

    # check the checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')


    # check which checkbox is on!
    if removepunc=="on":

        # list of punctuations from internet
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Punctuation Free Text','analyzed_text':analyzed}
        djtext=analyzed#to make work every fn together dont return any value


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized Text(Changed to UPPERCASE)', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space is Removed.', 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcount == "on"):
        analyzed = "Number of characters:  " + str(len(djtext)) + "  including space and punctuations."

        params = {'purpose': 'Charcters are Counted', 'analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount !="on"):
        return HttpResponse("ERROR!! Please Choose an Operation!")




    return render(request, 'analyze.html', params)