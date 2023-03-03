# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    nodes_at_depth = [[] for _ in range(n)]
    root = None
    
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            nodes_at_depth[parent].append(i)
            
            
    max_height = 0
    # Your code here
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        max_height = max(max_height, depth)
        for child in nodes_at_depth[node]:
            stack.append((child, depth + 1))

    return max_height


def main():
    filename = input("Enter input filename (leave blank for keyboard input): ").strip()
    if filename and 'a' in filename.lower():
        print("Invalid filename, please try again.")
        return
    if filename:
        try:
            with open(f"data/{filename}") as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
        except FileNotFoundError:
            print("File not found, please try again.")
            return
    else:
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents of each node: ").strip().split()))

    # Compute and print the height of the tree
    height = compute_height(n, parents)
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
#print(numpy.array([1,2,3]))