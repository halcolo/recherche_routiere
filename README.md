

## Overview

This project is part of a research project about road accidents, a random forest classification algorithm is used in order to identify which are the most important features that can determine the prediction of an accident, this work is part of a research project carried out for the **Université Lumiere Lyon 2** in 2023.

### Introduction
Since the popularization of the automobile, researchers have studied road accidents with the aim of improving user safety. canada. In this study, we seek to use modern data science techniques to classify road accidents in France, in order to identify associated risk factors. To do this, we use data from [data.gouv.fr](http://data.gouv.fr/), which we analyze using a random forest algorithm. The results of this study will allow us to determine the factors that influence the severity of an accident and to propose ways to avoid them.

### How to use

 [Download individual data for the year 2022](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/). This data set will be used as the main data set for this project and more data sets can be added, but with more computing power it will be much better to process for the type of evaluations performed.

Within the data folder, create a folder for each year to be evaluated and within the data_cleanning.ipynb file, examine the years to be cleaned and add if there are older or newer ones, this first file will allow you to clean the files, unite them into one and delete them. some columns not very relevant.

![Screenshot 2024-01-01 at 22 13 56](https://github.com/jdalfons/recherche_routiere/assets/25759070/a6320eb5-61df-4f95-a9c3-42a89ee7c1ba)

After this you can check results in the `data_explore.ipynb` file, **Note**: last result with the report of classification is the most exigent process and can take more than 30 minutes in geeration 