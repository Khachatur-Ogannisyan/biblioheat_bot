from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Настройка доступа к Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("for-biblioheat-04e19b2c029e.json", scope)  # Путь к JSON-файлу
client = gspread.authorize(creds)

# Открываем Google таблицу
sheet = client.open(for biblioheat_bot).sheet1  # Укажите название вашей таблицы

# Функция обработки сообщений от пользователя
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text  # Получаем текст от пользователя
    data = sheet.get_all_records()  # Загружаем все данные из таблицы

    # Поиск совпадений
    for row in data:
        if query.lower() in str(row).lower():  # Проверяем наличие текста в строке
            await update.message.reply_text(f"Найдено: {row}")
            return

    await update.message.reply_text("Ничего не найдено 😔")

# Настройка и запуск бота
def main():
    # Создаем приложение
    application = Application.builder().token(8061703889:AAHWhFDcMl9Shmqy_EBT4xn9msB95BDcu3o).build()

    # Добавляем обработчик сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
