import os
import pandas as pd

# Configuration
TABLE_NAME = "cicd_menu_api_mapping"
MENU_CSV_PATH = "docs/menu.csv"
API_LIST_CSV_PATH = "docs/api_list.csv"
OUTPUT_DIR = "results"
OUTPUT_SQL_PATH = os.path.join(OUTPUT_DIR, f"{TABLE_NAME}.sql")


def is_empty(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, float) and pd.isna(value):
        return True
    return str(value).strip() == ""


def sanitize_str(value: object) -> str:
    if value is None:
        return ""
    # Remove wrapping quotes and normalize whitespace
    s = str(value).strip().strip("'").strip('"').strip()
    return s


def build_api_ids(df_api: pd.DataFrame) -> pd.Series:
    """
    Build stable api_id values using the same convention as before:
    {api_type}_{per-type-sequence}
    """
    counters: dict[str, int] = {}
    api_ids: list[str] = []
    for _, row in df_api.iterrows():
        api_type = sanitize_str(row.get("api_type", ""))
        if api_type not in counters:
            counters[api_type] = 0
        counters[api_type] += 1
        api_ids.append(f"{api_type}_{counters[api_type]}")
    return pd.Series(api_ids, index=df_api.index, name="api_id")


def main() -> None:
    # Read inputs
    df_menu = pd.read_csv(MENU_CSV_PATH, encoding="utf-8")
    df_api = pd.read_csv(API_LIST_CSV_PATH, encoding="utf-8")

    # Normalize columns
    # menu.csv expected columns: menu_id, solution_type, menu_category1, menu_category2, is_active

    mapping_values = []
    for _, row  in df_menu.iterrows():
        menu_id = row("menu_id")

        for index, row in df_api.iterrows():
            api_id = row("api_id")

            #here to insert menu_api_mapping table
            sql = f"('{menu_id}', '{api_id}')"
            mapping_values.append(sql)

    sql = "INSERT INTO menu_api_mapping (menu_id, api_id) VALUES\n" + ",\n".join(mapping_values) + ";"
    with open(OUTPUT_SQL_PATH, "w", encoding="utf-8") as f:
        f.write(sql)

    print(f"✅ Generated {len(mapping_values)} rows in {OUTPUT_SQL_PATH}")


if __name__ == "__main__":
    main()

