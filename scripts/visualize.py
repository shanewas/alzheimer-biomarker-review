import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

FIGURES_PATH = os.path.join(os.path.dirname(__file__), '..', 'figures')

def plot_yearly_trend(df):
    """Plot number of studies per year."""
    os.makedirs(FIGURES_PATH, exist_ok=True)

    yearly = df.groupby('year')['paper_id'].count()

    plt.figure(figsize=(10, 5))
    plt.plot(yearly.index, yearly.values, marker='o', color='#3498db', linewidth=2)
    plt.fill_between(yearly.index, yearly.values, alpha=0.2, color='#3498db')
    plt.xlabel('Year')
    plt.ylabel('Number of Studies')
    plt.title('Alzheimer Biomarker Research — Studies per Year')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_PATH, 'yearly_trend.png'), dpi=150)
    plt.close()
    print("Saved: figures/yearly_trend.png")

def plot_study_types(df):
    """Pie chart of study types."""
    counts = df['study_type'].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(counts.values, labels=counts.index,
            autopct='%1.1f%%', startangle=140,
            colors=['#2ecc71', '#3498db', '#e74c3c'])
    plt.title('Distribution of Study Types')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_PATH, 'study_types.png'), dpi=150)
    plt.close()
    print("Saved: figures/study_types.png")

def plot_sample_size_distribution(df):
    """Histogram of sample sizes across studies."""
    plt.figure(figsize=(9, 5))
    plt.hist(df['sample_size'], bins=12, color='#9b59b6', alpha=0.8, edgecolor='white')
    plt.xlabel('Sample Size')
    plt.ylabel('Frequency')
    plt.title('Sample Size Distribution Across Reviewed Studies')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_PATH, 'sample_size_dist.png'), dpi=150)
    plt.close()
    print("Saved: figures/sample_size_dist.png")

if __name__ == '__main__':
    from biomarker_analysis import load_data
    df = load_data()
    plot_yearly_trend(df)
    plot_study_types(df)
    plot_sample_size_distribution(df)
    print("All figures generated.")