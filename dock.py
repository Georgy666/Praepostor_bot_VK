#!/usr/bin/env python3
import vk_api
import time
import week
import const
import commands

vk = vk_api.VkApi(login=const.log, password=const.pas) # логинимся от себя
vk.auth()

values = {'out': 0,'count': 10,'time_offset': 60}

'''
1) out — если этот параметр равен 1, сервер вернет исходящие сообщения.
2) count — количество сообщений, которое необходимо получить.
3) time_offset — максимальное время, прошедшее с момента отправки сообщения до текущего момента в секундах.
4) last_message_id — идентификатор сообщения, полученного перед тем, которое нужно вернуть последним (при условии, что после него было получено не более count сообщений)
'''

response = vk.method('messages.get', values)
error_week = False
# Если переменная error_week = True, то будет выводится сообщение об устаревшем расписании

def send_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

    '''
    В vk.method мы можем вызывать любой метод из VK API и передавать параметры в виде словаря.
    В данном случае мы вызываем метод messages.send и в качестве параметров передаем id пользователя и текст сообщения.
    '''

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
        # Мы запоминаем параметр last_message_id, чтобы в следующий раз обрабатывать только новые сообщения.
    for item in response['items']:
        # цикл перебирает полученные данныне от юзера и выводит расписание
        # если сообщение от юзера совпадает со сравневаемым значением

        if response['items'][0]['body'] == 'пн' or response['items'][0]['body'] == 'Пн':
            send_msg(item['user_id'], week.mon_week)
            if error_week == True:
                send_msg(item['user_id'], commands.invalid_schedule)

        elif response['items'][0]['body'] == 'вт' or response['items'][0]['body'] == 'Вт':
            send_msg(item['user_id'], week.tue_week)
            if error_week == True:
                send_msg(item['user_id'], commands.invalid_schedule)

        elif response['items'][0]['body'] == 'ср' or response['items'][0]['body'] == 'Ср':
            send_msg(item['user_id'], week.wed_week)
            if error_week == True:
                send_msg(item['user_id'], commands.invalid_schedule)

        elif response['items'][0]['body'] == 'чт' or response['items'][0]['body'] == 'Чт':
            send_msg(item['user_id'], week.thu_week)
            if error_week == True:
                send_msg(item['user_id'], commands.invalid_schedule)

        elif response['items'][0]['body'] == 'пт' or response['items'][0]['body'] == 'Пт':
            send_msg(item['user_id'], week.fri_week)
            if error_week == True:
                send_msg(item['user_id'], commands.invalid_schedule)

        elif response['items'][0]['body'] == 'сб' or response['items'][0]['body'] == 'Сб':
            send_msg(item['user_id'], week.sat_week)
            if error_week == True:
                send_msg(item['user_id'], commands.invalid_schedule)

        elif response['items'][0]['body'] == 'Помощь' or response['items'][0]['body'] == 'помощь':
            send_msg(item['user_id'], commands.help_command)

        elif response['items'][0]['body'] == 'Куратор' or response['items'][0]['body'] == 'куратор':
            send_msg(item['user_id'], commands.number)

    time.sleep(1) # сон на 1 сек, чтобы бот отвечал не моментально

'''
Это сообщение то, что внутри него. Мы запрашиваем "user_id", чтобы отвечать
конкретному пользователю и "body", чтобы получать текст сообщения.

{u'count': 3441,
 u'items': [{u'body': u'\u041f\u0438\u0448\u0435\u043c \u0431\u043e\u0442\u0430 \u0434\u043b\u044f \u0432\u043a!',
   u'date': 1491934484,
   u'id': 7387,
   u'out': 0,
   u'read_state': 0,
   u'title': u' ... ',
   u'user_id': 23107592},
  {u'body': u'\u041f\u0440\u0438\u0432\u0435\u0442 \u0425\u0430\u0431\u0440!',
   u'date': 1491934479,
   u'id': 7386,
   u'out': 0,
   u'read_state': 0,
   u'title': u' ... ',
   u'user_id': 23107592}]}
'''
