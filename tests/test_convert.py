import io
import pandas as pd
import pytest

from csv_converter import convert


SAMPLE_CSV = """a,b,c
1,2,3
4,5,6
"""


def test_read_csv(tmp_path):
    p = tmp_path / "sample.csv"
    p.write_text(SAMPLE_CSV)
    df = convert.read_csv(str(p))
    assert list(df.columns) == ["a", "b", "c"]
    assert df.shape == (2, 3)


def test_filter_columns(tmp_path):
    p = tmp_path / "sample.csv"
    p.write_text(SAMPLE_CSV)
    df = convert.read_csv(str(p))
    df2 = convert.filter_columns(df, ["b", "a"])
    assert list(df2.columns) == ["b", "a"]
    assert df2.shape == (2, 2)


def test_filter_missing_column(tmp_path):
    p = tmp_path / "sample.csv"
    p.write_text(SAMPLE_CSV)
    df = convert.read_csv(str(p))
    with pytest.raises(ValueError):
        convert.filter_columns(df, ["nope"]) 
