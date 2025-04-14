import pymysql

def get_connection():
    # Устанавливаем соединение с базой данных
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='system' #!
    )

def load_data(query="SELECT * FROM users"):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Выполняем запрос для получения записей
            cursor.execute(query)
            rows = cursor.fetchall()

            # Получаем имена колонок таблицы users
            cursor.execute("SHOW COLUMNS FROM users")
            columns = [column[0] for column in cursor.fetchall()]

        return rows, columns

    except Exception as e:
        raise e

    finally:
        if connection:
            connection.close()

def add_record(username, passwordd, role): #!
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Выполняем запрос для добавления новой записи в таблицу users
            sql = """INSERT INTO users (username, passwordd, role) 
                     VALUES (%s, %s, %s)"""
            values = (username, passwordd, role) #!
            cursor.execute(sql, values)
            connection.commit()

    except Exception as e:
        raise e

    finally:
        if connection:
            connection.close()

def update_record(username, passwordd, role, selected_id): #!
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Выполняем запрос для обновления данных записи в таблице users
            sql = """UPDATE users SET username = %s, passwordd = %s, role = %s 
                     WHERE id = %s"""
            values = (username, passwordd, role, selected_id) #!
            cursor.execute(sql, values)
            connection.commit()

    except Exception as e:
        raise e

    finally:
        if connection:
            connection.close()

def delete_record(selected_id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Выполняем запрос для удаления записи из таблицы users
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (selected_id,))
            connection.commit()

    except Exception as e:
        raise e

    finally:
        if connection:
            connection.close()

def get_record_by_id(selected_id):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Получаем текущие данные выбранной записи
            cursor.execute("SELECT * FROM users WHERE id = %s", (selected_id,))
            current_data = cursor.fetchone()
            return current_data

    except Exception as e:
        raise e

    finally:
        if connection:
            connection.close()
