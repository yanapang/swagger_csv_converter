"""Command-line interface for csv_converter."""
from __future__ import annotations

import argparse
import sys
from typing import List, Optional

from . import ConvertJsonToCsv


def parse_args(argv: Optional[List[str]] = None):
    p = argparse.ArgumentParser(description="Simple CSV reader/writer using pandas")
    p.add_argument("--input", "-i", required=True, help="Input CSV path")
    p.add_argument("--output", "-o", required=True, help="Output CSV path")
    p.add_argument("--columns", "-c", nargs="*", help="Optional list of columns to keep")
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    df = ConvertJsonToCsv.read_csv(args.input)
    df2 = ConvertJsonToCsv.filter_columns(df, args.columns)
    ConvertJsonToCsv.write_csv(df2, args.output)
    print(f"Wrote {len(df2)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    # Allow running as: python -m csv_converter.cli
    sys.exit(main())
