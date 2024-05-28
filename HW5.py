immutable_var = (1, 2, 3, True, 'ban')
print(immutable_var)
# immutable_var[3] = 4   -->  'tuple' object does not support item assignment
mutable_list = [1, 2, 3, True, 'ban']
print(mutable_list)
mutable_list[0] = 2
mutable_list[1] = 3
mutable_list[2] = 4
mutable_list[3] = False
mutable_list[4] = 'unbanned'
print(mutable_list)
