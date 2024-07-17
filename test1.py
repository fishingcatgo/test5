

a =[]
b=[1,2]
c=['1']

if a :
    print('a')

if b :
    print('b')

if c :
    print('c')

# grep -rn "领导人" ./ 

batch=[i for i in range(100)]
print(batch)

# for key in batch

def split_list_by_batch_size(lst, batch_size):
    return [lst[i:i + batch_size] for i in range(0, len(lst), batch_size)]

# print(split_list_by_batch_size(batch,10))

batch_size=9
for key,bat in enumerate([batch[i:i + batch_size] for i in range(0, len(batch), batch_size)]):
    print('标记：',key*batch_size)
    print(f'第{key}个',bat)


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