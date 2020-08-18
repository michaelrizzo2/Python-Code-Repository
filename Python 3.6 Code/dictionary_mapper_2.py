dict_list=[{'fruit':"apple"},{'fruit':'banana'}]

dictionary_mapping={"fruit":"fruita"}

dict_remapper=lambda dict_list,dictionary_mapping:[{dictionary_mapping[key]:value} for index,entry in enumerate(dict_list) for key,value in entry.items()]

dict_list=dict_remapper(dict_list,dictionary_mapping)

print (f'dict list is {dict_list}')

pass
