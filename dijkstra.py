from collections import defaultdict
import math
import sys
import heapq

def main():
    """Main function."""
    args = sys.argv     # get command line arguments
    if len(args) < 2:
        print("Error: No data set provided. Exiting...")
        quit()

    fp = args[1]    # get filename from command line arguments
    
    edges = extract_edges(fp)   # get list of edges from test case
    d, path = shortest_path(edges, "A", "B")    # get shortest path and distance
    prettyPrint(d, path)    # make it pretty :)


def extract_edges(filepath):
    """Returns data from formatted input file as edges."""

    try:
        V = []

        with open(filepath) as f:
            for line in f:
                line.strip("\n")
                e = line.split()
                edge = (e[0], e[1], int(e[2]))
                V.append(edge)

        return V
    except:
        print("Error reading file.")


def shortest_path(edges, s, target):
    """Returns shortest path from source to target vertex. Uses Dijsktra's Algorithm"""

    graph = defaultdict(list)   # represent graph as dictionary/map of edges + weights
    for head, tail, weight in edges:
        graph[head].append((weight, tail))

    queue, seen, min_d = [(0, s, [])], set(), {s: 0}    # use heapq as priority queue to track verticies

    while queue:    # while the queue is not empty, check weights of each neighbor
        (dist, v1, path) = heapq.heappop(queue)   # get current vertex from the queue
        if v1 not in seen:
            seen.add(v1)    # mark current vertex as seen
            path = [v1] + path
            if v1 == target:    # algorthm is done when target vertex is reached.
                return (dist, path)

            for d, v2, in graph.get(v1, ()):    # compare distances
                if v2 in seen:
                    continue
                prev = min_d.get(v2, None)
                next = dist + d
                if prev is None or next < prev:
                    min_d[v2] = next    # if proposed path is shorter, update the next vertex
                    heapq.heappush(queue, (next, v2, path))


def prettyPrint(d, path):
    """prettyPrint prints the path and its distance in a much prettier format."""

    print("============================RESULTS==============================")
    print("Shortest Path: {}".format(path))
    print("Distance: {}".format(d))



main()
