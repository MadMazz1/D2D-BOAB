import webbrowser
import discord
from D2D_BOAB import function
import random

client = discord.Client(intents=discord.Intents.all())
ck = '!'  # Command Key


def get_response(message: str) -> str:
    p_message = message.lower()
    # Chat Commands
    if p_message == f'{ck}check':
        return str("BOAB is running at maximum efficiency!")

    if p_message == f'{ck}hello' or p_message == f'{ck}hi':
        return str(f"Hi there! Type '!help' for a list of commands.")

    if p_message == f'{ck}bye':
        return str("See you later!")

    if p_message == f'{ck}who\'s the man?' or p_message == f'{ck}whos the man?':
        return str("You are!")

    if p_message == f'{ck}roll':
        return str(random.randint(1, 6))

    if p_message == f'{ck}donate':
        url = 'https://paypal.me/Kiolleron?locale.x=en_US'
        webbrowser.open(url)

    if p_message == f'{ck}smile':
        return str('(*^▽^*)')

    if p_message == f'{ck}smile1':
        return str('(*^_^*)')

    if p_message == f'{ck}smile2':
        return str('(✿◡‿◡)')

    if p_message == f'{ck}smile3':
        return str('♪(^∇^*)')

    if p_message == f'{ck}sad':
        return str('＞︿＜')

    if p_message == f'{ck}sad1':
        return str('≡(▔﹏▔)≡')

    if p_message == f'{ck}sad2':
        return str('┗( T﹏T )┛')

    if p_message == f'{ck}flip':
        return str('┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻')

    if p_message == f'{ck}rose':
        return str('--<-<-<@')


    if p_message == f'{ck}quote':
        quote = function.get_quote()
        return quote

    if p_message == f'{ck}lottery':
        lottery = function.lottery()
        return lottery

    if p_message == f'{ck}coinflip':
        flip = function.coin_flip()
        return flip

    if p_message == f'{ck}date' or p_message == f"{ck}what is today?":
        time = function.time()
        return time

    if p_message == f"{ck}yt":
        url = 'https://www.youtube.com'
        return url

    if p_message == f"{ck}Is Brad still gay?".lower():
        responses = ['Brad is definitely the gayest human being on the planet. However, Paulie is about to take the lead.',
                     'The Gayest...', 'Brad will suck yo dick fo a nickel, son...', 'He might be....',
                     'He might not be...', 'Brad is the absolute gayest human being on the planet Earth.. He would suck your schlong for a nickle.']
        return random.choice(responses)

    if p_message == f"{ck}Who is the gayest of us all?".lower():
        responses = ['@paulie#3126, without a doubt.', 'Still @paulie#3126', 'Definitely @paulie#3126',
                     'That award goes to @paulie#3126', 'Maybe @Jiko#4922... But definetely @paulie#3126',
                     '@paulie#3126 should get to know @Brad#4859']
        return random.choice(responses)

    if p_message == f'{ck}commands':
        return str('''```Commmands:
        !help - Displays List of Command
        !boab - Query BOAB - Ask anything!
        !date - Displays Todays Date (Weekday, d/m/yyyy, Time)
        !quote - Gives you a random quote to uplift your spirit!
        !donate - Donate to Jiko's Tooth Fund!
        !slap - Bitch slaps another user. - Example: !slap @paulie
        !clear - Deletes messages. - Example: !clear 10 (Clears last 10 messages in the channel)
        !userinfo - Provides info about @USER. Example: !userinfo @Name#1234
        !lottery - Chooses this weeks winning Lotto Numbers! (Hopefully)
        !insult - Insult @USER. Example: !insult @NAME#1234 
        !roll - Rolls a dye (Random Number: 1-6)
        !coinflip - Flips a coin. (Heads/Tails)
        !yt - Query YouTube videos.
        !google - Query Google. 
        !check - Checks to see if BOAB is alive.
        There are some hidden commands - Ask Mazz about them!```
        ''')

    # return 'I didn\'t understand what you wrote. Try typing"!help".'
