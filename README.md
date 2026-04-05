# AIDev Dataset Mirror

Mirror of the [hao-li/AIDev](https://huggingface.co/datasets/hao-li/AIDev) dataset from Hugging Face.

## Dataset Info
- **Source:** hao-li/AIDev
- **Config:** all_pull_request
- **Size:** 939k+ pull requests
- **Purpose:** AI-generated code review analysis

## Files
- `data/aidev_pull_requests.jsonl` - Full dataset in JSONL format
- `data/dataset_summary.json` - Dataset metadata
- `scripts/` - Analysis and processing scripts

## Qodo Integration
This repository is configured with Qodo Code Review for analyzing AI-generated pull request data and code quality.

## Usage
```python
from datasets import load_dataset
ds = load_dataset("hao-li/AIDev", "all_pull_request")
