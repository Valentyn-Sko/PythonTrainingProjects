import sqlite3


def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("Create table if NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()


def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("insert into store values (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def delete(item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("delete from store where item=?", (item,))
    conn.commit()
    conn.close()


def updateQty(item, newQty):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("update store set quantity= ? where item=?", (newQty, item,))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("select * from store")
    rows = cur.fetchall()
    conn.close()
    print(rows)


def my_prog():
    create_table()
    # insert('item3', 30, 0.3)
    # delete('item3')
    updateQty('item1', 30)
    view()


if __name__ == "__main__":
    my_prog()
