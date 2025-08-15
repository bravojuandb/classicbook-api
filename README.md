
# API for my Classicbook ETL pipeline project

A FastAPI service that serves data from my Classic Book ETL pipeline, 
providing TSV and JSON endpoints for easy integration.


## How to run locally

# Set your GitHub raw URL for imitation.tsv
export DATA_URL="https://github.com/bravojuandb/classicbook-datasets/tree/main/data/aligned/book1_aligned.tsv"

# Start the API
uvicorn app:app --reload