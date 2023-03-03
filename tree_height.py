# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    
    heights = [0]*n
    
    for i in range(n-1, -1, -1):
        parent = parents[i]
        if parent == -1:
            heights[i] = 1
        else:
            
            heights[i] = 1 + heights[parent]
  
    return max(heights)


def main():
    
    input_type = input("Enter input type (K for keyboard input, F for file input): ")
    if input_type == "F":
      
        filename = input("Enter filename: ")
        if "a" in filename:
            print("Invalid filename")
            return
        try:
         
            with open("inputs/" + filename, "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found")
            return
    else:
     
        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of each node: ").split()))
    
 
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))