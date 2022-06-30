import mysql.connector, time, datetime, asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='5303733211:AAGWjltJu7TnjA1DonWMp18KYyZSDDq0i0c')
dp = Dispatcher(bot, storage = MemoryStorage())

""" states for order_id request"""
class OrderRequest(StatesGroup):
    waiting_for_order_id = State()
    order_id_got = State()


"""DB connect"""
conn = connect(host="localhost",
		user="cy70928_phoenix",
        password="Donteverfakeit000",
        port=3306,
        database="cy70928_phoenix")
cursor = conn.cursor()
#id of last executed order
executed = 0


"""DB funcs"""

async def timer(message: types.Message):
    """timer for db upgrade"""
    while True:
        #test
        limit = 30
        #final
        #limit = 10800 #3 hours
        time.sleep(limit)
        await db_count(message)   

async def db_count(message: types.Message): 
    """execute last order's id's"""
    cursor.execute("SELECT id FROM orders_order")
    tmp = cursor.fetchall()
    for i in tmp:
        last_order = i[0]
    await db_updater(last_order, message)

async def db_updater(last_order, message):
    """check db for new orders and take all new orders"""
    global executed
    if last_order > executed:
        cursor.execute("SELECT id FROM orders_order WHERE ?<id", (executed, ))
        new_orders = cursor.fetchall()
        while executed != last_order:
            for i in new_orders:
                order_id = i[0]
                print('last orders',order_id) #test
                await message.reply('Новый заказ')
                await get_order_info(message, order_id)
                executed = order_id
                print('ex', executed) #test

async def get_order_info (message, order_id):
    """search order by id"""
    try:
        
        #execute customer's data
        cursor.execute("""SELECT id, first_name, last_name, email, 
                    city, address, postal_code, created, comment, delivery_price 
                    FROM orders_order WHERE id=?""", (order_id,))
        customer_data = cursor.fetchall()
        #execute items data
        cursor.execute("""SELECT main_item.title, orders_orderitem.quantity, orders_orderitem.total_price
                       FROM main_item INNER JOIN orders_orderitem 
                        ON main_item.id=orders_orderitem.product_id WHERE orders_orderitem.order_id=?""", (order_id,))
        item_data = cursor.fetchall() 
        #print('data has been received')# test              
        await message.reply(f'Данные клиента: {customer_data} \n Товары: {item_data}') 
                                        
    except:
        await message.reply('Заказ не найден')

async def last_orders (message: types.Message):
    """orders from week ago to yesterday"""
    #test
    start = datetime.timedelta(hours=1)
    period = start - datetime.timedelta(minutes=30)
    #start = datetime.datetime.now()
    #period = start - datetime.timedelta(days=6)
    cursor.execute("SELECT id FROM orders_order WHERE created BETWEEN ? AND ?", (period, start, ))
    order_ids=cursor.fetchall()
    for i in order_ids:
        order_id = i[0]
        await get_order_info(message, order_id)

"""commands"""


async def start(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}! Для продолжения введи команду.\n Список команд доступен по команде /help')


async def help(message: types.Message):
    commands = ['/start', '/help', '/orderinfo', '/lastorders']
    service_commands = ['/timer', '/db_count']
    await message.reply(f'Доступные команды: \n {commands} \n Служебные команды: \n {service_commands}')
         
async def get_order_id(message: types.Message):
    """requests for order_id by command"""
    await message.reply('Введи номер заказа')
    await OrderRequest.waiting_for_order_id.set()
    

async def order_info(message: types.Message, state: FSMContext):
    """saves order_id and calls get_order_info func"""
    if message.text.isnumeric():
        order_id = int(message.text)
        #print(order_id)
        await OrderRequest.next()
        #print('saved') #test
        await get_order_info(message, order_id)
    else:
        print('incorrect input') #test
        await message.answer('Неверный ввод')


"""command handlers"""
dp.register_message_handler(start, commands='start', state='*')
dp.register_message_handler(help, commands='help', state='*')
dp.register_message_handler(get_order_id, commands="orderinfo", state="*")
dp.register_message_handler(last_orders, commands='lastorders', state='*')
dp.register_message_handler(timer, commands='timer', state='*')
dp.register_message_handler(order_info, state=OrderRequest.waiting_for_order_id)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)