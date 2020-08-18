sum_reducer=lambda acc,x:acc+x
acc=0
for i in range(1,5):
    acc=sum_reducer(acc,i)
    print (f'sum is {acc}')
