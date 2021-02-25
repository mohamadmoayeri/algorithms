def limit(arr,min=None,max=None):

    min_check=lambda val:True if min is None else (val>=min)

    max_check=lambda val:True if max is None else (val<=max)

    return [val for val in arr if min_check(val) and max_check(val)]




print(limit([1,2,4,5,7,8,9,10],7))

print(limit([1,2,4,5,7,8,9,10],max=7,min=5))

print(limit([1,2,4,5,7,8,9,10],max=7))

