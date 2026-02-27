# src/ Folder

## Overview
This folder contains **reusable Python modules and functions** for the project.

Instead of writing code in notebooks, extract reusable logic into modules here and import them into notebooks.

## Module Organization

### `__init__.py`
Makes `src/` a Python package. Can be empty or contain package-level imports.

### `data_loader.py`
Functions for loading and reading data files:
- `load_raw_donations()` - Load raw donation data
- `load_processed_data()` - Load cleaned data
- `load_donor_metadata()` - Load donor information

### `data_processor.py`
Functions for cleaning and transforming data:
- `clean_dates()` - Standardize date formats
- `remove_duplicates()` - Identify and remove duplicate rows
- `calculate_donation_stats()` - Compute frequency, totals, etc.

### `utils.py`
General utility functions:
- `format_currency()` - Format numbers as currency
- `get_date_range()` - Extract date ranges from data
- `calculate_statistics()` - Common calculations

## How to Import

In notebooks, import modules from `src/`:

```python
import sys
sys.path.append('../src')

from data_loader import load_raw_donations, load_processed_data
from data_processor import clean_dates, remove_duplicates
from utils import format_currency

# Use functions in analysis
donations = load_raw_donations()
donations_clean = clean_dates(donations)
```

Or import at top of notebook:

```python
from src.data_loader import load_raw_donations
from src.data_processor import clean_dates
from src.utils import format_currency
```

## Best Practices

✅ **DO**:
- Extract reusable code from notebooks into modules
- Write functions with clear inputs and outputs
- Include docstrings explaining what functions do
- Use type hints for clarity
- Test functions before using in notebooks
- Keep modules focused on specific tasks

❌ **DON'T**:
- Write analysis logic in src/ (keep in notebooks)
- Create circular imports between modules
- Mix multiple unrelated functions in one module
- Hardcode paths or magic numbers
- Commit untested code

## Module Template

```python
'''
data_loader.py - Functions for loading donation and donor data
'''

def load_raw_donations(filepath='data/raw/donations.csv'):
    '''
    Load raw donation data from CSV.
    
    Parameters:
        filepath (str): Path to raw data file
        
    Returns:
        pd.DataFrame: Donation records
    '''
    import pandas as pd
    return pd.read_csv(filepath)

def load_processed_data(filepath='data/processed/donations_cleaned.csv'):
    '''
    Load processed, cleaned donation data.
    
    Parameters:
        filepath (str): Path to processed data file
        
    Returns:
        pd.DataFrame: Clean donation records
    '''
    import pandas as pd
    return pd.read_csv(filepath)
```

## Testing
Create simple test functions or write tests in notebooks to verify modules work:

```python
# Test in notebook
from src.data_loader import load_raw_donations

data = load_raw_donations()
print(f"Loaded {len(data)} donation records")
print(data.head())
```

## See Also
- [../STRUCTURE.md](../STRUCTURE.md) - Project structure
- [../notebooks/README.md](../notebooks/README.md) - How to import modules
