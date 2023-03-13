# this py test the reference and copy
def try_to_change_list_contents(the_list):
    print('got', the_list)
    print('id1', id(the_list))
    the_list.append('four')
    print('id2', id(the_list))
    print('changed to', the_list)


outer_list = ['one', 'two', 'three']

print('before, outer_list =', outer_list, "id=", id(outer_list))
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)
