import networkx as nx
travel_time = 10

def parse_input():
    input_file = open("input2.txt", "rt")# open input text file for reading

    input = input_file.readlines()  # read input in as string
    input = ''.join(input) #convert read list to string
    input_file.close()  # close the file
    input = input.split(" ")  # split the input string on spaces
    input = input[1:]  # remove 'elevator' from list

    # split the input list into the start floor and the target floors
    start = input[0]
    floors = input[1]

    # parse the starting floor to only the floor number
    start = start.split("=")[1:]
    start = int(start[0])

    # parse target floors to list of integers
    floors = floors.split("=")[1:]
    floors = "".join(floors).split(",")
    floors = [eval(i) for i in floors]

    return start, floors

#Create the weighted, undirected graph
def create_graph(start, floors):
    #Create graph
    G = nx.Graph()

    #Create all nodes
    floors.insert(0, int(start)) #consolidate list of all floors
    G.add_nodes_from(floors) #add nodes to graph

    #Create weighted edges
    for x in floors:
        for y in floors:
            #Do not add self edges
            if(x == y):
                continue
            #do not repeat edges
            elif(G.has_edge(x,y) == True):
                continue
            else:
                weight = abs(x-y) * travel_time #calculate cost
                G.add_edge(x,y, weight=weight) #add weighted edge with cost as edge weight

    return G

#Compute the travel cost of a given list of edges
def compute_cost(list):
    total_cost = 0
    for item in list:
        total_cost += abs(item[0]- item[1]) * travel_time

    return total_cost

#Find the shortest path for the elevator
def find_path(Graph, start):
    mst = nx.minimum_spanning_tree(Graph, weight="weight") #calculate the minimum spanning tree of the graph (Kruskal's)

    dfs_path = list(nx.dfs_edges(mst, source=start)) #Use DFS to search through the MST

    #Process DFS list to ensure continuity
    for i in range(len(dfs_path)):
        if(i == 0):
            continue
        else:
            prev_item = dfs_path[i-1]

        #When DFS returns to top of MST
        if(dfs_path[i][0] == start):
            source = prev_item[1]
            target = dfs_path[i][1]
            dfs_path.pop(i) #remove discontinuity
            new_tuple = (source, target)
            dfs_path.insert(i, new_tuple) #insert new, continuous path

    dfs_cost = compute_cost(dfs_path) #compute the total cost of the path
    return dfs_path, dfs_cost

#generate the proper output given a path
def create_output(path, start):
    final_path = []
    final_path.append(start)
    for edge in path:
        final_path.append(edge[1])
    final_path = ','.join(str(x) for x in final_path)
    return final_path

def main():
    start, floors = parse_input() #parse the input
    Graph = create_graph(start, floors) #Generate the graph
    path, cost = find_path(Graph, start) #find the shortest path
    output = create_output(path, start) #Create output in proper format
    print(cost, output)

main()
