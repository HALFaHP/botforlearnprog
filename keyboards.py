from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


enterkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python', callback_data='Python_learning')
        ],
        [
            InlineKeyboardButton(text='JavaScript', callback_data='Javascript_learning')
        ],
        [
            InlineKeyboardButton(text='C++', callback_data='C++_learning')
        ],
        [
            InlineKeyboardButton(text='Git', callback_data='Git_learning')
        ]
    ]
)

python_moduls_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Основы', callback_data='Python_learning_foundations')
        ],
        [
            InlineKeyboardButton(text='Расширенный курс', callback_data='Python_learning_extentions')
        ],
        [
            InlineKeyboardButton(text='ООП', callback_data='Python_learning_OOP')
        ]
    ]
)


javascript_moduls_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Основы', callback_data='javascript_learning_foundations')
        ],
        [
            InlineKeyboardButton(text='Расширенный курс', callback_data='javascript_learning_extentions')
        ],
        [
            InlineKeyboardButton(text='ООП', callback_data='javascript_learning_OOP')
        ]
    ]
)


cplusplus_moduls_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Основы', callback_data='cplusplus_learning_foundations')
        ],
        [
            InlineKeyboardButton(text='Расширенный курс', callback_data='cplusplus_learning_extentions')
        ],
        [
            InlineKeyboardButton(text='ООП', callback_data='cplusplus_learning_OOP')
        ]
    ]
)


git_moduls_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Основы', callback_data='git_foundations')
        ],
        [
            InlineKeyboardButton(text='Фишки', callback_data='git_tricks')
        ]
    ]
)












































rowspykb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Арифметические операции', url='google.com')
        ],
        [
            InlineKeyboardButton(text='Ввод/вывод данных', url='google.com')
        ],
        [
            InlineKeyboardButton(text='Общее описание', url='google.com')
        ]
    ]
)