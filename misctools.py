
def lists_to_dict(list1, list2):
    returner = {}
    for l1 in list1:
        for l2 in list2:
            returner[l1] = l2
            list2.remove(l2)
            break

def sprint(object):
    s = str(object)
    if s is not None:
        print(s)
    else:
        print("could not be converted to string")