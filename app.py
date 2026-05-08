from flask import Flask, render_template, request
import sqlite3

app = Flask(_name_)

# =========================
# DATABASE
# =========================

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


# База түзүү
conn = get_db()

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()

# =========================
# HOME
# =========================

@app.route("/")
def home():
    return render_template("login.html")


# =========================
# REGISTER
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()

        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return """
        <h1 style='color:green;text-align:center;margin-top:100px;'>
        Сиздин запрос текшерилүүдө...
        </h1>
        """

    return render_template("register.html")


# =========================
# RUN
# =========================

if _name_ == "_main_":
    app.run(debug=True)
