from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint


# Підключення до MongoDB (локально або Atlas)
# Для Atlas заміни URI на свій
client = MongoClient("mongodb://localhost:27017/")

# Створюємо базу даних та колекцію
db = client["cats_db"]
collection = db["cats"]


# -------------------------------
# CREATE (створення документа)
# -------------------------------
def create_cat(name: str, age: int, features: list):
    """Додає нового кота до колекції"""
    try:
        cat = {"name": name, "age": age, "features": features}
        result = collection.insert_one(cat)
        print(f"✅ Кота додано з _id: {result.inserted_id}")
    except Exception as e:
        print(f"❌ Помилка при додаванні кота: {e}")


# -------------------------------
# READ (читання)
# -------------------------------
def get_all_cats():
    """Виводить усіх котів"""
    try:
        cats = collection.find()
        for cat in cats:
            pprint(cat)
    except Exception as e:
        print(f"❌ Помилка при читанні: {e}")


def get_cat_by_name(name: str):
    """Знаходить кота за ім'ям"""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            pprint(cat)
        else:
            print("❌ Кота не знайдено")
    except Exception as e:
        print(f"❌ Помилка при пошуку кота: {e}")


# -------------------------------
# UPDATE (оновлення)
# -------------------------------
def update_cat_age(name: str, new_age: int):
    """Оновлює вік кота за ім'ям"""
    try:
        result = collection.update_one(
            {"name": name}, {"$set": {"age": new_age}}
        )
        if result.matched_count:
            print(f"✅ Вік кота '{name}' оновлено")
        else:
            print("❌ Кота не знайдено")
    except Exception as e:
        print(f"❌ Помилка при оновленні віку: {e}")


def add_feature(name: str, feature: str):
    """Додає нову характеристику коту"""
    try:
        result = collection.update_one(
            {"name": name}, {"$push": {"features": feature}}
        )
        if result.matched_count:
            print(f"✅ Характеристику додано для кота '{name}'")
        else:
            print("❌ Кота не знайдено")
    except Exception as e:
        print(f"❌ Помилка при оновленні характеристик: {e}")


# -------------------------------
# DELETE (видалення)
# -------------------------------
def delete_cat(name: str):
    """Видаляє кота за ім'ям"""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print(f"✅ Кота '{name}' видалено")
        else:
            print("❌ Кота не знайдено")
    except Exception as e:
        print(f"❌ Помилка при видаленні кота: {e}")


def delete_all_cats():
    """Видаляє всіх котів"""
    try:
        result = collection.delete_many({})
        print(f"✅ Видалено {result.deleted_count} котів")
    except Exception as e:
        print(f"❌ Помилка при масовому видаленні: {e}")


# -------------------------------
# DEMO приклади використання
# -------------------------------
if __name__ == "__main__":
    # Додавання котів
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat("Murzik", 5, ["сірий", "любить рибу", "муркотить"])

    print("\n--- Усі коти ---")
    get_all_cats()

    print("\n--- Пошук Барсика ---")
    get_cat_by_name("Barsik")

    print("\n--- Оновлюємо вік Барсика ---")
    update_cat_age("Barsik", 4)

    print("\n--- Додаємо характеристику ---")
    add_feature("Murzik", "любить спати на дивані")

    print("\n--- Видаляємо Барсика ---")
    delete_cat("Barsik")

    print("\n--- Усі коти після змін ---")
    get_all_cats()

    print("\n--- Видаляємо всіх котів ---")
    delete_all_cats()