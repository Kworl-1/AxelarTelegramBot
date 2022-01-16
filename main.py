# IMPORTS
import telebot
from telebot import types
import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup as BS

#LOADS
load_dotenv()
bot_token = os.getenv('Token')
bot = telebot.TeleBot(bot_token)
    

# BOT_LOGICS
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Начать')
    markup.add(item1,)
    bot.send_message(message.chat.id, 'Привет,{0.first_name}! Это бот Axelar Network.'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Начать':
        markup_info = types.ReplyKeyboardMarkup(resize_keyboard=True)
        about = types.KeyboardButton("О проекте")
        markup_info.add(about)
        bot.send_message(message.chat.id, 'Немного информации о проекте', parse_mode="HTML", reply_markup=markup_info)
    if message.text == 'О проекте':
        markup_about = types.ReplyKeyboardMarkup(resize_keyboard=True)
        team  = types.KeyboardButton('Команда')
        sponsors = types.KeyboardButton('Спонсоры')
        eco_sys = types.KeyboardButton('Экосистема')
        links = types.KeyboardButton('Офф. ссылки')
        news = types.KeyboardButton('Блог проекта')
        faq  = types.KeyboardButton('Часто задаваемые вопросы')
        markup_about.add(team, sponsors, eco_sys,links,news, faq)
        bot.send_message(message.chat.id,'<b>AXELAR NETWORK</b>'+'\n'+'<i>Axelar network</i> - это универсальная платформа взаимодействия, которая соединяет все блокчейны через децентрализованную сеть и SDK протоколов и API. Используя сеть и SDK, разработчики могут эффективно создавать новые соединения и интегрировать свои децентрализованные приложения со всеми экосистемами блокчейна, создавая более широкий доступ к пользователям, активам, ликвидности и другим приложениям.'+'\n' + '\n' + '<b>Чем Axelar отличается от других современных кросс-чейн решений?</b>'+'\n' + '\n' + 'Axelar отличается от других подходов к межцепочечной совместимости тем, что он:' + '\n' + '🔺 Децентрализованный и открытый для участия всех желающих' + '\n' + '🔺 Универсальный подход к подключению, обеспечивающий масштабируемость в произвольных цепочках L1, L2, Proof of Work (PoW) или Proof of Stake (POS)' + '\n' + '🔺Способен выполнять функции маршрутизации и перевода сообщений между экосистемами' + '\n' + '🔺 Открыт для любого разработчика, желающего интегрироваться поверх сети', parse_mode="HTML", reply_markup=markup_about)
    if message.text == 'Команда':       
        markup_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton('Назад')
        markup_back.add(back)
        markup = types.InlineKeyboardMarkup()
        jun1=types.InlineKeyboardButton("👨 [СОУЧЕРЕДИТЕЛЬ | ИНЖЕНЕР] Sergey Gorbunov", url='https://cs.uwaterloo.ca/~sgorbuno/')
        markup.row(jun1)
        jun2=types.InlineKeyboardButton("👨 [СОУЧЕРЕДИТЕЛЬ | ИНЖЕНЕР] Georgios Vlachos", url='https://www.linkedin.com/in/georgiosvlachos')
        jun3=types.InlineKeyboardButton("👨 [ENGINEERING] Christian Gorenflo", url='https://www.linkedin.com/in/christian-gorenflo-8a3394124', parse_mode='HTML')
        markup.row(jun2, jun3)
        jun4=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Gus Gutoski", url='https://www.linkedin.com/in/ggutoski/')
        markup.row(jun4)
        jun5=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Stelios Daveas", url='https://www.linkedin.com/in/sdaveas/')
        jun6=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] João Sousa", url='https://www.linkedin.com/in/jcs47/')
        markup.row(jun5,jun6)
        jun7=types.InlineKeyboardButton("👩 [СООБЩЕСТВО] Kate Stapleton", url='https://twitter.com/kaite_stapleton')
        markup.row(jun7)
        jun8=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Sammy Liu", url='https://www.linkedin.com/in/liu-sammy/')
        jun9=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Jackson Virgo", url='https://twitter.com/envlocal')
        markup.row(jun8,jun9)
        jun10=types.InlineKeyboardButton("👨 [ИНЖЕНЕР Haiyi Zhong", url='https://www.linkedin.com/in/haiyi-zhong-6274108b/')
        markup.row(jun10)
        jun11=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Michael De Luca", url='https://www.linkedin.com/in/delucamike/')
        jun12=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Jacky Yuan", url='https://www.linkedin.com/in/yijie-jacky-yuan-40b31212b/')
        markup.row(jun11,jun12)
        jun13=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Milap Sheth", url='https://www.linkedin.com/in/milapsheth1/')
        markup.row(jun13)
        jun14=types.InlineKeyboardButton("👨 [БЕЗНЕС ОПЕРЦИИ] Nav Pannu", url='https://www.linkedin.com/in/navjitpannu/')
        jun15=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Canh Trinh", url='https://www.linkedin.com/in/canhtrinh/')
        markup.row(jun14,jun15)
        jun16=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Wil Collins", url='https://twitter.com/wc3po')
        markup.row(jun16)
        jun17=types.InlineKeyboardButton("👨 [ИНЖЕНЕР] Talal Ashraf", url='https://www.linkedin.com/in/talalashraf/')
        jun18=types.InlineKeyboardButton("👨 [МАРКЕТИНГ] Eli Laipson", url='https://twitter.com/EliLaipson')
        markup.row(jun17,jun18)
        bot.send_message(message.chat.id,'<b>Команда проекта:</b>',reply_markup=markup, parse_mode='HTML')
    if message.text == 'Спонсоры':
        markup_backers = types.InlineKeyboardMarkup()
        backers1=types.InlineKeyboardButton('COINBASE',url='https://www.coinbase.com/ru/')
        backers2=types.InlineKeyboardButton('BINANCE', url='https://www.binance.com/ru')
        backers3=types.InlineKeyboardButton('GALAXE DIGITAL', url='https://www.galaxydigital.io/')
        backers4=types.InlineKeyboardButton('DRAGONFLY CAPITAL', url='https://www.dcp.capital/')
        markup_backers.add(backers1,backers2,backers3,backers4)
        bot.send_message(message.chat.id,'<b>Спонсоры проекта проекта:</b>',reply_markup=markup_backers, parse_mode='HTML')
    if message.text == 'Экосистема':
        markup_eco = types.InlineKeyboardMarkup()
        eco1 = types.InlineKeyboardButton('AVALANCHE', url='https://www.avax.network/')
        eco2 = types.InlineKeyboardButton('TERRA', url='https://www.terra.money/')
        eco3 = types.InlineKeyboardButton('POLYGON', url='https://polygon.technology/')
        eco4 = types.InlineKeyboardButton('MOONBEAN', url='https://moonbeam.network/')
        markup_eco.add(eco1,eco2,eco3,eco4)
        bot.send_message(message.chat.id,'<b>Экосистема:</b>',reply_markup=markup_eco, parse_mode='HTML')
    if message.text == 'Офф. ссылки':
        markup_links = types.InlineKeyboardMarkup()
        link1=types.InlineKeyboardButton('🌎 Сайт проекта', url='https://axelar.network/')
        link2=types.InlineKeyboardButton('✈️ Телеграм', url='https://t.me/axelarcommunity')
        link3=types.InlineKeyboardButton('🐦Твиттер', url='https://twitter.com/axelarcore')
        link4=types.InlineKeyboardButton('📒 Medium', url='http://medium.com/axelar')
        link5=types.InlineKeyboardButton('🎮 Дискорд', url='https://discord.gg/aRZ3Ra6f7D')
        links6=types.InlineKeyboardButton('📺Youtube', url='https://www.youtube.com/channel/UCf8GFg58fdp1iZwLAOV1Tgg')
        markup_links.add(link1,link2,link3,link4, link5, links6)
        bot.send_message(message.chat.id,'<b>Офф. ссылки:</b>',parse_mode='HTML',reply_markup=markup_links)
    if message.text =='Блог проекта':
        r=requests.get('https://axelar.network/blog')
        html=BS(r.content,'html.parser')
        for el in html.select(".elementor-posts-container > .category-uncategorized"):
            title = el.select(".elementor-post__title > a")
            tit = title[0].text
            date = el.select('.elementor-post__meta-data > .elementor-post-date')
            date_post = date[0].text
            discription = el.select('.elementor-post__excerpt > p')
            url=el.find(class_='elementor-post__thumbnail__link', href=True)
            url_post = url['href']
            bot.send_message(message.chat.id, f'  {tit}' + '\n' + f'{date_post}' + '\n' + f'  {url_post}')
    if message.text == 'Часто задаваемые вопросы':
        markup_faq = types.InlineKeyboardMarkup()
        faq1 = types.InlineKeyboardButton('Кто может взаимодействовать с Axelar?',callback_data='q1')
        faq2 = types.InlineKeyboardButton('Аудиты', callback_data='q2')
        faq3 = types.InlineKeyboardButton('Тестовя сеть', callback_data='q3')
        faq4 = types.InlineKeyboardButton('Как связаться с командой?', callback_data='q4')
        markup_faq.add(faq1, faq2, faq3,faq4)
        bot.send_message(message.chat.id, '<b>Часто задаваемы вопросы:</b>', parse_mode='HTML', reply_markup=markup_faq)


@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data == 'q1':
        bot.send_message(call.message.chat.id, '<b>C Axelar могут взаимодейстовать:</b>', parse_mode='HTML')
        bot.send_message(call.message.chat.id, '<b>Обычные пользователи</b>  которые хотят  перести свои средства из одной сети в другую, для этого Axelar реалтзовали приложение Satellite', parse_mode='HTML')
        bot.send_message(call.message.chat.id, '<b>Разработчики протоколов</b>  могут взаимодействовать с Axlear подключая свой блокчейны к сети Axlear', parse_mode='HTML')
        bot.send_message(call.message.chat.id, '<b>разработчки приложении</b>  подключившись к Axelar, они смогут отправлять запросы на взаимодействие с активами всех поддерживаемых экосистем.', parse_mode='HTML')
    if call.data == 'q2':
        bot.send_message(call.message.chat.id, '<b>Axelar прошла следющие аудиты:</b>', parse_mode='HTML')
        bot.send_message(call.message.chat.id, '🔺 NCC', parse_mode='MarkdownV2')
        bot.send_message(call.message.chat.id, '🔺[Cure53](https://cure53.de/)', parse_mode='MarkdownV2')
        bot.send_message(call.message.chat.id, '🔺[Oak Security](https://www.oaksecurity.io/)', parse_mode='MarkdownV2')
    if call.data =='q3':
        bot.send_message(call.message.chat.id, 'Тестовя сеть Axelar будет до и после запуска основной сети. Обновление тествой сети будет ккждые 4-8 недели. Продолжительсность тестовой сети будет зависеть от сложности тестируемой функции и других факторов', parse_mode='HTML')
    if call.data =='q4':
        bot.send_message(call.message.chat.id, '<b>Бля связи с комадой можно испольовать следующее:</b>', parse_mode='HTML')
        bot.send_message(call.message.chat.id, '🔺[Discord](https://discord.com/invite/aRZ3Ra6f7D)', parse_mode='MarkdownV2')
        bot.send_message(call.message.chat.id, '🔺[Telegram](https://t.me/axelarcommunity)', parse_mode='MarkdownV2')

# START_BOT
bot.polling(non_stop=True)