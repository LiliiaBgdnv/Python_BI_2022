import sys
#Task 1
def sequential_map(*args):
    # Unpack all the arguments, write the functions to a list, and write the last argument as a container.
    *func_lst, conteiner = [*args]
    for func in func_lst:
        # Overwrite to the container the result of the function applied to each element.
        conteiner = map(func, conteiner)
    return list(conteiner)

#Task 2
def consensus_filter(*args):
    # Unpack all the arguments, write the functions to a list, and write the last argument as a container.
    *func_lst, conteiner = [*args]
    for func in func_lst:
        conteiner =  filter(func, conteiner)
    return conteiner

#Task 3
def conditional_reduce(*args):
    # Unpack all the arguments, write the functions to a list, and write the last argument as a container
    *func_lst, conteiner = [*args]
    # Write the first number in first_element, and all the others in *elements_list (which return True in the first function)
    first_element, *elements_list = list(filter(func_lst[0], conteiner))
    for elem in elements_list:
        first_element = func_lst[1](first_element, elem)
    return first_element

#Task 4
def func_chain(*args):
    def pain(x):
        for func in args:
          x = func(x)
        return x
    return pain
   
#Task 5 ()   
def my_print(*args, sep=' ', end='\n', file=sys.stdout):
    if file == None:
        sys.stdout.write(f'{sep.join("{}".format(elem) for elem in args)}{end}')
    else:
        f = open(file, 'w')
        f.write(f'{sep.join("{}".format(elem) for elem in args)}{end}')
        f.close()
