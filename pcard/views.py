import json
from django.http import HttpResponse
from django.shortcuts import render  # , redirect
from django.core.files.storage import FileSystemStorage

"""import numpy as np
import urllib
import json
import cv2
import os"""
# import ast
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
from django.conf import settings
from django import db
from .forms import UploadImageForm
from .forms import ImageUploadForm
from .forms import UploadFileForm

from .models import aadhardb, dirverdata, voteriddata, panddata, panapi, aadharapi, drvingapi, voterapi
# import our OCR function
# import pandas as pd
from .ocr import ocr
# import re
from .adhar import adhar
from .voterid import voterid
from .driver import driver_license


# from .bank import bank_details_sbi, bank_details_alla, bank_details_yes
# from .driver import driver_license
# db.connections.close_all()

def home(request):
    return render(request, 'pcard/home.html', {})


def Hbase(request):
    return render(request, 'pcard/base.html')


def index(request):
    return render(request, 'pcard/index.html', {})


def aadhar(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.image.name
            # print(settings.MEDIA_URL, "cgfcgvhvhvh")
            adhar_text = adhar(settings.MEDIA_ROOT_URL + imageURL)
            # print(adhar_text, "HHH")
            # obj={
            #    'form':form, 'post':post, 'adhar_text': adhar_text, 'img_src' : imageURL 
            # }
            # adhar_text=json.loads(json.dumps(adhar_text))
            ad_name = adhar_text[0]
            ad_dob = adhar_text[2]
            ad_gender = adhar_text[3]
            ad_num = adhar_text[1]
            obj = {
                "Name": ad_name,
                "DOB": ad_dob,
                "Gender": ad_gender,
                "Number": ad_num
            }

            myobj = aadhardb(aadharnumber=ad_num, aadharname=ad_name, aadharbirth=ad_dob, aadhargender=ad_gender,
                             aadharimage=imageURL)
            myobj.save()

            return render(request, 'pcard/aadhar.html',
                          {"adhar_text": obj, 'img_src': imageURL, 'adharno': adhar_text[1]})



    else:
        form = ImageUploadForm()
    return render(request, 'pcard/aadhar.html', {'form': form})


def voter_id(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.image.name
            # print(settings.MEDIA_URL, "cgfcgvhvhvh")
            voterid_text = voterid(settings.MEDIA_ROOT_URL + imageURL)
            print(voterid_text)
            v_name = voterid_text[0]
            v_fname = voterid_text[1]

            print("voters_name", v_name)
            print("voters_father name", v_fname)

            # obj={
            #    'form':form, 'post':post, 'adhar_text': adhar_text, 'img_src' : imageURL 
            # }
            # adhar_text=json.loads(json.dumps(adhar_text))

            vobj = voteriddata(votername=v_name, voterfname=v_fname, voterimage=imageURL)
            vobj.save()

            return render(request, 'pcard/voterid.html', {"voterid_text": voterid_text, 'img_src': imageURL})

    else:
        form = ImageUploadForm()
    return render(request, 'pcard/voterid.html', {'form': form})


def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
        return render(request, 'pcard/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})

    else:
        form = UploadImageForm()
        return render(request, 'pcard/uimage.html', {'form': form})


def ocr_core(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.image.name
            # print(imageURL)
            extracted_text = ocr(settings.MEDIA_ROOT_URL + imageURL)

            print(extracted_text)
            # print(extracted_text[6:24])
            # print(extracted_text[39:53])
            # print(extracted_text[69:79])
            # print(extracted_text[92:101])

            fname = extracted_text[0]
            fathername = extracted_text[1]
            dob = extracted_text[2]
            pno = extracted_text[3]

            pobj = panddata(panno=pno, fathername=fathername, name=fname, pandob=dob, panimage=imageURL)
            pobj.save()

            return render(request, 'pcard/pcard.html',
                          {'form': form, 'post': post, 'extracted_text': extracted_text, 'img_src': imageURL})

    else:

        form = ImageUploadForm()

    return render(request, 'pcard/pcard.html', {'form': form})


def bank_id(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        temp = request.POST['select_bank']
        # print(temp, "VVVV")
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            fileURL = settings.MEDIA_URL + form.instance.file.name
            # print(fileURL)
            if temp == "SBI":
                bank_text = bank_details_sbi(settings.MEDIA_ROOT_URL + fileURL)
            elif temp == "Alla":
                bank_text = bank_details_alla(settings.MEDIA_ROOT_URL + fileURL)
            elif temp == "Yes":
                bank_text = bank_details_yes(settings.MEDIA_ROOT_URL + fileURL)
            # print(extracted_text)
            # print(bank_text, "HHH")
            """
            
            b_no = bank_text[0]
            b_name = bank_text[1]
            b_code = bank_text[2]
            b_op_bal = bank_text[3]
            b_cl_bal = bank_text[4]
            b_t_debit = bank_text[5]
            b_t_credit = bank_text[6]
            b_t_bal = bank_text[7]
            obj = {
                "Credit" : b_t_credit,
                "Balance": b_t_bal
            }
            """
            """obj = [
                bank_text[0],
                bank_text[1],
                bank_text[2],
                bank_text[3],
                bank_text[4],
                bank_text[5],
                bank_text[6],
                bank_text[7],
                
            ]
            list_text_as_a_string = json.dumps(obj, indent=2)"""
            return render(request, 'pcard/bank.html', {'form': form, 'bank_text': bank_text})
            # return render(request, 'pcard/bank.html', {'form':form, 'bank_text': bank_text})

    else:
        form = UploadFileForm()
    return render(request, 'pcard/bank.html', {'form': form})


def driver_id(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.image.name
            # print(imageURL)
            driver_text = driver_license(settings.MEDIA_ROOT_URL + imageURL)
            print(driver_text)
            print("name", driver_text[0])
            drlicencename = driver_text[0]
            drlicencelname = driver_text[1]
            drlicenceno = driver_text[2]
            print(drlicenceno, drlicencename, drlicencelname)
            myobj = dirverdata(drlicenceno=drlicenceno, drlicencename=drlicencename, drlicencelname=drlicencelname,
                               drlicenceimage=imageURL)
            myobj.save()
            return render(request, 'pcard/driver.html',
                          {'form': form, 'post': post, 'driver_text': driver_text, 'img_src': imageURL})

    else:
        form = ImageUploadForm()
    return render(request, 'pcard/driver.html', {'form': form})


def pandataverification(request):
    if request.method == 'POST':

        pandate = request.POST.get('pandate')
        panid = request.POST.get('panid')
        alldata = panapi.objects.filter(uid=panid)

        for x in alldata:
            if panid != x.uid:
                return HttpResponse('not equal')
            elif pandate != x.dob:
                return HttpResponse('not equal')
            else:
                return render(request, 'pcard/responseapi.html', {'alldata': alldata})

    form = ImageUploadForm()

    return render(request, 'pcard/pcard.html', {'form': form})


# def pandataverification(request):
#     if request.method == 'POST':
#
#         panid = request.POST.get('panverify')
#         # alldata = panddata.objects.filter(panno=panid)
#         alldata=panapi.objects.filter(uid=panid)
#         try:
#             # data = panddata.objects.get(panno=panid)
#             data=panapi.objects.get(uid=panid)
#         except Exception as e:
#             data = None
#
#         if (data != None):
#
#             return render(request, 'pcard/responseapi.html', {'alldata': alldata})
#             # return HttpResponse("success")
#         else:
#             return HttpResponse("not in db")
#
#     return HttpResponse("successs......")
#

def drivingdataverification(request):
    if request.method == 'POST':

        drivingid = request.POST.get('drivingverify')
        alldata = drvingapi.objects.filter(uid=drivingid)
        try:
            data = drvingapi.objects.get(uid=drivingid)
        except Exception as e:
            data = None

        if (data != None):

            return render(request, 'pcard/drivingresponse.html', {'alldata': alldata})
            # return HttpResponse("success")
        else:
            return HttpResponse("not in db")

    form = ImageUploadForm()
    return render(request, 'pcard/driver.html', {'form': form})


def voterdataverification(request):
    if request.method == 'POST':

        voterid = request.POST.get('voterverify')
        alldata = voterapi.objects.filter(voterid=voterid)
        try:
            data = voterapi.objects.get(voterid=voterid)
        except Exception as e:
            data = None

        if (data != None):

            return render(request, 'pcard/voterresponse.html', {'alldata': alldata})
            # return HttpResponse("success")
        else:
            return HttpResponse("not in db")

    form = ImageUploadForm()
    return render(request, 'pcard/voterid.html', {'form': form})


def aadhardataverification(request):
    if request.method == 'POST':
        aadhardate = request.POST.get('aadhardate')
        aadharid = request.POST.get('aadharid')
        alldata = aadharapi.objects.filter(uid=aadharid)

        for x in alldata:

            if aadharid != x.uid:
                return HttpResponse("not equal")
            elif aadhardate != x.dob:
                return HttpResponse("not equal")
            else:
                return render(request, 'pcard/aadharresponse.html', {'alldata': alldata})

    form = ImageUploadForm
    return render(request, 'pcard/aadhar.html', {'form': form})
# def aadhardataverification(request):
#     if request.method == 'POST':
#
#         aadharid = request.POST.get('aadharverify')
#         # alldata = voteriddata.objects.filter(aadharno=aadharid)
#         try:
#             data = aadharapi.objects.get(uid=aadharid)
#         except Exception as e:
#             data = None
#
#         if (data != None):
#
#             # return render(request, 'pcard/drivingresponse.html', {'alldata': alldata})
#             return HttpResponse("success")
#         else:
#             return HttpResponse("not in db")
#
#     return HttpResponse("successs......")
