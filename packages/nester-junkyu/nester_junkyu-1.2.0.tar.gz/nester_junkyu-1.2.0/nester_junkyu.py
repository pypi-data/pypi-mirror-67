""" this file is a nester.py module and provide print_list function.
    it print all elements when input contains list recursively
    it is from head first python book"""
movies = ['123', ['junkyu', 'hyeyoung'], '345', ['123456', ['567', '456', '345']]]

def print_list(l, nest=False, level = 0):
    """
        input:
            l - no matter when it is single instance or list
            level - number of tabs placed before print item
    """
    for each_item in l:        
        if isinstance(each_item, list):
            print_list(each_item, nest, level + 1)
        else:
            if nest:
                for i in range(level):
                    print("\t", end="")
            print(each_item)
