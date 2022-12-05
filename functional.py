import sys
def sequential_map(*args):
    *func_lst, conteiner = [*args] #unpack all the arguments, write the functions to a list, and write the last argument as a container
    for func in func_lst:
        conteiner = func(conteiner) #overwrite to the container the result of the function applied to each element
    return [x for x in conteiner]
def consensus_filter(*args):
    *func_lst, conteiner = [*args] #unpack all the arguments, write the functions to a list, and write the last argument as a container
    for func in func_lst:
        conteiner =  list(filter(func, conteiner))
    return conteiner
def conditional_reduce(*args):
    *func_lst, conteiner = [*args] #unpack all the arguments, write the functions to a list, and write the last argument as a container
    first_element, *elements_list = list(filter(func_lst[0], conteiner)) #write the first number in first_element, and all the others in *elements_list (which return True in the first function)
    for elem in elements_list:
        first_element = func_lst[1](first_element, elem)
    return first_element
def func_chain(*args):
    def pain(x):
        for func in args:
          result = func(result)
        return result
    return pain
def my_print(*args, sep=' ', end='\n', file='o.txt'):
    if file == None:
        sys.stdout.write(f'{sep.join("{}".format(elem) for elem in args)}{end}')
    else:
        f = open(file, 'w')
        f.write(f'{sep.join("{}".format(elem) for elem in args)}{end}')
        f.close()
