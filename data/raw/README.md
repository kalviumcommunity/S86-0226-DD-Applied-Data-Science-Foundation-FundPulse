# data/raw/ Folder

## Overview
This folder contains **original, unmodified** source data files as received from data providers.

**GOLDEN RULE**: This folder is read-only. Never edit or delete files here.

## File Documentation

### Donations Data
- **File**: [Add your raw data file name here]
- **Source**: [Document where this data comes from]
- **Date Received**: [YYYY-MM-DD]
- **Format**: CSV / Excel / JSON / etc.
- **Records**: [Number of rows]
- **Columns**: [List key columns]
- **Size**: [File size]

### Donor Metadata (if applicable)
- **File**: [Add your raw data file name here]
- **Source**: [Document source]
- **Date Received**: [YYYY-MM-DD]
- **Format**: CSV / Excel / JSON / etc.
- **Records**: [Number of rows]
- **Notes**: [Any special information]

## Data Quality Notes
- List any known data quality issues
- Document missing values or anomalies
- Note if data includes test or duplicate records
- Document date ranges covered

## Processing Steps
When processing this raw data, follow these basic steps:
1. Load data from this folder
2. Inspect for quality issues
3. Clean and transform
4. Save cleaned version to `../processed/`
5. Document all transformations in processing script

## How to Use
```python
import pandas as pd

# Load raw data
df = pd.read_csv('data/raw/donations_raw_2024.csv')

# Never modify this data in place
# Instead, create processed version in data/processed/
```

## Important Reminders
- ⛔ Do NOT modify files in this folder
- ⛔ Do NOT delete or move files
- ⛔ Do NOT save new versions here
- ✅ DO document data sources and dates
- ✅ DO keep backups elsewhere if critical
