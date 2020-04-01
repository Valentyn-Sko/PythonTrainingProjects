import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "create table if NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "insert into book values (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from book where title=? OR author=? or year=? or isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "delete from book where id=?", (id,))
    conn.commit()
    conn.close()


def update(id,title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "update book set title=?, author=?, year=?,isbn=? where id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
# insert('tower','king',1980,123456789)

print(search(title='it'))
print(search(author='king'))
print(search(year=1980))
print(search(isbn=123456789))
print(view())
#delete(2)
update(3,'tower1','king',1980,123456789)
print(view())
