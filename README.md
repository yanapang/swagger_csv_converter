# csv_converter

Small pandas-based helper for reading and manipulating CSVs with a tiny CLI.

Quickstart

1. Create and activate a virtual environment (recommended):

   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run tests:

   python -m pytest -q

4. Example usage (convert CSV and select columns):

   python -m csv_converter.cli --input data/in.csv --output data/out.csv --columns col1 col2

Files created

- `src/csv_converter/convert.py` — core helpers (read, filter, write)
- `src/csv_converter/cli.py` — simple CLI
- `tests/test_convert.py` — pytest tests
- `requirements.txt` — dependencies

- in order to conver file, add swagger json file on ./src/csv_converter path, and converted file will be also created on the same directory.

Notes

- This project keeps things minimal. If you want parquet support, add `pyarrow` to `requirements.txt`.
