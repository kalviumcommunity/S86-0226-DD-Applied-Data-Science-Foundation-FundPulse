# Project Assumptions - FundPulse

This document lists all explicit and implicit assumptions made in the FundPulse analysis.

Making assumptions explicit is critical for reproducibility and for reviewers to understand what we held to be true.

---

## Data Assumptions

### ✓ Donor Data
- [ ] Donor IDs are **unique** and consistent throughout the dataset
  - *Why*: We use donor_id as the primary key for grouping donations
  - *Impact*: If an individual has multiple IDs, they appear as separate donors
  - *Mitigation*: Email or name matching would help identify duplicates

- [ ] A donor is represented by a **single row** (if in separate donor table)
  - *Why*: We assume one identity per donor_id
  - *Impact*: Contradictory information about same donor could occur
  - *Mitigation*: Data validation checks on load

- [ ] Donor information does **not change** during the time period
  - *Why*: We don't track donor name/email history
  - *Impact*: Changes in donor contact info are not captured
  - *Mitigation*: Use most recent contact info found

### ✓ Donation Records
- [ ] Each row represents **one distinct donation transaction**
  - *Why*: We count and sum rows to calculate donation frequency/totals
  - *Impact*: Duplicate rows would overcount donations
  - *Mitigation*: Deduplication step in data cleaning

- [ ] Donation amounts are **always positive** (or zero)
  - *Why*: We don't expect refunds or corrections in this dataset
  - *Impact*: Negative amounts could indicate refunds (not analyzed)
  - *Mitigation*: Validation check flags negative amounts

- [ ] Donation amounts are in **USD currency** only
  - *Why*: Currency is not specified in data
  - *Impact*: Foreign donations (if present) could skew analysis
  - *Mitigation*: Code comments document currency assumption

- [ ] Donation **dates are accurate** and in chronological order
  - *Why*: We use dates for time-based analysis
  - *Impact*: Misdated donations could appear in wrong period
  - *Mitigation*: Flag dates outside reasonable range

- [ ] All donations in the dataset have been **reported by the effective date**
  - *Why*: Late-reported donations could miss their correct period
  - *Impact*: Recent months may undercount if donations reported with delay
  - *Mitigation*: Analysis uses data as-provided (assumes ready for analysis)

### ✓ Data Completeness
- [ ] The dataset includes **all donations** in the time period
  - *Why*: Analysis assumes no missing donations
  - *Impact*: If donations are systematically missing, patterns are incomplete
  - *Mitigation*: Cross-check with external donation tracking if possible

- [ ] Missing values are **randomly distributed**, not systematic
  - *Why*: Some fields (like campaign_name) may be nullable
  - *Impact*: If campaigns are selectively recorded, trends are biased
  - *Mitigation*: Analyze missing data patterns before proceeding

- [ ] The dataset is **not heavily anonymized** (has usable donor IDs)
  - *Why*: We need to track individual donors
  - *Impact*: Completely anonymized data prevents repeat donor analysis
  - *Mitigation*: Data provided with unique donor identifiers

---

## Analytical Assumptions

### ✓ Repeat Donor Definition
- [ ] **"Repeat Donor"** is defined as any donor with **2 or more donations**
  - *Why*: Simple binary threshold; industry-common definition
  - *Impact*: Donors with 1 donation excluded from repeat analysis
  - *Mitigation*: Alternative threshold (3+ donations) analyzed separately if needed
  - *Review*: This threshold can be adjusted in `configs/constants.py`

- [ ] Repeat status is **cumulative** within the dataset time period
  - *Why*: We count all donations, past and present
  - *Impact*: A donor's repeat status only reflects this dataset (not historical)
  - *Mitigation*: Time period clearly noted in analysis

### ✓ Donation Frequency
- [ ] Frequency measured at **donor level** (not organization level)
  - *Why*: Each donor's giving pattern tracked independently
  - *Impact*: Organization donations treated same as individual donations
  - *Mitigation*: Donor type stratified in analysis if differences important

- [ ] Frequency measured over **entire dataset time period**
  - *Why*: We don't normalize by time (e.g., donations per year)
  - *Impact*: Older time periods don't affect analysis results
  - *Mitigation*: If needed, can recalculate frequency per year

- [ ] **Time between donations** treated as linear, with no acceleration/deceleration expected
  - *Why*: Simplifies analysis; we don't fit curves or trends within series
  - *Impact*: We measure average gap; patterns within gaps not analyzed
  - *Mitigation*: Could do deeper temporal analysis if patterns important

### ✓ Trend Analysis
- [ ] **Seasonal patterns** are based on **calendar periods** (months/quarters)
  - *Why*: Aligns with typical fundraising calendar
  - *Impact*: Business cycles (fiscal year, etc.) not captured
  - *Mitigation*: Can recalculate on fiscal calendar if needed

- [ ] **High-effectiveness periods** identified by **above-average donation counts**
  - *Why*: Simple threshold relative to baseline
  - *Impact*: "Normal" months not distinguished; comparison is relative
  - *Mitigation*: Statistical testing (e.g., z-scores) could strengthen conclusions

- [ ] **Campaign attribution** is accurate (if campaign field present)
  - *Why*: Assume donations logged with correct campaign
  - *Impact*: Misattributed donations skew campaign effectiveness
  - *Mitigation*: Validate campaign names against known campaigns

- [ ] **No external events** significantly affect donations beyond campaigns
  - *Why*: Analysis assumes campaigns are primary driver
  - *Impact*: Economy, news, regulations affecting giving are not captured
  - *Mitigation*: Qualitative review of high-effectiveness periods

---

## Business Context Assumptions

### ✓ Organization Context
- [ ] This is a **non-profit organization** (implicitly)
  - *Why*: Problem statement specifies non-profits
  - *Impact*: For-profit fundraising patterns may differ
  - *Mitigation*: Analysis designed for non-profit context

- [ ] **Donation data is current** and reflects recent giving patterns
  - *Why*: Trends identified are used for strategy going forward
  - *Impact*: Outdated data may not reflect current donor behavior
  - *Mitigation*: Analysis should be re-run periodically

### ✓ Stakeholder Assumptions
- [ ] **Results will be used for fundraising strategy**
  - *Why*: Problem statement indicates actionable insights expected
  - *Impact*: Analysis focused on patterns relevant to fundraising
  - *Mitigation*: Verify findings practical before implementation

- [ ] **Donors want to be identified and contacted** (not privacy concern)
  - *Why*: Actionable insights often require donor identification
  - *Impact*: Analysis respects GDPR/privacy if applicable
  - *Mitigation*: Ensure anonymization before sharing outside organization

---

## Technical Assumptions

### ✓ Environment
- [ ] **Python 3.8+** available with standard data libraries (pandas, numpy)
  - *Why*: Code written in Python
  - *Impact*: Different versions may have compatibility issues
  - *Mitigation*: `requirements.txt` documents package versions

- [ ] **Jupyter Notebooks** can be executed in VS Code or JupyterLab
  - *Why*: Notebooks used for analysis
  - *Impact*: Analysis requires notebook environment
  - *Mitigation*: Equivalent Python scripts available if needed

### ✓ File Paths
- [ ] **Relative paths** are correct from project root
  - *Why*: Code uses paths like `data/raw/donations.csv`
  - *Impact*: Code fails if run from different directory
  - *Mitigation*: Always run scripts from project root

- [ ] **File paths use forward slashes** (work on Windows, Mac, Linux)
  - *Why*: Cross-platform compatibility
  - *Impact*: Windows backslashes could cause issues
  - *Mitigation*: `pathlib.Path()` used for OS-independent paths

---

## Known Limitations

These are explicitly acknowledged constraints (not assumptions we made, but issues we're aware of):

1. **No individual-level insights** - Data aggregated; patterns don't identify *why* donors give
2. **No predictive models** - Analysis is descriptive, not predictive
3. **No cost analysis** - Doesn't account for fundraising costs for campaigns
4. **Limited by time period** - Patterns only valid for data's time range
5. **No A/B testing** - Can't determine causation; only correlation observed

---

## Validation Checklist

Before finalizing analysis, verify these assumptions:

- [ ] Donor IDs are unique (check for duplicates)
- [ ] No duplicate donation records exist
- [ ] Donation amounts are positive (or investigate negatives)
- [ ] Dates are in valid range and not future-dated
- [ ] Campaign names are consistent (no typos or variants)
- [ ] Missing data documented and handled appropriately
- [ ] Repeat donor threshold of 2 documented in code
- [ ] All relative file paths work from project root
- [ ] Analysis produces same results on re-run

---

## Assumption Evolution

As analysis progresses or data changes, update this document:

| Date | Assumption | Change | Reason |
|------|-----------|--------|--------|
| 2024-01-15 | Repeat donor = 2+ donations | Original | Initial definition |
| [Update date] | [If changed] | [New definition] | [Why changed] |

---

## See Also
- [METHODOLOGY.md](./METHODOLOGY.md) - How assumptions are used in analysis
- [DATA_DICTIONARY.md](./DATA_DICTIONARY.md) - Data field definitions and validation
- [../PROBLEM_STATEMENT.md](../PROBLEM_STATEMENT.md) - Project context and goals
