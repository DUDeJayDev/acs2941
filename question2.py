# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given scores. 
# Store them in a list and find the score of the runner-up. 

# The first argument contains n.
# The second line contains an array of n integers each separated by a space. 

def runner_up(n, arr):
    sort = list(sorted(set(arr)))
    largest = sort[-1]
    sort.remove(largest)

    print(sort[-1])

runner_up(5, [2, 3, 6, 6, 5])
runner_up(4, [1, 2, 3, 4])
runner_up(2, [3, 5])
