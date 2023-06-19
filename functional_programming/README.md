
The script was run on Windows 10 WSL2 Ubuntu 20.04 LTS.

## sequential_map function 
**input:** any number of functions and a container with some values. 

**output:** a list of results of sequentially applying the passed functions to the values in the container. 

## consensus_filter function 
**input:** any number of functions that return True or False and a container of some values.

**output:** a list of values that, when passed to all functions, return True.

## conditional_reduce function 

**input:** 2 functions, and a container of values. The first function takes 1 argument and returns True or False, the second takes 2 arguments and returns a value. 

**output:** one value.

## func_chain function
**input:** any number of functions. 

**output:** the function combining all passed in consecutive executions. 

## analog to the print function
In addition to what you want to print, you can specify the file, the delimiter and the line terminator.
>>>>>>> parent of 6c86b04 (Запрос на слияние #13 от LiliiaBgdnv/hw_OOP)
