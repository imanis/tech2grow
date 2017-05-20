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
    # calculate the euclidean distance between two 2D points
    return math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


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

    print(cat_matrix[604][12])
    # construct and fill the graph :o
    G = nx.Graph()
    # add edges (implicitly nodes)
    for node in nodes:
        # get nbrs
        # print(node[2], node[3])
        nbrs = get_element_matrix_nighboors(node[2], node[3], cat_matrix)
        # print(nbrs)
        for nbr in nbrs:
            if nbr != 0:
                # print(str(node[0]), str(nbr))
                G.add_edge(str(node[0]), str(nbr))

    # populate node's data
    for n in nodes:
        G.node[n[0]]['cat'] = n[1]
        G.node[n[0]]['abs'] = n[2]
        G.node[n[0]]['ord'] = n[3]

    # print(G.edges())
    # populate edges' data
    for (u, v, d) in G.edges():
        # print(v)
        G.edge[u][v]['weight'] = euclidean_distance((G.node[u]['abs'], G.node[u]['ord']),
                                                    (G.node[v]['abs'], G.node[v]['ord']))
        # print(G.edge[u][v]['weight'])


def main():
    # print('hello')
    cats = read_data_csv()
    graph = build_graph(cats)


if __name__ == '__main__': main()
