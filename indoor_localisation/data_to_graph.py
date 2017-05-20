import networkx as nx
import pandas as pd
import numpy as np


#########################################################################################
#   The purpose of this script is to model category data as graph.
#   This will help us to guide the person through the category graph inside the store
#########################################################################################


#import data as csv into pd dataframe
categories = pd.read_csv("./data/STORE_CATEGORY_LOCALIZATION.txt", sep="|", header=0,encoding='latin-1')

# lets see some data
print(categories.head())

# filter on pilote store FRA118
categories_FRA118 = categories[categories.STORE_KEY=="FRA118"]

# deal with duplicate HYP_GRP_CLASS_KEY values by adding an auto-increment prefix
l = [str(x) for x in categories['HYP_GRP_CLASS_KEY'].values]
temp = list(map(lambda x: x[1]+'_'+str(l[:x[0]].count(x[1]) + 1) if l.count(x[1]) > 1 else x[1], enumerate(l)))
categories['HYP_GRP_CLASS_KEY'] = temp

# prepare nodes
cat_matirix = np.zeros((1000,1000))

# get cats as nodes
nodes=[]
for index, row in categories_FRA118.iterrows():
    #print(row['HYP_GRP_CLASS_KEY'], row['HYP_GRP_CLASS_DESC'], row['ABSCISSA'],row['ORDINATE'] )
    nodes.append((row['HYP_GRP_CLASS_KEY'], row['HYP_GRP_CLASS_DESC'], row['ABSCISSA'],row['ORDINATE']))
    
#insert nodes into matrix
for node in nodes:
    cat_matirix[node[3]][node[2]]=node[0]of the

def get_element_matrix_nighboors(rowNumber, columnNumber,matrix):
    """
    a function that return an element nighboors in the matrix
    """
    radius=1
    nighboors = [cat_matirix[i][j] if  i >= 0 and i < len(cat_matirix) and j >= 0 and j < len(cat_matirix[0]) else 0 for j in range(columnNumber-radius, columnNumber+radius+1) for i in range(rowNumber-radius, rowNumber+ radius+1)]
    # delete the central element
    nighboors.pop(int(len(nighboors)/2)+1)
    # returnt nighboors ! yea homee
    return nighboors


# construct andd fill the graph :o 
G=nx.Graph()
# add edges (implicitly nodes) 
for node in nodes:
    # get nbrs 
    nbrs = get_element_matrix_nighboors(node[2],node[3],cat_matirix)
    for nbr in nbrs:
        G.add_edge(node[0],nbr) 

# populate node's data 
for node in nodes:
    G[node[0]]['cat'] = node[1]
    G[node[0]]['abs'] = node[2]
    G[node[0]]['ord'] = node[3]





