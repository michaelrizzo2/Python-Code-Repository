list_to_check=["",0.2,"Yes","No",None]
def my_truth_checker(list_to_check):
    for object in list_to_check:
        if object in ["",None]:
            print(f'object {object} is not truthful')
        else:
            print(f'object {object} is truthful')
my_truth_checker(list_to_check)
