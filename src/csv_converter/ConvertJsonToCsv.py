import json
import pandas as pd

# Option 1️⃣: read from local file
JSON_FILE_NAME = "docs/api-docs.json"  # Replace with your CSV file path

with open(JSON_FILE_NAME, "r", encoding="utf-8") as f:
    swagger = json.load(f)

# Option 2️⃣: (if you want to fetch via URL instead)
# import requests
# url = "http://localhost:8080/v3/api-docs"
# swagger = requests.get(url).json()

paths = swagger.get("paths", {})

data = []
for path, methods in paths.items():
    # Iterate through each HTTP method (GET, POST, PUT, DELETE, etc.)
    for method, operation in methods.items():
        # Extract tags and comments (description) from the operation definition
        if isinstance(operation, dict):
            tags = operation.get("tags", [])
            tag_str = ", ".join(tags) if tags else "untagged"
            comments = operation.get("description", "No description provided")
        else:
            tag_str = "untagged"
            comments = "No description provided"
        
        # Build a row with path, HTTP method, tags, and comments
        data.append({
            "path": path,
            "method": method.upper(),
            "tags": tag_str,
            "comments": comments
        })

df = pd.DataFrame(data, columns=["path", "method", "tags", "comments"])
# Sort by tags first, then by path, then by method
df = df.sort_values(by=["tags", "path", "method"]).reset_index(drop=True)

output_path = "docs/swagger_paths.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ Exported {len(df)} rows sorted by tags to {output_path}")
