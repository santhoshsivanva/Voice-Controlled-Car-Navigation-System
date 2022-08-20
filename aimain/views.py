from json import dumps
from django.http.response import HttpResponse
from django.shortcuts import render
import multiprocessing
import datetime
import gtts
from random import randint
from playsound import playsound
from aimain.models import Aisource, Type, motioncontrol
from geopy.geocoders import Nominatim
# welcome=gtts.gTTS("Welcome to AI car system")
# welcome.save("welcome.mp3")
# l=gtts.gTTS("your location is updated")
# l.save("welome.mp3")
# auu=gtts.gTTS("automatic mode intialized and checking for hardware errors")
# auu.save("new_auto.mp3")
# manualmode=gtts.gTTS("Manual mode activated")
# manualmode.save("manual.mp3")
# shortpath=gtts.gTTS("Searching for shortest path")
# shortpath.save("shortest.mp3")
# start=gtts.gTTS("System started Get ready for the journey")
# start.save("start.mp3")
number = randint(1, 100)
geolocator = Nominatim(user_agent="v.sivan777vss@gmail.com")


def index(request):
    p = multiprocessing.Process(target=playsound, args=("welcome.mp3",))
    if(p.is_alive == True):
        p.terminate()
    p.start()
    

    time1 = datetime.datetime.now()
    hour, minutes, seconds, day, month, year = time1.strftime("%I"), time1.strftime(
        "%M"), time1.strftime("%S"), time1.strftime("%d"), time1.strftime("%b"), time1.strftime("%Y")


    return render(request, "index/index.html", {
        "hour": hour, "minutes": minutes, "seconds": seconds, "day": day, "month": month, "year": year, "number": number
    })

# Create your views here.


def manual(request):
    p = multiprocessing.Process(target=playsound, args=("manual.mp3",))
    if(p.is_alive == True):
        p.terminate()
    p. start()

    try:
        Type.objects.create(automated_Mode="No", manual_Mode="Yes")
    except Exception as E:
        print("Error: "+E)
    return render(request, "index/manualmode.html", {})


def automatedMode(request):
    p = multiprocessing.Process(target=playsound, args=("new_auto.mp3",))
    if(p.is_alive == True):
        p.terminate()
    p.start()

    try:
        Type.objects.create(automated_Mode="Yes", manual_Mode="No")
        motioncontrol.objects.create(
            sensor="Yes", camera="Yes", radar="Yes", sonar="Yes")
    except Exception as E:
        print("Error: "+E)

    return render(request, "index/motioncontrol.html", {})


def check(request):
    time1 = datetime.datetime.now()
    hour, minutes, seconds, day, month, year = time1.strftime("%I"), time1.strftime(
        "%M"), time1.strftime("%S"), time1.strftime("%d"), time1.strftime("%b"), time1.strftime("%Y")

    country="India"

    if request.method == "POST":
        issue = 0
        message = ""
        source_ = request.POST.get("source")
        destination_ = request.POST.get("des")

        if(source_ == ""):
            message = "Please Check Your Entry"
            issue = 1

        elif(destination_ == ""):
            message = "Please Check Your Entry"
            issue = 1

        elif(source_ == "" and destination_ == ""):
            message = "Please Check Your Entry"
            issue = 1

        elif(source_.isalpha() == False or destination_.isalpha() == False):
            message = "Please Check Your Entry"
            issue = 1

        elif(source_.isalpha() == False and destination_.isalpha() == False):
            message = "Please Check Your Entry"
            issue = 1

        else:
            source_ = request.POST["source"]
            destination_ = request.POST["des"]
            Aisource.objects.create(
                source=source_.lower(), destination=destination_.lower())
            message = "successfully updated"

            p = multiprocessing.Process(target=playsound, args=("welome.mp3",))
            if(p.is_alive == True):
                p.terminate()
            p. start()

            loc1 = geolocator.geocode(source_+','+country)
            loc2 = geolocator.geocode(destination_+','+country)
            data = [
                [str(loc1.latitude),str(loc1.longitude)],
                [str(loc2.latitude),str(loc2.longitude)]
            ]
            data=dumps(data)

            return render(request, "index/index1.html", {
                "hour": hour, "minutes": minutes, "seconds": seconds, "day": day, "month": month, "year": year, "number": number, "message": message, "issue": issue,
                "source": source_, "des": destination_,"data":data })
          

    return render(request, "index/index1.html", {
        "hour": hour, "minutes": minutes, "seconds": seconds, "day": day, "month": month, "year": year, "number": number, "message": message, "issue": issue, })


# Handler404 must be placed first among other views..
def error_404(request, exception):
    data = {}
    return render(request, 'index/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'index/404.html', data)

def map(request):
    return render(request,'index/map.html')