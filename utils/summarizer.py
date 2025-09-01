import os
import re
from typing import Optional

_USE_TRANSFORMERS = os.getenv("USE_TRANSFORMERS", "0") == "1"

_summarizer = None

if _USE_TRANSFORMERS:
    try:
        from transformers import pipeline
        # A light, commonly available summarization model
        _summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    except Exception:
        _summarizer = None # fallback below

def _naive_sent_split(text: str):
    # Simple sentence splitter without NLTK
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p]

def summarize_text(text: Optional[str], max_chars: int = 500) -> Optional[str]:
    """Return a short summary of `text`.
    - If transformers pipeline is enabled & available, use it.
    - Else: take first 2–3 sentences up to ~max_chars.
    """
    if not text:
        return None

    text = text.strip()
    if _summarizer:
        try:
        # distilbart works best with <1024 tokens; chunk if needed (skipped for brevity)
            out = _summarizer(text, max_length=120, min_length=40, do_sample=False)
            if out and isinstance(out, list) and out[0].get("summary_text"):
                return out[0]["summary_text"].strip()
        except Exception:
            pass # fall back to heuristic

# Heuristic fallback: take first 2–3 sentences within limit
sents = _naive_sent_split(text)
summary = []
for s in sents:
    if sum(len(x) for x in summary) + len(s) <= max_chars or len(summary) < 2:
        summary.append(s)
    else:
        break
    return " ".join(summary).strip()