from django.shortcuts import render
from django.http import HttpResponse
from .modules import ApiGet
from .models import donneesCov
import requests
import json

#Partie qui va gérer la page index de CovVisu
def index(request):
    maListeRecuperee=apiGenericProcess()
    print(maListeRecuperee)

    return render(request,'CovVisu/index.html', {"context":maListeRecuperee})





# Partie qui va récupérer et traiter les data corona
def apiGenericProcess():
    objetTransitionnel = ResultGrab()
    objetTransitionnelPostDigest = JSONDigest(objetTransitionnel)
    objetArendre=applicationCalcul(objetTransitionnelPostDigest)
    return objetArendre


def ResultGrab():
    url="http://corona-api.com/countries/FR"
    response = requests.get(url)
    if response.status_code != 200:
        print("Erreur : " + str(response.status_code))
    else:
        myResult = response.content

    return myResult


def JSONDigest(objetTransitionnel):
    text = json.loads(objetTransitionnel.decode('utf-8'))
    return text


def applicationCalcul(objetTransitionnelPostDigest):
    objetATravailler = objetTransitionnelPostDigest["data"]["timeline"]  # takes previous measures
    #print(objetATravailler)
    n=0
    dicoToGive={}
    while n<20:

            #print("Date : " + str(objetATravailler[n]["date"]) + " Décès :" + str(objetATravailler[n]["new_deaths"]) + " Nouveaux cas :" + str(
            #    objetATravailler[n]["new_confirmed"]))
            dicoToGive[n]=[str(objetATravailler[n]["date"]),objetATravailler[n]["new_deaths"], objetATravailler[n]["new_confirmed"]]
            n+=1
    print(dicoToGive)
    return dicoToGive