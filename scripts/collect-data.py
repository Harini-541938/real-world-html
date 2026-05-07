import json
import os
from datetime import datetime
import requests

DATA_FILE = "data/log.json"

# Example public API
response = requests.get("https://api.github.com")
api_status = response.status_code

entry = {
    "timestamp": datetime.utcnow().isoformat(),
    "github_api_status": api_status
}

# Create folder if missing
os.makedirs("data", exist_ok=True)

# Load existing data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = []

# Append new entry
data.append(entry)

# Save updated log
with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=2)

print("Data collected successfully")
