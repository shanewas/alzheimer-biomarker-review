import pandas as pd
import numpy as np
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')

def generate_summary_tables(df):
    """Generate summary tables from reviewed papers."""
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # Table 1: Performance by biomarker
    table1 = df.groupby('biomarker').agg(
        num_studies=('paper_id', 'count'),
        mean_sensitivity=('sensitivity', 'mean'),
        std_sensitivity=('sensitivity', 'std'),
        mean_specificity=('specificity', 'mean'),
        std_specificity=('specificity', 'std'),
        total_subjects=('sample_size', 'sum')
    ).round(3)

    table1.to_csv(os.path.join(OUTPUT_PATH, 'table1_biomarker_performance.csv'))
    print("Table 1 — Biomarker Performance:")
    print(table1.to_string())

    # Table 2: Performance by study type
    table2 = df.groupby('study_type').agg(
        num_studies=('paper_id', 'count'),
        mean_sensitivity=('sensitivity', 'mean'),
        mean_specificity=('specificity', 'mean'),
        mean_sample_size=('sample_size', 'mean')
    ).round(3)

    table2.to_csv(os.path.join(OUTPUT_PATH, 'table2_study_type_performance.csv'))
    print("\nTable 2 — Performance by Study Type:")
    print(table2.to_string())

    # Table 3: Top performing studies
    table3 = df.nlargest(10, 'sensitivity')[
        ['paper_id', 'year', 'biomarker', 'sensitivity',
         'specificity', 'sample_size', 'study_type']
    ]
    table3.to_csv(os.path.join(OUTPUT_PATH, 'table3_top_studies.csv'), index=False)
    print("\nTable 3 — Top 10 Studies by Sensitivity:")
    print(table3.to_string(index=False))

    print("\nAll tables saved to data/")

if __name__ == '__main__':
    from biomarker_analysis import load_data
    df = load_data()
    generate_summary_tables(df)