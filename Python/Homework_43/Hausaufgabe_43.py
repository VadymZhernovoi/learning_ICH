"""
1.  Добавление товаров.
    Создайте программу, которая подключается к MongoDB и:
        выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
        очищает коллекцию перед началом
        добавляет 3 товара с полями: name, price, stock
        выводит сообщение о количестве добавленных товаров
Пример вывода:
3 products inserted.
"""
from pymongo import MongoClient, errors


def print_result_update(coll_products, cnt_updated):
    print(f"\nPrices updated for {cnt_updated} products\n")
    print("Updated products:")
    for product in coll_products.find({}):
        print(f"- {product["name"]} - ${product["price"]}")


try:
    client = MongoClient(
        "mongodb://ich_editor:verystrongpassword"
        "@mongo.itcareerhub.de/?readPreference=primary"
        "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit")

    client.admin.command("ping")

    db = client["ich_edit"]

    collection_name = "products_210225_Zhernovoi"
    coll_products = db[collection_name]

    # очищает коллекцию перед началом
    if coll_products.estimated_document_count() > 0:  # удалим коллекцию, если она есть, а .insert_ создаст автоматом новую
        coll_products.drop()
        print(f"Deleted collection '{collection_name}'.\n")
    # или так
    # result = coll_products.delete_many({})
    # print(f"Deleted {result.deleted_count} products from '{collection_name}' collection.\n")

    products = [
        {"name": "iPhone 13 Pro", "price": 999.99, "stock": 123},
        {"name": "Epson XP-4205", "price": 129.49, "stock": 321},
        {"name": "Pic X-xx", "price": 0.33, "stock": 438},
    ]
    result = coll_products.insert_many(products)
    print(f"{len(result.inserted_ids)} products inserted.\n")

    # 2.  Увеличение цен.
    #     Продолжите предыдущую задачу. Теперь программа должна:
    #         увеличить цену всех товаров на 20%
    #         вывести количество обновлённых записей
    #         затем вывести список всех товаров с новыми ценами
    # Пример вывода:
    # Prices updated for 3 products.
    #
    # Updated products:
    # - Pen - $1.80
    # - Notebook - $4.79
    # - Backpack - $30.00

    coll = coll_products.find({})
    update_cnt = 0
    for rec in coll:
        new_price = round(rec["price"] * 1.2, 2)
        result = coll_products.update_one({"_id": rec["_id"]}, {"$set": {"price": new_price}})
        update_cnt += result.modified_count

    print_result_update(coll_products, update_cnt)

    # или так интереснее
    result = coll_products.update_many({}, [
        {"$set": {"price": {"$round": [{"$multiply": ["$price", 1.2]}, 2]}}}
    ])

    print_result_update(coll_products, result.modified_count)

except errors.WriteError:
    print(f"Не удаётся записать в коллекцию '{collection_name}'")
except errors.ConnectionFailure:
    print("Ошибка подключения к MongoDB")
except errors.OperationFailure:
    print("Ошибка авторизации или запроса")
