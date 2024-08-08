# Data Structure Implementations

This repository contains implementations of basic data structures in Python.

## Data Structures Implemented

### 1. Linked List
A Linked List is a linear data structure where each element is a separate object, called a node. Each node contains data and a reference (or link) to the next node in the sequence. The time complexity for searching is O(n), inserting is O(1) if the node reference is known (O(n) if searching is needed), and deleting is O(1) if the node reference is known (O(n) if searching is needed).

### 2. Queue
A Queue is a linear data structure that follows the First In, First Out (FIFO) principle. Elements are added at the rear and removed from the front. The time complexity for enqueue and dequeue are O(1).

### 3. Stack
A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle. Elements are added and removed from the top of the stack. The time complexity for push and pop operations is O(1).

### 4. Hash Table
A Hash Table is a data structure that maps keys to values using a hash function. It allows for fast data retrieval through an index-like lookup, with the average time complexity for search, insert, and delete operations being O(1). 

### 5. Binary Search
Binary Search is an efficient algorithm for finding a target value within a sorted array. It repeatedly divides the search interval in half, comparing the target value to the middle element. If they match, the search ends; otherwise, the search continues in left side or right side, with a time complexity of O(log n) space complexity for iterative method is O(1) while space complexity for recursive method is O(logn).
