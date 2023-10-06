from django.shortcuts import render
import requests
import asyncio
import os
from uagents import Agent, Context
import python_weather
# Create your views here.

async def home(ctx: Context, city):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(city)
        
        # returns the current day's forecast temperature (int)
        temperature = weather.current.temperature
        # ctx.logger.info(f'Temperature in Mumbai: {temperature}°C')
        return temperature