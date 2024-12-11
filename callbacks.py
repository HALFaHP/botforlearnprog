from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import asyncio

router = Router()


@router.callback_query(F.data == "Python_learning_foundations")
async def ptyhon_explanation_founds(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Переменные:\n <a href='https://metanit.com/python/tutorial/2.2.php'>Статья</a>\n <a href='https://rutube.ru/video/d3df7e9cbd4c485c01551e01c21df770/'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Арифметические операции:\n <a href='https://metanit.com/python/tutorial/2.3.php'>Статья</a>\n <a href='https://rutube.ru/video/dedc163ffae8a5a072f9cdb73a667238/?t=0'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Условные операторы:\n <a href='https://metanit.com/python/tutorial/2.6.php'>Статья</a>\n <a href='https://rutube.ru/video/fae45ab3f9cbb2c212640a3e360dda62/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Циклы:\n <a href='https://metanit.com/python/tutorial/2.7.php'>Статья</a>\n <a href='https://rutube.ru/video/cf31c6be8f845ba3645114392654f711/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Функции:\n <a href='https://metanit.com/python/tutorial/2.8.php'>Статья</a>\n <a href='https://rutube.ru/video/3d6bf7a7d5302d8b429775b5ff5161b5/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "Python_learning_extentions")
async def ptyhon_explanation_extentions(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Списки:\n <a href='https://metanit.com/python/tutorial/3.1.php'>Статья</a>\n <a href='https://rutube.ru/video/a69b046faf02f297513222c0b4d6237d/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Кортежи:\n <a href='https://metanit.com/python/tutorial/3.2.php'>Статья</a>\n <a href='https://rutube.ru/video/b061db48dfddce21c6e035657a18938e/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Словари:\n <a href='https://metanit.com/python/tutorial/3.4.php'>Статья</a>\n <a href='https://rutube.ru/video/9ad5e7970c24de78a6172752b9b26e0c/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Множества:\n <a href='https://metanit.com/python/tutorial/3.5.php'>Статья</a>\n <a href='https://rutube.ru/video/25c7ed1f30421e4a7ad17eff90a97fb2/?playlist=536976'>Видео</a>",
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "Python_learning_OOP")
async def ptyhon_explanation_oop(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Введение:\n <a href='https://metanit.com/python/tutorial/7.1.php'>Статья</a>\n <a href='https://rutube.ru/video/2168aa1a1b76af58bef24e95f7d0ba9f/?playlist=537372'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Классы:\n <a href='https://metanit.com/python/tutorial/7.6.php'>Статья</a>\n <a href='https://rutube.ru/video/38ef3a2db2919eecf4d5e7f62a2595e1/?playlist=537372'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Методы классов:\n <a href='https://diveintopython.org/ru/learn/classes/methods'>Статья</a>\n <a href='https://rutube.ru/video/408086cd61a97647d042b3f2ff148847/?playlist=537372'>Видео</a>",
        disable_web_page_preview=True,
    )


####################################################################################################


@router.callback_query(F.data == "javascript_learning_foundations")
async def javascript_explanation_founds(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Переменные:\n <a href='https://learn.javascript.ru/variables'>Статья</a>\n <a href='https://rutube.ru/video/a6d062ee8cb5f4836563af47159d2bfe/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Арифметические операции:\n <a href='https://learn.javascript.ru/operators'>Статья</a>\n <a href='https://rutube.ru/video/ff3f7a9bac6bae00c6801e025684bd61/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Условные операторы:\n <a href='https://learn.javascript.ru/ifelse'>Статья</a>\n <a href='https://rutube.ru/video/73ba4167e43a78aca192fdda87ea4ade/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Циклы:\n <a href='https://learn.javascript.ru/while-for'>Статья</a>\n <a href='https://rutube.ru/video/194fdfc0cd70ccf119762d139316ca04/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Функции:\n <a href='https://learn.javascript.ru/function-basics'>Статья</a>\n <a href='https://rutube.ru/video/1f69c96193f93388f2064f8545530ab4/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "javascript_learning_extentions")
async def javascript_explanation_extentions(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Особенности:\n <a href='https://learn.javascript.ru/javascript-specials'>Статья</a>\n <a href='https://rutube.ru/video/b63facabba61c891f6dff07db2aa38f7/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Массивы:\n <a href='https://learn.javascript.ru/coding-style'>Статья</a>\n <a href='https://rutube.ru/video/a08522c4efc4c6f239e49274d5a10180/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Рекурсия:\n <a href='https://learn.javascript.ru/recursion'>Статья</a>\n <a href='https://rutube.ru/video/dcd98fb32bf5762aa5a56a1191a6ff6e/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "javascript_learning_OOP")
async def javascript_explanation_oop(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Основы:\n <a href='https://learn.javascript.ru/object'>Статья</a>\n <a href='https://rutube.ru/video/51526cdcbc3994aeb0d169c207f729b6/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Детали:\n <a href='https://learn.javascript.ru/constructor-new'>Статья</a>\n <a href='https://rutube.ru/video/481d935bb16742c3b88995ec6611b7cf/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )


#######################################################################################################


@router.callback_query(F.data == "cplusplus_learning_foundations")
async def cplusplus_explanation_founds(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Переменные:\n <a href='https://metanit.com/cpp/tutorial/2.2.php'>Статья</a>\n <a href='https://rutube.ru/video/2a20b4d7941282ebc9a825b64807b1aa/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Арифметические операции:\n <a href='https://metanit.com/cpp/tutorial/2.6.php'>Статья</a>\n <a href='https://rutube.ru/video/3608642742bfada8ff948323f0183ae5/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Условные операторы:\n <a href='https://metanit.com/cpp/tutorial/2.12.php'>Статья</a>\n <a href='https://rutube.ru/video/0e55935e9746cec86ef89cc483201993/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Циклы:\n <a href='https://metanit.com/cpp/tutorial/2.13.php'>Статья</a>\n <a href='https://rutube.ru/video/4ff0d2414f1cb94964dfa1efdfc6750a/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Функции:\n <a href='https://metanit.com/cpp/tutorial/3.1.php'>Статья</a>\n <a href='https://rutube.ru/video/0bac6e6023cc2558fb356e66590c65bb/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "cplusplus_learning_extentions")
async def cplusplus_explanation_extentions(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Указатели:\n <a href='https://metanit.com/cpp/tutorial/4.1.php'>Статья</a>\n <a href='https://rutube.ru/video/c4f83b80b24bee26294faa25de246904/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Массивы:\n <a href='https://metanit.com/cpp/tutorial/2.15.php'>Статья</a>\n <a href='https://rutube.ru/video/c5cdb2a6d3e04bc638e44a5a97969504/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Исключения:\n <a href='https://metanit.com/cpp/tutorial/6.1.php'>Статья</a>\n <a href='https://rutube.ru/video/592da29378921336522ad7a39c70f4e3/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )


@router.callback_query(F.data == "cplusplus_learning_OOP")
async def cplusplus_explanation_oop(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Подробно:\n <a href='https://metanit.com/cpp/tutorial/5.1.php'>Статья</a>\n <a href='https://rutube.ru/plst/539238/'>Видео</a>",
        disable_web_page_preview=True,
    )
    await callback.message.answer(
        f"Экспресс:\n <a href='https://habr.com/ru/sandbox/189562/'>Статья</a>\n <a href='https://rutube.ru/video/15d1a7a94a2f8c34d9d91ab79db19331/?r=wd'>Видео</a>",
        disable_web_page_preview=True,
    )


#######################################################################################################
@router.callback_query(F.data == "git_foundations")
async def git_foundations_explanation(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Основы:\n <a href='https://habr.com/ru/articles/541258/'>Статья</a>\n <a href='https://habr.com/ru/articles/472600/'>Статья</a>\n <a href='https://yandex.ru/video/preview/7176999558890663768?aabrnd=476118051'>Видео</a>",
        disable_web_page_preview=True,
    )
    # await callback.message.answer(f"Фишки:\n <a href='https://metanit.com/python/tutorial/7.6.php'>Статья</a>\n <a href='https://rutube.ru/video/38ef3a2db2919eecf4d5e7f62a2595e1/?playlist=537372'>Видео</a>", disable_web_page_preview=True)


@router.callback_query(F.data == "git_tricks")
async def git_foundations_explanation(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer(
        f"Фишки:\n <a href='https://metanit.com/python/tutorial/7.6.php'>Статья</a>\n <a href='https://rutube.ru/video/38ef3a2db2919eecf4d5e7f62a2595e1/?playlist=537372'>Видео</a>",
        disable_web_page_preview=True,
    )
