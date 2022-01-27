import os
import sqlite3


def get_unique_names() -> list:
    """
    :return: list of unique employees' names in the database
    """
    db_path = os.path.join(os.getcwd(), "chinook.db")
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    query = """
        SELECT DISTINCT FirstName
        FROM employees;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    connect.close()

    print(f"Unique names are:")
    for item in result:
        item = list(item)
        for employee_name in item:
            print(f"{employee_name}")

    return result


def get_price(item_id, quantity) -> float:
    """
    :param item_id: the id of the item we want to buy
    :param quantity: the amount of this item
    :return: the item`s final price
    """
    db_path = os.path.join(os.getcwd(), "chinook.db")
    connect = sqlite3.connect(db_path)
    cursor = connect.cursor()
    query = f"""
        SELECT UnitPrice * {quantity}
        FROM invoice_items
        WHERE TrackId = {item_id};
    """
    cursor.execute(query)
    record = cursor.fetchall()
    connect.close()
    result = float(record[0][0])

    return result


get_unique_names()
order_income = get_price(1, 10)
print(order_income)


