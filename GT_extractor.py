import numpy as np 
import pandas as pd 
from pathlib import Path 
import ast 
import pywt

def get_gt():
    root = 'C:/Users/Haiya/Downloads/OneDrive_2025-09-19/'
    csv = 'PELICAN Sorted Patients(Sheet1).csv'
    csv_path = Path(root + csv)
    df = pd.read_csv(csv_path)
    patient_ids = (
    pd.to_numeric(df['Record ID'].astype(str).str.extract(r'(\d+)')[0], errors='coerce')
      .dropna()
      .astype(int)
      .tolist()
)
    return patient_ids
