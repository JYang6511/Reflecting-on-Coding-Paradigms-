'''
Implement a function that will flatten and sort an array of integers in ascending order, 
and which adheres to a functional programming paradigm.

Remember, when writing in a functional style:
Keep variables immutable
Write only pure functions
Remember, functions may be higher order
Once a functional solution to this problem has been implemented, answer the following questions.

How does this solution ensure data immutability?

This solution does not ensure data immutability because it modifies the original input array. 

Is this solution a pure function? Why or why not?

No, this solution is not a pure function. A pure function should not have side effects or modify external state. 
However, this function modifies the state of the arr list as well as the input array


Is this solution a higher order function? Why or why not?

No, this solution is not a higher-order function. 
A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result. 

Would it have been easier to solve this problem using a different programming style?

maybe a recursion way

Why in particular is functional programming a helpful paradigm when solving this problem?

Functional programming can be helpful when solving this problem because it emphasizes immutable data and avoids side effects
'''


def sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

list = [[11, 4, 44], [222, 5, 2]]
sorted_list = sort(list)
print(sorted_list)