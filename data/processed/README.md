# data/processed/ Folder

## Overview
This folder contains **cleaned, transformed** data files ready for analysis.

Files here are:
- Generated from scripts that process data in `../raw/`
- Always **regenerable** from raw data
- Safe to delete and recreate
- Ready to use in analysis notebooks

## File Documentation

### Donations - Cleaned
- **File**: `donations_cleaned.csv`
- **Created By**: [notebook or script name]
- **Source**: `../raw/donations_raw_2024.csv`
- **Transformations Applied**:
  - Removed duplicate records
  - Standardized date format
  - [List other transformations]
- **Records**: [Number of rows]
- **Date Updated**: [YYYY-MM-DD]

## Processing Documentation
Each processed file should have associated documentation:
- Which raw files were combined/transformed
- Data cleaning steps applied
- Rows removed and why
- Null values handled (how?)
- Date ranges in final data

## How to Use
```python
import pandas as pd

# Load processed data (cleaned and ready)
df_donations = pd.read_csv('data/processed/donations_cleaned.csv')

# This data is ready for analysis
print(df_donations.head())
print(df_donations.info())
```

## Regeneration
If you need to regenerate processed data:
1. Run the cleaning script/notebook
2. New file will be created here
3. Old file will be overwritten (or backed up)
4. Always commit processed data script, not the file itself

## File Naming Convention
```
{description}_cleaned.{ext}
```

Examples:
- `donations_cleaned.csv`
- `donors_deduplicated.csv`
- `campaign_data_processed.csv`

## See Also
- [../raw/README.md](./raw/README.md) - Raw data documentation
- [../STRUCTURE.md](../STRUCTURE.md) - Project structure overview
