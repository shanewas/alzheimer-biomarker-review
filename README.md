# alzheimer-biomarker-review

Literature review dataset and analysis scripts for Alzheimer's disease biomarker research (2018–2019).

Conducted alongside the OCT deep learning research published in IEEE (2019).

## Overview

A systematic review of published studies on Alzheimer's disease biomarkers —
covering amyloid-beta, tau proteins, FDG-PET imaging, and MRI volumetrics.
Scripts aggregate performance metrics (sensitivity, specificity) across reviewed
papers and visualize trends.

## Methodology

- Reviewed 30+ published studies (2010–2019)
- Extracted key metrics: sensitivity, specificity, sample size, study type
- Compared biomarker performance across longitudinal, cross-sectional, and case-control designs
- Generated summary tables and visualizations

## Key Findings

- Amyloid-beta and tau biomarkers consistently showed highest sensitivity
- Longitudinal studies reported more reliable specificity estimates
- Sample sizes varied widely (20–500 subjects) across reviewed literature

## Scripts

| Script | Description |
|---|---|
| `scripts/biomarker_analysis.py` | Load data, correlation matrix, performance summary |
| `scripts/visualize.py` | Generate figures — trends, distributions, study types |
| `scripts/summary_tables.py` | Export summary tables to CSV |

## Figures

- `figures/biomarker_performance.png` — Sensitivity vs specificity scatter by biomarker
- `figures/yearly_trend.png` — Studies published per year
- `figures/study_types.png` — Distribution of study designs
- `figures/sample_size_dist.png` — Sample size histogram

## Setup
```bash
git clone https://github.com/shanewas/alzheimer-biomarker-review.git
cd alzheimer-biomarker-review
pip install -r requirements.txt
python scripts/biomarker_analysis.py
```

## Related

- IEEE Paper: [Alzheimer's Disease Prediction Using CNNs on OCT Images](https://ieeexplore.ieee.org/document/9306649)
- Related repo: [Optical-Coherence-Tomographic-Analysis](https://github.com/shanewas/Optical-Coherence-Tomographic-Analysis)