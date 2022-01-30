# Arrays

## What is an Array?
In computer science, an array is a data structure consisting of a collection of elements, each identified by at least one array index or key. An array is stored such that the position of each element can be computed from its index by a mathmatical formula.

## Why do we need an Array?
Storing collections of elements

## Types of Array
* One-dimensional: an array with a bunch of values having been declared with a single index
* Two-dimensional: an array with a bunch of values having been declared with a double index
* Three-dimensional: an array with a bunch of values having been declared with a triple index

## Arrays in Memory
* One-dimensional: located contiguously in memory
* Two-dimensional: represented as a one dimensional contiguous array
* Three-dimensional: represented as a one dimensional contiguous array

## Insertion
1. At [0] all elements need to shift to the right O(N)
2. At end of array O(1)
3. In the middle still O(N)

## Access
1. At an index O(1)

## Searching for an Element
1. Binary search O(logN) for sorted array
2. Looking at each element O(N)

## Deletion
1. O(N) if index is not last index
2. O(1) if last index

## One Dimensional
| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Creation  | O(1)            | O(N)             |
| Insertion | O(1) / O(N)     | O(1)             |
| Traverse  | O(N)            | O(1)             |
| Access    | O(1)            | O(1)             |
| Search    | O(N)            | O(1)             |
| Deletion  | O(1) / O(N)     | O(1)             |

## Two Dimensional
| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Creation  | O(1)            | O(N)             |
| Insertion | O(1) / O(MN)    | O(1)             |
| Traverse  | O(MN)           | O(1)             |
| Access    | O(1)            | O(1)             |
| Search    | O(MN)           | O(1)             |
| Deletion  | O(1) / O(MN)    | O(1)             |