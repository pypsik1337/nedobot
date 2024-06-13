from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)

def make_kb_ipoteka(items: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text = item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)