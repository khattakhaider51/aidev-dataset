"""
Script to analyze AI-generated PRs in the AIDev dataset
"""
from datasets import load_dataset
import json
from collections import Counter

def analyze_aidev():
    print("Loading AIDev dataset...")
    ds = load_dataset("hao-li/AIDev", "all_pull_request")
    
    data = ds['train']
    print(f"\n📊 Dataset Analysis:")
    print(f"Total PRs: {len(data)}")
    
    # Analyze key columns
    if 'label' in data.column_names:
        labels = Counter([record['label'] for record in data if 'label' in record])
        print(f"\nLabel Distribution:")
        for label, count in labels.most_common():
            print(f"  {label}: {count}")
    
    print(f"\nColumns: {data.column_names}")
    
    # Save analysis results
    with open("analysis_results.json", "w") as f:
        json.dump({
            "total_records": len(data),
            "columns": data.column_names
        }, f, indent=2)
    
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    analyze_aidev()
