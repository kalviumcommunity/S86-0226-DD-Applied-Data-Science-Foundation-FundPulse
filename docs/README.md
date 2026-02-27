# docs/ Folder

## Overview
This folder contains all **project documentation**—the narrative and technical details that explain the analysis.

Well-documented projects are easier to understand, maintain, and share with teammates and stakeholders.

## Documentation Files

### `README.md` (This file)
Index of all documentation in this folder

### `DATA_DICTIONARY.md`
Comprehensive description of all data fields:
- Column names and data types
- Description of what each field represents
- Valid value ranges
- Missing value conventions
- Example values

Use this when team members need to understand the data structure.

### `METHODOLOGY.md`
Explanation of analysis approach:
- Why specific methods were chosen
- Steps in the analysis pipeline
- Statistical techniques used
- Assumptions underlying analysis
- Limitations and caveats

Use this when someone reviews your work and needs to understand your reasoning.

### `ASSUMPTIONS.md`
List of all assumptions made:
- Data quality assumptions
- Temporal assumptions (date ranges, continuity)
- Analytical assumptions (distributions, relationships)
- Business assumptions (what "repeat donor" means, etc.)

Use this to make implicit assumptions explicit and testable.

## Content Guidelines

### DATA_DICTIONARY.md Template
```markdown
# Data Dictionary

## donors.csv

| Column | Type | Description | Example | Missing? |
|--------|------|-------------|---------|----------|
| donor_id | Integer | Unique donor identifier | 1001 | None |
| name | String | Donor full name | Jane Smith | Rare |
| email | String | Contact email | jane@example.com | Common |
| amount | Float | Donation amount ($) | 50.00 | None |
| date | Date | Donation date | 2024-01-15 | None |

```

### METHODOLOGY.md Template
```markdown
# Analysis Methodology

## Overview
Our approach to analyze donor behavior consists of four phases:

## Phase 1: Data Preparation
- Load raw donation records
- Validate data quality
- Remove duplicates
- Standardize dates and currency

## Phase 2: Exploratory Analysis
- Basic statistics on donations
- Distribution of donation amounts
- Frequency of donors

## Phase 3: Repeat Donor Analysis
- Identify donors with multiple donations
- Calculate repeat rate
- Analyze time between donations

## Phase 4: Trend Analysis
- Identify seasonal patterns
- Calculate by-period statistics
- Determine high-effectiveness periods

## Assumptions
- Donor IDs are unique and consistent
- Dates are in YYYY-MM-DD format
- All amounts are in USD
```

### ASSUMPTIONS.md Template
```markdown
# Project Assumptions

## Data Assumptions
- [ ] Donor identifiers are unique within dataset
- [ ] Donation amounts are positive numbers
- [ ] Dates are valid and in chronological order
- [ ] No future-dated donations in dataset

## Analytical Assumptions
- [ ] "Repeat donor" = 2 or more donations
- [ ] Donation frequency measured in calendar months
- [ ] Seasonal patterns analyzed on monthly basis
- [ ] No multi-year campaigns affecting patterns

## Business Assumptions
- [ ] Marketing campaigns roughly aligned with calendar months
- [ ] Donation source data captures all transactions
- [ ] Donor IDs remain consistent over time
```

## Best Practices

✅ **DO**:
- Keep documentation updated with code changes
- Use clear, simple language
- Include examples and tables
- Document assumptions explicitly
- Reference notebooks/code that implements findings

❌ **DON'T**:
- Leave documentation out of sync with code
- Write in overly technical jargon
- Assume readers know project context
- Make assumptions implicit (document them!)
- Leave TODOs or incomplete sections

## How to Maintain Documentation

### After Data Changes
- Update DATA_DICTIONARY.md if fields change
- Update ASSUMPTIONS.md if assumptions shift

### After Adding Analysis
- Update METHODOLOGY.md with new steps
- Document new calculations or logic

### Before Final Submission
- Verify all documentation is complete
- Check grammar and clarity
- Ensure examples match actual data
- Reference notebooks for complex steps

## See Also
- [../STRUCTURE.md](../STRUCTURE.md) - Project structure overview
- [../PROBLEM_STATEMENT.md](../PROBLEM_STATEMENT.md) - Project goals and objectives
- [../notebooks/README.md](../notebooks/README.md) - Notebook standards
