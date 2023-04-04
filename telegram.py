import telebot
from classes.groot import Groot

import os
import dotenv
dotenv.load_dotenv()

botId = os.getenv("bot_id")
bot = telebot.TeleBot(botId, parse_mode="MARKDOWN")

WORD_LEN = 3
grootSequence = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,/'!?;:()"
assert len(grootSequence) <= 4 ** WORD_LEN
groot = Groot(grootSequence, WORD_LEN)


@bot.message_handler(func=lambda msg: True)
def getMessage(msg):
    s = msg.text
    print(f"User message: {s}")
    
    if s.startswith(".enc"):
        try:
            grootStr = groot.encode(s[4:].strip())
            bot.send_message(msg.chat.id, f"Hehe here it is `{grootStr}`. Enjoy!")
        except:
            specialTxt = "Don't do this :("
            bot.send_message(msg.chat.id, f"`{groot.encode(specialTxt)}`") 
    
    elif s.startswith(".dec"):
        plain = groot.decode(s[4:].strip())
        
        if plain == "":
            specialTxt = "Don't do this :("
            bot.send_message(msg.chat.id, f"`{groot.encode(specialTxt)}`")
        else:
            bot.send_message(msg.chat.id, "Throwing groot spell ✨✨✨")
            bot.send_message(msg.chat.id, f"{plain}")
        
    else:
        plain = groot.decode(s)
        if plain == "":
            specialTxt = "You don't seem to understand my language haha"
        else:
            specialTxt = "Voh you are learning fast"
        
        bot.send_message(msg.chat.id, f"`{groot.encode(specialTxt)}`")        


bot.infinity_polling()
