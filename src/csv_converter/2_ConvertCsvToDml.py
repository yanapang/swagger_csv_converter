import json
import pandas as pd

'''
# CVS Converter: Convert CSV to Dml.

해당 csv 파일은 ConvertJsonToCsv.py 를 통해 생성된 파일이 아닌, 
권한별 api_type이 추가된 파일입니다.

docs/api_list_example.csv 파일의 heading 참고.

# 다음 형식으로 변경됨.
INSERT INTO TABLE_NAME (api_id, solution_type, api_path, api_description, is_active) VALUES
    (${UUID}, {SOLUTION_TYPE}, ${PATH}, ${DESCRIPTION}, TRUE);

'''

# Define constants
TABLE_NAME = "cicd_api" # Replace with your Table name
SOLUTION_TYPE = "VIOLA_CICD" # Replace with your Solution Type

# Read the CSV file
csv_file = "docs/api_list.csv"  # Replace with your CSV file path
df = pd.read_csv(csv_file, encoding="utf-8")

# Generate DML queries
values = []
api_type_counters = {}  # Dictionary to keep track of numbering for each api_type

for index, row in df.iterrows():

    api_type = row["api_type"]
    api_path = row["api_path"]
    http_method = row["http_method"]
    
    if pd.isna(api_type) or str(api_type).strip() == "":
        continue

    api_description = row.get("api_description", "No description provided")

    # Increment the counter for the current api_type
    if api_type not in api_type_counters:
        api_type_counters[api_type] = 0
    api_type_counters[api_type] += 1

    api_id = f"{api_type}_{api_type_counters[api_type]}"

    value = f"('{api_id}', '{SOLUTION_TYPE}', '{api_path}', '{http_method}', '{api_description}', TRUE)"
    values.append(value)

query = f"INSERT INTO {TABLE_NAME} (api_id, solution_type, api_path, http_method, api_description, is_active) VALUES\n" + ",\n".join(values) + ";"

# Write queries to a file
with open(f"results/{TABLE_NAME}_init_data.sql", "w") as f:
    f.write(query)

print(f"✅ Generated DML query for {len(values)} rows in output.sql")