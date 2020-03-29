import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='test_db_for_practice' user='test_ps_test' password='test_ps_test' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("Create table if NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='test_db_for_practice' user='test_ps_test' password='test_ps_test' host='localhost' port='5432'")


    cur = conn.cursor()
    cur.execute("insert into store values (%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()


def delete(item):
    conn = psycopg2.connect(
        "dbname='test_db_for_practice' user='test_ps_test' password='test_ps_test' host='localhost' port='5432'")


    cur = conn.cursor()
    cur.execute("delete from store where item=%s", (item,))
    conn.commit()
    conn.close()


def updateQty(item, newQty):
    conn = psycopg2.connect(
        "dbname='test_db_for_practice' user='test_ps_test' password='test_ps_test' host='localhost' port='5432'")


    cur = conn.cursor()
    cur.execute("update store set quantity= %swhere item=%s", (newQty, item,))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='test_db_for_practice' user='test_ps_test' password='test_ps_test' host='localhost' port='5432'")


    cur = conn.cursor()
    cur.execute("select * from store")
    rows = cur.fetchall()
    conn.close()
    print(rows)


def my_prog():
    create_table()
    insert('item3', 30, 0.3)
    # delete('item3')
    #updateQty('item1', 30)
    view()


if __name__ == "__main__":
    my_prog()
