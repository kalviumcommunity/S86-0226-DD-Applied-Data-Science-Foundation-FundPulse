# notebooks/ Folder

## Overview
This folder contains **Jupyter notebooks** for data exploration, analysis, and reporting.

Notebooks are the **primary communication tool**—they combine code, outputs, and explanations.

## Notebook Organization

Use a **numbering system** to establish execution order:

```
01_data_exploration.ipynb      # Initial data understanding
02_data_cleaning.ipynb         # Cleaning and preprocessing
03_analysis.ipynb              # Main analysis work
04_visualization.ipynb         # Charts and visualizations
05_summary_report.ipynb        # Final findings and recommendations
```

## Notebook Best Practices

### Structure
- ✅ Include a title heading at the start
- ✅ Add Markdown cells explaining purpose and intent
- ✅ Use headings to organize sections
- ✅ Separate code cells by task/concept
- ✅ Include output interpretation in Markdown

### Reproducibility
- ✅ Run notebooks top-to-bottom before submission
- ✅ Restart kernel and re-run to verify
- ✅ Use relative paths: `data/raw/...` not `C:/Users/...`
- ✅ Import reusable code from `src/`
- ✅ Document all assumptions clearly

### Code Quality
- ✅ Use descriptive variable names
- ✅ Add comments for complex logic
- ✅ Use functions from `src/` to avoid duplication
- ✅ Include error handling
- ✅ Keep cells focused on single tasks

### Markdown Cells
- ✅ Explain **why** the code runs, not just **what** it does
- ✅ Describe assumptions and limitations
- ✅ Interpret results and findings in context
- ✅ Use lists and formatting for clarity

### Cleanup Before Submission
- ❌ Remove test/experimental cells
- ❌ Clear unnecessary output
- ❌ Fix spelling and grammar in Markdown
- ❌ Delete debug or exploratory code
- ✅ Verify all cells execute without errors

## File Naming Convention

```
{number:02d}_{description}.ipynb
```

Examples:
- `01_data_exploration.ipynb`
- `02_data_cleaning.ipynb`
- `03_donor_analysis.ipynb`

## Typical Workflow

1. **Exploration** (01): Load, inspect, understand raw data
2. **Cleaning** (02): Transform and prepare for analysis
3. **Analysis** (03): Core analytical work and calculations
4. **Visualization** (04): Charts, plots, visual summaries
5. **Reporting** (05): Final findings and recommendations

## Example Notebook Template

```markdown
# Donor Analysis - Data Exploration

## Overview
This notebook loads and explores the raw donation data to understand:
- Data structure and contents
- Data quality and completeness
- Initial patterns and distributions

## Load and Inspect Data
[Code cell: Load data]
[Markdown: Describe what we see]

## Explore Columns
[Code cell: Inspect columns]
[Markdown: Interpret findings]

## Summary
[Markdown: Key observations]
```

## See Also
- [../STRUCTURE.md](../STRUCTURE.md) - Project folder structure
- [../src/README.md](../src/README.md) - How to import and use modules
