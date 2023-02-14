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

def stats_by_gen_vis(df1):
    avg_stats_by_gen = df1.groupby('Generation').mean()
    plt.figure(figsize=(15, 8))
    gfg = sns.lineplot(data=df1, x="Type 1", y="Total", hue="Generation", ci=None, palette='hls', style="Generation", markers=True)
    # for legend text
    plt.setp(gfg.get_legend().get_texts(), fontsize='13')  
    # for legend title
    plt.setp(gfg.get_legend().get_title(), fontsize='20') 
    plt.title('Total Stats Average by Type and Generation')
    plt.show()

def top_10_types_by_generation(df1):
    plt.figure(figsize=(15,8))
    #take the top 10 Types
    top_types=df1['Type 1'].value_counts()[:10]
    #take the pokemons of the type with highest numbers, top 10
    df3=df1[df1['Type 1'].isin(top_types.index)]
    # this plot shows the points belonging to individual pokemons
    sns.swarmplot(x='Generation',y='Total',data=df3,hue='Legendary')
    # It is distributed by Type
    plt.axhline(df3['Total'].mean(),color='red',linestyle='dashed')
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