from psycopg2 import pool

# Initialize connection pool
connection_pool = None


def initialize_connection_pool():
    global connection_pool
    connection_pool = pool.SimpleConnectionPool(
        1,
        20,
        dbname="jktech",
        user="postgres",
        password="password",
        host="localhost",
        port="5432",
    )


def establish_db_connection():
    global connection_pool
    if connection_pool is None:
        initialize_connection_pool()
    try:
        return connection_pool.getconn()
    except Exception as e:
        print(f"Error establishing database connection: {e}")
        return None


def create_tables():
    conn = establish_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                embeddings FLOAT8[] NOT NULL
            )
            """
        )
        conn.commit()
        cursor.close()
        connection_pool.putconn(conn)
    else:
        print("Failed to create tables due to connection error.")
