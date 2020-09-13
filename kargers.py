#
#
# kargers min-cut randomized contraction algorithm
#
#
# (c) Mike Knerr 2019
# 
# ver: 0.15

# based on tim roughgarden's version
# of karger's min-cut algorithm 

import numpy as np
import matplotlib.pyplot as plt
import os
#import math as m
#from statistics import median

import random as rand
import copy

#graphfile='graphdata.txt'

def load_graph_from(fname):

#
# inputs: a file containing data about the nodes and
#         the adjacent nodes in format node number
#         followed by a list of adjacent nodes

 
# outputs:  a dictionary of lists 
#           the keys are the node numbers and each list
#           contains the variable number of adjacent node numbers 
 
    g={}
    ilist=[]
    
    f = open(fname, 'r')
    ilist = f.readlines()
    f.close()
    
     #  file has to be stripped of tabs and newlines
     #  as possible delimiters and converted into ints
  
    for i  in range(len(ilist)):             
        # the one-liners stuff you can do with python!
        # its a little rough on the eyes but... works
        ilist[i]=ilist[i].split('\t') # split into strings
        ilist[i]=ilist[i][0:len(ilist[i])-1] # strips out ending newline
        ilist[i]=list(map(int,ilist[i])) # convert strings to ints
        idx=int(ilist[i][0])
        g[idx]=ilist[i][1:len(ilist)-1]

    return g

    

def get_random_edge(graph):
   
    v = rand.choice(list(graph.keys())) #get a random node number
    w = rand.choice(graph[v]) # get one of its adjacent node randomly
    
    return(v,w)

    
  
def contract_nodes(graph, supernode, adjnode):

  # supernode absorbs and replaces the adjacent node 
  # assumes undirected graph ie pointers on all edges go both ways
  
      for node in graph[adjnode]:  # merge all nodes adj node is adjacent to
            if node != supernode:  # dont create a self-loop
                graph[supernode].append(node) # merge adj nodes into super
                
            graph[node].remove(adjnode)  # since adjnode is absorbed it doesnt exist       
                
            if node != supernode: # put in supernode in its place
                graph[node].append(supernode) 
              
      del graph[adjnode]  # adj node was just absorbed is no longer in graph
            
      return


def run_graph(graph,iterations):
                
    savedgraphs=[]
    savedcuts=[]
       
    for i in  range(iterations): 
        
        g = copy.deepcopy(graph) # get fresh copy 
         
        while len(g)>2:
            v1,v2= get_random_edge(g)
            contract_nodes(g,v1,v2)

        savedgraphs.append(g) 
        # just get any node from the collapsed graph and save the 
        # save the number of its adjacent nodes as the cut 
        savedcuts.append( len(g[min(g.keys())]) ) # get some any entry cut len
        
    return min(savedcuts),savedcuts

   
 
###### START HERE ######

### TEST algo development with some minimal cases
# to see if code holds up

# test a null case
    
    # what if mincut=0
    g={1:[]}
    r= run_graph(g,10) 
    r[0]
    
    # one node in a self-loop  
    # and no edges
    g={1:[1]}
    #mincut of self loop = 1
    run_graph(g,10)

    # 2 node linear 
    # mincut is 1
    g = {1: [2], 2: [1]}
    r=run_graph(g,10)
    r[0]
    
    # 3 node linear
    # mincut is 1
    g = {1:[2], 2:[1,3], 3:[2]} 
    r=run_graph(g,10)
    r[0]
    
    # attach 3rd back to node 1 to create a n-cycle 
    # mincut is 1
    g = {1:[2,3], 2:[1,3], 3:[2,1]} 
    run_graph(g,10)
    r[0]
    
    # 3 node fully connected
    # mincut is 2
    g = {1:[2,3], 2:[1,3], 3:[1,2]} 
    r=run_graph(g,10)
    r[0]
     
    g = {1:[2,3], 2:[1,3], 3:[2,1]} 
    r=run_graph(g,10)
    r[0]
    
    # attach 4th to node 3 in 3 node fully connected
    # mincut is 1
    g = {1:[2,3], 2:[1,3], 3:[1,2,4], 4:[3]} 
    r=run_graph(g,10)
    r[0]
    
    # fully connected square 
    # mincut is 3
    g  = {1:[2,3,4],2:[1,3,4],3:[1,2,4],4:[1,2,3]} 
    r= run_graph(g,100)
    r[0]
    
    # attach 5th node to node 4 from the fully connected square 
    # mincut is 1
    g  = {1:[2,3,4],2:[1,3,4],3:[1,2,4],4:[1,2,3,5], 5:[4]} #mincut=1 : dangling node attached to fully connected square
    r=run_graph(g,50)
    r[0]
  
    # attach 5th node to node 4 AND 3
    # mincut is 2 
    g  = {1:[2,3,4],2:[1,3,4],3:[1,2,4,5],4:[1,2,3,5],5:[3,4]} #mincut=1 : dangling node attached to fully connected square
    r=run_graph(g,1000)
    r[0]
    max(r[1])
    
# each entry in dictionary graph is a (key,list) 
# get adjacency list to run
    
    # load a graph or use a g from above
    g = load_graph_from("graphdata.txt")  
    
    testresults=[]
    minlist=[]
    ntests = 25 # run this far then check for convergence
    
    for tests in range(1,ntests+1):
        r=run_graph(g,tests)
        testresults.append(r)
        minlist.append(r[0])
    
    #min(minlist)
    print("Current run of: ",ntests)
    print("Current min: ",min(minlist))
    




