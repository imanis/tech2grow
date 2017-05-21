"""
Project: tech2grow
Author: main
Created On: 5/20/17
"""

import sys

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from scipy.spatial import distance


#########################################################################################
#   The purpose of this script is to model products's categories  as graph.             #
#   This will help us to guide the person through the category graph inside the store   #
#########################################################################################


def get_element_matrix_nighboors(rowNumber, columnNumber, cat_matrix):
    """
    a function that return an element nighboors in the matrix
    """
    MID_ELEM = 4
    radius = 100
    nighboors = [cat_matrix[i][j] if i >= 0 and i < len(cat_matrix) and j >= 0 and j < len(cat_matrix[0])
                 else 0 for j in range(columnNumber - radius, columnNumber + radius + 1)
                 for i in range(rowNumber - radius, rowNumber + radius + 1)]
    # delete the central element
    # nighboors.pop(MID_ELEM)
    # return nighboors ! yea homee
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
    cats = []
    for index, row in categories.iterrows():
        cats.append((str(row['HYP_GRP_CLASS_KEY']), row['HYP_GRP_CLASS_DESC'], row['ABSCISSA'], row['ORDINATE']))

    # insert nodes into matrix
    for node in cats:
        cat_matrix[node[3]][node[2]] = node[0] + ''

    # construct andd fill the graph :o 
    G=nx.Graph()
    # add edges (implicitly nodes) 
    for cat in cats:
        # get nbrs 
        nbrs = get_element_matrix_nighboors(cat[3], cat[2], cat_matrix)
        for nbr in nbrs:
            if nbr != '':
                G.add_edge(cat[0], str(nbr))

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

    return G, cat_matrix


def get_shortest_path(entry_tuple, target_key, graph, cat_matrix):
    """
    Use the entry_tuple (node informations) to add an entry node into the graph, then use Bidirectional Dijkstra
    Algorithm to find the shortest path (if it exists) from entry node to the traget node
    :param entry_tuple: Entry node tuple comprising (key, description, x and y)
    :param target_key: The key characterizing the category node we want to find
    :param graph: The bidirectional graph to look into
    :param cat_matrix: categories 2D map matrix
    :return: shortest path (if it exists)
    """
    graph.add_node(entry_tuple[0], cat=entry_tuple[1], abs=entry_tuple[2], ord=entry_tuple[3])
    nbrs = get_element_matrix_nighboors(entry_tuple[3], entry_tuple[2], cat_matrix)
    for nbr in nbrs:
        if nbr != '':
            graph.add_edge(entry_tuple[0], str(nbr))
    try:
        length, path = nx.bidirectional_dijkstra(graph, entry_tuple[0], target_key)
        print(path)
        print(length)
    except:
        # catch prblm in data
        print("Unexpected error:", sys.exc_info()[0])
        pass


def main():
    # print('hello')
    cats_df = read_data_csv()
    # print(cats_df.head(20))
    graph, cat_matrix = build_graph(cats_df)
    print(graph.edges())
    # print(graph.node['600_2'])
    get_shortest_path(('E01', 'Entry Node 1', 530, 422), '602_2', graph, cat_matrix)
    # nx.draw_circular(graph)
    #plt.show()

    edges = graph.edges(data=True)
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos=pos)
    nx.draw_networkx_labels(graph, pos=pos)
    colors = ['r', 'b', 'y']
    linewidths = [20, 10, 5]
    for ctr, edgelist in enumerate(edges):
        print(pos)
        nx.draw_networkx_edges(graph, pos=pos, edgelist=edgelist, edge_color=colors[ctr], width=linewidths[ctr])
    plt.show()
    plt.savefig('this.png')

if __name__ == '__main__': main()
