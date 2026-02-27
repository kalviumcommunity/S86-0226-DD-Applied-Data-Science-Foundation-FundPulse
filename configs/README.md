# configs/ Folder

## Overview
This folder contains **configuration files and constants** for the project.

Centralize settings here instead of hardcoding them in code (makes changes easy).

## Files

### `config.yaml`
Main project configuration file:
- File paths and data locations
- Analysis parameters and thresholds
- Project metadata

Example:
```yaml
# Project Information
project_name: FundPulse
version: 1.0
description: Non-profit donation analysis

# Data Paths
data:
  raw: data/raw/
  processed: data/processed/

# Output Paths
outputs:
  figures: outputs/figures/
  reports: outputs/reports/
  models: outputs/models/

# Analysis Parameters
analysis:
  min_repeat_donor_threshold: 2
  date_format: "%Y-%m-%d"
  currency_symbol: "$"
  
# Processing Options
processing:
  handle_missing: "drop"
  remove_duplicates: true
  standardize_amounts: true
```

### `constants.py`
Python file for constants used in code:

```python
'''
constants.py - Project-wide constants
'''

# File paths
RAW_DATA_PATH = 'data/raw/'
PROCESSED_DATA_PATH = 'data/processed/'
FIGURES_PATH = 'outputs/figures/'
REPORTS_PATH = 'outputs/reports/'

# Analysis parameters
MIN_REPEAT_DONOR_THRESHOLD = 2
DATE_FORMAT = "%Y-%m-%d"
CURRENCY_SYMBOL = "$"

# Data processing
MISSING_DATA_STRATEGY = "drop"
REMOVE_DUPLICATES = True

# Visualization defaults
FIGURE_DPI = 300
FIGURE_FORMAT = "png"
FIGURE_STYLE = "seaborn"
```

## How to Use

### In Python Code

```python
from configs.constants import RAW_DATA_PATH, MIN_REPEAT_DONOR_THRESHOLD
import pandas as pd

# Use constants in code
df = pd.read_csv(RAW_DATA_PATH + 'donations.csv')

# Find repeat donors
repeat_donors = df.groupby('donor_id').size()
repeat_donors = repeat_donors[repeat_donors >= MIN_REPEAT_DONOR_THRESHOLD]
```

### For Configuration Files

```python
import yaml

# Load configuration
with open('configs/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Access settings
data_path = config['data']['raw']
threshold = config['analysis']['min_repeat_donor_threshold']
```

## Benefits

✅ **Centralized Settings**: Change values in one place
✅ **Reproducibility**: Clear parameters for rerunning analysis
✅ **Collaboration**: Others understand configuration choices
✅ **Maintainability**: Easy to update as project evolves

## Best Practices

✅ **DO**:
- Define all configurable parameters here
- Document what each setting controls
- Use meaningful names
- Include range/type information
- Update documentation when adding settings

❌ **DON'T**:
- Hardcode paths in analysis code
- Use magic numbers without explanation
- Store sensitive data (passwords, tokens) here
- Commit secrets to version control (use env vars)

## See Also
- [../STRUCTURE.md](../STRUCTURE.md) - Project structure
- [../notebooks/README.md](../notebooks/README.md) - How to import constants
