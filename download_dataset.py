from datasets import load_dataset
import json
import os

# Load the AIDev dataset
print("Loading hao-li/AIDev dataset...")
ds = load_dataset("hao-li/AIDev", "all_pull_request")

# Create directory structure
os.makedirs("data", exist_ok=True)

# Save dataset as JSONL for version control
print(f"Total PR records: {len(ds['train'])}")

with open("data/aidev_pull_requests.jsonl", "w") as f:
    for record in ds['train']:
        f.write(json.dumps(record) + "\n")

print("Dataset downloaded and saved to data/aidev_pull_requests.jsonl")

# Create a summary
summary = {
    "dataset_name": "hao-li/AIDev",
    "config": "all_pull_request",
    "total_records": len(ds['train']),
    "columns": list(ds['train'].column_names)
}

with open("data/dataset_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Summary saved to data/dataset_summary.json")
