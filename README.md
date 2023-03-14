### Task 1

A `MyDict` class that completely replicates the behavior of a regular dictionary, but we get both keys and values when iterating.
### Task 2

The `iter_append` function that "adds" a new element to the end of the iterator, returning an iterator that includes the original elements and the new element. 
### Task 3

Two classes `MyString` and `MySet`, which are descendants of `str` and `set`, but also carry additional methods. The methods return an instance of 
the current class, not the parent class.

### Task 4

`Switch_privacy` decorator:

> - Makes all public methods of the class private
> - Makes all private methods of the class public
> - Dunder methods and protected methods remain unchanged

### Task 5

`OpenFasta` context manager.

The object works like normal files in python.
When iterating over the object, we will not need to get a string from a file, but a special FastaRecord object. 
It stores the sequence information in itself. The `read_record` and `read_records` methods are written, which in sense correspond to `readline()`
and `readlines()` in regular files, but they should output `FastaRecord` object(s) instead of strings
The constructor takes one argument-the path to the file.
The class must be an efficient use of memory, with the expectation of working with very large files
FastaRecord object. 

This is a class with three fields:

`seq` - sequence

`id_` - sequence ID (this is what is in the fasta file in the string beginning with > before the first space. *For example, >GTD326487.1 Species anonymous 24 chromosome)*

`description` - what is left after the ID *For example, >GTD326487.1 Species anonymous 24 chromosome*.

### Task 6

A code that allows you to get all possible (non-unique) genotypes when crossing two organisms.
For example, all possible outcomes of crossing "Aabb" and "Aabb" (non-unique) are

> AAbb
> 
> AAbb
> 
> AAbb
> 
> AAbb
> 
> Aabb
> 
> Aabb
> 
> Aabb
> 
> Aabb
> 
> Aabb
> 
> Aabb
> 
> Aabb
> 
> Aabb
> 
> aabb
> 
> aabb
> 
> aabb
> 
> aabb

2. A function which calculates the probability of a certain genotype (its expected proportion in the offspring). 

3. A code outputting all unique genotypes in crosses 'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн' and 'АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН' which contain the following combination of 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛл' alleles

4. A code which calculates the probability of the genotype 'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн' in the cross between 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн' and 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн'

![image](https://user-images.githubusercontent.com/109213422/224983996-b4e1b5b1-3205-4fb1-8abc-9bd2bfb83968.png)
