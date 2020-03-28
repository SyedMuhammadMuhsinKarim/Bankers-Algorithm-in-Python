import numpy as np

claim = np.array([[3, 2, 2], [6, 1, 3], [3, 1, 4], [4, 2, 2]])
allocation = np.array([[1, 0, 0], [6, 1, 2], [2, 1, 1], [0, 0, 2]])
resources = np.array([9, 3, 6])

sum_of_allocation = np.zeros(len(resources), dtype='int') # Intialization

for c in range(len(resources)): sum_of_allocation[c] = np.sum(np.ndarray.flatten(allocation[:, c:c+1]))
 
available =  resources - sum_of_allocation

needed = claim - allocation

def bankers_implementation(available):
	for i in range(needed.shape[0]):
		if (np.all(np.less_equal(needed[i], available))) and (not np.any(needed[i]) != True): 
			available += allocation[i]
			claim[i] = np.zeros(len(resources), dtype='int')
			allocation[i] = np.zeros(len(resources), dtype='int')
			needed[i] = np.zeros(len(resources), dtype='int')
			return available, i
			break

processes = np.zeros(claim.shape[0], dtype='int') # Intialization

inc = 0
while not np.any(allocation) != True: 
		left_resources, process = bankers_implementation(available)
		print ("Available: ", left_resources)
		processes[inc] = process
		inc += 1
	
print("process order: ", processes)
