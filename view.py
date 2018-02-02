import requests, asyncio, discord
import parsing, controller
from discord.ext import commands

kino_bot = commands.Bot(command_prefix="!")
controller = controller.Controller()

@kino_bot.event
async def on_ready():
    print("CONNECTED")

@kino_bot.command()
async def imdb(*args):
    await kino_bot.say(parsing.Parsing(" ".join(args)).get_rating())

@kino_bot.command()
async def addMovie(*args):
    movie_name = " ".join(args)
    message = controller.create(movie_name)
    await kino_bot.say(message)


@kino_bot.command()
async def movie(*args):
    movie_name = " ".join(args)
    print(movie_name)
    message = controller.get_movie(movie_name)
    await kino_bot.say(message)

@kino_bot.command()
async def delMovie(*args):
    movie_name = " ".join(args)
    message = controller.delete(movie_name)
    await kino_bot.say(message)

@kino_bot.command(pass_context=True)
async def rate(ctx):
    author_name = str(ctx.message.author).split("#")[0]
    author_id = str(ctx.message.author).split('#')[1]
    movie_name, rating = ctx.message.content.split(",")
    movie_name = movie_name.split("!rate ")[1]
    answer = controller.rate(movie_name, author_id, rating)
    if len(answer) > 5:
        await kino_bot.say(answer)
        return
    else:
        message = "{0} just rated {1} {2}/10\nThe new community rating is: {3}/10".format(author_name, movie_name, rating, answer)
        await kino_bot.say(message)

@kino_bot.command()
async def addSnap(*args):
    movie_name, snap = " ".join(args).split(',')
    message = controller.add_snap(movie_name, snap)
    await kino_bot.say(message)

@kino_bot.command()
async def synopsis(*args):
    movie_name = " ".join(args)
    message = parsing.Parsing(movie_name).get_synopsis()
    message = " ".join(message.split(" ")[20:len(message)])
    await kino_bot.say(movie_name + ":\n" + message)

@kino_bot.command()
async def helpKino(*args):
    with open("help.txt","r") as help_file:
        await kino_bot.say(help_file.read())
kino_bot.run('BOT-KEY')
