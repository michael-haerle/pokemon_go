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
[[Statistical Analysis](#stats)]
[[Conclusion](#conclusion)]
___


## <a name="project_description"></a>Project Description:
A project to do exploratory data analysis on one of the most popular mobile games since 2016. This will be done using a combination of data from pokemon go and the main series games. (Side note: The formula used to calculate what I call "Battle Stat" changes partway through this project. If you would like to know more please refer to the description below.

What is Battle Stat? Battle stat is the name I use to call stat that is used to mimic the actual performance in simulations. At first it was found using Damage Per Second^3 * Total Damage Output. However this has it flaws as it slightly favours bulky attackers and underrates the opposite. Thus a new formula was developed by redit user u/Elastic_Space, this formula is calculated from the 4th power root of Damage Per Second^3 * Total Damage Output.


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
- What S tier pokemon in Pokemon Go has the highest and lowest Battle Stat?
- What pokemon in Pokemon Go has the highest and lowest average battle stat between all of their move sets?
- 

### Need to haves (Deliverables):
- A new csv with updated pokemon data for up to generation 8.
- A final report notebook
- A function that will take a Pokemon name as an input and output its stats and best moveset.


### Nice to haves (With more time):
 - 


### Steps to Reproduce:
- 

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

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: (Ex. Chi Square)


#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is: Blank and Blank are independent
- The alternate hypothesis (H<sub>1</sub>) is: There is a relationship between Blank and Blank

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:
- We reject the null hypothesis that Blank and Blank are independent
- There is a relationship between Blank and Blank
- P-Value 
- Chi2 
- Degrees of Freedom 


***


## <a name="conclusion"></a>Conclusion:

- 

#### Next Steps Here 

[[Back to top](#top)]
