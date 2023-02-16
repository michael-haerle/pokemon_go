# Standard imports
import pandas as pd
# Vis imports
import matplotlib.pyplot as plt
import seaborn as sns
# Stats imports
from scipy.stats import spearmanr

def wrangle_df():
    df = pd.read_csv('comprehensive_dps_updated.csv')
    df.rename(columns = {'ER' : 'Battle_Stat'}, inplace = True)
    df1 = pd.read_csv('Pokemon.csv')
    df1.rename(columns = {'Name' : 'Pokemon'}, inplace = True)
    df_best_attack_set = pd.read_csv('Best_Attack_Set_Updated.csv')
    df_best_attack_set.drop("Unnamed: 0", axis='columns', inplace=True)
    df_best_attack_set.drop("Unnamed: 20", axis='columns', inplace=True)
    df_best_attack_set['Type 1'] = df_best_attack_set['Type 1'].str.strip()
    return df, df1, df_best_attack_set

