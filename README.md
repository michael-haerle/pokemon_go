# <a name="top"></a> Pokemon Go and the Main Series Games
![]()

by: Michael Haerle

<p>
  <a href="https://github.com/michael-haerle" target="_blank">
    <img alt="Michael" src="https://img.shields.io/github/followers/michael-haerle?label=Follow_Michael&style=social" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Conclusion](#conclusion)]
___


## <a name="project_description"></a>Project Description:
A project to do exploratory data analysis on one of the most popular mobile games since 2016. This will be done using a combination of data from pokemon go and the main series games. (Side note: The formula used to calculate what I call "Battle Stat" changes partway through this project. If you would like to know more please refer to the description below.

What is Battle Stat? Battle stat is the name I use to call stat that is used to mimic the actual performance in simulations. At first it was found using Damage Per Second^3 * Total Damage Output. However this has it flaws as it slightly favours bulky attackers and underrates the opposite. Thus a new formula was developed by redit user u/Elastic_Space, this formula is calculated from the 4th power root of Damage Per Second^3 * Total Damage Output. They named this value ER or Equivalent Rating which I refer to as Battle_Stat as I feel it's more intuitive.


[[Back to top](#top)]

***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:
- Create README.md with data dictionary, come up with questions to lead the exploration and the steps to reproduce.
- Acquire data from kaggle and various websites online.
- Clean and prepare data for exploration. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- Produce at least 4 clean and easy to understand visuals.
- Clearly define hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Create csv file for other people to use in the future.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.


### Project goals: 
- My goal is to perform exploraty analysis on Pokemon Go and the main series Pokemon games.


### Initial questions:
- What pokemon in Pokemon Go has the highest and lowest cp?
- What "S tier pokemon" in Pokemon Go has the highest and lowest Battle Stat?
- What pokemon in Pokemon Go has the highest and lowest average battle stat between all of their move sets?
- What primary type has the highest average total stats?
- What does the highest and lowest average total stats look like compared? (Dragon vs Bug)
- 

### Need to haves (Deliverables):
- A new csv with updated pokemon data for up to generation 8.
- A final report notebook
- A function that will take a Pokemon name as an input and output its stats and best moveset.


### Nice to haves (With more time):
 - Feature engineering columns for if the pokemon is a mythical, ultra beast, baby form, has multiple forms, or has a primal form.


### Steps to Reproduce:
- Download the csv's found in the git repository, the wrangle.py file, and the final_notebook.ipynb.
- Then run the final_notebook.

***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

- 


***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| Pokemon | Name of the pokemon | object |
| DPS | Damage per Second | float64 |
| TDO | Total Damage Output | float64 |
| Battle_Stat | Name used to replace ER(refer to paragraph in the project description for more info) | float64 |
| Max_CP_Lv40 | The max CP(Combat Power) a Pokemon can have at level 40 in Pokemon GO) | int64 |
| Fast_Move | The fast attack the Pokemon uses in Pokemon GO | object |
| Charged_Move | The charged attack the Pokemon uses in Pokemon GO | object |
| # | The id number of the pokemon in the games | float64 |
| Type 1 | The primary type of the pokemon | object |
| Type 2 | The secondary type of the pokemon | object |
| Total | The sum of HP, Attack, Defense, Sp. Atk, Sp. Def, and Speed | float64 |
| HP | The Hit Points or health of the pokemon | float64 |
| Attack | The numerical value assigned to the damage a pokemons physical attacks will do | float64 |
| Defense | The numerical value assigned to the pokemon to take reduced damage from a physical attack | float64 |
| Sp. Atk | The numerical value assigned to the damage a pokemons non-physical attacks will do | float64 |
| Sp. Def | The numerical value assigned to the pokemon to take reduced damage from a non-physical attack | float64 |
| Speed | The numerical value that determines how fast the pokemon is, this determines who attacks first | float64 |
| Generation | What generation the pokemon comes from | float64 |
| Legendary | 1 if the pokemon is a legendary, 0 if the pokemon is not a legendary | object |


***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Prepare steps: 
- 

*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py
    - explore.py


### Takeaways from exploration:
- 


***


## <a name="conclusion"></a>Conclusion:

- 

#### Next Steps Here 

[[Back to top](#top)]
