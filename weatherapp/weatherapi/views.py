from django.shortcuts import render
import requests
import asyncio
import os
from uagents import Agent, Context
import python_weather
# Create your views here.

async def weather(ctx: Context, city):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(city)
        
        # returns the current day's forecast temperature (int)
        temperature = weather.current.temperature
        # ctx.logger.info(f'Temperature in Mumbai: {temperature}°C')
        
        return temperature
    

def home(request):
    if request.method == 'POST':
        post_data = request.POST
        # You can access specific POST parameters by their names
        city = post_data.get('city')
        temp = asyncio.run(weather(request, city))
        context = {'temp': temp}
        # Render the HTML template with the data
        return render(request, 'home.html', context)
    context = {'temp': -1}
    return render(request,'home.html', context)

# def my_post(request):

#     my_data = asyncio.run(weather(request, 'Delhi'))
#     context = {'my_data': my_data}
#     # Render the HTML template with the data
#     return render(request, 'home.html', context)
