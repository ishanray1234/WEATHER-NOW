import asyncio
import os
from uagents import Agent, Context
import python_weather

async def getweather(ctx: Context, city):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(city)
        
        # returns the current day's forecast temperature (int)
        temperature = weather.current.temperature
        # ctx.logger.info(f'Temperature in Mumbai: {temperature}°C')
        return temperature

if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    city=input("Enter city name:")
    min_temp=(int)(input("Enter minimum temperature:"))
    max_temp=(int)(input("Enter maximum temperature:"))


    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    alice = Agent(name="alice", seed="alice recovery phrase")

    @alice.on_interval(period=2.0)
    async def say_hello(ctx: Context):
        temp=await getweather(ctx,city)
        # min_temp=23
        # max_temp=30
        if(temp<min_temp or temp>max_temp):
            ctx.logger.info(f'{temp}:You are fucked')
        else:
            ctx.logger.info(f'Temperature in {city}: {temp}°C')
    alice.run()

