from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .madrigalWeb import madrigalWeb
from gtfls.models import ExpF, ExpL, FilesDwnld
import os
import sys
import time
from datetime import datetime
from gtfls.forms import InputForm
from django.utils import timezone
import webbrowser


def parameterform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            location = form.cleaned_data['location']
            fromdate= form.cleaned_data['fromdate']
            todate= form.cleaned_data['todate']
            if (location == '1'): #PFSIR was chosen
                madrigalUrl = 'http://isr.sri.com/madrigal'
                instrumentcode = 61
                testData = madrigalWeb.MadrigalData(madrigalUrl)
                expList = testData.getExperiments(instrumentcode, fromdate.year,fromdate.month,fromdate.day,0,0,0,
                    todate.year,todate.month,todate.day,0,0,0, local=1)
            elif(location == '2'):
                madrigalUrl = 'http://madrigal.haystack.mit.edu/madrigal' #MillstoneHill Was Chosen
                instrumentcode = 30
                testData = madrigalWeb.MadrigalData(madrigalUrl)
                expList = testData.getExperiments(instrumentcode, fromdate.year,fromdate.month,fromdate.day,0,0,0,
                    todate.year,todate.month,todate.day,0,0,0, local=1)
            # newcgiurl = madrigalWeb.MadrigalData(madrigalUrl)
            # expList = newcgiurl.getExperiments(61, fromdate.year,fromdate.month,fromdate.day,0,0,0,
            #     todate.year,todate.month,todate.day,0,0,0, local=1)
            ExpL.objects.all().delete()
            for i in range(len(expList)):
                q = ExpL( pub_date = timezone.now() , madrigalUrl = expList[i].madrigalUrl,
                         name = expList[i].name, realUrl = expList[i].realUrl, 
                         url = expList[i].url, madid = expList[i].id)
                q.save()


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/gtfls/dispfiles/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'gtfls/inputinfo.html', {'form': form})

def dispfiles(request):
    latest_expList = ExpL.objects.all()
    #template = loader.get_template('polls/listexp.html')
    context = {'latest_expList': latest_expList}

    return render(request, 'gtfls/dispfiles.html', context)

def fndwnld(request, experimentid): #get the experiment files from the experiments
    #linktofile = get_object_or_404(Question, madid = experimentid)
    madrigalUrl = 'http://isr.sri.com/madrigal'
    testData = madrigalWeb.MadrigalData(madrigalUrl) 
    fileList = testData.getExperimentFiles(experimentid) #onetomanyrelation to all of the possible files to the experiment
    if not fileList: #need to find a way to save the URL
        madrigalUrl = 'http://madrigal.haystack.mit.edu/madrigal'
    testData = madrigalWeb.MadrigalData(madrigalUrl)
    fileList = testData.getExperimentFiles(experimentid) 
    ExpF.objects.all().delete() #delete the list of items from the previous run
    linktofile = get_object_or_404(ExpL, madid = experimentid) #raise an error if this object does not exist
    for i in range(len(fileList)):
        x = ExpF(expId = fileList[i].expId, expName = fileList[i].name.replace("/", "-"), kinddatdesc = fileList[i].kindatdesc, expl= linktofile)
        x.save()

    ids = list(ExpF.objects.values()) #convert QuerySet to Dict so that it can be displayed on website
    allcontext = {'ids':ids}
    return render(request, 'gtfls/fndwnld.html', allcontext) #send the information to the html file


def downloadfiles(request, experimentid, expName):
    user_fullname = 'Ashaki Gumbs' #these variables will have to change and an input will be required eventually
    user_email = 'agumbs@bu.edu'
    user_affiliation = 'Boston University'
    #fileinfo = get_object_or_404(ExpL, madid = experimentid).madrigalUrl
    expName= expName.replace("-", "/")
    expName = expName.strip( '-')
    fileName = expName.rsplit("/", 1)[1]
    testData = madrigalWeb.MadrigalData(get_object_or_404(ExpL, madid = experimentid).madrigalUrl) #get the appropiate url from the database
    j = FilesDwnld(upload = testData.downloadFile(expName, "/home/ashaki/Documents/Research_Semeter_Group/madpython/bucsp/gtfls/media/" + fileName + ".hdf5"  , "Ashaki Gumbs", "agumbs@bu.edu","Boston University", 
                        "hdf5"))
    j.save()
    os.system("python testing.py")
    webbrowser.open("google.com")
    return render(request, 'gtfls/downloadfiles.html')


