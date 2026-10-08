import os
import re
import sqlite3
from contextlib import closing

from flask import Flask, abort, redirect, render_template_string, request

DB_PATH = os.environ.get("DB_PATH", "reviews.db")
COURSE_CODE = re.compile(r"[A-Z]{2}\d{3}[A-Z0-9]")  # e.g. DD2482, DD142X

PAGE = """<!doctype html>
<title>KTH course reviews</title>
<h1>KTH course reviews</h1>
<form method="post">
  <input name="course" placeholder="DD2482" required pattern="[A-Za-z]{2}[0-9]{3}[A-Za-z0-9]">
  <select name="rating">{% for i in range(5, 0, -1) %}<option>{{ i }}</option>{% endfor %}</select>
  <textarea name="body" required maxlength="2000"></textarea>
  <button>Post anonymously</button>
</form>
{% for course, rating, body, created in reviews %}
<article><h3>{{ course }} &middot; {{ rating }}/5</h3><p>{{ body }}</p><small>{{ created }}</small></article>
{% endfor %}
"""


def query(sql, args=()):
    with closing(sqlite3.connect(DB_PATH)) as con, con:
        return con.execute(sql, args).fetchall()


query(
    "CREATE TABLE IF NOT EXISTS reviews (course TEXT NOT NULL,"
    " rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5), body TEXT NOT NULL,"
    " created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)"
)

app = Flask(__name__)


@app.get("/")
def index():
    reviews = query(
        "SELECT course, rating, body, created FROM reviews ORDER BY rowid DESC LIMIT 100"
    )
    return render_template_string(PAGE, reviews=reviews)


@app.post("/")
def add_review():
    course = request.form.get("course", "").strip().upper()
    rating = request.form.get("rating", "")
    body = request.form.get("body", "").strip()
    if (
        not COURSE_CODE.fullmatch(course)
        or rating not in list("12345")
        or not 0 < len(body) <= 2000
    ):
        abort(400)
    query(
        "INSERT INTO reviews (course, rating, body) VALUES (?, ?, ?)",
        (course, int(rating), body),
    )
    return redirect("/", 303)


@app.get("/health")
def health():
    return "ok"
