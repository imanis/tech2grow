"""
Project: tech2grow
Author: main
Created On: 5/20/17
"""

import math

import networkx as nx
import pandas as pd


#########################################################################################
#   The purpose of this script is to model category data as graph.                      #
#   This will help us to guide the person through the category graph inside the store   #
#########################################################################################


def get_element_matrix_nighboors(rowNumber, columnNumber, cat_matrix):
    """
    a function that return an element nighboors in the matrix
    """
    MID_ELEM = 4
    radius = 1
    nighboors = [cat_matrix[i][j] if i >= 0 and i < len(cat_matrix) and j >= 0 and j < len(cat_matrix[0])
                 else 0 for j in range(columnNumber - radius, columnNumber + radius + 1)
                 for i in range(rowNumber - radius, rowNumber + radius + 1)]
    # delete the central element
    nighboors.pop(MID_ELEM)
    # returnt nighboors ! yea homee
    return nighboors


def euclidean_distance(p1, p2):
    # get the "vol de oiseau"  distance between two points
    dst = distance.euclidean(p1,p2)
    return dst

def read_data_csv():
    # import data as csv into pd dataframe
    categories = pd.read_csv("../data/STORE_CATEGORY_LOCALIZATION.txt", sep="|", header=0, encoding='latin-1')

    # filter on pilote store FRA118
    categories_FRA118 = categories[categories.STORE_KEY == "FRA118"]

    # deal with duplicate HYP_GRP_CLASS_KEY values by adding an auto-increment prefix
    l = [str(x) for x in categories_FRA118['HYP_GRP_CLASS_KEY'].values]
    temp = list(map(lambda x: x[1] + '_' + str(l[:x[0]].count(x[1]) + 1) if l.count(x[1]) > 1 else x[1], enumerate(l)))
    categories_FRA118['HYP_GRP_CLASS_KEY'] = temp

    return categories_FRA118


def build_graph(categories):
    # prepare nodes
    cat_matrix = [['' for i in range(1000)] for j in range(1000)]
    # cat_matrix = np.zeros(shape=(1000, 1000))

    # get cats as nodes
    nodes = []
    for index, row in categories.iterrows():
        nodes.append((str(row['HYP_GRP_CLASS_KEY']), row['HYP_GRP_CLASS_DESC'], row['ABSCISSA'], row['ORDINATE']))

    # insert nodes into matrix
    for node in nodes:
        cat_matrix[node[3]][node[2]] = node[0] + ''

    # construct andd fill the graph :o 
    G=nx.Graph()
    # add edges (implicitly nodes) 
    for cat in cats:
        # get nbrs 
        nbrs = get_element_matrix_nighboors(cat[3],cat[2],cat_matirix)
        for nbr in nbrs:
            if nbr!="":
                G.add_edge(str(cat[0]),str(nbr)) 

    # populate node's data 
    for n in cats:
        G.node[n[0]]['cat'] = n[1]
        G.node[n[0]]['abs'] = n[2]
        G.node[n[0]]['ord'] = n[3]            

        # populate edge's weight 
    for u,v,a in G.edges(data=True):
        try:
            p1=(G.node[u]['abs'],G.node[u]['ord'])
            p2=(G.node[v]['abs'],G.node[v]['ord'])
            G.edge[u][v]['weight'] = euclidean_distance(p1,p2)  
        except:
            #catch prblm in data
            pass


def main():
    # print('hello')
    cats = read_data_csv()
    graph = build_graph(cats)


if __name__ == '__main__': main()
