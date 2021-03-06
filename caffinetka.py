import bs4, requests, datetime, time
from telebot import TeleBot

# Списки
AbakanL = ['Абакан', 'абакан', 'Абакасик','а', 'аб', 'аба', 'абак', 'абака', 'абк', 'абдуль', 'хуй',
'А', 'Аб', 'Аба', 'Абак', 'Абака']
KrskL = ['Красноярск', 'красноярск', 'Красный','К', 'Кр', 'Кра', 'Крас', 'Красн', 'Красно', 'Красноя', 'Краснояр',
'к', 'кр', 'кра', 'крас', 'красн', 'красно', 'красноя', 'краснояр', 'красноярс', 'красноярск', 'крск']
NabChL = ['Н', 'На', 'Наб', 'Набе', 'Набер', 'Набере', 'Набереж', 'Набережн', 'Набережны','Набережные',
'Набережные Челны', 'н', 'на', 'наб', 'набе', 'набер', 'набере', 'набереж', 'набережны', 'набережные', 'набережныечелны',
'набережные челны', 'челны', 'Челны', 'чел', 'чалы', 'член', 'нч']
spisok1 = AbakanL + KrskL + NabChL
#
clock = datetime.datetime.now()
#
app = TeleBot(__name__)
TOKEN = "553633377:AAEGKsPtdewL56-45neHf3RbiQ7tYorhFXQ"
bot = TeleBot(TOKEN)
@app.route ('/weather ?(.*)')
def get_weather(message, city):
    if city in KrskL:
        s = requests.get("https://sinoptik.com.ru/погода-красноярск")
        b = bs4.BeautifulSoup(s.text, "html.parser")
        # Утро
        U = b.select(" .temperature .p3")[0].getText()
        U += b.select(" .temperature .p4")[0].getText()
        # День

        D = b.select(" .temperature .p5")[0].getText()
        D += b.select(" .temperature .p6")[0].getText()
        # Вечер

        V = b.select(' .temperature .p7')[0].getText()
        V += b.select(' .temperature .p8')[0].getText()
        # Ночь

        N = b.select(" .temperature .p1")[0].getText()
        N += b.select(" .temperature .p2")[0].getText()
        # Общий

        O = b.select(" .rSide .description")[0].getText()
        #
        xxx = ('Смотрим в небо\nАнализируем звезды\nШаманы установили следующие показатели\n-'
               '\nТекущие время:' + clock.strftime('%H:%M'))
        zzz = (
                '\nТекущая дата: ' + clock.strftime('%d.%m.%Y') + '\n-' + '\nУтром: ' + U + '\nДнём: ' + D + '\n-' +
                '\nВечером: ' + V + '\nНочью: ' + N + '\n' + O)

        xxx + zzz
        xxx = xxx + zzz
        app.send_message(message['chat']['id'], xxx)
    else:
        app.send_message(message['chat']['id'], 'no such city')

bot.polling(none_stop=True)
