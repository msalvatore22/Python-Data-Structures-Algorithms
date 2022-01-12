# Recursion Notes

## What is recursion?
- Recursion is a way of solving a problem by having a function call itself
- Performing the same operation multiple times with different inputs
- In every step we try smaller inputs to make the problem smaller
- A base condition is needed to stop the recursion, or else infinite loop will occur
- Ussually and be solved in an iterative way as well

## Why do we need recursion?
- Recursive thinking is important in programming and it helps you break down big problems into smaller ones
- Need to be able to divide problem into similar sub-problems
- Trees and graphs
- Interview questions
- Used in many algorithms (divide and conquer, greedy and dynamic programing)

## How recursion works
- A method calls itself
- Exit from infinite loop
- Call stack, computer needs to go back and call the function

| Points | Recursion | Iteration |    |   
| ------ | --------- | --------- | -- |
| Space Efficiency | No | Yes | No stack memory for iteration |
| Time efficient   | No | Yes | Recusion needs more time for pop and push elements to stack memory which makes recusion less time efficient |
| Easy to code     | Yes | No | We use recursion especially in the cases we know a problem can be divided into similar sub problems |