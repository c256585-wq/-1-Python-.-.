def validate_database(database):
    if database is None:
        print("Ошибка: база данных отсутствует.")
        return False

    if not isinstance(database, list):
        print("Ошибка: база данных имеет неверный тип.")
        return False

    if not database:
        print("Ошибка: база данных пуста.")
        return False

    if len(database) < 25:
        print("Ошибка: в базе данных менее 25 записей "f"({len(database)}).")
        return False

    return True