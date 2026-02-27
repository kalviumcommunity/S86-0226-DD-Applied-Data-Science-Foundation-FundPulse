# outputs/ Folder

## Overview
This folder contains all **generated results** from analysis and modeling:
- Visualizations (charts, plots, graphs)
- Reports and summaries
- Trained models (if applicable)
- Summary statistics and tables

Files here are **regenerable** from code in `notebooks/` and `src/` and can be safely deleted.

## Subfolders

### `figures/`
Store visualizations and charts:
- `.png`, `.pdf`, `.svg` image files
- Matplotlib, Seaborn, Plotly outputs
- Dashboard screenshots
- Example: `donation_frequency_histogram.png`, `trend_by_month.pdf`

### `reports/`
Store written reports and summaries:
- Markdown summary files
- HTML reports
- Excel files with statistics
- Example: `donor_analysis_summary.md`, `fundraising_effectiveness.xlsx`

### `models/`
Store trained models (if applicable):
- Pickle files, joblib dumps
- Model parameters and metadata
- Model performance metrics
- Example: `donor_clustering_model.pkl`

## File Naming Convention

Use descriptive names with underscores:

```
{description}_{version}.{extension}
```

Examples:
- `donation_trend_by_month.png`
- `repeat_donor_analysis_v1.pdf`
- `fundraising_effectiveness_report.md`
- `donor_clustering_model_v2.pkl`

## How to Generate Outputs

Save outputs from notebooks using Python:

```python
import matplotlib.pyplot as plt
import os

# Create figures subdirectory if needed
os.makedirs('outputs/figures', exist_ok=True)

# Generate and save plot
plt.figure(figsize=(10, 6))
plt.hist(donations['amount'], bins=30)
plt.title('Donation Amount Distribution')
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.savefig('outputs/figures/donation_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

print("Plot saved to outputs/figures/donation_distribution.png")
```

## Best Practices

✅ **DO**:
- Name files descriptively
- Include dates if versions evolve: `report_2024_01.md`
- Save high-resolution images (dpi=300)
- Document what each output represents
- Organize by subfolder (figures, reports, models)

❌ **DON'T**:
- Save outputs to root or data/ folders
- Use vague names like `output1.png`, `result.xlsx`
- Commit large binary files to version control
- Store ungenerated (downloaded) files here
- Leave temporary or test files here

## Regeneration
If you modify analysis code:
1. Re-run notebooks (cells will regenerate outputs)
2. Outputs folder files are overwritten
3. Old versions are lost (use git to track versions)

## See Also
- [../STRUCTURE.md](../STRUCTURE.md) - Project structure overview
- [../notebooks/README.md](../notebooks/README.md) - Where outputs are generated
