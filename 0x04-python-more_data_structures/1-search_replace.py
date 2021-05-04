#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    else:
        nlist=[]
        for i in my_list:
            if i==search:
                nlist.append(replace)
            else:
                nlist.append(i)
        return nlist
