import pandas as pd
# tobacco
tobacco_df = pd.read_csv("Data/Raw/TobaccoUsage.csv",usecols=["Year","State","Never smoked"])
# def convert_percentage(dataFrame):
#     result = []
#     for item in dataFrame['Never smoked']:
#         result.append(float(item.rstrip("%")))
#     dataFrame["Never smoked"] = result
#     return dataFrame

# tobacco
# cancer
def sort(dataToProcesse,colName):
    result = []
    result = dataToProcesse.sort_values(colName)
    return result

cancer_df = pd.read_csv("Data/Raw/UnitedStateCancer.csv",usecols=["States","Cancer Sites","Year","Count"])

def groupByYear(dataFrame):
    dataFrame = dataFrame.loc[dataFrame['States'] == 'Alabama']
    dataFrame = dataFrame[dataFrame["Cancer Sites"] == "Liver"]
    dataFrame = sort(dataFrame, "Year")
    years =[]
    states =[]
    counts = []
    occured = 0
    sumation = 0
    for item in dataFrame['Year'][0:len(dataFrame)]:
        if item != occured:
            occured = item
            years.append(item)
            states.append("Alabama")
    for year_occirance in years:
        sumation=0
        for index , item in dataFrame.iterrows() :
            if(year_occirance == item['Year']):
                sumation += item['Count']
        counts.append(sumation)
    dataFrame = dataFrame[~dataFrame.duplicated(['Year'])]
    dataFrame['Count'] = counts
    return dataFrame





tobacco_df = pd.read_csv("Data/Raw/TobaccoUsage.csv", usecols=["Year", "State", "Never smoked"])
# Tobacco
def groupBy(dataFrame):
    dataFrame = dataFrame.loc[dataFrame['State'] == 'Alabama']
    dataFrame = sort(dataFrame, "Year")
    counts = []
    for index , item in dataFrame.iterrows() :
        x =float(item['Never smoked'].rstrip("%"))
        sumation = 100 - x
        counts.append(sumation)
    dataFrame["count"] = counts
    dataFrame.drop("Never smoked" , axis=1 , inplace=True)
    return dataFrame




# tobacco
def removeFromList(data):
    indexes = []
    list = []
    for index,row in data.iterrows() :
        if row['State'] != "Alabama" or row['Year'] < 2000:
            indexes.append(index)
    data.drop(indexes , axis=0 , inplace=True)
    list = data
    return list


# cancer
def removeFromList2(data):
    indexes = []
    for index,row in data.iterrows() :
        if (row['Year'] <= 2000 and row['Year'] >= 2010) or row['States'] != "Alabama" :
            indexes.append(index)
    data.drop(indexes , axis=0 , inplace=True)
    return data

# tobacco
# cancer
# def cleanData(data):
#     if(data.isnull().sum()):
#         dataMedian = data.median()
#         data.fillna(dataMedian,inplace=True)


# tobacco
# cancer
def mergeDF(firstDf,secondeDf,cols):
 return pd.merge(firstDf, secondeDf, on=cols)
