import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
import openai

# توكن تيليجرام
TELEGRAM_TOKEN = "7640591639:AAFyWEd46DWrI8uEabBzvZEHbE88Fl1Zamo"

# مفتاح OpenAI
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

async def handle_message(update: Update, context):
    user_message = update.message.text

    # نربط البوت بشخصية VismoraMedQ
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """أنت الآن GPT باسم VismoraMedQ.
تقوم بإنشاء أسئلة اختيار من متعدد (MCQ) في المواضيع الطبية (تشريح، فسيولوجيا، علم الأمراض، علم الأدوية، الطب السريري، والممارسة المبنية على الأدلة).
المستويات: مبتدئ، متوسط، خبير، أو مختلط.
الأنماط: سيناريو سريري، تذكير مفاهيم، أو مختلط.
تدعم تخصيص منطقة التركيز (التشخيص، العلاج، المضاعفات... إلخ).
كل سؤال يحتوي على 5 خيارات على الأقل مع شرح مفصل للإجابة الصحيحة وتحليل لكل خيار خاطئ، بالإضافة إلى نقطة تعليمية أساسية.
"""
            },
            {"role": "user", "content": user_message}
        ]
    )

    await update.message.reply_text(response.choice_
