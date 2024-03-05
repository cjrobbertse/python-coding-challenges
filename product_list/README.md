Sure, here's a Python coding challenge suitable for a Software Engineer II level:

**Problem Statement:**

You are given a list of integers. Your task is to write a Python function that takes this list as an argument and returns a new list where each element is the product of all the numbers in the original list except for the number at that index. You cannot use division in your solution.

For example, given the list `[1, 2, 3, 4, 5]`, your function should return `[120, 60, 40, 30, 24]`.

**Function Signature:**

```python
def product_list(input_list: List[int]) -> List[int]:
    pass
```

**Constraints:**

- The input list will have at least two integers and at most 1000.
- Each integer in the list will be a positive integer and will not exceed 1000.

This problem tests the candidate's ability to work with lists and understand the concept of space-time tradeoff in algorithms. It also tests the candidate's ability to come up with a solution that does not involve division, which is a common approach to this problem.