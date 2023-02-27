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
            palette = ['royalblue', 'aqua', 'deeppink', 'red', 'darkkhaki', 'slateblue',
                            'sienna', 'gold', 'grey', 'pink', 'mediumorchid', 'lightgray', 'tan', 'dodgerblue',
                            'limegreen', 'lightskyblue', 'wheat', 'olivedrab'])
    plt.title('Dragon as a primary type has the highest average total stats')

def dragon_vs_bug_atk_def_vis(df_best_attack_set):
    dragon=df_best_attack_set[(df_best_attack_set['Type 1']=='Dragon') | ((df_best_attack_set['Type 2'])=="Dragon")] 
    bug=df_best_attack_set[(df_best_attack_set['Type 1']=='Bug') | ((df_best_attack_set['Type 2'])=="Bug")]
    plt.scatter(dragon.Attack.head(100),dragon.Defense.head(100),c='mediumblue',label='Dragon',marker="*",s=25)
    plt.scatter(bug.Attack.head(100),bug.Defense.head(100),c='olivedrab',label="Bug",s=20)
    plt.xlabel("Attack")
    plt.ylabel("Defense")
    dragon_avg_attack = dragon.Attack.mean()
    dragon_avg_defense = dragon.Defense.mean()
    plt.axhline(dragon_avg_attack, label='Dragon Attack Average', c = 'royalblue')
    plt.axvline(dragon_avg_defense, label='Dragon Defense Average', c = 'royalblue')
    bug_avg_attack = bug.Attack.mean()
    bug_avg_defense = bug.Defense.mean()
    plt.axhline(bug_avg_attack, label='Bug Attack Average', c = 'yellowgreen')
    plt.axvline(bug_avg_defense, label='Bug Defense Average', c = 'yellowgreen')
    plt.legend()
    plt.title('Dragon vs Bug Comparing Attack and Defense')
    plt.plot()
    fig=plt.gcf()  #get the current figure using .gcf()
    fig.set_size_inches(12,6) #set the size for the figure
    plt.show()

def dragon_vs_bug_spatk_spdef_vis(df_best_attack_set):
    dragon=df_best_attack_set[(df_best_attack_set['Type 1']=='Dragon') | ((df_best_attack_set['Type 2'])=="Dragon")] 
    bug=df_best_attack_set[(df_best_attack_set['Type 1']=='Bug') | ((df_best_attack_set['Type 2'])=="Bug")]
    plt.scatter(dragon['Sp. Atk'].head(100),dragon['Sp. Def'].head(100),c='mediumblue',label='Dragon',marker="*",s=25)
    plt.scatter(bug['Sp. Atk'].head(100),bug['Sp. Def'].head(100),c='olivedrab',label="Bug",s=20)
    plt.xlabel("Sp. Atk")
    plt.ylabel("Sp. Def")
    dragon_avg_attack = dragon['Sp. Atk'].mean()
    dragon_avg_defense = dragon['Sp. Def'].mean()
    plt.axhline(dragon_avg_attack, label='Dragon Sp. Atk Average', c = 'royalblue')
    plt.axvline(dragon_avg_defense, label='Dragon Sp. Def Average', c = 'royalblue')
    bug_avg_attack = bug['Sp. Atk'].mean()
    bug_avg_defense = bug['Sp. Def'].mean()
    plt.axhline(bug_avg_attack, label='Bug Sp. Atk Average', c = 'yellowgreen')
    plt.axvline(bug_avg_defense, label='Bug Sp. Def Average', c = 'yellowgreen')
    plt.legend()
    plt.title('Dragon vs Bug Comparing Sp Attack and Sp Defense')
    plt.plot()
    fig=plt.gcf()  #get the current figure using .gcf()
    fig.set_size_inches(12,6) #set the size for the figure
    plt.show()

def stats_by_gen_vis(df_best_attack_set):
   Gen1 = df_best_attack_set[df_best_attack_set.Generation == 1]
   Gen1 = Gen1.groupby('Type 1').mean()
   Gen1 = Gen1.reset_index()
   Gen1 = Gen1[['Type 1', 'Total']]
   Gen1_2 = {'Type 1': 'Flying', 'Total': 0}
   Gen1 = Gen1.append(Gen1_2, ignore_index = True)
   Gen1 = Gen1.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen2 = df_best_attack_set[df_best_attack_set.Generation == 2]
   Gen2 = Gen2.groupby('Type 1').mean()
   Gen2 = Gen2.reset_index()
   Gen2 = Gen2[['Type 1', 'Total']]
   Gen2_2 = {'Type 1': 'Flying', 'Total': 0}
   Gen2 = Gen2.append(Gen2_2, ignore_index = True)
   Gen2 = Gen2.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen3 = df_best_attack_set[df_best_attack_set.Generation == 3]
   Gen3 = Gen3.groupby('Type 1').mean()
   Gen3 = Gen3.reset_index()
   Gen3 = Gen3[['Type 1', 'Total']]
   Gen3_2 = {'Type 1': 'Flying', 'Total': 0}
   Gen3 = Gen3.append(Gen3_2, ignore_index = True)
   Gen3 = Gen3.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen4 = df_best_attack_set[df_best_attack_set.Generation == 4]
   Gen4 = Gen4.groupby('Type 1').mean()
   Gen4 = Gen4.reset_index()
   Gen4 = Gen4[['Type 1', 'Total']]
   Gen4_2 = {'Type 1': 'Flying', 'Total': 0}
   Gen4 = Gen4.append(Gen4_2, ignore_index = True)
   Gen4 = Gen4.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen5 = df_best_attack_set[df_best_attack_set.Generation == 5]
   Gen5 = Gen5.groupby('Type 1').mean()
   Gen5 = Gen5.reset_index()
   Gen5 = Gen5[['Type 1', 'Total']]
   Gen5_2 = {'Type 1': 'Fairy', 'Total': 0}
   Gen5 = Gen5.append(Gen5_2, ignore_index = True)
   Gen5 = Gen5.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen6 = df_best_attack_set[df_best_attack_set.Generation == 6]
   Gen6 = Gen6.groupby('Type 1').mean()
   Gen6 = Gen6.reset_index()
   Gen6 = Gen6[['Type 1', 'Total']]
   Gen6_2 = {'Type 1': 'Ground', 'Total': 0}
   Gen6 = Gen6.append(Gen6_2, ignore_index = True)
   Gen6 = Gen6.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen7 = df_best_attack_set[df_best_attack_set.Generation == 7]
   Gen7 = Gen7.groupby('Type 1').mean()
   Gen7 = Gen7.reset_index()
   Gen7 = Gen7[['Type 1', 'Total']]
   Gen7_2 = {'Type 1': 'Flying', 'Total': 0}
   Gen7 = Gen7.append(Gen7_2, ignore_index = True)
   Gen7 = Gen7.set_index('Type 1').sort_index(ascending=True).reset_index()
   Gen8 = df_best_attack_set[df_best_attack_set.Generation == 8]
   Gen8 = Gen8.groupby('Type 1').mean()
   Gen8 = Gen8.reset_index()
   Gen8 = Gen8[['Type 1', 'Total']]
   Gen8 = Gen8.set_index('Type 1').sort_index(ascending=True).reset_index()
   plt.figure(figsize=(15, 8))
   plt.plot('Type 1', 'Total', data=Gen1, label='Gen 1')
   plt.plot('Type 1', 'Total', data=Gen2, label='Gen 2', linestyle='dotted')
   plt.plot('Type 1', 'Total', data=Gen3, label='Gen 3', linestyle='dashed')
   plt.plot('Type 1', 'Total', data=Gen4, label='Gen 4', linestyle='dashdot')
   plt.plot('Type 1', 'Total', data=Gen5, label='Gen 5', marker='.')
   plt.plot('Type 1', 'Total', data=Gen6, label='Gen 6', marker='s')
   plt.plot('Type 1', 'Total', data=Gen7, label='Gen 7', marker='o')
   plt.plot('Type 1', 'Total', data=Gen8, label='Gen 8', marker='*')
   plt.ylim(200)
   plt.ylabel('Average Total Stats')
   plt.xlabel('Type 1')
   plt.title('Average Total Stats by Primary Type')
   plt.legend(fontsize=13)
   plt.show()

def top_10_types_by_generation(df_best_attack_set):
    plt.figure(figsize=(15,8))
    #take the top 10 Types
    top_types=df_best_attack_set['Type 1'].value_counts()[:10]
    #take the pokemons of the type with highest numbers, top 10
    df3=df_best_attack_set[df_best_attack_set['Type 1'].isin(top_types.index)]
    # this plot shows the points belonging to individual pokemons
    sns.swarmplot(x='Generation',y='Total',data=df3,hue='Legendary')
    # It is distributed by Type
    plt.title('Top 10 Pokemon by Type and Average Total Stats in Each Generation')
    plt.show()

def primary_type_pie_chart():
    #define data
    labels = ['Water', 'Normal', 'Grass', 'Bug', 'Psychic', 'Fire', 'Electric', 'Rock', 'Dragon', 'Ground',
            'Ghost', 'Dark', 'Poison', 'Steel', 'Fighting', 'Ice', 'Fairy', 'Flying']

    data = [14.0, 12.2, 8.8, 8.6, 7.1, 6.5, 5.5, 5.5, 4.0, 4.0, 4.0, 3.9, 3.5, 3.4, 3.4, 3.0, 2.1, 0.5]
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1,0.1, 0.1, 0.1)  # only "explode" the 3rd slice 

    #define Seaborn color palette to use
    # colors = sns.color_palette('pastel')[0:18]
    colors = ['dodgerblue', 'wheat', 'limegreen', 'olivedrab', 'deeppink', 'red', 'gold', 'darkkhaki', 'royalblue',
            'tan', 'slateblue', 'grey', 'mediumorchid', 'lightgray', 'sienna', 'aqua', 'pink', 'lightskyblue']

    #create pie chart
    plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', explode=explode)
    plt.axis('equal')
    plt.title("Percentage of Different Primary Types of Pokemon")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    plt.show()

def secondary_type_pie_chart():
    #define data
    labels = ['Flying', 'Ground', 'Poison', 'Psychic', 'Fighting', 'Grass', 'Fairy', 'Steel', 'Dark', 'Dragon',
            'Water', 'Ghost', 'Ice', 'Rock', 'Fire', 'Electric', 'Normal', 'Bug']

    data = [23.4, 8.5, 8.2, 8.0, 6.3, 6.0, 5.6, 5.3, 4.8, 4.3, 3.4, 3.4, 3.4, 3.4, 2.9, 1.4, 1.0, 0.7]
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1, 0.1,0.1, 0.1, 0.1)  # only "explode" the 3rd slice 

    #define Seaborn color palette to use
    # colors = sns.color_palette('pastel')[0:18]
    colors = ['lightskyblue', 'tan', 'mediumorchid', 'deeppink', 'sienna', 'limegreen', 'pink', 'lightgray', 'grey', 'royalblue',
            'dodgerblue', 'slateblue', 'aqua', 'darkkhaki', 'red', 'gold', 'wheat', 'olivedrab']

    #create pie chart
    plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', explode=explode)
    plt.axis('equal')
    plt.title("Percentage of Different Secondary Types of Pokemon")
    plt.plot()
    fig=plt.gcf()
    fig.set_size_inches(7,7)
    plt.show()

def corr_heatmap(df_best_attack_set):
    plt.figure(figsize=(10,8))
    sns.heatmap(df_best_attack_set.corr(),annot=True, cmap='icefire')
    plt.title('Correlation Heatmap')
    plt.xticks(rotation=80)
    plt.show()

def box_plot(df_best_attack_set):
    plt.figure(figsize=(10,8))
    df_box=df_best_attack_set.drop(['Generation','Total', '#', 'Legendary',
     'Max_CP_Lv40', 'Battle_Stat', 'TDO', 'DPS', 'Fast_Move', 'Charged_Move'],axis=1)
    sns.boxplot(data=df_box)
    plt.title('Stats Outliers')
    plt.show()
    return df_box

def s_tier_attackers(df_best_attack_set):
    S_tier_attackers = ['Kartana', 'Terrakion', 'Shadow Metagross', 'Shadow Machamp',
                    'Shadow Mewtwo', 'Shadow Salamence', 'Shadow Dragonite', 'Mega Latios',
                    'Mega Gengar', 'Mega Charizard Y', 'Shadow Mamoswine']
    df_S_tier_attackers = df_best_attack_set[(df_best_attack_set.Pokemon == 'Kartana') | (df_best_attack_set.Pokemon == 'Terrakion') |
                  (df_best_attack_set.Pokemon == 'Shadow Metagross') | (df_best_attack_set.Pokemon == 'Shadow Machamp') |
                  (df_best_attack_set.Pokemon == 'Shadow Mewtwo') | (df_best_attack_set.Pokemon == 'Shadow Salamence') |
                  (df_best_attack_set.Pokemon == 'Shadow Dragonite') | (df_best_attack_set.Pokemon == 'Mega Latios') |
                  (df_best_attack_set.Pokemon == 'Shadow Gengar') | (df_best_attack_set.Pokemon == 'Mega Charizard Y') |
                  (df_best_attack_set.Pokemon == 'Shadow Mamoswine')]
    return df_S_tier_attackers