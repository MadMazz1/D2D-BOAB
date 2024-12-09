import discord
import responses
import function
from discord.ext import commands
import openai

# Defines discord intents(permissions) and openai key
intents = discord.Intents.all()
intents.message_content = True
openai.api_key = 'INSERT API KEY HERE'


# Generates response from OpenAI
def generate_response(input_text):
    model_engine = "text-davinci-002"
    prompt = input_text

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = completions.choices[0].text
    return message


# Defines send_message()
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


# Runs the Discord bot from 'graphics.py'
def run_discord_bot():
    client = commands.Bot(command_prefix='!', intents=intents)
    TOKEN = 'INSERT DISCORD API KEY HERE'

    # Queries OpenAI for a response.
    @client.command()
    async def boab(ctx, *, input_text: str):
        response = generate_response(input_text)
        await ctx.send(response)

    # Slap command
    @client.command()
    async def slap(ctx, user: discord.Member):
        gif_url = "https://tenor.com/view/slap-slapping-charlie-murphy-chappelle-chappelles-gif-20069417"
        await ctx.send(f"{ctx.author.mention} just slapped the fuck out of {user.mention}!")
        await ctx.send(gif_url)

    # Insult @user command
    @client.command()
    async def insult(ctx, user: discord.Member):
        insult1 = function.rand_insult()
        await ctx.send(f"{user.mention}, {insult1}")

    # Deletes messages in a channel.
    @client.command()
    async def clear(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"{ctx.author.mention} deleted {limit} message(s).")

    # Deletes messages up until the message id provided.
    @client.command()
    async def clear_until(ctx, message_id: int):
        async for message in ctx.channel.history(limit=None):
            if message.id == message_id:
                break
            await message.delete()

    # Queries YT for a particular video, and returns the a link to search results.
    @client.command()
    async def yt(ctx, *, search_query: str):
        youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
        await ctx.send(f"Here's a YouTube link for '{search_query}':\n {youtube_url}")

    # Queries Google
    @client.command()
    async def google(ctx, *, search_query: str):
        google_url = f"https://www.google.com/search?q={search_query}"
        await ctx.send(f"Googling '{search_query}'...\n *Search Results:\n {google_url}*")

    # Displays info about @USER
    @client.command()
    async def userinfo(ctx, user: discord.Member):
        join_date = user.joined_at.strftime("%m/%d/%Y, %H:%M:%S")
        roles = [role.name for role in user.roles if role.name != '@everyone']

        if user.name == 'Kmazz':
            roles.append('The Man')

        if user.name == 'paulie':
            roles.append('Likes Men')

        if user.name == 'Brad':
            roles.append('Wants to re-enact Brokeback Mountain with Paulie')

        if user.name == 'Jiko':
            roles.append('Nice Pee-Pee')

        status = user.status
        activity = user.activity.name if user.activity else 'None'
        created_at = user.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        count = 0
        last_message = None
        async for message in ctx.channel.history(limit=None, oldest_first=True, after=user.created_at):
            if message.author == user:
                count += 1
                last_message = message
        messages = count
        await ctx.send(f"Name: {user.name}\n"
                       f"Join Date: {join_date}\n"
                       f"Roles: {roles}\n"
                       f"Status: {status}\n"
                       f"Activity: {activity}\n"
                       f"Account Created: {created_at}\n"
                       f"Message Count: {messages} in Channel: '#{ctx.channel}'\n"
                       f"Last Message: {last_message.content}")

    # Let's host know that bot client is now running.
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Tells client to ignore it's own messages.
        if message.author == client.user:
            return

        # Listens for commands
        await client.process_commands(message)

        # Listens for users messages in all channels. If user message starts with '?' instead of '!' -
        # - then response will be sent in a private message.
        username = str(message.author)
        user_message = str(message.content.lower())
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" - Channel: ({channel})')

        # Supposed to send response as a private message. - Not currently working for some reason...
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)