import os
import csv
import requests
from fastapi import FastAPI, Response, HTTPException

app = FastAPI()

DATA_URL = os.getenv("DATA_URL")
if not DATA_URL:
    raise RuntimeError("DATA_URL environment variable not set.")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/export/tsv")
def export_tsv():
    try:
        r = requests.get(DATA_URL, timeout=10)
        r.raise_for_status()
        return Response(content=r.text, media_type="text/tab-separated-values; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/export/json")
def export_json():
    try:
        r = requests.get(DATA_URL, timeout=10)
        r.raise_for_status()
        rows = list(csv.DictReader(r.text.splitlines(), delimiter="\t"))
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))