import os
from statistics import fmean
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv

from services.google_books import fetch_books_for_title, GoogleBooksError
from utils.summarize import summarize_text
from utils.sentiment import score_text, label_for_score, compute_sentiment

load_dotenv() # load .env if present

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/search")
def api_search():
    query = (request.args.get("book") or "").strip()
    if not query:
        return jsonify({"error": "Missing 'book' query parameter"}), 400