import discord
import requests
import json
import datetime
import random
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents.all())


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def lottery():
    first = random.randint(1, 69)
    second = random.randint(1, 69)
    third = random.randint(1, 69)
    fourth = random.randint(1, 69)
    fifth = random.randint(1, 69)
    ball = random.randint(1, 26)
    return f"Numbers: {first}, {second}, {third}, {fourth}, {fifth} | Powerball: {ball}"


def coin_flip():
    coin = ['Heads', 'Tails']
    choice = random.choice(coin)
    return choice


def time():
    now = datetime.datetime.today()
    the_time = datetime.datetime.time(now)
    today = datetime.datetime.today()
    the_date = datetime.date.today()
    the_date = the_date.strftime('%m/%d/%Y')
    day = datetime.date.weekday(today)
    if day == 6:
        day = 'Sunday'
    if day == 5:
        day = 'Saturday'
    if day == 4:
        day = 'Friday'
    if day == 3:
        day = 'Thursday'
    if day == 2:
        day = 'Wednesday'
    if day == 1:
        day = 'Tuesday'
    if day == 0:
        day = 'Monday'
    return f"Today is {day}, {the_date} at {the_time}."
