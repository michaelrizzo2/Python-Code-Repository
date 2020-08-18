dict_list=[{'fruit':"apple"},{'fruit':'banana'}]
dictionary_mapping={"fruit":"fruita"}
def dict_remapper(dict_list,dictionary_mapping):
    for index,entry in enumerate(dict_list):
        for key,value in entry.items():
            dict_list[index]={dictionary_mapping[key]:value}
    return dict_list
dict_list=dict_remapper(dict_list,dictionary_mapping)
print (f'dict list is {dict_list}')
