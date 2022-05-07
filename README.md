# Bankers-Algorithm-in-Python (Using Numpy)
Operating System: Banker's Deadlock Avoidance Algorithm (Hardcoded) Implementation in Python (Using Numpy aka Numerical Python)

**Examples taken by Book: Operating System by William Stallings**

### Implementation
```Python
if __name__ == '__main__':
    claim = np.array([[3, 2, 2], [6, 1, 3], [3, 1, 4], [4, 2, 2]])
    allocation = np.array([[1, 0, 0], [6, 1, 2], [2, 1, 1], [0, 0, 2]])
    resources = np.array([9, 3, 6])
    
    processes = processes_order(allocation, claim, resources)
    print ("Processes: ", processes)
```
