from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
import asyncio

TOKEN = '7483301543:AAF9wHD4m_B8IUMOMA9GSu0VwFXbCQTuJws'

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Обробник команди /start
@dp.message(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привіт! Я твій бот на Django з використанням aiogram.")


# Обробник текстових повідомлень
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        update = Update.to_object(request.body.decode('utf-8'))
        asyncio.run(dp.feed_update(bot, update))
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'error': 'invalid request method'})

