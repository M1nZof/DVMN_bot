import time
from textwrap import dedent

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
            )
            if response.ok:
                review_response = response.json()
                if review_response['status'] == 'found':
                    timestamp = review_response['new_attempts'][0]['timestamp']

                    text = dedent(f'''
                    Преподаватель проверил работу!
                    
                    Название урока: {review_response["new_attempts"][0]["lesson_title"]}
                    Ссылка на урок: {review_response["new_attempts"][0]["lesson_url"]}''')
                    bot.send_message(chat_id=chat_id, text=text)
                elif review_response['status'] == 'timeout':
                    timestamp = review_response['timestamp_to_request']
        except requests.exceptions.ReadTimeout:
            continue
        except ConnectionError:
            time.sleep(60)
