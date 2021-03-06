import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
from time import sleep
from telebot.web import get_alert
global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
# def respond():
#    # retrieve the message in JSON and then transform it to Telegram object
#    update = telegram.Update.de_json(request.get_json(force=True), bot)

#    chat_id = update.message.chat.id
#    msg_id = update.message.message_id

#    # Telegram understands UTF-8, so encode text for unicode compatibility
#    text = update.message.text.encode('utf-8').decode()
#    # for debugging purposes only
#    print("got text message :", text)
#    # the first time you chat with the bot AKA the welcoming message
#    if text == "/start":
#        # print the welcoming message
#        bot_welcome = """
#        Welcome to Chull bot, made by Shubrah. The bot is using the service from http://avatars.dicebear.com/ to generate cool looking avatars based on the name you enter. Start with typing your name.
#        """
#        # send the welcoming message
#        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)


#    else:
#        try:
#            # clear the message we got from any non alphabets
#            text = re.sub(r"\W", "_", text)
#            # create the api link for the avatar based on http://avatars.adorable.io/
#            url = "https://avatars.dicebear.com/api/open-peeps/{}.png".format(text.strip())
#            # reply with a photo to the name the user sent,
#            # note that you can send photos by url and telegram will fetch it for you
#            bot.sendChatAction(chat_id=chat_id, action="typing")
#            sleep(0.5)
#            bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
#        except Exception:
#            # if things went wrong
#            bot.sendMessage(chat_id=chat_id, text="There was a problem, stay tuned", reply_to_message_id=msg_id)


#    return 'ok'



def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
#    if text == "/info":
# #        # print the welcoming message
#        bot_welcome = """
#        Welcome to Chull bot, made by Shubrah. The bot notifies with the availability of tickets for Spider NWH in Patna for the dates 26, 27, 28, 29 December
#        """
#        # send the welcoming message
#        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
   # for debugging purposes only
   print("got text message :", text)
   # here call your smart reply message
   reply = get_alert()
   bot.sendMessage(chat_id=chat_id, text=reply, reply_to_message_id=msg_id)



@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
   s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if s:
       return "webhook setup chill vmro"
   else:
       return "webhook setup failed, kat gya"

@app.route('/')
def index():
   return 'Chal gya vro, pawry kro'


if __name__ == '__main__':
   app.run(threaded=True)