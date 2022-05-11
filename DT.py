import pandas as pd
import math

def lowest_gini(data):
    leastG=math.inf
    allG=[]
    rows = data.shape[0]
    if data.shape[1] == 1:
        rootnode, allG, G = target, [], 0
    for col in data.iloc[:,:-1]:
        features=set(data[col])
        G=0
        for feature in features:
            total, y, n=0, 0, 0
            for i, row in data.iterrows():
                if data[col][i]==feature:
                    total+=1
                    if data[target][i]==target_values[0]:
                        y+=1
                    else:
                        n+=1

            gi=1-(y/total)**2-(n/total)**2
  
            G+=(total/rows)*gi
            allG.append(G)
            
        if G<leastG:
            rootnode=col
            leastG=G

    return rootnode, allG, G



def decision_tree(root,data):
    childnodes1=set(data[root])
    for child in childnodes1:
        dt.append(child)
        df=data[data.values==child]
        df=(df.drop([root],axis=1))
        df =(df.drop_duplicates())
        root2,allG,g =lowest_gini(df)


        if set(allG) == {0.0} or root2 == target: #if every answer is 0
                 for j, row in data.iterrows():
                    if (data[root][j]==child) and  data[target][j]==target_values[0]:
                        dt.append([target,'yes'])
                        break
                    elif (data[root][j]==child) and  data[target][j]==target_values[1]:
                        dt.append([ target,'no'])
                        break
        elif g == 0:
            for i in set(data[root2]):
                for j, row in data.iterrows():
                    if (data[root][j]==child) and data[root2][j] == i and  data[target][j]==target_values[0]:
                        dt.append([root2, i, 'yes'])
                        break
                    elif (data[root][j]==child) and data[root2][j] == i and  data[target][j]==target_values[1]:
                        dt.append([root2, i , 'no'])
                        break
        else:
            dt.append(root2)
            decision_tree(root2,df)
            
  
    return dt
  
#WEATHER DATASET

df = pd.read_csv("weather-data.csv")
print(df)

target = 'Decision'
target_values = ['Yes','No']
original_data = df.copy()
data = df.iloc[:,1:]
root, allG, g =lowest_gini(data)
dt = [root]
decision_tree(root,data)
