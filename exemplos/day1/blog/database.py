from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()

conn.execute(
    """\
    CREATE TABLE if not exists post (
        id integer PRIMARY KEY AUTOINCREMENT,
        title vachar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """
)

posts = [
    {
        "title": "Python é eleita a liguagem mais popular",
        "content": """\
        A lingaguem Python foi eleita a linguagem mias popular pela revista
        tech masters e  segue dominando o mundo.
        """,
        "author": "Satoshi Namamoto",
    },
    {
        "title": "Como criar um blog utilizando Python",
        "content": """\
        Neste tutorial você aprenderá como criar um blolg utilizando Python.
        <pre>import make a blog </pre>
        """,
        "author": "Guido Van  Rossum",
    },
]

count = cursor.execute("SELECT * FROM post;").fetchall()

if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author)
        """,
        posts
    )
    conn.commit()

posts = cursor.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2
