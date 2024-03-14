import networkx as nx


def parse_input():
    input_file = open("input.txt", "rt")# open input text file for reading

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

parse_input()


