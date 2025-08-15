
# API for my Classicbook ETL pipeline project

A FastAPI service that serves data from my Classic Book ETL pipeline, 
providing TSV and JSON endpoints for easy integration.


## How to run locally

# Set your GitHub raw URL for imitation.tsv
export DATA_URL="https://raw.githubusercontent.com/<your-username>/classicbook-datasets/main/data/imitation.tsv"

# Start the API
uvicorn app:app --reload