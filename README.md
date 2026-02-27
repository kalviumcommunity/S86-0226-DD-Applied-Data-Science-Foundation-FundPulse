# FundPulse: Non-Profit Donation Analysis

**Analyzing donor behavior to identify repeat donors, donation frequency trends, and periods of high fundraising effectiveness.**

---

## 📋 Quick Overview

FundPulse is a Data Science project focused on understanding donation patterns in non-profit organizations. By analyzing donation records, we identify:

- **Repeat Donors**: Who gives multiple times?
- **Frequency Trends**: How often do donors give?
- **High-Effectiveness Periods**: When is fundraising most successful?

This project demonstrates professional Data Science practices through clean organization, clear documentation, and reproducible analysis.

---

## 📁 Project Structure

```
FundPulse/
├── README.md                    # This file
├── STRUCTURE.md                 # Detailed folder organization guide
├── PROBLEM_STATEMENT.md         # Complete problem definition
│
├── data/                        # All data-related files
│   ├── raw/                     # ← Original, untouched source data
│   ├── processed/               # ← Cleaned, transformed data
│   └── README.md                # Data folder documentation
│
├── notebooks/                   # Jupyter notebooks (primary analysis)
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── README.md
│
├── src/                         # Reusable Python modules
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_processor.py
│   ├── utils.py
│   └── README.md
│
├── outputs/                     # Generated results (plots, reports)
│   ├── figures/                 # Charts and visualizations
│   ├── reports/                 # Analysis summaries
│   └── README.md
│
├── configs/                     # Configuration and constants
│   └── README.md
│
└── docs/                        # Project documentation
    ├── DATA_DICTIONARY.md       # Data field definitions
    ├── METHODOLOGY.md           # Analysis approach
    ├── ASSUMPTIONS.md           # Explicit assumptions
    └── README.md
```

---

## 🔄 Data Lifecycle: Raw → Processed → Outputs

This project demonstrates **the three stages of data handling**—the foundation of reproducible, trustworthy Data Science:

### Stage 1: Raw Data (`data/raw/`)

**Purpose**: Store original, unmodified source data exactly as received.

✅ **Golden Rule**: This folder is **READ-ONLY**. Never edit files here.

```
data/
└── raw/
    ├── donations_raw_2024.csv          ← Original data file
    └── README.md                        ← Document sources and dates
```

**Why?**
- Preserves evidence of original data
- Enables reproducibility (always start from same source)
- Protects against accidental corruption
- Creates audit trail of what data we started with

**Example:**
```python
# Loading raw data (read-only)
import pandas as pd
df_raw = pd.read_csv('data/raw/donations_raw_2024.csv')
# NEVER modify df_raw directly—create a copy if you need to clean
```

---

### Stage 2: Processed Data (`data/processed/`)

**Purpose**: Store cleaned, transformed datasets created from raw data.

```
data/
└── processed/
    ├── donations_cleaned.csv            ← Processed from raw
    ├── donors_deduplicated.csv          ← Processed from raw
    └── README.md                        ← Document transformations
```

**Why?**
- Separates raw from cleaned (clarity)
- Documents transformation steps
- Enables reproducibility (regenerate from raw anytime)
- Protects raw data from accidental modification

**Transformation Flow:**
```
data/raw/donations_raw_2024.csv
         ↓ (cleaning script)
data/processed/donations_cleaned.csv
         ↓ (analysis notebooks)
outputs/figures/  &  outputs/reports/
```

**Regenerating Processed Data:**
```python
# In a cleaning script/notebook:
df_raw = pd.read_csv('data/raw/donations_raw_2024.csv')

# Clean and transform
df_clean = df_raw.drop_duplicates()
df_clean['date'] = pd.to_datetime(df_clean['date'])

# Save to processed folder (never overwrite raw!)
df_clean.to_csv('data/processed/donations_cleaned.csv', index=False)

print("✓ Processed data saved. Raw data remains untouched.")
```

---

### Stage 3: Outputs (`outputs/`)

**Purpose**: Store final or intermediate results (plots, reports, models).

```
outputs/
├── figures/
│   ├── donation_distribution.png
│   ├── trend_by_month.pdf
│   └── seasonal_pattern.png
├── reports/
│   ├── repeat_donor_analysis.md
│   ├── fundraising_effectiveness.xlsx
│   └── summary_findings.pdf
└── README.md
```

**Why This Is Separate from Data Folders:**
- Outputs are **generated results**, not input data
- Should never be committed to raw or processed
- Safe to delete and regenerate
- Easy to organize by type (figures, reports, models)

**Example Output Generation:**
```python
# In analysis notebook:
import matplotlib.pyplot as plt

# Generate visualization
plt.figure(figsize=(10, 6))
plt.hist(df['donation_amount'], bins=30)
plt.title('Donation Distribution')

# Save to outputs (NOT to data folder!)
plt.savefig('outputs/figures/donation_distribution.png', dpi=300)
plt.close()

print("✓ Figure saved. Data remains clean and separate.")
```

---

## ⚠️ Critical Principles: Preventing Data Contamination

### ✗ What NOT to Do

**❌ Problem 1: Modifying Raw Data**
```python
# WRONG! Modifies original file
df = pd.read_csv('data/raw/donations.csv')
df = df.drop_duplicates()  # Lost original duplicates!
df.to_csv('data/raw/donations.csv')  # Overwrites source!
```

**✅ Solution:**
```python
# RIGHT! Preserves raw, creates processed
df_raw = pd.read_csv('data/raw/donations.csv')
df_clean = df_raw.drop_duplicates()
df_clean.to_csv('data/processed/donations_cleaned.csv')
```

---

**❌ Problem 2: Mixing Outputs with Data**
```python
# WRONG! Output stored with input data
plt.savefig('data/raw/donation_distribution.png')  # ❌ Confuses files!
```

**✅ Solution:**
```python
# RIGHT! Outputs separated
plt.savefig('outputs/figures/donation_distribution.png')  # ✓ Clear
```

---

**❌ Problem 3: Unclear Data Flow**
```
No documentation of:
- Where did processed data come from?
- What transformations were applied?
- Can we regenerate it?
```

**✅ Solution:**
```
Each folder has README.md explaining:
- Source of raw data with dates
- Transformations applied to get processed
- How to regenerate if needed
```

---

## 🚀 Getting Started

### 1. Add Your Raw Data

Place your raw donation data file in `data/raw/`:

```bash
cp your_donations_data.csv data/raw/donations_raw_2024.csv
```

Then document it in `data/raw/README.md`:

```markdown
### Donations Data
- **File**: donations_raw_2024.csv
- **Source**: [Where it came from]
- **Date Received**: 2024-01-15
- **Records**: [Number of rows]
```

### 2. Create a Cleaning Script

Create a notebook or script that:
- Reads from `data/raw/`
- Cleans and transforms
- Saves to `data/processed/`

**Example: `notebooks/02_data_cleaning.ipynb`**

### 3. Run Analysis Notebooks

Create analysis notebooks in `notebooks/`:
- Read from `data/processed/`
- Perform analysis
- Save outputs to `outputs/figures/` and `outputs/reports/`

### 4. Verify the Flow

```
✓ data/raw/donations_raw_2024.csv     (unchanged)
  ↓
✓ data/processed/donations_cleaned.csv (regenerable from raw)
  ↓
✓ outputs/figures/*.png               (regenerable from processed)
✓ outputs/reports/*.md                (regenerable from processed)
```

---

## 📖 Documentation Files

| File | Purpose |
|------|---------|
| **[STRUCTURE.md](./STRUCTURE.md)** | Detailed folder roles and naming conventions |
| **[PROBLEM_STATEMENT.md](./PROBLEM_STATEMENT.md)** | Project goals, success criteria, definitions |
| **[docs/DATA_DICTIONARY.md](./docs/DATA_DICTIONARY.md)** | Description of all data fields |
| **[docs/METHODOLOGY.md](./docs/METHODOLOGY.md)** | Analysis approach and techniques |
| **[docs/ASSUMPTIONS.md](./docs/ASSUMPTIONS.md)** | All explicit assumptions in the analysis |

---

## ✅ Checklist: Before Final Submission

- [ ] Raw data is safe in `data/raw/` (never modified)
- [ ] Processed data saved in `data/processed/` (can regenerate from raw)
- [ ] Outputs saved in `outputs/` (not mixed with data folders)
- [ ] Each folder has a README.md explaining its purpose
- [ ] Data flow is one-directional: raw → processed → outputs
- [ ] All scripts/notebooks read from correct source folder
- [ ] All scripts/notebooks write to correct destination folder
- [ ] Relative paths work from project root: `data/raw/...`
- [ ] Notebooks run top-to-bottom without errors
- [ ] Documentation is complete and current

---

## 🔑 Key Takeaway

**Raw data is evidence. Treat it like evidence.**

- Raw data should never be modified
- Processing steps should be documented and reproducible
- Outputs should be clearly separated from inputs
- This structure ensures trust, reproducibility, and professionalism

---

## 📚 Learn More

- See [STRUCTURE.md](./STRUCTURE.md) for complete organization details
- See [PROBLEM_STATEMENT.md](./PROBLEM_STATEMENT.md) for project objectives
- See `docs/` folder for data dictionary, methodology, and assumptions

---

**Project**: S86-0226-DD Applied Data Science Foundation
**Topic**: Non-Profit Donation Analysis
**Status**: In Progress
**Last Updated**: February 27, 2026