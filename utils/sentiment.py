# utils/sentiment.py
from typing import Dict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()

def score_text(text: str) -> float:
    if not text:
        return 0.0
    return float(_analyzer.polarity_scores(text).get("compound", 0.0))

def label_for_score(score: float) -> str:
    if score >= 0.05:
        return "Positive"
    if score <= -0.05:
        return "Negative"
    return "Neutral"

def compute_sentiment(text: str) -> Dict[str, float | str]:
    comp = score_text(text)
    return {"compound": comp, "label": label_for_score(comp)}