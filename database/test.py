import psycopg2
from dotenv import dotenv_values

config = dotenv_values()

try:
    # connect
    connection = psycopg2.connect(
        host=config['HOST'],
        user=config['USER'],
        password=config['PASSWORD'],
        database=config['DB_NAME']
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server vesion: {cursor.fetchone()}")


    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM users;

            """
        )

        #connection.commit()
        print(f"[INFO] {cursor.fetchone()}")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection in locals():
        connection.close()
        print("[INFO] PostgreSQL connection closed")

