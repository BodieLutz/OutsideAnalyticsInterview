This script simulates the operation of a single elevator. The goal of the elevator is to minimize the travel time
to get to each and every floor. The script assumes that the input will follow the exact same format of
"elevator start=# floors=#,#,#,#" with a single start floor and a variable amount of floors to visit. The output of the
program will be in the form of "[total travel time] [path of elevator]" and will print to stdout.

EXAMPLE COMMAND LINE EXECUTION:

Using input file:
    python elevator.py input.txt

Using arguments:
    python elevator.py elevator start=12 floors=2,9,1,32


The methodology of this script is to create a fully-connected, undirected, weighted graph wherein each node represents a
floor to visit, edges represent the ability for the elevator to travel from the current floor to the target floor, and
edge weights represent the travel cost to travel from a source floor to a target floor. For example, assume the start
floor of the elevator is floor 2, and the only floor to visit is floor 12. Floor 2 and floor 12 are nodes in the graph,
there exists an undirected edge between the nodes because the elevator can travel from floor 2 to floor 12 and
vice-versa. The weight of the edge is equal to the number of floors traveled multiplied by the time to travel a single
floor. In this case, with a per-floor travel time of 10, the number of floors traveled is (12 - 2) = 10, so the total
travel time is 10 x 10 = 100.

The only dependency of this program is the NetworkX library used to build and operate on the graph.

Assumptions:
 - The execution of this script represents the use of a single elevator, and that elevator must visit all floors
 - The goal of the elevator is to minimize the cost to visit all floors
 - There are no extra calls to the elevator other than the list of floors inputted
 - This program only calculates the cost to visit all inputted floors
 - The input to the program follows the same format as in the email
 - Input will always follow the exact same format
 - After the elevator visits the last floor, it will remain where it is
 - The elevator will only visit a floor one time

Features Not Implemented:
 - Additional elevator calls during the execution of the input path
 - Output elsewhere from stdout

