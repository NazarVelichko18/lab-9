import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["db"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
collection = db["collection"]

# Додавання документів (еквівалент записів в таблиці)
data1 = {"name": "Кобзар", "author": "Т. Шевченко", "student": "Назар"}
data2 = {"name": "Федько-халамидник", "author": "В. Винниченко", "student": "Льоня"}
data3 = {"name": "Енеїда", "author": "І. Котляревський", "student": "Вітя"}

# Вставка документів
inserted_data1 = collection.insert_one(data1)
inserted_data2 = collection.insert_one(data2)
inserted_data3 = collection.insert_one(data3)

# Оновлення документа
query = {"name": "Кобзар"}
new_data = {"$set": {"student": "Вітя"}}
collection.update_one(query, new_data)

# Видалення документа
delete_query = {"name": "Енеїда"}
collection.delete_one(delete_query)

#Пошук документа
search_query = {"name": "Кобзар"}
print("Знайдено книгу:")
for document in collection.find(search_query):
    print(document)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")
for document in collection.find():
    print(document)

# Закриття підключення
client.close()
