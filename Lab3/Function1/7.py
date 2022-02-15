def has_33(nums):
    ok = True
    for i in range(len(nums)-1):
        if nums[i] ==3 and nums[i+1]==3:
            ok = True
            return ok
        else:
            ok = False
            
    return ok

arr  = list(map(int, input().split()))

if has_33(arr)==True:
    print("List contains 3 next 3")
else:
    print('List do NOT contains 3 next 3')
    