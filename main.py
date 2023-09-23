import requests
import telegram
import os

from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    dvmn_token = os.getenv('DVMN_TOKEN')
    timestamp = os.getenv('TIMESTAMP')
    chat_id = os.getenv('TG_USER_ID')

    bot = telegram.Bot(token=tg_token)

    while True:
        try:
            response = requests.get(
                "https://dvmn.org/api/long_polling/",
                timeout=90,
                headers={'Authorization': dvmn_token},
                params={'timestamp': timestamp}
            ).json()
            timestamp = response['new_attempts'][0]['timestamp']

            bot.send_message(
                chat_id=chat_id,
                text='Преподаватель проверил работу! \n\n'
                     f'Название урока: {response["new_attempts"][0]["lesson_title"]}\n'
                     f'Ссылка на урок: {response["new_attempts"][0]["lesson_url"]}'
            )
        except requests.exceptions.ReadTimeout:
            continue
        except ConnectionError:
            continue
