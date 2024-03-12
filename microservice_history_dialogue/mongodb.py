import pymongo
from datetime import datetime

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Подключение к локальному MongoDB
db = client["chat_history"]  # Создание базы данных

# Создание коллекции для хранения истории диалогов
chat_collection = db["dialogs"]

# Функция для сохранения сообщения в базу данных
def save_dialog(timestamp, id_doc, user, message, message_app):
    dialog = {"timestamp": timestamp, "id_doc": id_doc, "user": user, "message": message, "message_app": message_app}
    chat_collection.insert_one(dialog)

# Пример сохранения диалогов
current_time = datetime.now()  # Текущее время
user_message = "Привет, как дела?"
application_message = "Привет! Всё отлично, спасибо!"


save_dialog(current_time, 1, "User1", user_message, application_message)


# Вывод всех сообщений из базы данных
print("История диалогов:")
for dialog in chat_collection.find():
    print(f"{dialog['timestamp']}, {dialog['id_doc']}, {dialog['user']}, {dialog['message']}, {dialog['message_app']}")
