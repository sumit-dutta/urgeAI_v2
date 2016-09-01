
import pandas as pd


def readJson(path):

    with open(path, 'rb') as f:
        data = f.readlines()

    data = map(lambda x: x.rstrip(), data)

    data_json_str = "[" + ','.join(data) + "]"


    data_df = pd.read_json(data_json_str)
    return data_df



def readCsv(path):
    df = pd.read_csv(path)
    return df


def getCloumnNames(df):
    return list(df.columns.values)


def createDummyVariables(inputList):
     distinctList = list(set(inputList))
     df = pd.DataFrame(columns=distinctList)
     i = 0
     for input in inputList:
         newRow = []
         for cat in distinctList:
             if(input == cat):
                 newRow.append(1)
             else:
                 newRow.append(0)
         df.loc[i] = newRow
         i= i+1
         print input
         print newRow
     return df



def concatDataframes(*dfs):
    result = pd.DataFrame()
    for df in dfs:
        result = pd.concat([result,df], axis=1)
    return result


