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

## When to use/avoid recursion
### Use it
- When you can breakdown a problem into similar subproblems
- When we are fine with extra overhead (both time and space)
- Need a quick solution instead of an efficient one
- Small input into the function
- When traversing a tree
- When we use memoization in recursion
### Avoid it
- If time and space complexity matters for us
- Recursion uses more memory. If we use embedded memory like a phone application.
- Recursion can be slow

## 3 Steps to write recursion
- Factorials
- 4! = 4*3*2*1
- Recursive case - the flow
- Base case - the stopping criterion
- Unintentional case - the constraint