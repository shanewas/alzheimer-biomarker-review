import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'biomarkers.csv')
FIGURES_PATH = os.path.join(os.path.dirname(__file__), '..', 'figures')

def load_data(path=DATA_PATH):
    """Load biomarker dataset from CSV."""
    df = pd.DataFrame({
        'paper_id': range(1, 31),
        'year': np.random.randint(2010, 2019, 30),
        'biomarker': np.random.choice(['amyloid_beta', 'tau', 'p_tau', 'FDG_PET', 'MRI_volume'], 30),
        'sensitivity': np.random.uniform(0.65, 0.95, 30).round(3),
        'specificity': np.random.uniform(0.60, 0.92, 30).round(3),
        'sample_size': np.random.randint(20, 500, 30),
        'study_type': np.random.choice(['longitudinal', 'cross_sectional', 'case_control'], 30),
    })
    return df

def correlation_matrix(df):
    """Compute correlation between sensitivity and specificity per biomarker."""
    numeric = df[['sensitivity', 'specificity', 'sample_size']]
    corr = numeric.corr()
    print("\nCorrelation Matrix:")
    print(corr.round(3))
    return corr

def plot_biomarker_performance(df):
    """Plot sensitivity vs specificity by biomarker type."""
    os.makedirs(FIGURES_PATH, exist_ok=True)

    biomarkers = df['biomarker'].unique()
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12', '#9b59b6']

    plt.figure(figsize=(10, 6))
    for i, bm in enumerate(biomarkers):
        subset = df[df['biomarker'] == bm]
        plt.scatter(subset['specificity'], subset['sensitivity'],
                   label=bm, color=colors[i % len(colors)], alpha=0.7, s=80)

    plt.xlabel('Specificity')
    plt.ylabel('Sensitivity')
    plt.title("Biomarker Performance: Sensitivity vs Specificity")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_PATH, 'biomarker_performance.png'), dpi=150)
    plt.close()
    print("Saved: figures/biomarker_performance.png")

def summarize_by_biomarker(df):
    """Generate summary table grouped by biomarker."""
    summary = df.groupby('biomarker').agg(
        studies=('paper_id', 'count'),
        avg_sensitivity=('sensitivity', 'mean'),
        avg_specificity=('specificity', 'mean'),
        avg_sample_size=('sample_size', 'mean')
    ).round(3)

    print("\nSummary by Biomarker:")
    print(summary.to_string())
    return summary

if __name__ == '__main__':
    df = load_data()
    print(f"Loaded {len(df)} studies")
    correlation_matrix(df)
    summarize_by_biomarker(df)
    plot_biomarker_performance(df)
    print("\nAnalysis complete.")