# Analysis of the 0-1 Knapsack Problem using Greedy and Dynamic Approaches

This repository contains a Jupyter notebook that analyzes the 0-1 Knapsack
Problem using two different algorithms: a greedy approach and a dynamic
programming approach. The notebook also provides a comparison between the two
approaches and discusses their advantages and disadvantages.

## What is the 0-1 Knapsack Problem?

The 0-1 Knapsack Problem is a classic optimization problem in computer science,
in which a set of items has to be packed into a knapsack with a limited
capacity, such that the total value of the items is maximized. Each item has a
weight and a value, and can only be packed once (hence the "0-1" constraint).

The problem can be stated as follows:

_Given a set of n items, each with a weight w_i and a value v_i, and a knapsack
of capacity W, find a subset of the items that maximizes the total value,
subject to the constraint that the total weight does not exceed the capacity._

## Greedy Approach

The greedy approach to the 0-1 Knapsack Problem consists of sorting the items by
their value-to-weight ratio (i.e., v_i / w_i), and then adding the items to the
knapsack in decreasing order of their ratio until the knapsack is full.

The advantage of the greedy approach is that it is simple and fast, with a time
complexity of O(n log n) due to the sorting step. However, the greedy approach
is not guaranteed to find the optimal solution, as it may leave some valuable
items out if their weight is too high.

## Dynamic Programming Approach

The dynamic programming approach to the 0-1 Knapsack Problem consists of
building a table that stores the maximum value that can be achieved for each
combination of items and capacities, and then backtracking to find the optimal
subset of items that achieves the maximum value.

The advantage of the dynamic programming approach is that it guarantees to find
the optimal solution, with a time complexity of O(nW) where n is the number of
items and W is the knapsack capacity. However, the dynamic programming approach
requires more memory and computational resources than the greedy approach.

## Conclusion

In this notebook, we analyzed the 0-1 Knapsack Problem using both a greedy
approach and a dynamic programming approach. We found that the greedy approach
is simple and fast, but may not find the optimal solution, while the dynamic
programming approach is guaranteed to find the optimal solution, but requires
more resources.

We hope this notebook helps you understand and appreciate the trade-offs between
different approaches to optimization problems. Feel free to use the code and
algorithms presented here in your own projects!
