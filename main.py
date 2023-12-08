from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyBoardButton, InlineKeyboardMarkup
import telebot
from telebot import types
import datetime
import re

bot = telebot.TeleBot("6526798932:AAHFG6ljiplUv-WRuXylJG5-h_OMBSpiTSQ")

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyBoardButton(text='but1', url='vk.com')
ib2 = InlineKeyBoardButton(text='but1', url='vk.com')
ikb.add(ib1, ib2)

@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.send_message(chat_id=message.from_user.id, text="Продукт 1", reply_markup=ikb)
bot.polling(none_stop=True, interval=0)








# import telebot
#
# from telebot import types
#
# bot = telebot.TeleBot('6526798932:AAHFG6ljiplUv-WRuXylJG5-h_OMBSpiTSQ')
#
# @bot.message_handler(content_types=['text'])
#  def get_text_messages(message):
#      if message.text == "/start":
#          bot.send_message(message.from_user.id, "отвечает на страрт")
#
# def send_product_selection(message):
#     products = ['Продукт 1', 'Продукт 2', 'Продукт 3']  # Здесь нужно указать список продуктов
#     markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     for product in products:
#         markup.add(types.KeyboardButton(product))
#     bot.send_message(message.chat.id, 'Выберите нужный продукт:', reply_markup=markup)
#     bot.register_next_step_handler(message, verify_product)
#
# def verify_product(message):
#     product = message.text  # Здесь нужно проверить, содержится ли выбранный продукт в списке продуктов
#     if product in products:
#         send_address_input(message)
#     else:
#         bot.send_message(message.chat.id, 'Выберите продукт из списка:')
#         bot.register_next_step_handler(message, verify_product)
#
# def send_address_input(message):
#     bot.send_message(message.chat.id, 'Введите адрес:')
#     bot.register_next_step_handler(message, verify_address)
#
# def verify_address(message):
#     address = message.text  # Здесь нужно проверить актуальность адреса
#     if address_check_passed:  # Здесь нужно проверить, пройдена ли проверка актуальности адреса
#         send_date_selection(message)
#     else:
#         bot.send_message(message.chat.id, 'Адрес недействителен. Введите корректный адрес:')
#         bot.register_next_step_handler(message, verify_address)
#
# def send_date_selection(message):
#     dates = ['Дата 1', 'Дата 2', 'Дата 3']  # Здесь нужно указать список доступных дат
#     markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
#     for date in dates:
#         markup.add(types.KeyboardButton(date))
#     bot.send_message(message.chat.id, 'Выберите желаемую дату установки:', reply_markup=markup)
#     bot.register_next_step_handler(message, verify_date)
#
# def verify_date(message):
#     date = message.text  # Здесь нужно проверить, содержится ли выбранная дата в списке доступных дат
#     if date in dates:
#         send_time_selection(message)
#     else:
#         bot.send_message(message.chat.id, 'Выберите доступную дату из списка:')
#         bot.register_next_step_handler(message, verify_date)
#
# def send_time_selection(message):
#     times = ['Утро', 'День', 'Вечер']  # Здесь нужно указать список доступных временных промежутков
#     markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
#     for time in times:
#         markup.add(types.KeyboardButton(time))
#     bot.send_message(message.chat.id, 'Выберите желаемое время:', reply_markup=markup)
#     bot.register_next_step_handler(message, verify_time)
#
# def verify_time(message):
#     time = message.text  # Здесь нужно проверить, содержится ли выбранное время в списке доступных временных промежутков
#     if time in times:
#         send_contact_input(message)
#     else:
#         bot.send_message(message.chat.id, 'Выберите доступное время из списка:')
#         bot.register_next_step_handler(message, verify_time)
#
# def send_contact_input(message):
#     bot.send_message(message.chat.id, 'Оставьте контактный номер в формате +7 или 8:')
#     bot.register_next_step_handler(message, verify_contact)
#
# def verify_contact(message):
#     contact = message.text  # Здесь нужно проверить валидность контактного номера
#     if contact_valid:  # Здесь нужно проверить, является ли контактный номер валидным
#         send_name_input(message)
#     else:
#         bot.send_message(message.chat.id, 'Введите корректный контактный номер в формате +7 или 8:')
#         bot.register_next_step_handler(message, verify_contact)
#
# def send_name_input(message):
#     bot.send_message(message.chat.id, 'Введите имя и фамилию:')
#     bot.register_next_step_handler(message, verify_name)
#
# def verify_name(message):
#     name = message.text  # Здесь нужно проверить валидность введенного имени и фамилии
#     if name_valid:  # Здесь нужно проверить, является ли введенное имя и фамилия валидными
#         # Здесь можно сохранить все данные клиента в базу данных
#         bot.send_message(message.chat.id, 'Спасибо! Ваши данные сохранены.')
#         send_confirmation(message)
#     else:
#         bot.send_message(message.chat.id, 'Введите корректное имя и фамилию:')
#         bot.register_next_step_handler(message, verify_name)
#
# def send_confirmation(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
#     markup.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
#     bot.send_message(message.chat.id, 'Вы хотите подтвердить оформление заявки?', reply_markup=markup)
#     bot.register_next_step_handler(message, confirm_order)
#
# def confirm_order(message):
#     if message.text == 'Да':
#         # Здесь можно отправить специалистам данные оформленной заявки
#         bot.send_message(message.chat.id, 'Заявка оформлена. Спасибо!')
#     elif message.text == 'Нет':
#         bot.send_message(message.chat.id, 'Оформление заявки отменено.')
#     else:
#         bot.send_message(message.chat.id, 'Пожалуйста, выберите "Да" или "Нет":')
#         bot.register_next_step_handler(message, confirm_order)
# bot.polling(none_stop=True, interval=0)
