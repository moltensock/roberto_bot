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

req = []
shop = [{'sender': 313354983,
         'balance': 1000,
         'is_true_sides': 0,
         'is_true_deaths': 0},
        {'sender': 605574836,
         'balance': 1000,
         'is_true_sides': 0,
         'is_true_deaths': 0},
        {'sender': 263861517,
         'balance': 1000,
         'is_true_sides': 0,
         'is_true_deaths': 0},
        {'sender': 447434376,
         'balance': 1000,
         'is_true_sides': 0,
         'is_true_deaths': 0},
        {'sender': 338010077,
         'balance': 1000,
         'is_true_sides': 0,
         'is_true_deaths': 0}
        ]
total = []
group = 210073314
totalize = 0
totalize_max = 0
totalize_side = 0
total_side = 'ТОТАЛИЗАТОР НА СТОРОНЫ:\n'

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

        if rm == "оформить заявку":
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
                shop.append(dict(sender=sender, balance=0, is_true_sides=0, is_true_deaths=0))  # creating player's slot
                send_message(sender, 'Поздравляю, у тебя появился кошелёк. Держи ухо востро: скоро там появятся '
                                     'деньги! Если они, конечно, у тебя были...')
                for admin in admins:
                    mes = f'Игрок {sayer_name} (id{sender}) создал кошелёк и хочет деняк'
                    send_message(admin, mes)
        elif rm[:2] == 'id':
            for i in range(len(admins)):
                if sender == admins[i]:
                    rm = rm[2:]
                    k = rm.split(' ')
                    ending1 = find_ending(k[1])
                    for j in range(len(shop)):
                        if shop[j - 1]['sender'] == int(k[0]):
                            shop[j - 1]['balance'] += int(k[1])
                            bal = shop[j - 1]['balance']
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
            keyboard.add_button('Бондаж', color=VkKeyboardColor.PRIMARY)
            keyboard.add_button('Прослушка', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Проклятие')
            keyboard.add_button('Амулет')
            keyboard.add_line()
            keyboard.add_button('Больше предметов', color=VkKeyboardColor.PRIMARY)
            send_button(sender, "текст текст текст текст текст текст текст текст текст текст текст")
        elif rm == 'больше предметов':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Заказная статья')
            keyboard.add_line()
            keyboard.add_button('Бутылка водки', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Сыворотка правды')
            keyboard.add_line()
            keyboard.add_button('Убийство проверяющего', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Вернуться к списку предметов')
            send_button(sender, "текст текст текст текст текст текст текст текст текст текст текст")
        elif rm[:13] == 'обнулить банк':
            rm = rm[14:]
            for i in range(len(admins)):
                if sender == admins[i]:
                    if rm == 'смертей':
                        totalize = 0
                        total = []
                        totalize_max = 0
                        for i in range(len(shop)):
                            shop[i - 1]['is_true_deaths'] = 0
                        send_message(sender, 'Банк тотализатора смертей обнулён. Мы готовы к новой фазе!')
                    elif rm == 'сторон':
                        totalize_side = 0
                        total_side = 'ТОТАЛИЗАТОР НА СТОРОНЫ:\n'
                        for i in range(len(shop)):
                            shop[i - 1]['is_true_sides'] = 0
                        send_message(sender, 'Банк тотализатора сторон обнулён. Мы готовы к новой фазе!')
        elif rm[:14] == 'обнулить людей':
            rm = rm[15:]
            for i in range(len(admins)):
                if sender == admins[i]:
                    if rm == 'смерти':
                        total = []
                        totalize_max = 0
                        for i in range(len(shop)):
                            shop[i - 1]['is_true_deaths'] = 0
                        send_message(sender, 'Банк тотализатора смертей сохранён. Мы готовы к новой фазе!')
                    elif rm == 'стороны':
                        total_side = 'ТОТАЛИЗАТОР НА СТОРОНЫ:\n'
                        for i in range(len(shop)):
                            shop[i - 1]['is_true_sides'] = 0
                        send_message(sender, 'Банк тотализатора сторон сохранён. Мы готовы к новой фазе!')
        elif rm == 'ставки тотализатора':
            for k in range(len(admins)):
                if sender == admins[k]:
                    itogs = 'СПИСОК АЗАРТНЫХ ИГРОКОВ:\n\n'
                    print(total)
                    for i in range(totalize_max + 1):
                        for j in range(len(total)):
                            if total[j - 1][1] == i:
                                itogs += f'{i}: {total[j - 1][0]}\n'
                        itogs += '\n'
                    itogs += '\n' + total_side
                    send_message(sender, itogs)
        elif rm == 'тотализатор' or rm == 'количество смертей' or rm == 'стороны умерших' or rm[:6] == 'вангую' or rm == 'cветлые' or rm == 'cерые' or rm == 'tёмные' or rm == 'cветлые и тёмные' or rm == 'cерые и светлые' or rm == 'tёмные и серые' or rm == 'bсе стороны':
            hour = int(datetime.datetime.today().strftime('%H'))
            # minute = int(datetime.datetime.today().strftime('%M'))
            if hour == 22 or hour == 16:
                if rm == 'тотализатор':
                    keyboard = VkKeyboard(inline=True)
                    keyboard.add_button('Количество смертей')
                    keyboard.add_line()
                    keyboard.add_button('Стороны умерших', color=VkKeyboardColor.PRIMARY)
                    send_button(sender, 'На что ты хочешь поставить?')
                elif rm == 'стороны умерших':
                    keyboard = VkKeyboard(inline=True)
                    keyboard.add_button('Cветлые')
                    keyboard.add_button('Tёмные')
                    keyboard.add_line()
                    keyboard.add_button('Cерые', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Cветлые и тёмные')
                    keyboard.add_line()
                    keyboard.add_button('Cерые и светлые', color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button('Tёмные и серые')
                    keyboard.add_line()
                    keyboard.add_button('Bсе стороны', color=VkKeyboardColor.PRIMARY)
                    send_button(sender, 'Выбери, кто сегодня потеряет игроков (стоимость ставки: 5 делликов):')
                    # for i in range(len(shop)):
                    #     if shop[i - 1]['sender'] == sender:
                    #         shop[i - 1]['is_true_sides'] = 1
                elif rm == 'cветлые' or rm == 'cерые' or rm == 'tёмные' or rm == 'cветлые и тёмные' or rm == 'cерые и светлые' or rm == 'tёмные и серые' or rm == 'bсе стороны':
                    for i in range(len(shop)):
                        if shop[i - 1]['sender'] == sender:
                            if shop[i - 1]['is_true_sides'] == 0:
                                if shop[i - 1]['balance'] - 5 >= 0:
                                    shop[i - 1]['balance'] -= 5
                                    bal = shop[i - 1]['balance']
                                    totalize_side += 5
                                    total_side += f'{sayer_name}\n — {rm.capitalize()}'
                                    ending = find_ending(shop[i - 1]['balance'])
                                    send_message(sender, f'Твоя ставка: {rm.capitalize()} потеряют игрока. '
                                                         f'\nТекущий баланс: {bal} деллик{ending}.\nСпасибо за участие '
                                                         f'и да пребудет с тобой удача! ')
                                    shop[i - 1]['is_true_sides'] = 1
                                    ending2 = find_ending(totalize_side)
                                    for admin in admins:
                                        mes = f'Новая ставка в тотализатор (стороны)\n{sayer_name} vk.com/id{sender}\n\nСторона: {rm.capitalize()}\nТекущий банк: {totalize_side} деллик{ending2} '
                                        send_message(admin, mes)
                                else:
                                    send_message(sender,
                                                 'На твоём счёте недостаточно делликов для участия. Попробуй '
                                                 'уменьшить ставку!')
                            else:
                                send_message(sender, 'Твоя ставка уже учтена! Приходи в следующий раз.')
                elif rm == 'количество смертей':
                    for i in range(len(shop)):
                        if shop[i - 1]['sender'] == sender:
                            ending = find_ending(shop[i - 1]['balance'])
                            bal = shop[i - 1]['balance']
                            message = f'Твой баланс: {bal} деллик{ending}. Напиши \"Вангую [число смертей] [' \
                                      f'ставка в делликах]\", чтобы участвовать в тотализаторе на итоги. Пример: ' \
                                      f'Вангую 3 10 — для ставки в размере 10 делликов на смерть 3 игроков.'
                            send_message(sender, message)
                elif rm[:6] == 'вангую':
                    rm = rm[7:]
                    try:
                        rm = rm.split(' ')
                    except IndexError:
                        send_message(sender, 'Ой! Что-то пошло не так...')
                    except ValueError:
                        send_message(sender, 'Ой! Что-то пошло не так...')
                    for i in range(len(shop)):
                        if shop[i - 1]['sender'] == sender:
                            print('k')
                            if shop[i - 1]['is_true_deaths'] == 0:
                                print('a')
                                ending1 = find_ending(rm[1])
                                if shop[i - 1]['balance'] - int(rm[1]) >= 0 and int(rm[1]) > 0:
                                    shop[i - 1]['balance'] -= int(rm[1])
                                    totalize += int(rm[1])
                                    shop[i - 1]['is_true_deaths'] = 1
                                    total.append([sayer_name, int(rm[0])])
                                    if int(rm[1]) > totalize_max:
                                        totalize_max = int(rm[1])
                                    ending3 = find_ending(totalize)
                                    ending2 = find_ending(shop[i - 1]['balance'])
                                    bal = shop[i - 1]['balance']
                                    message = f'Твоя ставка: {rm[1]} деллик{ending1}. Количество смертей: {rm[0]}.\n ' \
                                              f'Текущий баланс: {bal} деллик{ending2}.\nСпасибо за участие и да ' \
                                              f'пребудет с тобой удача! '
                                    send_message(sender, message)
                                    for admin in admins:
                                        mes = f'Новая ставка в тотализатор (смерти)\n{sayer_name} vk.com/id{sender}\n\nРазмер ' \
                                              f'ставки: {rm[1]} деллик{ending1}\nКоличество смертей: {rm[0]}\n\n' \
                                              f'Текущий банк: {totalize} деллик{ending3} '
                                        send_message(admin, mes)
                                else:
                                    send_message(sender,
                                                 'На твоём счёте недостаточно делликов для участия. Попробуй '
                                                 'уменьшить ставку!')
                            elif shop[i - 1]['is_true_deaths'] == 1:
                                send_message(sender, 'Твоя ставка уже учтена! Приходи в следующий раз.')
            else:
                send_message(sender, 'Тотализатор пока не работает. Попробуй позже')
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