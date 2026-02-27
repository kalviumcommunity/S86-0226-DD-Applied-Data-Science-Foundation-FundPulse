# Analysis Methodology - FundPulse

This document describes the approach, techniques, and reasoning behind the FundPulse analysis.

---

## Overview

The FundPulse analysis follows a structured pipeline to transform raw donation data into actionable insights about donor behavior.

The analysis is divided into four phases:
1. **Data Preparation** - Loading and cleaning
2. **Exploratory Analysis** - Understanding patterns
3. **Repeat Donor Analysis** - Identifying engaged donors
4. **Trend Analysis** - Discovering seasonal/campaign patterns

---

## Phase 1: Data Preparation

### Objective
Transform raw data into a clean, analysis-ready dataset.

### Steps

#### 1.1 Data Loading
- Load donation records from `data/raw/`
- Verify file format and completeness
- Check for obvious data corruption

```python
import pandas as pd
df = pd.read_csv('data/raw/donations.csv')
```

#### 1.2 Data Validation
- Check data types (dates are actually dates, amounts are numeric)
- Identify missing values and their extent
- Detect outliers that may indicate errors

```python
# Check for nulls
print(df.isnull().sum())

# Validate amount ranges
print(df['donation_amount'].describe())
```

#### 1.3 Date Standardization
- Ensure all dates follow YYYY-MM-DD format
- Parse date strings to datetime objects
- Handle date edge cases (leap years, month boundaries)

```python
df['donation_date'] = pd.to_datetime(df['donation_date'], format='%Y-%m-%d')
```

#### 1.4 Deduplication
- Identify duplicate donation records
- Remove exact duplicates (same donor, amount, date)
- Document duplicate count and removal strategy

```python
# Check for duplicates
duplicates = df.duplicated(subset=['donor_id', 'donation_date', 'donation_amount'])
print(f"Found {duplicates.sum()} duplicate records")
df = df.drop_duplicates()
```

#### 1.5 Currency Validation
- Ensure all amounts are positive (or document negative donations)
- Check for unreasonable outliers (e.g., impossible large donations)
- Document amount statistics

```python
# Check amount distribution
print(df['donation_amount'].describe())

# Flag outliers (e.g., > 99th percentile)
outliers = df[df['donation_amount'] > df['donation_amount'].quantile(0.99)]
```

### Output
- `data/processed/donations_cleaned.csv` - Clean, deduplicated data ready for analysis

---

## Phase 2: Exploratory Analysis

### Objective
Understand the overall shape, distribution, and basic patterns in the data.

### Key Questions
- How many donations and donors are in the dataset?
- What is the distribution of donation amounts?
- What is the time span of the data?
- Are there obvious patterns or clusters?

### Techniques

#### 2.1 Descriptive Statistics
Calculate basic statistics on key fields:
- Count of donations and unique donors
- Mean, median, standard deviation of amounts
- Min/max donation amounts
- Date range

```python
print(f"Total donations: {len(df)}")
print(f"Unique donors: {df['donor_id'].nunique()}")
print(f"Average donation: ${df['donation_amount'].mean():.2f}")
print(f"Date range: {df['donation_date'].min()} to {df['donation_date'].max()}")
```

#### 2.2 Distribution Analysis
- Visualize distribution of donation amounts (histogram, box plot)
- Identify if distribution is normal, skewed, or multimodal
- Check for heavy-tailed distribution (few large donors)

#### 2.3 Temporal Patterns
- Count donations by month and year
- Visualize donation frequency over time
- Identify if there are obvious seasonal patterns

```python
donations_by_month = df.groupby(df['donation_date'].dt.to_period('M')).size()
donations_by_month.plot()
```

### Output
- Initial observations and patterns documented in notebook

---

## Phase 3: Repeat Donor Analysis

### Objective
Identify donors who give multiple times and understand their engagement patterns.

### Definition
**Repeat Donor**: A donor who has made 2 or more donations in the dataset time period.

### Steps

#### 3.1 Identify Repeat Donors
Count donations per donor and classify:

```python
donation_counts = df.groupby('donor_id').size()
repeat_donors = donation_counts[donation_counts >= 2]
single_donors = donation_counts[donation_counts == 1]

repeat_count = len(repeat_donors)
total_count = donation_counts.nunique()
repeat_rate = repeat_count / total_count * 100
```

#### 3.2 Repeat Donor Characteristics
Analyze patterns among repeat donors:
- What percentage are repeat donors? (repeat_rate)
- How many donations do repeat donors make on average?
- What is the average time between donations?

```python
# Average donations per repeat donor
avg_repeat_donations = repeat_donors.mean()

# Time between donations
df_sorted = df.sort_values(['donor_id', 'donation_date'])
df_sorted['days_since_last'] = df_sorted.groupby('donor_id')['donation_date'].diff()
avg_days_between = df_sorted['days_since_last'].mean()
```

#### 3.3 Comparison: Repeat vs Single Donors
Compare average donation amounts:

```python
repeat_donor_ids = repeat_donors.index
repeat_avg_amount = df[df['donor_id'].isin(repeat_donor_ids)]['donation_amount'].mean()
single_avg_amount = df[~df['donor_id'].isin(repeat_donor_ids)]['donation_amount'].mean()
```

### Output
- `outputs/reports/repeat_donor_analysis.md` - Summary findings
- `outputs/figures/repeat_donor_distribution.png` - Visualizations

---

## Phase 4: Trend Analysis

### Objective
Identify temporal patterns in donations that reveal high-effectiveness fundraising periods.

### Steps

#### 4.1 Period-Based Aggregation
Group donations by period (month, quarter, campaign):

```python
# By month
donations_by_month = df.groupby(df['donation_date'].dt.to_period('M')).agg({
    'donation_id': 'count',
    'donation_amount': 'sum'
})

# By quarter
donations_by_quarter = df.groupby(df['donation_date'].dt.to_period('Q')).agg({
    'donation_id': 'count',
    'donation_amount': 'sum'
})
```

#### 4.2 Trend Identification
Detect high-effectiveness periods:
- Periods with donation count above average
- Periods with total amount above average
- Months/quarters consistently high performing

```python
# Calculate average and determine high-performing periods
avg_monthly = donations_by_month['donation_amount'].mean()
high_performers = donations_by_month[donations_by_month['donation_amount'] > avg_monthly]
```

#### 4.3 Seasonal Pattern Detection
Check for consistent seasonal patterns:
- Same months in different years performing similarly
- Campaigns or events driving peaks
- Holiday or year-end bias

```python
# Extract month from period and aggregate
df['month'] = df['donation_date'].dt.month
seasonal = df.groupby('month')['donation_amount'].agg(['sum', 'count', 'mean'])
```

#### 4.4 Visualization
Create trend visualizations:
- Line plot: donations over time
- Bar plot: donations by month
- Multiple-year comparison

### Output
- `outputs/figures/donation_trend.png` - Time series visualization
- `outputs/figures/seasonal_pattern.png` - Seasonal pattern chart
- `outputs/reports/trend_analysis.md` - Findings summary

---

## Statistical Techniques Used

### Aggregation
- `groupby()` to group donations by donor, month, campaign
- `sum()`, `mean()`, `count()` for summary statistics

### Time-Based Analysis
- `datetime` objects for date manipulation
- Period-based grouping (month, quarter, year)
- Time differences to calculate inter-donation intervals

### Visualization
- Matplotlib/Seaborn for static plots
- Histograms for distributions
- Line plots for trends
- Bar charts for comparisons

---

## Limitations and Caveats

1. **Data Completeness**: Analysis assumes data is complete; missing or late-reported donations affect results
2. **Time Period**: Trends identified only reflect time period in dataset; older patterns may differ
3. **External Factors**: Doesn't account for economic conditions, news events affecting giving
4. **Causation**: Identifies patterns, not causes (e.g., why January has more donations)
5. **Donor Context**: Anonymous donor data; unlikely for individual-level insights

---

## Reproducibility

To reproduce this analysis:
1. Place raw data in `data/raw/`
2. Run notebooks in order: `01_exploration` → `02_cleaning` → `03_analysis`
3. All outputs regenerated in `outputs/`
4. Results should match previous run (within floating-point precision)

---

## See Also
- [ASSUMPTIONS.md](./ASSUMPTIONS.md) - Key assumptions underlying analysis
- [DATA_DICTIONARY.md](./DATA_DICTIONARY.md) - Field definitions
- [../PROBLEM_STATEMENT.md](../PROBLEM_STATEMENT.md) - Project goals
