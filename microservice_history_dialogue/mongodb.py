import pymongo
import motor.motor_asyncio
from datetime import datetime
import asyncio

async def main():
    # Подключение к MongoDB
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["chat_history"]  # Создание базы данных

    # Создание коллекции для хранения истории диалогов
    chat_collection = db["dialogs"]

    # Функция для сохранения сообщения в базу данных
    async def save_dialog(timestamp, id_doc, user, message, message_app):
        dialog = {"timestamp": timestamp, "id_doc": id_doc, "user": user, "message": message, "message_app": message_app}
        chat_collection.insert_one(dialog)

    # Пример сохранения диалогов
    current_time = datetime.now()  # Текущее время
    user_message = "Привет, как дела?"
    application_message = "Привет! Всё отлично, спасибо!"

    save_dialog(current_time, 1, "User1", user_message, application_message)


    # Вывод всех сообщений из базы данных
    print("История диалогов:")
    async for dialog in chat_collection.find({}):
        print(f"{dialog['timestamp']}, {dialog['id_doc']}, {dialog['user']}, {dialog['message']}, {dialog['message_app']}")


if __name__ == "__main__":
    asyncio.run(main())