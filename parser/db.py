import psycopg2

connection = psycopg2.connect(
            user="postgres",             # ваше имя пользователя в PostgreSQL
            password="mysecretpassword",         # ваш пароль
            host="127.0.0.1",                 # адрес сервера базы данных, обычно localhost
            port="5433",                      # порт
            database="postgres"     # имя вашей базы данных
        )
cur = connection.cursor()


def insert_data_into_table(data):
    cursor = connection.cursor()

    # Исправленный запрос SQL
    insert_query = "INSERT INTO vk_comment (comment) VALUES (%s)"

    cursor.execute(insert_query, (data,))


    connection.commit()

        # Вывод информации о вставке данных
    print("Данные успешно вставлены")

