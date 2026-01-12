from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Router
from loggerq import logger, new_user_logger

router = Router()


def log_user_message(message: Message):
    user = message.from_user
    username = user.username or "нет"
    log_text = f"{user.id} (@{username}) | {user.first_name or '?'} → {message.text}"
    logger.info(log_text)

ADMIN_ID = "584261576"

@router.message(CommandStart())
async def start_handler(message: Message):
    log_user_message(message)
    #код для получение ид юзера + имени 
    user_id = message.from_user.id
    username = message.from_user.username or "net username"
    first_name = message.from_user.first_name or "net first name"
    
    #отправить инфу МНЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ
    
    notification = (
        f"какой-то еблан запустил бота:\n"
        f"идишка: <code>{user_id}</code>\n"
        f"юзер: @{username}\n"
        f"отображаемое имя: {first_name}"
    )

    try:
        await message.bot.send_message(
            chat_id=ADMIN_ID,
            text=notification,
            parse_mode="HTML"  # хтмл для красвивого отображения
        )
    except Exception as e:
        print(f"Не удалось отправить админу уведомление: {e}")

    new_user_logger.info(
        f"{user_id} | @{username} | {first_name}"
        )

    await message.answer(
        "Привет. Я auto-reply бот.\n"
        "Напиши любое сообщение."
    )

@router.message(
    F.text.lower().contains("привет") |
    F.text.lower().contains("ку") |
    F.text.lower().contains("хай") |
    F.text.lower().contains("йй") |
    F.text.lower().contains("здарова")
)
async def hello_handler(message: Message):
    log_user_message(message)
    await message.answer("привет чувак")

@router.message(
    F.text.lower().contains("как дела") |
    F.text.lower().contains("кд") |
    F.text.lower().contains("шо ты") |
    F.text.lower().contains("чо ты") |
    F.text.lower().contains("как ты")
)
async def how_are_you_handler(message: Message):
    log_user_message(message)
    await message.answer("нормас, ты че?")

    
@router.message(F.text)
async def log_all_messages(message: Message):
    log_user_message(message)
    await message.answer("я получил твоё сообщение ")
    