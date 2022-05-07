import numpy as np

def calc_alloction(resources, allocation, claim):
    """
    This function calculates the allocation and needed resources
    
    args:
        resources (numpy.ndarray): The resources matrix
        allocation (numpy.ndarray): The allocation matrix
        claim (numpy.ndarray): The claim matrix
        
    returns:
        available (numpy.ndarray): The available resources
        needed (numpy.ndarray): The needed resources
    """
    
    sum_of_allocation = np.zeros(len(resources), dtype='int') # Intialization
    for c in range(len(resources)): 
        sum_of_allocation[c] = np.sum(np.ndarray.flatten(allocation[:, c:c+1]))
 
    available =  resources - sum_of_allocation
    needed = claim - allocation
    
    return available, needed

def bankers_implementation(available, needed):
    """
    This function implements the banker's algorithm to find the processes order in the order of allocation
    
    args:
        available (numpy.ndarray): The available resources
        needed (numpy.ndarray): The needed resources
        
    returns:
        left_resources (numpy.ndarray): The left resources
        process (int): The process number
    """
    
    for i in range(needed.shape[0]):
        if (np.all(np.less_equal(needed[i], available))) and (not np.any(needed[i]) != True): 

            available += allocation[i]

            claim[i] = np.zeros(len(resources), dtype='int')
            allocation[i] = np.zeros(len(resources), dtype='int')
            needed[i] = np.zeros(len(resources), dtype='int')

            return available, i

def processes_order(allocation, claim, resources):
    """ This function returns the processes order in the order of allocation

    Args:
        allocation (numpy.ndarray): The allocation matrix
        claim (numpy.ndarray): The claim matrix
        resources (numpy.ndarray): The resources matrix

    Returns:
        processes_order (list): The processes order
    """
    
    available, needed = calc_alloction(resources, allocation, claim)
    processes = np.zeros(claim.shape[0], dtype='int') # Intialization
    inc = 0
    while not np.any(allocation) != True: 
        left_resources, process = bankers_implementation(available, needed) # bankers_implementation
        print ("Available resources: ", left_resources)
        processes[inc] = process 
        inc += 1 
        
    return processes
