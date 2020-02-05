import random as r

### Implementation ###
"""
Solution of the problem implemented as two different version, but used the first version which is iterative one.
"""
def shared_tasks(P, Q):
    R = []
    for task_P in P:                                # Iterate over all tasks in P bag
        for task_Q in Q:                            # Iterate over all tasks in Q bag for each task in P bag
            if task_Q == task_P:                    # Compare each task in Q bag with current task in P bag
                R.append(Q.pop(Q.index(task_Q)))    # If two tasks are equal then remove it from Q bag
                break                               # in order not to compare again and add it shared tasks bag of R
    return R

def shared_tasks_v2(P, Q):
    return [Q.pop(Q.index(task_Q)) for task_P in P for task_Q in Q if task_Q == task_P]

### Test Cases ###

print("Test Case 1")

P = ['V','Y','X','Y','U','V','W','W']
Q = ['Y','V','X','U','U','V']

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)
R = shared_tasks(P,Q)
print("Shared Tasks Bag R\t: ",R)

print("Test Case 2")

L_MIN = 5
L_MAX = 10

T = 'UVWXY'
P = [r.choice(T) for i in range(r.randint(L_MIN, L_MAX))]
Q = [r.choice(T) for i in range(r.randint(L_MIN, L_MAX))]

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)
R = shared_tasks(P,Q)
print("Shared Tasks Bag R\t: ",R)


print("Test Case 3")

L_MIN = 5
L_MAX = 10

T = 'MNTUVXYZ'
P = [r.choice(T) for i in range(r.randint(L_MIN, L_MAX))]
Q = [r.choice(T) for i in range(r.randint(L_MIN, L_MAX))]

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)
R = shared_tasks(P,Q)
print("Shared Tasks Bag R\t: ",R)

