from telebot import types

#Кнопка для отправки номера
def num_button():
    #Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #Создаем сами кнопки
    item1 = types.KeyboardButton('Поделиться контактом', request_contact=True)

    #Добавляем кнопки в пространство
    kb.add(item1)
    return kb

#Кнопка для отправки локации
def loc_button():
    # Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создаем сами кнопки
    item1 = types.KeyboardButton('Поделиться геопозицией', request_location=True)

    # Добавляем кнопки в пространство
    kb.add(item1)
    return kb

def remove():
    types.ReplyKeyboardRemove()


#Кнопки для вывода товаров
def main_menu_buttons(products_from_db):
    #Создается пространство для кнопок
    kb = types.InlineKeyboardMarkup(row_width= 2)

    #Создаем несгораюмую кнопку корзины
    cart = types.InlineKeyboardButton(text= 'Корзина', callback_data= 'cart')
    #Создать кнопки с продуктами
    all_products = [types.InlineKeyboardButton(text = f'{i[1]}', callback_data= i[1]) for i in products_from_db]

    #Объединяем кнопки с пространством
    kb.row(cart)
    kb.add(*all_products)

    #Возвращаем пространство

    return kb

#Кнопки выбора количества
def choose_product_count(current_amount=1, plus_or_minus =''):
    #Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=3)

    #Создаем несгораемые кнопки
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
    add_to_cart = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')

    #Отслеживание плюса и минуса
    if plus_or_minus == 'increment':
        new_amount = int(current_amount) + 1

        count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    elif plus_or_minus == 'decrement':
       if int(current_amount) > 1:
            new_amount = int(current_amount) - 1

            count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    #Объединяем пространства
    kb.add(minus, count, plus)
    kb.row(add_to_cart)
    kb.row(back)

    return kb

#кнопки корзины
def cart_buttons():
    #Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=1)

    #Создаем кнопки
    clear_cart = types.InlineKeyboardButton(text='Очистить корзину', callback_data='clear_cart')
    order = types.InlineKeyboardButton(text='Оформить заказ', callback_data='order')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')

    #Объединяем кнопки с пространством
    kb.add(clear_cart, order, back)
    return kb