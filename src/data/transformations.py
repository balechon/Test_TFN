import pandas as pd
import numpy as np
from scipy import stats

def analyze_outliers_with_target(df, numeric_columns, target_column, z_threshold=3):
    outlier_summary = []
    
    for col in numeric_columns:
        z_scores = np.abs(stats.zscore(df[col]))
        
        outliers = z_scores > z_threshold
    
        outliers_target_1 = (outliers & (df[target_column] == 1)).sum()
        outliers_target_0 = (outliers & (df[target_column] == 0)).sum()
    
        total_outliers = outliers_target_1 + outliers_target_0
    
        percent_target_1 = (outliers_target_1 / total_outliers) * 100 if total_outliers > 0 else 0
        percent_target_0 = (outliers_target_0 / total_outliers) * 100 if total_outliers > 0 else 0
        outlier_summary.append({
            'Variable': col,
            'Total_Outliers_Target_1': outliers_target_1,
            'Total_Outliers_Target_0': outliers_target_0,
            'Percent_Outliers_Target_1': percent_target_1,
            'Percent_Outliers_Target_0': percent_target_0,
            'Total_Outliers': total_outliers,
            'Percent_Outliers': (total_outliers / len(df)) * 100
        })
    
    summary_df = pd.DataFrame(outlier_summary)
    summary_df = summary_df.sort_values('Total_Outliers', ascending=False)
    
    return summary_df