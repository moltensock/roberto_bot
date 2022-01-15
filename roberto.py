intro = "текст"
kill1 = "Убийство\nФаза активации: любая\nДействие контракта: ты заключишь контракт с " \
        "синьором Бесом, и единоразово он уберёт с твоей дороги одного твоего врага.\nДополнительно: активируется в " \
        "текущую фазу на любого игрока. "
heal1 = "Исцеление\nФаза активации: ночная\nДействие контракта: ты заключишь контракт с " \
        "донной Тарой, и единоразово в трансплантологической клинике тебе, или игроку по твоему выбору, осуществят " \
        "пересадку из подпольного банка органов.\nДополнительно: можно использовать как на себя, так и на другого " \
        "игрока. Активируется только в ночную фазу, можно оставить распоряжение на активацию в следующую с указанием " \
        "точных условий активации. "
find1 = "Раскрытие роли\nФаза активации: любая\nДействие контракта: ты заключишь контракт с " \
        "доном Алом, и единоразово он раскроет тебе роль человека, на которого ты укажешь.\nДополнительно: при " \
        "сообщении результата держателю контракта, действия роли Миледи не учитываются. Активируется в текущую фазу, " \
        "результат приходит после окончания фазы, но до итогов (день – 16:00, ночь – 22:00). "
close1 = "Подмена роли\nФаза активации: любая\nДействие контракта: ты заключишь контракт к " \
         "синьором Рабастаном, и единоразово он подменит ваше досье в случае проверки.\nДополнительно: можно " \
         "использовать как на себя, так и на другого игрока. При активации контракта вы заблаговременно указываете " \
         "желаемую роль. Именно она будет сообщаться игроку, решившему вас проверить. В случае проверки Шерифа или " \
         "Дона результатом проверки будет сторона выбранной вами роли "
immune1 = "Иммунитет\nФаза активации: дневная\nДействие контракта: ты заключишь контракт с " \
          "синьориной Кэнди, и единоразово синьорина Кэнди подарит тебе экскурсию по своему заведению. Это время ты " \
          "проведёшь безопасно… и сладко.\nДополнительно: можно использовать как на себя, так и на другого игрока. " \
          "Активируется только в дневную фазу. При активации контракта вы, или другой игрок, на которого вы " \
          "активируете контракт, будете под защитой от любого воздействия – лечение, убийство, проверка, и так далее, " \
          "но, если у вас активная дневная роль и фаза активации совпала с ходом вашей роли, вы также не сможете " \
          "совершать каких-либо действий. Контракт лишает вас права голоса на дневном голосовании. "
vote1 = "Дополнительные голоса\nФаза активации: дневная\nДействие контракта: ты заключишь контракт с синьором " \
        "Питером, и единоразово он внесёт правки в листы " \
        "голосования, добавив шесть голосов к твоему голосу.\nДополнительно: голоса можно активировать только на того " \
        "игрока, против которого вы голосовали. "

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def send_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})


def send_button(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                       'keyboard': keyboard.get_keyboard()})


def send_sticker(sender, sticker):
    authorize.method('messages.send', {'user_id': sender, 'sticker_id': sticker, 'random_id': get_random_id()})


def get_name(sayer_id):
    sender_info = getting_api.users.get(user_ids=sayer_id)[0]
    full_name = sender_info.get('first_name') + ' ' + sender_info['last_name']
    return full_name


def find_ending(num):
    num = int(num)
    ending = 'ов'
    if num % 10 == 1:
        ending = ''
    elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        ending = 'а'
    return ending


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
req = []
shop = []
group = 210073314
au = 0

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

        if rm == "аукцион":
            i = 0
            for i in range(len(admins)):
                if sender == admins[i]:
                    au = 1
                    kill0 = 8
                    heal0 = 7
                    find0 = 7
                    close0 = 5
                    immune0 = 7
                    vote0 = 8

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
        elif rm == "хочу контракт" and au == 1:
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
            send_button(sender, "текстааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа")
        elif rm == "список" and au == 1:
            for i in range(len(admins)):
                if sender == admins[i]:
                    itog = finally_end()
                    send_message(sender, itog)
        elif rm[-9:] == "– забрать" and au == 1:
            false = 0
            k = 0
            for k in range(len(ids)):
                if sender == ids[k]:
                    send_message(sender, "текст")
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
                if count == 43:
                    au = 0
                    itog = finally_end()
                    for admin in admins:
                        send_message(admin, itog)
        elif rm == 'аукцион стоп':
            au = 0
            itog = finally_end()
            for admin in admins:
                send_message(admin, itog)
        elif rm == "оформить заявку":
            for i in range(len(req)):
                sender_id = req[i - 1]['sender']
                if sender_id == sender:
                    req.pop(i - 1)
                    break
            req.append(dict(sender=sender))  # creating player's slot
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Эви')
            keyboard.add_button('Черри')
            keyboard.add_button('Нат')
            keyboard.add_line()
            keyboard.add_button('Кирена')
            keyboard.add_button('Трики')
            send_button(sender, "🔪 [Шаг 1] Кто твой ведущий?")
        elif rm == "лавка роберто":
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Магазин')
            keyboard.add_button('Ставка')
            keyboard.add_line()
            keyboard.add_button('Тотализатор')
            keyboard.add_button('Баланс')
            send_button(sender, "текст")
        elif rm == 'баланс':
            ex = 0
            for i in range(len(shop)):
                if shop[i - 1]['sender'] == sender:
                    ex = 1
                    ending = find_ending(shop[i - 1]['balance'])
                    bal = shop[i - 1]['balance']
                    message = f'Твой баланс: {bal} деллик{ending}'
                    send_message(sender, message)
            if ex == 0:
                shop.append(dict(sender=sender, balance=0))  # creating player's slot
                send_message(sender, 'Поздравляю, у тебя появился кошелёк. Держи ухо востро: скоро там появятся '
                                     'деньги! Если они, конечно, у тебя были...')
        elif rm[:2] == 'id':
            for i in range(len(admins)):
                if sender == admins[i]:
                    rm = rm[2:]
                    k = rm.split(' ')
                    ending1 = find_ending(k[1])
                    for i in range(len(shop)):
                        if shop[i - 1]['sender'] == int(k[0]):
                            shop[i - 1]['balance'] += int(k[1])
                            bal = shop[i - 1]['balance']
                            ending2 = find_ending(bal)
                            message = f'Твой счёт пополнен на {k[1]} деллик{ending1}. Текущий баланс: {bal} деллик{ending2}'
                            adm = f'Баланс игрока vk.com/id{k[0]} пополнен на {k[1]} деллик{ending1}'
                            send_message(int(k[0]), message)
                            send_message(sender, adm)
                            send_message(313354983, adm)
        elif rm == 'магазин' or rm == 'вернуться к списку предметов':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Афера')
            keyboard.add_button('Кукла Вуду')
            keyboard.add_line()
            keyboard.add_button('Бондаж')
            keyboard.add_button('Прослушка')
            keyboard.add_line()
            keyboard.add_button('Проклятие')
            keyboard.add_button('Амулет')
            keyboard.add_line()
            keyboard.add_button('Больше предметов')
            send_button(sender, "текст текст текст текст текст текст текст текст текст текст текст")
        elif rm == 'больше предметов':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Заказная статья')
            keyboard.add_line()
            keyboard.add_button('Бутылка водки')
            keyboard.add_line()
            keyboard.add_button('Сыворотка правды')
            keyboard.add_line()
            keyboard.add_button('Убийство проверяющего')
            keyboard.add_line()
            keyboard.add_button('Вернуться к списку предметов')
            send_button(sender, "текст текст текст текст текст текст текст текст текст текст текст")
        else:
            for i in range(len(req)):
                sender_id = req[i - 1]['sender']
                if sender_id == sender:  # clarify if they're making a request
                    if rm == 'черри' or rm == 'эви' or rm == 'трики' or rm == 'кирена' or rm == 'нат':
                        req[i - 1]['host'] = rm.capitalize()
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Активное действие')
                        keyboard.add_line()
                        keyboard.add_button('Распоряжение')
                        send_button(sender, "❄ [Шаг 2] Что тебя интересует в этот раз?")
                    elif rm == 'активное действие':
                        req[i - 1]['type'] = 'Активное действие'
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Ход роли')
                        keyboard.add_line()
                        keyboard.add_button('Активация контракта')
                        send_button(sender, "❄ [Шаг 3] Какое действие ты хочешь совершить?")
                    elif rm == 'распоряжение':
                        req[i - 1]['type'] = 'Распоряжение на время отсутствия'
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('День')
                        keyboard.add_button('Ночь')
                        send_button(sender, '❄ [Шаг 3] Уточни фазу, в которую ты будешь отсутствовать.')
                    elif rm[:4] == 'день' or rm[:4] == 'ночь':
                        req[i - 1]['phase'] = rm
                        send_message(sender,
                                     "❄ [Шаг 4] На какой случай ты оставляешь распоряжение. \nОбязательно! Начни со "
                                     "слова \"Если\". Пример: если в меня будут стрелять. Если будут убивать "
                                     "члена моей команды. Если меня будут проверять и т.п.")
                    elif rm[:4] == 'если':
                        req[i - 1]['condition'] = rm
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Ход роли')
                        keyboard.add_line()
                        keyboard.add_button('Активация контракта')
                        send_button(sender, "❄ [Шаг 5] Какое действие нужно исполнить?")
                    elif rm == 'ход роли':
                        req[i - 1]['activity'] = rm
                        if req[i - 1]['type'] == 'Активное действие':
                            a = 4
                        else:
                            a = 6
                        send_message(sender,
                                     '❄ [Шаг {}] Уточни свою роль.\nОбязательно! Начни со слова \"Роль\". Пример: \"Роль '
                                     'дон\", \"Роль журналист\" и т.п.'.format(a))
                    elif rm == 'активация контракта':
                        req[i - 1]['activity'] = rm
                        if req[i - 1]['type'] == 'Активное действие':
                            a = 4
                        else:
                            a = 6
                        send_message(sender, '❄ [Шаг {}] Уточни используемый контракт.\nОбязательно! Начни со слова '
                                             '\"Контракт\". Пример: \"Контракт иммунитет\", \"Контракт слежка\" и т.п.'.format(
                            a))
                    elif rm[:4] == 'роль' or rm[:8] == 'контракт':
                        req[i - 1]['item'] = rm
                        if req[i - 1]['type'] == 'Активное действие':
                            a = 5
                        else:
                            a = 8
                        send_message(sender,
                                     '❄ [Шаг {}] На кого направлено твоё действие? Необходимо указать ссылку на '
                                     'страницу выбранного игрока (в формате https://vk.com/id) и его имя. '
                                     '\nПример: https://vk.com/nastya_vorobushek Кирена\nЕсли тебе нужно '
                                     'указать двух игроков, также указывай сначала ссылки: '
                                     'https://vk.com/nastya_vorobushek с Кирены https://vk.com/cherrss на '
                                     'Черри\nЕсли ты хочешь сходить на себя, так и напиши: На себя. Указывать '
                                     'на себя ссылку не нужно.\nЕсли ты используешь рацию, то напиши, на какую роль '
                                     'ты её используешь. Пример: На революционера. На шпиона'.format(a))
                    elif rm[:15] == 'https://vk.com/' or rm[:3] == 'на ':
                        req[i - 1]['victim'] = received_message
                        type_of = req[i - 1]['type'].capitalize()
                        activity = req[i - 1]['activity'].capitalize()
                        if req[i - 1]['item'][:4] == 'роль':
                            item1 = 'Роль'
                            item1_1 = 'роли'
                            item2 = req[i - 1]['item'][5:].capitalize()
                        else:
                            item1 = 'Контракт'
                            item1_1 = 'контракта'
                            item2 = req[i - 1]['item'][9:].capitalize()
                        victim = req[i - 1]['victim']
                        host = req[i - 1]['host']
                        try:
                            phase = req[i - 1]['phase'].capitalize()
                            condition = req[i - 1]['condition'].capitalize()
                        except KeyError:
                            phase, condition = '', ''

                        if phase != '':
                            send_message(sender, "Поздравляю, твоя заявка отправлена на рассмотрение! Твой ведущий "
                                                 "напишет тебе, как только она будет принята. Напомню, "
                                                 "что ты совершаешь следующее: \n\n{} — {}\nВремя отсутствия: {}\n"
                                                 "Условие исполнения: {}\nИсполнить: Действие {} {}\nНа кого: {}".format(
                                type_of, activity, phase, condition, item1_1, item2, victim))
                            for admin in admins:
                                send_message(admin, "Новая заявка (распоряжение на время отсутствия)\n{} vk.com/id{} "
                                                    "\nДиалог: vk.com/gim{}?sel={}\n\n "
                                                    "Ведущий: {}\n\nВремя отсутствия: {}\n\nУсловие исполнения: "
                                                    "{}\n\nДействие: {}\n\n{}: {}\n\nНа кого: {}".format(
                                    sayer_name, sender, group, sender, host, phase, condition, activity, item1, item2,
                                    victim))
                        else:
                            send_message(sender, "Поздравляю, твоя заявка отправлена на рассмотрение! Твой ведущий "
                                                 "напишет тебе, как только она будет принята. Напомню, что ты "
                                                 "совершаешь следующее: \n\n{} — {}\nИсполнить: Действие {} {}\nНа кого: {}".format(
                                type_of, activity, item1_1, item2, victim))
                            for admin in admins:
                                send_message(admin, "Новая заявка\n{} vk.com/id{}\nДиалог: "
                                                    "vk.com/gim{}?sel={}\n\nВедущий: {}\n\nДействие: {}\n\n"
                                                    "{}: {}\n\nНа кого: {}".format(
                                    sayer_name, sender, group, sender, host, activity, item1, item2, victim))
                        req.pop(i - 1)
                    break
