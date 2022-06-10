import sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

STATE = None
BIRTH_YEAR = 1
BIRTH_MONTH = 2
BIRTH_DAY = 3

"""Bot"""
# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f"Hi {first_name}, nice to meet you!")
    start_getting_birthday_info(update, context)
# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received') 
# function to handle normal text 
def text(update, context):
    global STATE
    if STATE == BIRTH_YEAR:
        return received_birth_year(update, context)
    if STATE == BIRTH_MONTH:
        return received_birth_month(update, context)
    if STATE == BIRTH_DAY:
        return received_birth_day(update, context)
def start_getting_birthday_info(update, context):
    global STATE
    STATE = BIRTH_YEAR
    update.message.reply_text(f"I would need to know your birthday, so tell me what year were you born in...")
def received_birth_year(update, context):
    global STATE
    try:
        today = datetime.date.today()
        year = int(update.message.text)
        
        if year > today.year:
            raise ValueError("invalid value")
        context.user_data['birth_year'] = year
        update.message.reply_text(f"ok, now I need to know the month (in numerical form)...")
        STATE = BIRTH_MONTH
    except:
        update.message.reply_text("it's funny but it doesn't seem to be correct...")
def main():
    TOKEN = ""    
    # create the updater, that will automatically create also a dispatcher and a queue to 
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))  
    # start your shiny new bot
    updater.start_polling()
    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()




