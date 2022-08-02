import os
import logging
from aiogram import Bot, Dispatcher, executor, types
# from config import TOKEN
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
def transliteration(s: str) -> str:
    ciril_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                     'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', \
                     'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', \
                     'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '-', '_']

    latin_letters = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', \
                     't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', 'y', 'ie', '', 'e', 'iu', 'ia', \
                     'A', 'B', 'V', 'G', 'D', 'E', 'E', 'ZH', 'Z', 'I', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', \
                     'T', 'U', 'F', 'KH', 'TS', 'CH', 'SH', 'SHCH', 'Y', 'IE', '', 'E', 'IU', 'IA', ' ', '-', '_']

    answer = ''
    for i in s:
        if i not in ciril_letters:
            return 'Некорректный ввод!'
        else:
            answer += latin_letters[ciril_letters.index(i)]
    return answer

def log(message):
    import datetime
    dtn = datetime.datetime.now()
    botlogfile = open('Bot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,
          'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello!, {user_name}, я умею кириллицу превращать в латиницу!!!'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')

    await message.reply(text)

@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name=} {user_id=} sent message: {text}')
    log(message)
    await bot.send_message(user_id, transliteration(text))

if __name__ == '__main__':
    executor.start_polling(dp)