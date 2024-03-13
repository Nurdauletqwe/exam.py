'''Добавление новых записей с указанием всех параметров
Просмотр списка всех доступных продуктов с их атрибутами.
Обновление информации о записи в базе данных.
Удаление записи из базы данных.
Добавление записи в корзину пользователя.
Оплата содержимого корзины и получение чека в формате Excel.
Использовать объектно-ориентированный подход при разработке.
Использовать базу данных для хранения информации о продуктах.
Обработать исключения, такие как неверный формат ввода или отсутствие соединения с базой данных.

7. Платформа для заказа еды с доставкой:
id (уникальный идентификатор блюда)
name (название блюда)
description (описание блюда)
price (цена блюда)
availability (доступность блюда для заказа)'''

import psycopg2
conn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='postgres', user='postgres', password='postgres')
cursor = conn.cursor()
class Food:
    def __init__(self, id, name, description, price, availability):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
class Order:
    def __init__(self, table):
        self.table = table
        self.dishes = []
    def add_food():
        name = input('Enter name of food: ')
        description = input('Enter description of food: ')
        price = int(input('Enter price of food: '))
        availability = input('Is this food available?: ')
        insert_query = f"INSERT INTO food (name, description, price, availability) VALUES ('{name}', '{description}', {price}, '{availability}')"
        cursor.execute(insert_query)
        conn.commit()
        print('Food added successfully!')

    def view_food():
        select_query = "SELECT * FROM food"
        cursor.execute(select_query)
        foods = cursor.fetchall()
        for food in foods:
            print(food)

    def update_food():
        food_id = int(input('Enter food ID to update: '))
        new_price = int(input('Enter new price: '))
        update_query = f"UPDATE food SET price = {new_price} WHERE id = {food_id}"
        cursor.execute(update_query)
        conn.commit()
        print('Food updated successfully!')

    def delete_food():
        food_id = int(input('Enter food ID to delete: '))
        delete_query = f"DELETE FROM food WHERE id = {food_id}"
        cursor.execute(delete_query)
        conn.commit()
        print('Food deleted successfully!')

    while True:
        print("\n1. Add food\n2. View food\n3. Update food\n4. Delete food\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_food()
        elif choice == 2:
            view_food()
        elif choice == 3:
            update_food()
        elif choice == 4:
            delete_food()
        elif choice == 5:
            break
        else:
            print("Choose only from 1 to 5!")

dish1 = Food('Pizza', 'a dish of Italian origin', 4000, 'available', 2)
dish2 = Food('Pasta', 'a dish originally from Italy', 5000, 'available', 1)
order1 = Order("Столик 1")
order2 = Order("Столик 2") 
print(order1)
print(order2)
cursor.close()
conn.close()