import sqlite3

connection = sqlite3.connect("telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")

#Создание 10 записей
#for i in range (1, 11):
#    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",(f"User{i}", f"example{i}@gmail.com", f"{i}0"))
#Конец создания



#добавление продукта
def add_product(product_id, titel, description, price):
    check_product = cursor.execute("SELECT * FROM Products WHERE id=&",(product_id,))

    if check_product.fetchone() is None:
        cursor.execute(f'''
    INSERT ITO Products VALUES('{product_id}','{titel}','{description}','{price}')
''')
    connection.commit()
#конец блока добавление продукта

#cursor.execute("SELECT * FROM Products")
#users = cursor.fetchall()
#for i in users:
#    print(f"{i}")



#выгрузка списка продуктов
def get_product_list():
    product_list = cursor.execute("SELECT * FROM Products;").fetchall()
    return product_list

#конец блока выгрузки
#products = get_product_list()
#for product in products:
#    print(product)

#Оцистка таблицы
#cursor.execute("SELECT * FROM Products")
#users = cursor.fetchall()
#for i in users:
#    cursor.execute("DELETE FROM Products WHERE id = ?", (f"{i[0]}",))
#Конец оцистки


connection.commit()
#connection.close()
