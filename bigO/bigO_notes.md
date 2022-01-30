# Big O Notation Notes

## Big O, Big Theta and Big Omega
- Big O: it is a complexity that is going to be less or equal to the worst case
- Big Omega: it is a complexity that is going to be at least more than the best case
- Big Theta: it is a complexity that is within bounds of the worst and the best cases

| Complexity | Name | Sammple | 
| ------ | --------- | --------- |
| O(1)   | Constant | Accessing a specific element in an array |
| O(N)   | Linear   | Loop through an array of elements |
| O(LogN)| Logarithmic | Find an element in a sorted array |
| O(N^2) | Quadratic | Looking at every index in an array twice |
| O(2^N) | Exponential | Double recursion in Fibonnaci |

| # | Description | Complexity | 
| ------ | --------- | --------- |
| Rule 1 | Any assignment statements and if statements that are executed once regardless of the size of the problem | O(1) |
| Rule 2 | A simple "for" loop from 0 to n (with no internal loops) | O(N) |
| Rule 3 | A nested loop of the same type takes quadratic time complexity | O(N^2) |
| Rule 4 | A loop, in which the controlling parameter is dividd by two at each step | O(logN) |
| Rule 5 | When dealing with multiple statements just add them up | |

