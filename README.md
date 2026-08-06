# GFT ViaCEP ETL Pipeline

A simple ETL pipeline in Python that reads Brazilian postal codes (CEP), retrieves address information from the ViaCEP API, and stores the results in multiple output formats.
This project was built as a study case focused on ETL pipelines, concurrent API requests, and data persistence using Python.

## Features

- Extract valid CEPs from a CSV file
- Fetch address data from the ViaCEP API
- Parallel processing with `ThreadPoolExecutor`
- HTTP connection reuse with `requests.Session()`
- Store results in SQLite, JSON and XML
- Export failed CEPs to CSV
- Unit tests and GitHub Actions workflow

## Project Structure

```
app/
├── extract/
├── transform/
├── load/
├── scripts/
└── samples/
```

## Installation

```bash
git clone https://github.com/<username>/gft-viacep.git
cd gft-viacep

python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## Running

```bash
python app/main.py
```

If the input CSV does not exist in /data, it will be generated automatically.

## Running Tests

```bash
pytest
```

## Docker

Build:

```bash
docker build -t gft-viacep .
```

Run:

```bash
docker run --rm gft-viacep
```

## Output

The pipeline generates in /data:

- `addresses.db`
- `addresses.json`
- `addresses.xml`
- `errors.csv`

## Technologies

- Python
- SQLite
- Requests
- ThreadPoolExecutor
- Pytest
- GitHub Actions
- Docker
