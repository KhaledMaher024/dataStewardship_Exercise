import pandas as pd
import csv
import AppLogic as app
tobacco_df = pd.read_csv("input/TobaccoUsage.csv",usecols=["Year","State","Never smoked"])
tobaccoList = app.removeFromList(tobacco_df)
tobaccoList = app.groupBy(tobaccoList)
tobaccoList = app.sort(tobaccoList , "Year")

cancer_df = pd.read_csv("input/UnitedStateCancer.csv",usecols=["States","Cancer Sites","Year","Count"])
cancer_list = app.removeFromList2(cancer_df)
cancer_list= app.groupByYear(cancer_list)
cancer_list = app.sort(cancer_list, "Year")

merged_df = app.mergeDF(tobaccoList , cancer_list,['Year'])
merged_df.drop("States" , axis=1 , inplace=True)
print(merged_df)
merged_df.to_csv('output/transformed.csv')
