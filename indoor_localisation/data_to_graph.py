import networkx as nx
import pandas as pd
import numpy as np


#import data as csv into pd dataframe
categories = pd.read_csv("./data/STORE_CATEGORY_LOCALIZATION.txt", sep="|", header=0,encoding='latin-1')

# lets see some data
categories.head()

# filter on pilote store FRA118
categories_FRA118 = categories[categories.STORE_KEY=="FRA118"]

# prepare nodes
cat_matirix = np.zeros((1000,1000))

# add node to Graph
nodes=[]
for index, row in categories_FRA118.iterrows():
    #print(row['HYP_GRP_CLASS_KEY'], row['HYP_GRP_CLASS_DESC'], row['ABSCISSA'],row['ORDINATE'] )
    nodes.append((row['HYP_GRP_CLASS_KEY'], row['HYP_GRP_CLASS_DESC'], row['ABSCISSA'],row['ORDINATE']))
    
#insert nodes into matrix
for node in nodes:
    cat_matirix[node[3]][node[2]]=node[0]

# construct andd fill the graph :o 
G=nx.Graph()
for node in nodes:
    G.add_node(node) 



