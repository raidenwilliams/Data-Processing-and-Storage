# World Bank of Pyhton 

## Getting started
### Requirements 
- base python installation

### Installation
- ```git clone https://github.com/raidenwilliams/Data-Processing-and-Storage.git```
- ```cd Data-Processing-and-Storage```

### Commands to run 
```python main.py```
- Follow further commands given in CLI
```
 ___________________________________
|                                   |
|      Commands are as follows      |
|___________________________________|
|                                   |
| Begin: b                          |
| Put: p                            |
| Get: g                            |
| Commit: c                         |
| Rollback: r                       |
| Transfer: t                       |
| Exit: e                           |
|___________________________________|
```

### Future Assignment Details 
For this mini project, I think that it would need to have proper test cases so students can run tests on the code and ensure it passes. This is the standard for most other coding projects but I think it would help ensure we are doing the correct operations. I think that if we are going to do the assignment as well it should be named something about banking or transactions to get this idea across that we are talking about cash transactions. I think that this could also be done by including a transaction function that could ensure a proper flow of beginning a transaction, putting values and committing them, then editing the values and returning the new values of each account. I tried to implement this for fun and thoroughly enjoyed coding this mini-project!


# Testing with expected outputs
```
 ___________________________________
|                                   |
|   Welcome to Python World Bank!   |
|___________________________________|

 ___________________________________
|                                   |
|      Commands are as follows      |
|___________________________________|
|                                   |
| Begin: b                          |
| Put: p                            |
| Get: g                            |
| Commit: c                         |
| Rollback: r                       |
| Transfer: t                       |
| Exit: e                           |
|___________________________________|

Input command:
g
Input key: a
-> Key a does not exist in db

Input command:
p
Input key: a
Input val: 5
-> No transaction in progress

Input command:
b
-> Transaction started

Input command:
p
Input key: a
Input val: 5
-> Put message: a 5

Input command:
g
Input key: a
-> Null, transaction in progress

Input command:
p
Input key: a
Input val: 6
-> Put message: a 6

Input command:
c
-> Transaction committed

Input command:
g
Input key: a
-> Get message: a 6

Input command:
c
-> No transaction in progress

Input command:
r
-> No transaction in progress

Input command:
g
Input key: b
-> Key b does not exist in db

Input command:
b
-> Transaction started

Input command:
p
Input key: b
Input val: 10
-> Put message: b 10

Input command:
r
-> Transaction rolled back

Input command:
g
Input key: b
-> Key b does not exist in db

```
