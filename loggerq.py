

import logging

#конфигурацию логирования один раз
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    handlers=[
        logging.FileHandler("bot_messages.log", encoding='utf-8'),
        logging.StreamHandler()  # вывод в консоль
    ]
)

# экспортируем логгер
logger = logging.getLogger("bot_logger")

#логгер для новых юзеров , создание отдельного файла логов
new_user_handler = logging.FileHandler("new_users.log", encoding='utf-8')
new_user_handler.setFormatter(logging.Formatter('%(asctime)s | NEW USER | %(message)s'))

new_user_logger = logging.getLogger("new_users")
new_user_logger.setLevel(logging.INFO)
new_user_logger.addHandler(new_user_handler)
new_user_logger.addHandler(logging.StreamHandler()) #вывод в консоль