import sqlite3, time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


"""DB connect"""
conn = sqlite3.connect('/home/spacecat/CODE/phoenix_flamme2/phoenix_db3', check_same_thread=False)
cursor = conn.cursor()
#id of last executed order
executed = 0

"""DB funcs"""

def timer(update, context):
    """timer for db upgrade"""
    while True:
        limit = 10800
        time.sleep(limit)
        db_count(update)   

def db_count(update): #WORKS!
    """count lines in db table"""
    cursor.execute("SELECT id FROM orders_order")
    tmp = cursor.fetchall()
    for i in tmp:
        last_order = i[0]
    db_updater(last_order, update)

def db_updater(last_order, update):# WORKS
    """check db for new orders and take all new orders"""
    global executed
    if last_order > executed:
        cursor.execute("SELECT id FROM orders_order WHERE ?<id", (executed, ))
        new_orders = cursor.fetchall()
        while executed != last_order:
            for i in new_orders:
                order_id = i[0]
                print('last orders',order_id) #test
                update.message.reply_text('Новый заказ')
                get_order_info(update, order_id)
                executed = order_id
                print('ex', executed) #test

def get_order_info (update,order_id):
    """search order by id"""
    try:
        
        #execute customer's data
        cursor.execute("""SELECT id, first_name, last_name, email, 
                    city, address, postal_code, created, paid, comment 
                    FROM orders_order WHERE id=?""", (order_id,))
        customer_data = cursor.fetchall()
        #execute items data
        cursor.execute("""SELECT main_item.title, orders_orderitem.quantity, orders_orderitem.total_price
                       FROM main_item INNER JOIN orders_orderitem 
                        ON main_item.id=orders_orderitem.product_id WHERE orders_orderitem.order_id=?""", (order_id,))
        item_data = cursor.fetchall()                 
        return update.message.reply_text(f'Данные клиента: {customer_data} \n Товары: {item_data}')
    except:
        return update.message.reply_text('Заказ не найден')

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
    service_commands = ['/timer', '/db_count']
    update.message.reply_text(f'Доступные команды: \n {commands} \n Служебные команды: \n {service_commands}')

def orderinfo(update, context):
    order_id = int(update.message.text)
    get_order_info(update, order_id)
    
    
"""distribute user's text to func"""
def distributor(update, context): #has a conflict between this func and others
    update.message.reply_text('Введи номер заказа')
    text_received = update.message.text
    if text_received.isnumeric():
        orderinfo(update, text_received)

"""main func"""
def main():
    TOKEN = "5303733211:AAGWjltJu7TnjA1DonWMp18KYyZSDDq0i0c"
    #create updater
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    #handlers for base commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('timer', timer))
    #handlers for custom commands
    dispatcher.add_handler(CommandHandler('orderinfo', distributor))
    #text handler
    dispatcher.add_handler(MessageHandler(Filters.text, distributor))
    #TEST HANDLERS
    #dispatcher.add_handler(CommandHandler('db_count', db_count)) #execute new orders
    #activate updates
    updater.start_polling()
    #run
    updater.idle()

if __name__=='__main__':
    main()