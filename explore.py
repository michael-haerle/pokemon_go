# Standard imports
import pandas as pd
# Vis imports
import matplotlib.pyplot as plt
import seaborn as sns
# Stats imports
from scipy.stats import spearmanr

def base_function(df_best_attack_set):
    x = input('Type a Pokemons name to find its best moveset.')
    result = df_best_attack_set[df_best_attack_set.Pokemon == x]
    print(result)


def find_best_moveset(df_best_attack_set):
    x = input('Type a Pokemons name to find its best moveset.')
    result = df_best_attack_set[df_best_attack_set.Pokemon == x]
    print(result)
    loop = 'active'
    while loop == 'active':
        choice = input('Would you like to check another Pokemon? Y/N')
        if choice == 'Y':
            base_function(df_best_attack_set)
        elif choice == 'N':
            print('Thank you have a great day!')
            break
        else:
            print('Please enter Y or N')

def pri_type_avg_stats(df_best_attack_set):
    avg_stats_by_primary_type = df_best_attack_set.groupby('Type 1').mean()
    avg_stats_by_primary_type_total = avg_stats_by_primary_type.sort_values('Total', ascending=False)
    plt.figure(figsize=(15, 8))
    sns.barplot(x = avg_stats_by_primary_type_total.index, y = avg_stats_by_primary_type_total.Total,
            palette = ['royalblue', 'lightgray', 'lightskyblue', 'deeppink', 'red', 'darkkhaki', 'grey',
                        'gold', 'slateblue', 'tan', 'aqua', 'dodgerblue', 'limegreen', 'sienna',
                        'pink', 'wheat', 'mediumorchid', 'olivedrab'])
    plt.title('Dragon as a primary type has the highest average total stats')