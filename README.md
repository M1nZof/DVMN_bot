# Бот с уведомлениями о проверке работ на [dvmn.org](dvmn.org)

## Установка зависимостей

`pip install -r requirements.txt`

## Переменные окружения

### Пример оформления

```shell
TG_TOKEN=123123123:t0k3NSym601s
DVMN_TOKEN=Token 0025748ndifgunidfg74535
TIMESTAMP=1695490091.705723
TG_USER_ID=12312312323
```

### Описание переменных окружения

- TG_TOKEN - Токен бота ([Получить токен](https://t.me/BotFather))
- DVMN_TOKEN - Токен для API DVMN ([Получить токен](https://dvmn.org/api/docs/))
- TIMESTAMP - Последняя дата получения результата проверки (в формате timestamp, можно получить [здесь](https://dvmn.org/api/user_reviews/))
- TG_USER_ID - Личный ID пользователя. [Узнать у бота](https://t.me/username_to_id_bot)

## Запуск бота

```shell
python main.py
```