def stack(lst, action, element=0):
    """
    A function for adding or removing in list to act as STACK

    Parameters
    ----------
    lst : list
        List of elements on which operations will be performed
    action : str
        Action of adding (add) or removing (remove) of element
    element : int
        This will be added to stack only if action is 'add'

    returns
    -------
    list : This returns the list after doing the operation of either Add/Remove action
    """
    assert isinstance(lst, list), "Passed object is not type of List"
    assert isinstance(action, str), "Passed action is not type of string"
    
    new_lst = list()

    if(action.lower() == 'add'):
        new_lst.append(element)
        new_lst = new_lst + lst
    elif(action.lower() =='remove'):
        if len(lst)>1:
            new_lst = lst[1:]
    else:
        raise Exception("Invalid Operstor - Allowed - add or remove")

    return new_lst


def queue(lst, action, element=0):
    """
    A function for adding or removing in list to act as QUEUE

    Parameters
    ----------
    lst : list
        List of elements on which operations will be performed
    action : str
        Action of adding (add) or removing (remove) of element
    element : int
        This will be added to queue only if action is 'add'

    returns
    -------
    list : This returns the list after doing the operation of either Add/Remove action
    """
    assert isinstance(lst, list), "Passed object is not type of List"
    assert isinstance(action, str), "Passed action is not type of string"
    
    new_lst = list()

    if(action.lower() == 'add'):
        new_lst = new_lst + lst
        new_lst.append(element)
    elif(action.lower() =='remove'):
        if len(lst)>1:
            new_lst = lst[1:]
    else:
        raise Exception("Invalid Operstor - Allowed - add or remove")

    return new_lst


new_list = [1,2,3,4]
print("Adding new element to the stack")
new_list=stack(new_list, 'add', 0)
print(new_list)

#print(stack(set([1,2,3,4]),'add', 0))

#new_list = []
print("Adding remove element from the stack")
new_list=stack(new_list, 'remove')
print(new_list)

#new_list = [1,2,3,4]
print("Adding new element to the queue")
new_list=queue(new_list, 'add', 0)
print(new_list)

#new_list = [1,2,3,4]
print("Adding remove element from the queue")
new_list=queue(new_list, 'remove')
print(new_list)