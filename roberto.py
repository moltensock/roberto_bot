#!/usr/bin/env python
# -*- coding: utf-8 -*-

intro = "Поздравляю с приобретением! Надеюсь, ты знаешь, что делаешь... В любом случае, на бумажке, которую ты " \
        "уносишь с собой, написано:\n\n "
kill1 = "➤Контракт: Убийство\nФаза активации: любая\nДействие контракта: Ты заключишь контракт с доном Джо, " \
        "и единоразово он уберёт с твоей дороги одного твоего врага.\nДополнительно: Активируется в текущую фазу на " \
        "любого игрока. "
heal1 = "➤Контракт: Лечение\nФаза активации: ночная\nДействие контракта: Ты заключишь контракт с донной Черри, " \
        "и единоразово она даст на выбор красную и синюю ампулы, одна из которых точно залечит какую-нибудь рану. " \
        "Возможно, душевную.\nДополнительно: Можно использовать как на себя, так и на другого игрока. Активируется " \
        "только в ночную фазу. "
find1 = "➤Контракт: Раскрытие роли\nФаза активации: любая\nДействие контракта: Ты заключишь контракт с синьориной " \
        "Киреной, и единоразово она раскроет тебе роль человека, на которого ты укажешь.\nДополнительно: Активируется " \
        "в текущую фазу, результат приходит после окончания фазы, но до итогов (день – после 16:00, ночь – после " \
        "22:00). "
close1 = "➤Контракт: Подмена роли\nФаза активации: любая\nДействие контракта: Ты заключишь контракт с доном " \
         "Вероной, и единоразово он подменит ваше досье в случае проверки.\nДополнительно: Можно использовать как на " \
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
gag1 = "➤Контракт: Кляп\nФаза активации: дневная\nДействие контракта: Ты заключишь контракт с синьором Элиасом, " \
       "и единоразово он сделает так, чтобы выбранный игрок замолчал, давая тебе возможность наслаждаться его " \
       "попытками корчить смешные гримасы в попытке что-то объяснить.\nДополнительно: Выбранный игрок лишается " \
       "возможности общаться текстовыми сообщениями, в его распоряжении будут только смайлики и стикеры. " \
       "Активируется в дневную фазу, но действие оказывает на ночную. Контракт не забирает возможность сделать ход " \
       "роли. \nВ случае нарушений условий предмета игрок получает 1 плеть, исключается из рандома контрактов, а его " \
       "контракт уходит тому, кто использовал предмет. Если у игрока на руках нет контракта, он получает 2 плети. "
jour1 = "➤Контракт: Частное расследование\nФаза активации: дневная\nДействие контракта: ты заключишь контракт с " \
        "синьориной Трики, и единоразово она позволит тебе выпустить дополнительную статью " \
        "журналиста.\nДополнительно: активируется в дневную фазу (до 16:00) на любых игроков, кроме себя и тех, " \
        "кто уже был упомянут в основных статьях журналиста. "
seek1 = "➤Контракт: Слежка\nФаза активации: любая\nДействие контракта: ты заключишь контракт с синьором Антоном, " \
        "и единоразово он устроит профессиональную слежку за игроком, на которого ты укажешь.\nДополнительно: " \
        "сообщается только первое действие, совершённое игроком за фазу, будь оно действием роли или контракта. " \
        "Активируется в текущую фазу, результат приходит после её окончания, но до итогов (день – после 16:00, " \
        "ночь – после 22:00). "

vodka_end = 'А паспорт-то у тебя есть? Ладно уж...\nИнструкция к применению: Откройте бутылку и подлейте виски в ' \
            'стакан сока выбранного вами игрока. Не забудьте сделать вид, что это не вы. '
ropes_end = 'Спасибо за покупку!\nИнструкция к применению: Свяжите выбранного вами человека. При неправильной ' \
            'эксплуатации обратитесь к специалисту. Не забудьте сделать вид, что это не вы. '
curse_end = 'Спасибо за покупку!\nИнструкция к применению: Убедитесь, что правильно назвали имя, иначе можете ' \
            'испортить жизнь ни в чём неповинному человеку. В любом случае не забудьте сделать вид, что это не вы. '
pure_end = 'Спасибо за покупку!\nИнструкция к применению: Наденьте на шею себе или выбранному вами игроку. Не снимайте.'
afer_end = 'Спасибо за покупку!\nИнструкция к применению: Не отдавайте компромат в руки выбранному игроку и ' \
           'запаситесь угрожающими фразами. Не забудьте сделать вид, что это не вы. '
truth_end = 'Спасибо за покупку!\nИнструкция к применению: Подлейте интересующему вас игроку и отойдите. Он сам вам ' \
            'всё расскажет и даже не вспомнит об этом. Не забудьте сделать вид, что это не вы. '
killer_end = 'Спасибо за покупку!\nИнструкция к применению: Когда вам придёт уведомление о проверке, сделайте звонок ' \
           'Роберто, и о вашем проверяющем позаботятся. Не забудьте сделать вид, что это не вы. '
voodoo_end = 'Спасибо за покупку!\nИнструкция: Положите на Куклу Вуду волос выбранного вами игрока. Потыкайте её ' \
             'иголочкой. Ждите. Не забудьте сделать вид, что это не вы. '
cham_end = 'Спасибо за покупку!\nИнструкция к применению: Посадите Хамелеона на ровную поверхность. Закройте глаза. ' \
           'Подумайте о контракте, который вы хотите. Ждите. Молитесь.\nP.S. Надеемся, он вас не съест. '

vodka1 = '➤Предмет: Бутылка виски\nФаза активации: ночная\nОписание: Только в Лавке Роберто вам доступна ' \
         'бутылка крепкого итальянского виски из самых тайных погребов Бергамо! Купите её, и вы гарантированно ' \
         'обезвредите своего врага на следующие несколько часов.\nДополнительно: Активируется только на другого ' \
         'человека в ночную фазу. На следующий день выбранный игрок не сможет голосовать, а также общаться в игровых ' \
         'беседах и альянсах. Если у выбранного игрока активная дневная роль, он также не сможет совершить свой ход. ' \
         '\nВ случае нарушений условий предмета игрок получает 1 плеть, исключается из рандома контрактов, а его ' \
        'контракт уходит тому, кто использовал предмет. Если у игрока на руках нет контракта, он получает 2 плети. '
ropes1 = '➤Предмет: Бондаж\nФаза активации: любая\nОписание: С эксклюзивным набором БДСМ-снаряжения выбранный вами ' \
         'человек и пошевелить пальцем не сможет! Удовольствие гарантировано!\nДополнительно: Активируется в любую ' \
         'фазу, но только на другого игрока. После активации на игрока он не сможет совершить каких-либо активных ' \
         'действий, в том числе и использовать контракт или предмет. Не распространяется на действия, совершённые ДО ' \
         'применения. Не лишает выбранного игрока права голоса, если активирован ночью. В случае активации в дневную ' \
         'фазу выбранный игрок лишается права голоса.\nО том, что игрока заблокировали бондажом, ему сообщается, ' \
         'как только обрабатывается заявка. '
curse1 = '➤Предмет: Порча\nФаза активации: любая\nОписание: Вам кто-то перешёл дорогу, но марать руки о него не ' \
         'хочется? Этому есть решение! По выгодной цене специалисты из Лавки Роберто наведут порчу на неугодного вам ' \
         'игрока, и жизнь ему будет несладка.\nДополнительно: Проклятый игрок умирает вместе с Ведьмой. О проклятии ' \
         'игроку не сообщается. '
pure1 = '➤Предмет: Амулет\nФаза активации: любая\nОписание: Боитесь, что городская Ведьма положит на вас свой ' \
        'коварный глаз? С Амулетом из Лавки Роберто она перестанет быть для вас угрозой! Купите сейчас, и вы будете ' \
        'защищены от любого сглаза до конца своих дней.\nДополнительно: Игрок наделяется иммунитетом как от уже ' \
        'наложенного проклятия, так и от возможности быть проклятым. '
afer1 = '➤Предмет: Компромат\nФаза активации: ночная\nОписание: Какую информацию только ни могут нарыть люди, ' \
        'которые знают, где искать. Так вот имейте в виду: мы знаем! Обратитесь в Лавку Роберто, и мы найдём столько ' \
        'грязи на вашего человечка, что ему просто придётся действовать по вашей указке.\nДополнительно: Выбирается ' \
        'два игрока — тот, который будет голосовать, и тот, против кого будут голосовать в следующую дневную фазу. ' \
        'Жертва не имеет права говорить остальным игрокам о том, что она попала под влияние предмета. \nВ случае ' \
        'нарушений условий предмета игрок получает 1 плеть, исключается из рандома контрактов, а его контракт уходит ' \
        'тому, кто использовал предмет. Если у игрока на руках нет контракта, он получает 2 плети.'
truth1 = '➤Предмет: Сыворотка правды\nФаза активации: любая\nОписание: Магическое зелье только из отборных трав, ' \
         'под воздействием которого невозможно соврать! Хотите проверить подозрительного человека? Не доверяете ' \
         'своему союзнику? Тогда это то, что вам нужно! С помощью него вы сможете узнать, на какой стороне играет ' \
         'выбранный вами человек.\nДополнительно: Активируется в текущую фазу, результат приходит после окончания ' \
         'фазы, но до итогов (днём – после 16:00, ночью – после 22:00). О проверке игроку не сообщается. '
killer1 = '➤Предмет: Звонок киллеру\nФаза активации: любая\nОписание: У вас аллергия на проверки? Лавка Роберто ' \
        'подобрала для вас простое и гениальное решение: убейте того, кто проверяет! Результат вас приятно ' \
        'удивит!\nДополнительно: Активируется только при наличии проверки. В результате использования предмета ваша ' \
        'сторона/роль остаётся в секрете, а проверяющий вас игрок умирает, контракты Лечения и Иммунитета против ' \
        'этого предмета не действуют. Может быть использовано на другого игрока. '
voodoo1 = '➤Предмет: Кукла Вуду\nФаза активации: ночная\nОписание: Настоящий эксклюзив и лучший способ спутать ' \
          'противнику карты! С помощью Куклы Вуду вы можете перенаправить выстрел врага туда, куда только вам ' \
          'выгодно.\nДополнительно: Если игрок, использующий предмет, светлый или серый, он крадёт выстрел у мафии и ' \
          'направляет его в любого игрока по своему выбору, т.е. мафия выстрел не совершает. Если игрок, использующий ' \
          'предмет, тёмный, он крадёт выстрел у Маньяка и направляет его в любого игрока по своему выбору, ' \
          'т.е. Маньяк выстрел не совершает. Предмет можно активировать только с 18:00 до 19:00.\nЕсли обладатель ' \
          'Куклы Вуды убивает Мстителя, он умирает вместе с Мстителем. '
cham1 = '➤Предмет: Хамелеон\nФаза активации: любая\nОписание: Перед вами — уникальный зверёк, выведенный в секретных ' \
        'подземных лабораториях Бергамо. Да, внешне он похож на небольшую ящерицу, но по первому вашему желанию он ' \
        'может превратиться в то, чего вы хотите больше всего...\nДополнительно: Активируется в любую фазу. ' \
        'Выбирается контракт, действие которого нужно исполнить, и игрок, на которого будет направлено это действие. '

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime
import psycopg2


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


def get_bal(sender_):
    db_object.execute(f"SELECT balance FROM shop_table WHERE sender = {sender_}")
    bal = db_object.fetchone()[0]
    return bal


def get_balance(sender_):
    bal = get_bal(sender_)
    player_balance = f'баланс: {bal} деллик{find_ending(bal)}.'
    return player_balance


def buying(sender, item_end):
    db_object.execute("UPDATE shop_table SET balance = balance - 30 WHERE sender = {}".format(sender))
    db_connection.commit()
    db_object.execute("UPDATE shop_table SET items = 1 WHERE sender = {}".format(sender))
    db_connection.commit()
    player_balance = get_balance(sender)
    complete = item_end + f'\n\nТекущий {player_balance}'
    return complete


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
    itog += "\n\nКЛЯП:\n"
    for j in range(len(gag)):
        itog += gag[j] + "\n"
        j += 1
    itog += "\n\nСЛЕЖКА:\n"
    for j in range(len(seek)):
        itog += seek[j] + "\n"
        j += 1
    itog += "\n\nРАССЛЕДОВАНИЕ:\n"
    for j in range(len(jour)):
        itog += jour[j] + "\n"
        j += 1
    return itog


vodka = 4
ropes = 4
curse = 2
pure = 2
afer = 3
truth = 2
killer = 2
voodoo = 1
cham = 1

req = []
total = []
group = 213254137
totalize = 0
totalize_max = 0
totalize_side = 0
total_side = 'ТОТАЛИЗАТОР НА СТОРОНЫ:\n'

db_uri = 'postgres://aubkbpitosgnii:2100a90c07ce67264813bd42c5ef090455b4c91b9c965eb7ded4568f18122156@ec2-34-242-84-130.eu-west-1.compute.amazonaws.com:5432/d6oc4c6urml2ig'
db_connection = psycopg2.connect(db_uri, sslmode="require")
db_object = db_connection.cursor()

token = "49e47c560cfb951cf8ea67cf2e0a71bf73d00fb2fc51ad67c02c5bcc3332622a2f88fa1affe92302aacc0"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
getting_api = authorize.get_api()
upload = VkUpload(authorize)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # admins = [313354983]
        admins = [252868342]
        sender = event.user_id
        received_message = event.text
        rm = received_message.lower()
        sayer_name = get_name(sender)

        hour = int(datetime.datetime.today().strftime('%H')) + 3
        if hour >= 24:
            hour %= 24
        minute = int(datetime.datetime.today().strftime('%M'))

        if rm == "аукцион":
            i = 0
            for i in range(len(admins)):
                if sender == admins[i]:
                    kill0 = 6
                    heal0 = 5
                    find0 = 5
                    close0 = 4
                    immune0 = 5
                    vote0 = 6
                    gag0 = 5
                    seek0 = 3
                    jour0 = 3

                    kill = []
                    heal = []
                    find = []
                    close = []
                    immune = []
                    vote = []
                    gag = []
                    seek = []
                    jour = []

                    people = []
                    ids = []

                    count = 0
                    for j in range(len(admins)):
                        send_message(admins[j], "Да будет аукцион!")
                        j += 1
                    break
                elif sender != admins[i]:
                    i += 1
        elif rm == "хочу контракт" and (hour == 16 and minute >= 1 or hour == 17 and minute < 31):
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
            keyboard.add_button('Слежка – забрать')
            keyboard.add_line()
            keyboard.add_button('Кляп – забрать', color=VkKeyboardColor.PRIMARY)
            keyboard.add_button('Частное расследование – забрать', color=VkKeyboardColor.PRIMARY)
            send_button(sender,
                        "Ты входишь в небольшой книжный магазин на окраине города. Звоночек на двери издаёт вялый "
                        "звук, но продавщица за прилавком даже не поднимает на тебя взгляд.\nТы осматриваешься и "
                        "видишь у самого входа витрину, на которой большими буквами написано: \"ОТДАЁМ ДАРОМ\". На "
                        "самой витрине стоят небольшие коробки с разными надписями...")
        elif rm == "список":
            for i in range(len(admins)):
                if sender == admins[i]:
                    itog = finally_end()
                    send_message(sender, itog)
        elif rm[-9:] == "– забрать" and (hour == 16 and minute > 1 or hour == 17 and minute < 31):
            false = 0
            k = 0
            for k in range(len(ids)):
                if sender == ids[k]:
                    send_message(sender,
                                 "А не жирно ли тебе будет? Уходи с тем, что есть!")
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
                elif rm == "слежка":
                    if seek0 == 0:
                        runout(sender)
                    else:
                        giveaway(seek, seek1)
                        count += 1
                        seek0 -= 1
                elif rm == "кляп":
                    if gag0 == 0:
                        runout(sender)
                    else:
                        giveaway(gag, gag1)
                        count += 1
                        gag0 -= 1
                elif rm == "частное расследование":
                    if jour0 == 0:
                        runout(sender)
                    else:
                        giveaway(jour, jour1)
                        count += 1
                        jour0 -= 1
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

        elif rm == "оформить заявку" or rm == "заявка":
            for i in range(len(req)):
                sender_id = req[i - 1]['sender']
                if sender_id == sender:
                    req.pop(i - 1)
                    break
            req.append(dict(sender=sender))  # creating player's slot
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Мел')
            keyboard.add_button('Яна')
            keyboard.add_button('Егор')
            keyboard.add_line()
            keyboard.add_button('Кит')
            keyboard.add_button('Дуб')
            send_button(sender, "💊 [Шаг 1] Кто твой ведущий?")
        elif rm == "лавка роберто":
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Магазин')
            keyboard.add_button('Ставка')
            keyboard.add_line()
            keyboard.add_button('Тотализатор')
            keyboard.add_button('Баланс')
            send_button(sender, "Над твоей головой раздаётся звон дверного колокольчика, когда ты с трудом толкаешь "
                                "входную дверь. Полутёмное помещение освещается мягким янтарным светом настенных "
                                "светильников, отражаясь в стеклянных витринах расставленных вдоль стен шкафов.\nВ "
                                "глубине помещения ты замечаешь прилавок и скучающего за ним мужчину, "
                                "перелистывающего страницы потрёпанной книги. Роберто замечает тебя, лишь когда ты "
                                "подходишь вплотную к прилавку, и поднимает на тебя ехидный взгляд.\n– Чем могу быть "
                                "полезен?")
        elif rm == 'ставка':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Cвeтлые')
            keyboard.add_line()
            keyboard.add_button('Tёмныe')
            keyboard.add_line()
            keyboard.add_button('Ceрые')
            message = f'Выбери сторону, которая, по твоему мнению, одержит победу в этом сезоне:'
            send_button(sender, message)
        elif rm == 'cвeтлые' or rm == 'tёмныe' or rm == 'ceрые':
            db_object.execute(f"SELECT stav FROM shop_table WHERE sender = {sender}")
            stav = db_object.fetchone()[0]
            if stav == 0:
                bal = get_bal(sender)
                player_balance = get_balance(sender)
                rm1 = rm[:-1].capitalize()
                message = f'Твой {player_balance} Укажи, сколько ты хочешь поставить на победу {rm1}х. Напиши ' \
                          f'\"Ставка [количество делликов]\" (без кавычек). Например: Ставка 10 — для ставки ' \
                          f'в 10 делликов.\n\nДумай осторожно, второго шанса поставить у тебя не будет! '
                send_message(sender, message)
                db_object.execute("UPDATE shop_table SET side = \'{}\' WHERE sender = {}".format(rm, sender))
                db_connection.commit()
            else:
                send_message(sender, 'Больше ставку на победу стороны сделать нельзя! Надо было думать раньше!')
        elif rm[:7] == 'ставка ':
            bal = get_bal(sender)
            player_balance = get_balance(sender)
            rm = int(rm[7:])
            if bal >= rm:
                db_object.execute(f"SELECT side FROM shop_table WHERE sender = {sender}")
                side = db_object.fetchone()[0][:-1]
                db_object.execute(f"SELECT stav FROM shop_table WHERE sender = {sender}")
                stav = db_object.fetchone()[0]
                if side != '' and stav == 0:
                    bal -= rm
                    db_object.execute("UPDATE shop_table SET balance = {} WHERE sender = {}".format(bal, sender))
                    db_connection.commit()
                    db_object.execute("UPDATE shop_table SET stav = 1 WHERE sender = {}".format(sender))
                    db_connection.commit()
                    player_balance = get_balance(sender)
                    message = f'Твоя ставка на {side}х принята!\nТекущий {player_balance}'
                    send_message(sender, message)
                    for admin in admins:
                        ending = find_ending(rm)
                        mes = f'Новая ставка на победу\n{sayer_name} vk.com/id{sender}\n\nРазмер ' \
                              f'ставки: {rm} деллик{ending}\nСторона: {side}е'
                        send_message(admin, mes)
                else:
                    send_message(sender, 'Больше ставить на победу стороны нельзя! Надо было думать раньше!')
        elif rm == 'стоп ставки':
            for j in range(len(admins)):
                if sender == admins[j]:
                    db_object.execute("UPDATE shop_table SET side = 'рип' WHERE stav = 0")
                    db_connection.commit()
                    db_object.execute("UPDATE shop_table SET stav = 1 WHERE stav = 0")
                    db_connection.commit()
                    send_message(sender, 'Ставки на победу стороны больше не принимаются.')
        elif rm == 'баланс':
            db_object.execute(f"SELECT sender FROM shop_table WHERE sender = {sender}")
            result = db_object.fetchone()

            if not result:
                db_object.execute("INSERT INTO shop_table(sender, key) VALUES ({}, \'{}\')".format(sender, sayer_name))
                db_connection.commit()
                send_message(sender, 'Поздравляю, у тебя появился кошелёк. Держи ухо востро: скоро там появятся '
                                     'деньги! Если они, конечно, у тебя были...')
                mes = f'Игрок {sayer_name} (id{sender}) создал кошелёк и хочет деняк'
                send_message(252868342, mes)
                send_message (313354983, mes)

            else:
                bal = get_bal(sender)
                player_balance = 'Твой ' + get_balance(sender)
                send_message(sender, player_balance)
        elif rm[:2] == 'id':
            for j in range(len(admins)):
                if sender == admins[j]:
                    rm = rm[2:]
                    k = rm.split(' ')
                    player = int(k[0])
                    if k[1] == 'предмет':
                        db_object.execute(f"SELECT items FROM shop_table WHERE sender = {player}")
                        is_item = db_object.fetchone()[0]
                        if is_item == 1:
                            db_object.execute("UPDATE shop_table SET items = 0 WHERE sender = {}".format(sender))
                            db_connection.commit()
                            db_object.execute(f"SELECT key FROM shop_table WHERE sender = {player}")
                            name = db_object.fetchone()[0]
                            send_message(sender, 'Игрок {} использовал свой предмет'.format(name))
                        else:
                            send_message(sender, 'У этого игрока нет предмета')
                    else:
                        try:
                            ending1 = find_ending(k[1])
                            add = int(k[1])
                            db_object.execute(f"UPDATE shop_table SET balance = balance + {add} WHERE sender = {player}")
                            db_connection.commit()
                            player_balance = 'Текущий ' + get_balance(player)
                            message = f'Твой счёт пополнен на {add} деллик{ending1}. {player_balance}'
                            adm = f'Баланс игрока vk.com/id{player} пополнен на {add} деллик{ending1}'
                            send_message(int(k[0]), message)
                            send_message(sender, adm)
                            if sender != 313354983 or sender != 252868342:
                                send_message(313354983, adm)
                                send_message(252868342, adm)
                        except IndexError:
                            continue
        elif rm == 'магазин' or rm == 'вернуться к списку предметов':
            bal = get_bal(sender)
            player_balance = get_balance(sender)
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Компромат')
            keyboard.add_button('Кукла Вуду')
            keyboard.add_line()
            keyboard.add_button('Бондаж', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Порча')
            keyboard.add_button('Амулет')
            keyboard.add_line()
            keyboard.add_button('Больше предметов', color=VkKeyboardColor.PRIMARY)
            player_balance = 'Твой ' + player_balance
            message = f'Приветствую в своей лавке, дружище! Покажи-ка свой кошелёк... Хм... {player_balance} Не густо. Ладно, смотри, что у меня есть:\n\nКомпромат (шт.): {afer}\nКукла Вуду (шт.): {voodoo}\nБондаж (шт.): {ropes}\nПорча (шт.): {curse}\nАмулет (шт.): {pure}\n\nЕсли это тебя не устроит, за твоей спиной есть ещё прилавок.'
            send_button(sender, message)
        elif rm == 'больше предметов':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Хамелеон')
            keyboard.add_line()
            keyboard.add_button('Бутылка виски', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Сыворотка правды')
            keyboard.add_line()
            keyboard.add_button('Звонок киллеру', color=VkKeyboardColor.PRIMARY)
            keyboard.add_line()
            keyboard.add_button('Вернуться к списку предметов')
            message = f'Да, вот тут. Можешь рассмотреть поближе:\n\nХамелеон (шт.): {cham}\nБутылка виски (шт.): {vodka}\nСыворотка правды (шт.): {truth}\nЗвонок киллеру (шт.): {kill}\n\nЧто-то брать будешь или просто постоим? '
            send_button(sender, message)
        elif rm == 'компромат' or rm == 'кукла вуду' or rm == 'бондаж' or rm == 'хамелеон' or rm == 'порча' or rm == 'амулет' or rm == 'бутылка виски' or rm == 'сыворотка правды' or rm == 'звонок киллеру':
            keyboard = VkKeyboard(inline=True)
            keyboard.add_button('Вернуться к списку предметов')
            bal = get_bal(sender)
            player_balance = get_balance(sender)

            if rm == 'бутылка виски' and isinstance(vodka, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить бутылку виски')
                buying1 = vodka1
            elif rm == 'хамелеон' and isinstance(afer, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить хамелеона')
                buying1 = cham1
            elif rm == 'компромат' and isinstance(afer, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить компромат')
                buying1 = afer1
            elif rm == 'кукла вуду' and isinstance(voodoo, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить куклу Вуду')
                buying1 = voodoo1
            elif rm == 'бондаж' and isinstance(ropes, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить бондаж')
                buying1 = ropes1
            elif rm == 'порча' and isinstance(curse, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить порчу')
                buying1 = curse1
            elif rm == 'амулет' and isinstance(pure, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить амулет')
                buying1 = pure1
            elif rm == 'звонок киллеру' and isinstance(kill, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить звонок киллеру')
                buying1 = killer1
            elif rm == 'сыворотка правды' and isinstance(truth, str) is False:
                if bal >= 30:
                    keyboard.add_line()
                    keyboard.add_button('Kупить сыворотку правды')
                buying1 = truth1

            send_button(sender, buying1)
        elif rm[:6] == 'kупить':
            if hour == 16 or hour == 17 or hour == 22 or hour == 23:
                bal = get_bal(sender)
                player_balance = get_balance(sender)
                if bal >= 30:
                    db_object.execute(f"SELECT items FROM shop_table WHERE sender = {sender}")
                    items = db_object.fetchone()[0]
                    if items == 0:
                        rm = rm[7:]
                        if rm == 'бутылку виски' and isinstance(vodka, str) is False:
                            complete = buying(sender, vodka_end)
                            vodka -= 1
                            if vodka == 0:
                                vodka = 'SOLD OUT'
                        elif rm == 'компромат' and isinstance(afer, str) is False:
                            complete = buying(sender, afer_end)
                            afer -= 1
                            if afer == 0:
                                afer = 'SOLD OUT'
                        elif rm == 'куклу вуду' and isinstance(voodoo, str) is False:
                            complete = buying(sender, voodoo_end)
                            voodoo -= 1
                            if voodoo == 0:
                                voodoo = 'SOLD OUT'
                        elif rm == 'бондаж' and isinstance(ropes, str) is False:
                            complete = buying(sender, ropes_end)
                            ropes -= 1
                            if ropes == 0:
                                ropes = 'SOLD OUT'
                        elif rm == 'порчу' and isinstance(curse, str) is False:
                            complete = buying(sender, curse_end)
                            curse -= 1
                            if curse == 0:
                                curse = 'SOLD OUT'
                        elif rm == 'амулет' and isinstance(pure, str) is False:
                            complete = buying(sender, pure_end)
                            pure -= 1
                            if pure == 0:
                                pure = 'SOLD OUT'
                        elif rm == 'звонок киллеру' and isinstance(kill, str) is False:
                            complete = buying(sender, killer_end)
                            kill -= 1
                            if kill == 0:
                                kill = 'SOLD OUT'
                        elif rm == 'сыворотку правды' and isinstance(truth, str) is False:
                            complete = buying(sender, truth_end)
                            truth -= 1
                            if truth == 0:
                                truth = 'SOLD OUT'
                        elif rm == 'хамелеона' and isinstance(cham, str) is False:
                            complete = buying(sender, cham_end)
                            cham -= 1
                            if cham == 0:
                                cham = 'SOLD OUT'

                        send_message(sender, complete)
                        for admin in admins:
                            message = f'Новая покупка предмета\n{sayer_name} vk.com/id{sender}\n\nКупили: {rm}'
                            send_message(admin, message)
                    else:
                        send_message(sender,
                                     'У тебя уже есть предмет на руках! Сначала используй его, потом поговорим.')
                else:
                    send_message(sender, 'Ишь ты, чего хочешь! Иди денег сначала заработай!')
            else:
                send_message(sender, 'В данный момент магазин не работает. Попробуй позже.')
        elif rm[:14] == 'обнулить людей':
            rm = rm[15:]
            for admin in admins:
                if sender == admin:
                    if rm == 'смерти':
                        total = []
                        totalize_max = 0
                        db_object.execute("UPDATE shop_table SET is_true_deaths = 0")
                        db_connection.commit()
                        send_message(sender, 'Банк тотализатора смертей сохранён. Мы готовы к новой фазе!')
                    elif rm == 'стороны':
                        total_side = 'ТОТАЛИЗАТОР НА СТОРОНЫ:\n'
                        db_object.execute("UPDATE shop_table SET is_true_sides = 0")
                        db_connection.commit()
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
        elif rm == 'тотализатор' or rm == 'количество смертей' or rm == 'стороны умерших' or rm[
                                                                                             :6] == 'вангую' or rm == 'cветлые' or rm == 'cерые' or rm == 'tёмные' or rm == 'cветлые и тёмные' or rm == 'cерые и светлые' or rm == 'tёмные и серые' or rm == 'bсе стороны':
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
                elif rm == 'cветлые' or rm == 'cерые' or rm == 'tёмные' or rm == 'cветлые и тёмные' or rm == 'cерые и светлые' or rm == 'tёмные и серые' or rm == 'bсе стороны':
                    bal = get_bal(sender)
                    player_balance = get_balance(sender)
                    if bal - 5 >= 0:
                        db_object.execute(f"SELECT is_true_sides FROM shop_table WHERE sender = {sender}")
                        is_sides = db_object.fetchone()[0]
                        if is_sides == 0:
                            db_object.execute("UPDATE shop_table SET balance = balance - 5 WHERE sender = {}".format(sender))
                            db_connection.commit()
                            db_object.execute("UPDATE shop_table SET is_true_sides = 1 WHERE sender = {}".format(sender))
                            db_connection.commit()
                            player_balance = get_balance(sender)
                            total_side += f'{sayer_name} — {rm.capitalize()}\n'
                            send_message(sender, f'Твоя ставка: {rm.capitalize()} потеряют игрока. '
                                                 f'\nТекущий {player_balance}.\nСпасибо за участие '
                                                 f'и да пребудет с тобой удача! ')
                            ending2 = find_ending(totalize_side)
                            for admin in admins:
                                mes = f'Новая ставка в тотализатор (стороны)\n{sayer_name} vk.com/id{sender}\n\nСторона: {rm.capitalize()}'
                                send_message(admin, mes)
                        else:
                            send_message(sender, 'Твоя ставка уже учтена! Приходи в следующий раз.')
                    else:
                        send_message(sender, 'На твоём счёте недостаточно делликов для участия.')

                elif rm == 'количество смертей':
                    message = f'Твой {player_balance} Напиши \"Вангую [число смертей] [' \
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
                    db_object.execute(f"SELECT is_true_deaths FROM shop_table WHERE sender = {sender}")
                    is_deaths = db_object.fetchone()[0]
                    if is_deaths == 0:
                        ending1 = find_ending(rm[1])
                        bal = get_bal(sender)
                        player_balance = get_balance(sender)
                        minus = int(rm[1])
                        if bal - minus >= 0 and minus > 0:
                            db_object.execute(
                                "UPDATE shop_table SET balance = balance - {} WHERE sender = {}".format(minus, sender))
                            db_connection.commit()
                            db_object.execute("UPDATE shop_table SET is_true_deaths = 1 WHERE sender = {}".format(sender))
                            db_connection.commit()
                            total.append([sayer_name, minus])
                            if minus > totalize_max:
                                totalize_max = minus
                            ending3 = find_ending(totalize)
                            player_balance = get_balance(sender)
                            message = f'Твоя ставка: {rm[1]} деллик{ending1}. Количество смертей: {rm[0]}.\n ' \
                                      f'Текущий {player_balance}\nСпасибо за участие и да ' \
                                      f'пребудет с тобой удача! '
                            send_message(sender, message)
                            for admin in admins:
                                mes = f'Новая ставка в тотализатор (смерти)\n{sayer_name} vk.com/id{sender}\n\nРазмер ' \
                                      f'ставки: {rm[1]} деллик{ending1}\nКоличество смертей: {rm[0]}\n\n'
                                send_message(admin, mes)
                        else:
                            send_message(sender,
                                         'На твоём счёте недостаточно делликов для участия. Попробуй '
                                         'уменьшить ставку!')
                    elif is_deaths == 1:
                        send_message(sender, 'Твоя ставка уже учтена! Приходи в следующий раз.')
            else:
                send_message(sender, 'Тотализатор пока не работает. Попробуй позже')

        else:
            for i in range(len(req)):
                sender_id = req[i - 1]['sender']
                if sender_id == sender:  # clarify if they're making a request
                    if rm == 'мел' or rm == 'яна' or rm == 'егор' or rm == 'кит' or rm == 'дуб':
                        req[i - 1]['host'] = rm.capitalize()
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Активное действие')
                        keyboard.add_line()
                        keyboard.add_button('Распоряжение')
                        send_button(sender, "💊 [Шаг 2] Что тебя интересует в этот раз?")
                    elif rm == 'активное действие':
                        req[i - 1]['type'] = 'Активное действие'
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Ход роли')
                        keyboard.add_line()
                        keyboard.add_button('Активация контракта/предмета')
                        send_button(sender, "💊 [Шаг 3] Какое действие ты хочешь совершить?")
                    elif rm == 'распоряжение':
                        req[i - 1]['type'] = 'Распоряжение на время отсутствия'
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('День')
                        keyboard.add_button('Ночь')
                        send_button(sender, '💊 [Шаг 3] Уточни фазу, в которую ты будешь отсутствовать.')
                    elif rm[:4] == 'день' or rm[:4] == 'ночь':
                        req[i - 1]['phase'] = rm
                        send_message(sender,
                                     "💊 [Шаг 4] На какой случай ты оставляешь распоряжение. \nОбязательно! Начни со "
                                     "слова \"Если\". Пример: если в меня будут стрелять. Если будут убивать "
                                     "члена моей команды. Если меня будут проверять и т.п.")
                    elif rm[:4] == 'если':
                        req[i - 1]['condition'] = rm
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Ход роли')
                        keyboard.add_line()
                        keyboard.add_button('Активация контракта/предмета')
                        send_button(sender, "💊 [Шаг 5] Какое действие нужно исполнить?")
                    elif rm == 'ход роли':
                        req[i - 1]['activity'] = rm
                        if req[i - 1]['type'] == 'Активное действие':
                            a = 4
                        else:
                            a = 6
                        send_message(sender,
                                     '💊 [Шаг {}] Уточни свою роль.\nОбязательно! Начни со слова \"Роль\". Пример: \"Роль '
                                     'дон\", \"Роль журналист\" и т.п.'.format(a))
                    elif rm == 'активация контракта/предмета':
                        req[i - 1]['activity'] = rm
                        if req[i - 1]['type'] == 'Активное действие':
                            a = 4
                        else:
                            a = 6
                        send_message(sender,
                                     '💊 [Шаг {}] Уточни используемый контракт/предмет.\nОбязательно! Начни со слова '
                                     '\"Контракт\"/\"Предмет\". Пример: \"Контракт иммунитет\", \"Предмет прослушка\" и т.п.'.format(
                                         a))
                    elif rm[:4] == 'роль' or rm[:8] == 'контракт' or rm[:7] == 'предмет':
                        req[i - 1]['item'] = rm
                        if req[i - 1]['type'] == 'Активное действие':
                            a = 5
                        else:
                            a = 8
                        send_message(sender,
                                     '💊 [Шаг {}] На кого направлено твоё действие? Необходимо указать ссылку на '
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
                            item1 = 'Контракт/предмет'
                            item1_1 = 'контракта/предмета'
                            item2 = req[i - 1]['item'][8:].capitalize()
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
