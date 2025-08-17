
# API for my Classicbook ETL pipeline project

A FastAPI service that serves data from my Classic Book ETL pipeline, 
providing TSV and JSON endpoints for easy integration.


## How to run locally

1. Set the environmental variable:

```bash
export DATA_URL="https://raw.githubusercontent.com/bravojuandb/classicbook-datasets/refs/heads/main/data/aligned/book1_aligned.tsv"
```

2. Start the API
```bash
uvicorn app:app --reload
```