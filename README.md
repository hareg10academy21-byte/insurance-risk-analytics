# Insurance Risk Analytics

## Project Overview
This project analyzes historical insurance claims data for AlphaCare Insurance Solutions (ACIS) to identify low-risk customer segments and support data-driven pricing strategies.

## Objectives
- Perform exploratory data analysis (EDA)
- Analyze claim risk patterns
- Discover profitability trends
- Build reproducible analytics workflows

## Project Structure
- data/
- notebooks/
- src/
- reports/
- tests/

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Git & GitHub
## Data Version Control (DVC)

This project uses DVC (Data Version Control) to manage datasets and ensure reproducibility.

### Steps to Reproduce

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
pip install dvc
```

3. Pull tracked data from DVC storage:

```bash
dvc pull
```

4. Run data cleaning script:

```bash
python scripts/data_cleaning.py
```

### Datasets

* Raw dataset: `data/MachineLearningRating_v3.txt`
* Cleaned dataset: `data/cleaned_insurance_data.csv`

DVC ensures all dataset versions are reproducible and auditable.
