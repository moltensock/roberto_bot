intro = "Поздравляю с приобретением! Надеюсь, ты знаешь, что делаешь... В любом случае, на бумажке, которую ты " \
        "уносишь с собой, написано:\n\n "
kill1 = "➤Контракт: Убийство\nФаза активации: любая\nДействие контракта: Ты заключишь контракт с синьором Джо, " \
        "и единоразово он уберёт с твоей дороги одного твоего врага.\nДополнительно: Активируется в текущую фазу на " \
        "любого игрока. "
heal1 = "➤Контракт: Лечение\nФаза активации: ночная\nДействие контракта: Ты заключишь контракт с синьориной Черри, " \
        "и единоразово она даст на выбор красную и синюю ампулы, одна из которых точно залечит какую-нибудь рану. " \
        "Возможно, душевную.\nДополнительно: Можно использовать как на себя, так и на другого игрока. Активируется " \
        "только в ночную фазу. "
find1 = "➤Контракт: Раскрытие роли\nФаза активации: любая\nДействие контракта: Ты заключишь контракт с синьориной " \
        "Киреной, и единоразово она раскроет тебе роль человека, на которого ты укажешь.\nДополнительно: Активируется " \
        "в текущую фазу, результат приходит после окончания фазы, но до итогов (день – после 16:00, ночь – после " \
        "22:00). "
close1 = "➤Контракт: Подмена роли\nФаза активации: любая\nДействие контракта: Ты заключишь контракт с синьориной " \
         "Трики, и единоразово она подменит ваше досье в случае проверки.\nДополнительно: Можно использовать как на " \
         "себя, так и на другого игрока. При активации контракта вы заблаговременно указываете желаемую роль. Именно " \
         "она будет сообщаться игроку, решившему вас проверить. В случае проверки Шерифа или Дона результатом " \
         "проверки будет сторона выбранной вами роли.\nВ итогах данный контракт выходит ночью, раз в двое игровых " \
         "суток. "
immune1 = "➤Контракт: Иммунитет\nФаза активации: дневная\nДействие контракта: Ты заключишь контракт с донной Эви, " \
          "и единоразово она организует тебе поездку за город и заставит забыть обо всех интригах " \
          "Бергамо.\nДополнительно: Можно использовать как на себя, так и на другого игрока. Активируется только в " \
          "дневную фазу. При активации контракта вы, или другой игрок, на которого вы активируете контракт, " \
          "будете под защитой от любого воздействия – убийство, проверка, и так далее, но, если у вас активная " \
          "дневная роль и фаза активации совпала с ходом вашей роли, вы также не сможете совершать каких-либо " \
          "действий. Контракт лишает вас права голоса на дневном голосовании. "
vote1 = "➤Контракт: Дополнительные голоса\nФаза активации: дневная\nДействие контракта: Ты заключишь контракт с " \
        "синьором Тропой, и единоразово он внесёт правки в листы голосования, добавив шесть голосов к твоему " \
        "голосу.\nДополнительно: Голоса можно активировать только на того игрока, против которого вы голосовали. "

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime


def send_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})


def send_button(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                       'keyboard': keyboard.get_keyboard()})


def get_name(sayer_id):
    sender_info = getting_api.users.get(user_ids=sayer_id)[0]
    full_name = sender_info.get('first_name') + ' ' + sender_info['last_name']
    return full_name


def runout(sender):
    send_message(sender, "Слишком долго думаешь! Выбранный тобой предмет растворяется в воздухе прямо перед твоими "
                         "глазами. Может, стоит взять что-то другое?")


def giveaway(obj, obj1):
    obj.append(sayer_name)
    ids.append(sender)
    obj1 = intro + obj1
    send_message(sender, obj1)


def finally_end():
    itog = "Распределение контрактов:"
    itog += "\n\nИММУНИТЕТ:\n"
    for j in range(len(immune)):
        itog += immune[j] + "\n"
        j += 1
    itog += "\n\nУБИЙСТВО:\n"
    for j in range(len(kill)):
        itog += kill[j] + "\n"
        j += 1
    itog += "\n\nИСЦЕЛЕНИЕ:\n"
    for j in range(len(heal)):
        itog += heal[j] + "\n"
        j += 1
    itog += "\n\nРАСКРЫТИЕ РОЛИ:\n"
    for j in range(len(find)):
        itog += find[j] + "\n"
        j += 1
    itog += "\n\nПОДМЕНА РОЛИ:\n"
    for j in range(len(close)):
        itog += close[j] + "\n"
        j += 1
    itog += "\n\nГОЛОСА:\n"
    for j in range(len(vote)):
        itog += vote[j] + "\n"
        j += 1
    return itog


people = []
group = 210073314

token = "8d5b1a0549cd3d9528bfeccce5db1d8672f8c256a46822defab1aa2d83e4e6a177505a23a58283710742c"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
getting_api = authorize.get_api()
upload = VkUpload(authorize)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # admins = [605574836]
        admins = [313354983, 605574836, 263861517, 447434376, 338010077]
        received_message = event.text
        rm = received_message.lower()
        sender = event.user_id
        sayer_name = get_name(sender)
        hour = int(datetime.datetime.today().strftime('%H'))
        minute = int(datetime.datetime.today().strftime('%M'))

        if rm == "аукцион":
            i = 0
            for i in range(len(admins)):
                if sender == admins[i]:
                    kill0 = 0
                    heal0 = 0
                    find0 = 0
                    close0 = 2
                    immune0 = 0
                    vote0 = 1

                    kill = []
                    heal = []
                    find = []
                    close = []
                    immune = []
                    vote = []

                    people = []
                    ids = []

                    count = 0
                    for j in range(len(admins)):
                        send_message(admins[j], "Да будет аукцион!")
                        j += 1
                    break
                elif sender != admins[i]:
                    i += 1
        elif rm == "хочу контракт" and (hour == 16 and minute > 1 or hour == 17 and minute < 31):
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Иммунитет – забрать',
                                color=VkKeyboardColor.PRIMARY)  # POSITIVE зелёный, NEGATIVE красный, PRIMARY синий
            keyboard.add_button('Исцеление – забрать', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Дополнительные голоса – забрать')
            keyboard.add_line()
            keyboard.add_button('Убийство – забрать', color=VkKeyboardColor.PRIMARY)
            keyboard.add_button('Подмена роли – забрать', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Раскрытие роли – забрать')
            send_button(sender, "Ты входишь в небольшой книжный магазин на окраине Бергамо. Звоночек на двери издаёт вялый звук, но продавщица за прилавком даже не поднимает на тебя взгляд.\nТы осматриваешься и видишь у самого входа витрину, на которой большими буквами написано: \"ОТДАЁМ ДАРОМ\". На самой витрине стоят небольшие коробки с разными надписями...")
        elif rm == "список":
            for i in range(len(admins)):
                if sender == admins[i]:
                    itog = finally_end()
                    send_message(sender, itog)
        elif rm[-9:] == "– забрать" and (hour == 16 and minute > 20 or hour == 17 and minute < 31):
            false = 0
            k = 0
            for k in range(len(ids)):
                if sender == ids[k]:
                    send_message(sender, "Ты заглядываешь в коробку, но она, к твоем сожалению, оказывается пуста... Посмотри, может, что-то осталось в других?")
                    false = 1
                    break
                else:
                    k += 1
            if false != 1:
                rm = rm[:-10]
                if rm == "иммунитет":
                    if immune0 == 0:
                        runout(sender)
                    else:
                        giveaway(immune, immune1)
                        count += 1
                        immune0 -= 1
                elif rm == "убийство":
                    if kill0 == 0:
                        runout(sender)
                    else:
                        giveaway(kill, kill1)
                        count += 1
                        kill0 -= 1
                elif rm == "исцеление":
                    if heal0 == 0:
                        runout(sender)
                    else:
                        giveaway(heal, heal1)
                        count += 1
                        heal0 -= 1
                elif rm == "раскрытие роли":
                    if find0 == 0:
                        runout(sender)
                    else:
                        giveaway(find, find1)
                        count += 1
                        find0 -= 1
                elif rm == "подмена роли":
                    if close0 == 0:
                        runout(sender)
                    else:
                        giveaway(close, close1)
                        count += 1
                        close0 -= 1
                elif rm == "дополнительные голоса":
                    if vote0 == 0:
                        runout(sender)
                    else:
                        giveaway(vote, vote1)
                        count += 1
                        vote0 -= 1
                else:
                    send_message(sender, "Что-что?")
                if count == 42:
                    au = 0
                    itog = finally_end()
                    for admin in admins:
                        send_message(admin, itog)
        elif rm == 'аукцион стоп':
            au = 0
            itog = finally_end()
            for admin in admins:
                send_message(admin, itog)
