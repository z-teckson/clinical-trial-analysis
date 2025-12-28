#!/usr/bin/env python3
"""
Analysis script for Aversionex clinical trial.
Calculates mean number of drinks per day before and after treatment.
"""

import pandas as pd
import numpy as np

def load_data(data_path='data/trial_data.csv'):
    """Load trial data from CSV."""
    # This is a placeholder; actual implementation would read CSV
    # For demonstration, we'll create dummy data
    np.random.seed(42)
    n_patients = 100
    data = pd.DataFrame({
        'patient_id': range(n_patients),
        'gender': np.random.choice(['M', 'F'], n_patients),
        'drinks_before': np.random.randint(0, 20, n_patients),
        'drinks_after': np.random.randint(0, 15, n_patients),
        'heavy_days_before': np.random.randint(0, 30, n_patients),
        'heavy_days_after': np.random.randint(0, 30, n_patients),
        'craving_score': np.random.randn(n_patients) * 10 + 50
    })
    return data

def calculate_mean_drinks(data):
    """Calculate mean drinks before and after treatment."""
    mean_before = data['drinks_before'].mean()
    mean_after = data['drinks_after'].mean()
    return mean_before, mean_after

def calculate_heavy_drinking_episodes(data):
    """
    Calculate percentage of patients with at least one heavy drinking episode
    in the 30 days before and after treatment.
    
    Heavy drinking episode defined as:
      - >=5 drinks for men on a single day
      - >=4 drinks for women on a single day
    
    The dummy dataset provides counts of heavy drinking days per patient.
    A patient is considered to have experienced a heavy drinking episode
    if heavy_days > 0.
    """
    # Patients with at least one heavy day before treatment
    heavy_before = (data['heavy_days_before'] > 0).sum()
    percent_before = (heavy_before / len(data)) * 100
    
    # Patients with at least one heavy day after treatment
    heavy_after = (data['heavy_days_after'] > 0).sum()
    percent_after = (heavy_after / len(data)) * 100
    
    return percent_before, percent_after, heavy_before, heavy_after

def main():
    """Main analysis routine."""
    print("Loading trial data...")
    data = load_data()
    print(f"Total patients: {len(data)}")
    
    mean_before, mean_after = calculate_mean_drinks(data)
    print(f"Mean drinks per day before treatment: {mean_before:.2f}")
    print(f"Mean drinks per day after treatment: {mean_after:.2f}")
    
    # Heavy drinking episode analysis
    print("\n--- Heavy Drinking Episode Analysis ---")
    percent_before, percent_after, heavy_before, heavy_after = calculate_heavy_drinking_episodes(data)
    print(f"Patients with ≥1 heavy drinking episode before treatment: {heavy_before} ({percent_before:.1f}%)")
    print(f"Patients with ≥1 heavy drinking episode after treatment: {heavy_after} ({percent_after:.1f}%)")
    change = percent_after - percent_before
    print(f"Change in percentage: {change:+.1f} percentage points")
    
    # Clinical interpretation
    if percent_after < percent_before:
        print("Reduction in heavy drinking episodes suggests a positive treatment effect.")
    else:
        print("No reduction observed; further investigation needed.")

if __name__ == '__main__':
    main()