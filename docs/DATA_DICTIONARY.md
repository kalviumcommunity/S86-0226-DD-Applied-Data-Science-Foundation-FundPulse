# Data Dictionary - FundPulse

This document describes all data fields and their meanings in the FundPulse project.

---

## donations.csv (to be updated with actual data)

### Metadata
- **File Location**: `data/raw/donations.csv`
- **Format**: CSV (Comma-Separated Values)
- **Records**: [Number of donation records]
- **Date Range**: [YYYY-MM-DD] to [YYYY-MM-DD]
- **Updated**: [YYYY-MM-DD]

### Column Descriptions

| Column Name | Data Type | Description | Example | Null Handling | Notes |
|-------------|-----------|-------------|---------|----------------|-------|
| donor_id | Integer | Unique identifier for each donor | 1001, 2045, 3892 | None expected | Primary key for joining with donor info |
| donation_id | Integer | Unique identifier for each donation | 50001, 50002 | None expected | Primary key, auto-generated |
| donation_date | Date | Date donation was received | 2024-01-15 | None expected | Format: YYYY-MM-DD |
| donation_amount | Float | Amount donated in USD | 50.00, 100.50, 1000.00 | Empty represents $0 | Always positive; in US dollars |
| donation_frequency | Integer | Number of donations by this donor to date | 1, 2, 5, 12 | None expected | Cumulative count including current donation |
| campaign_name | String | Name of fundraising campaign (if applicable) | "New Year Drive", "Gala 2024" | Common | May be null for general donations |
| donation_source | String | Channel through which donation was received | "Online", "Mail", "Phone", "In-person" | Rare | Indicates donation method |
| donor_name | String | Full name of donor | "Jane Smith", "John Doe" | Rare | Used for personalization; optional PII |
| donor_email | String | Email address of donor | "jane@example.com" | Common | Used for communication; optional PII |
| donor_type | String | Classification of donor | "Individual", "Organization", "Foundation" | Rare | Indicates donor category |
| first_donation_date | Date | Date this donor first gave | 2022-06-10 | None expected | Used to calculate donor tenure |
| is_repeat_donor | Boolean | Whether donor has given more than once | TRUE, FALSE | None expected | TRUE if donation_frequency >= 2 |

---

## donors.csv (if separate from donations)

*Note: If donor information is in a separate file, document it here*

| Column Name | Data Type | Description | Example |
|-------------|-----------|-------------|---------|
| donor_id | Integer | Unique donor identifier | 1001 |
| donor_name | String | Full name | Jane Smith |
| donor_email | String | Email address | jane@example.com |
| donor_type | String | Individual/Organization/Foundation | Individual |
| registration_date | Date | Date donor registered | 2022-06-10 |
| location | String | Geographic location | New York, NY |
| total_donations | Integer | Lifetime number of donations | 5 |
| total_amount | Float | Lifetime donation amount ($) | 500.00 |

---

## Special Values and Conventions

### Missing Values
- **Null/Empty Representation**: Empty cells in CSV represent missing values
- **How Handled**: Specified in "Null Handling" column above
- **Date Missing**: Represented as empty string (not "NULL" or "N/A")
- **Amount Missing**: Represented as empty and interpreted as $0

### Date Format
- **Standard Format**: YYYY-MM-DD (ISO 8601)
- **Example**: 2024-01-15 (January 15, 2024)
- **Invalid Format**: 01/15/2024 (this is not the standard)

### Currency
- **Currency**: USD ($)
- **Decimal Places**: 2 (e.g., $50.00, not $50)
- **Negative Values**: Should not exist; if present, contact data source
- **Zero Values**: Represents $0 donations (unusual but possible test data)

### Boolean Values
- **TRUE Values**: "TRUE", "True", "true", "1", "Y", "Yes"
- **FALSE Values**: "FALSE", "False", "false", "0", "N", "No"

---

## Data Quality Notes

### Known Issues
- [Document any known quality issues here]
- Example: "Some early 2022 donations missing campaign names"
- Example: "Duplicate donor IDs may exist; use email for deduplication"

### Validation Rules
- Donation amounts must be >= 0
- Donation dates must be before or equal to today
- Donor IDs must be positive integers
- Email format should be valid (if populated)

---

## Related Documentation
- [METHODOLOGY.md](./METHODOLOGY.md) - How data is processed and analyzed
- [ASSUMPTIONS.md](./ASSUMPTIONS.md) - Assumptions about data content and quality
- [../data/raw/README.md](../data/raw/README.md) - Raw data file information
- [../data/processed/README.md](../data/processed/README.md) - Processed data transformations

---

## Questions About Data?
If you have questions about what a field means or how it's used:
1. Check this Data Dictionary first
2. Review processing scripts in `src/`
3. Look at example notebooks in `notebooks/`
4. Contact the data owner
