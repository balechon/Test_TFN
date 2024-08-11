import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pathlib import Path
from src.utils.project_paths import RAW_DATA_DIR

def detect_missing_columns(df):
    df_nulos=df.isna().sum().sort_values(ascending=False).reset_index().rename(columns={'index':'columna',0:'cantidad'})
    df_nulos['porcentaje']=(df_nulos['cantidad']/df.shape[0]).mul(100).round(2)
    df_nulos=df_nulos[df_nulos['cantidad']>0]
    return df_nulos


def map_susp_cobranza(x):
    if x == 'SI' or x == '1' or x == 1:
        return 1
    elif x == 'NO' or x == '0' or x == 0:
        return 0
    


def create_train_test_datasets(data_path:Path, target_col:'str',test_size=0.3, random_state=42):
    df = pd.read_csv(data_path)
    namefile = data_path.stem
    X = df.drop(columns=[target_col])
    y = df[target_col]
    X_train, y_test = train_test_split(df, test_size=test_size, stratify=y, random_state=random_state)

    train_path = RAW_DATA_DIR / f'{namefile}_train.csv'
    test_path = RAW_DATA_DIR / f'{namefile}_test.csv'
    X_train.to_csv(train_path, index=False)
    y_test.to_csv(test_path, index=False)
    
