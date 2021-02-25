arr=[1,1,45,1,2,2,3,6,7,8,54,2]


def top(arr):
    m=[]
    r=set()
    for i in arr:
        m.append(arr.count(i))
    max_arr=max(m)

    for j in arr:

        if arr.count(j)==max_arr:

            r.add(j)
        else:
            continue
    print(r)


    


top(arr)