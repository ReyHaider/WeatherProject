from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .key import api_key
import requests
import math
# from .models import Social

# Create your views here.


def index(request):
    return render(request, "home.html")


def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        response = requests.get(url).json()
        try:
            context = {
                "city_name": response["city"]["name"],
                "city_country": response["city"]["country"],
                "wind": response['list'][0]['wind']['speed'],
                "degree": response['list'][0]['wind']['deg'],
                "status": response['list'][0]['weather'][0]['description'],
                "cloud": response['list'][0]['clouds']['all'],
                'date': response['list'][0]["dt_txt"],
                'date1': response['list'][1]["dt_txt"],
                'date2': response['list'][2]["dt_txt"],
                'date3': response['list'][3]["dt_txt"],
                'date4': response['list'][4]["dt_txt"],
                'date5': response['list'][5]["dt_txt"],
                'date6': response['list'][6]["dt_txt"],


                "temp": round(response["list"][0]["main"]["temp"] - 273.0),
                "temp_min1": math.floor(response["list"][1]["main"]["temp_min"] - 273.0),
                "temp_max1": math.ceil(response["list"][1]["main"]["temp_max"] - 273.0),
                "temp_min2": math.floor(response["list"][2]["main"]["temp_min"] - 273.0),
                "temp_max2": math.ceil(response["list"][2]["main"]["temp_max"] - 273.0),
                "temp_min3": math.floor(response["list"][3]["main"]["temp_min"] - 273.0),
                "temp_max3": math.ceil(response["list"][3]["main"]["temp_max"] - 273.0),
                "temp_min4": math.floor(response["list"][4]["main"]["temp_min"] - 273.0),
                "temp_max4": math.ceil(response["list"][4]["main"]["temp_max"] - 273.0),
                "temp_min5": math.floor(response["list"][5]["main"]["temp_min"] - 273.0),
                "temp_max5": math.ceil(response["list"][5]["main"]["temp_max"] - 273.0),
                "temp_min6": math.floor(response["list"][6]["main"]["temp_min"] - 273.0),
                "temp_max6": math.ceil(response["list"][6]["main"]["temp_max"] - 273.0),


                "pressure": response["list"][0]["main"]["pressure"],
                "humidity": response["list"][0]["main"]["humidity"],
                "sea_level": response["list"][0]["main"]["sea_level"],


                "weather": response["list"][1]["weather"][0]["main"],
                "description": response["list"][1]["weather"][0]["description"],
                "icon": response["list"][0]["weather"][0]["icon"],
                "icon1": response["list"][1]["weather"][0]["icon"],
                "icon2": response["list"][2]["weather"][0]["icon"],
                "icon3": response["list"][3]["weather"][0]["icon"],
                "icon4": response["list"][4]["weather"][0]["icon"],
                "icon5": response["list"][5]["weather"][0]["icon"],
                "icon6": response["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

                "city_name": "Not Found, Check your spelling..."
            }

        return render(request, "results.html", context)
    else:
        return redirect('home')
