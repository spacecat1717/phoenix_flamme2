import sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


"""DB connect"""
conn = sqlite3.connect('/home/spacecat/CODE/phoenix_flamme2/phoenix_db3', check_same_thread=False)
cursor = conn.cursor()

"""DB funcs"""
def get_order_info (update,order_id):
    try:
        
        #execute customer's data
        cursor.execute("""SELECT id, first_name, last_name, email, 
                    city, address, postal_code, created, paid, comment 
                    FROM orders_order WHERE id=?""", (order_id,))
        customer_data = cursor.fetchall()
        #execute items data
        cursor.execute("""SELECT main_item.title, orders_orderitem.quantity, orders_orderitem.price
                       FROM main_item INNER JOIN orders_orderitem 
                        ON main_item.id=orders_orderitem.product_id WHERE orders_orderitem.order_id=?""", (order_id,))
        item_data = cursor.fetchall()                 
        print(cursor.fetchall())
        update.message.reply_text(f'Данные клиента:\n{customer_data}\nТовары:\n{item_data}')
    except:
        update.message.reply_text('Заказ не найден')

"""commands"""
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f'Привет, {first_name}!')
    update.message.reply_text('Для продолжения введи команду.\n Список команд доступен по команде /help')

def help(update, context):
    #orderinfo - upload info by order number
    #sendtrack - email to customer with track num
    #lastorders - orders for last week from DB
    commands = ['/start', '/help', '/orderinfo', '/sendtrack', '/lastorders']
    update.message.reply_text(f'Доступные команды: \n {commands}')

def orderinfo(update, context):
    #update.message.reply_text('Введи номер заказа')
    order_id = int(update.message.text)
    get_order_info(update, order_id)
    
    
"""destribute user's text to func"""
def distributor(update, context):
    update.message.reply_text('Введи номер заказа')
    text_received = update.message.text
    if text_received.isnumeric():
        orderinfo(update, text_received)

"""main func"""
def main():
    TOKEN = "token here"
    #create updater
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    #handlers for base commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    #handlers for custom commands
    dispatcher.add_handler(CommandHandler('orderinfo', distributor))
    #text handler
    dispatcher.add_handler(MessageHandler(Filters.text, distributor))
    #activate updates
    updater.start_polling()
    #run
    updater.idle()

if __name__=='__main__':
    main()