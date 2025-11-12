# csv_converter

Small pandas-based helper for converting Swagger JSON to CSV and CSV to SQL DML statements.

## Quickstart

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:

   ```bash
   python -m pytest -q
   ```

## Usage

### 1. Convert Swagger JSON to CSV - swagger json 파일 csv 파일로 변경

Converts Swagger/OpenAPI JSON documentation to CSV format:

```bash
cd src/csv_converter
python 1_ConvertJsonToCsv.py
```

**Requirements:**
- Place your Swagger JSON file at `docs/api-docs.json`\
```get your swagger json file from {SWAGGER_URL}/v3/api-docs```
- Output CSV will be created at `docs/swagger_paths.csv`

### 2. Convert CSV to SQL DML - api 리스트 테이블 insert query 생성

Converts CSV data to SQL INSERT statements:

```bash
cd src/csv_converter
python 2_ConvertCsvToDml.py
```

**Requirements:**
- Place your CSV file at `docs/api_list.csv` with columns: `api_type`, `api_path`, `http_method`, `api_description`\

<img width="1606" height="65" alt="image" src="https://github.com/user-attachments/assets/bd0c9d6d-73df-432b-832b-544df7d2d7e9" />

- Output SQL file will be created at `docs/cicd_api_init_data.sql`

**Features:**
- Automatically skips rows with empty `api_type` values
- Generates sequential IDs for each `api_type` (e.g., `developer_1`, `developer_2`)
- Handles empty descriptions by defaulting to "No description provided"

### CLI Usage

Simple CLI for CSV filtering:

```bash
python -m csv_converter.cli --input input.csv --output output.csv --columns col1 col2
```

## Project Structure

- `src/csv_converter/ConvertJsonToCsv.py` — converts Swagger JSON to CSV
- `src/csv_converter/ConvertCsvToDml.py` — converts CSV to SQL DML statements
- `src/csv_converter/cli.py` — simple CLI for CSV operations
- `tests/test_convert.py` — pytest tests
- `requirements.txt` — dependencies
- `docs/` — directory for input/output files

## Notes

- Input/output files are stored in the `docs/` directory
- Empty values in CSV are automatically detected and skipped using `pd.isna()` and empty string checks
- This project keeps things minimal. If you want parquet support, add `pyarrow` to `requirements.txt`.
