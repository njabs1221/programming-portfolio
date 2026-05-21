# Sparse Matrix Builder

Builds a full matrix from sparse coordinate input.

## Input format

```text
rows columns
number_of_entries
row column value
row column value
...
```

## Concepts used

- 2D vectors
- nested loops
- coordinate validation
- formatted output

## Build and run

```bash
g++ -std=c++17 main.cpp -o sparse-matrix-builder
./sparse-matrix-builder
```
