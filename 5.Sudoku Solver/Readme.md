# Challenge: Sudoku Solver
## Objective: 
Write a program to solve a given Sudoku puzzle.
  
## Instruction:
1. The input is a 9x9 grid representing a Sudoku puzzle, where empty cells are represented by 0.

2. The program should fill the empty cells with numbers from 1 to 9, following these rules:

   a. Each row must contain the numbers 1-9 without repetition.

   b. Each column must contain the numbers 1-9 without repetition.

   c. Each of the nine 3x3 sub-grids must contain the numbers 1-9 without repetition.

3. The program should return the solved Sudoku grid.

## Example input
```
[

[5, 3, 0, 0, 7, 0, 0, 0, 0],

[6, 0, 0, 1, 9, 5, 0, 0, 0],

[0, 9, 8, 0, 0, 0, 0, 6, 0],

[8, 0, 0, 0, 6, 0, 0, 0, 3],

[4, 0, 0, 8, 0, 3, 0, 0, 1],

[7, 0, 0, 0, 2, 0, 0, 0, 6],

[0, 6, 0, 0, 0, 0, 2, 8, 0],

[0, 0, 0, 4, 1, 9, 0, 0, 5],

[0, 0, 0, 0, 8, 0, 0, 7, 9]

]
```
## Example Output
```
[

[5, 3, 4, 6, 7, 8, 9, 1, 2],

[6, 7, 2, 1, 9, 5, 3, 4, 8],

[1, 9, 8, 3, 4, 2, 5, 6, 7],

[8, 5, 9, 7, 6, 1, 4, 2, 3],

[4, 2, 6, 8, 5, 3, 7, 9, 1],

[7, 1, 3, 9, 2, 4, 8, 5, 6],

[9, 6, 1, 5, 3, 7, 2, 8, 4],

[2, 8, 7, 4, 1, 9, 6, 3, 5],

[3, 4, 5, 2, 8, 6, 1, 7, 9]

]
```