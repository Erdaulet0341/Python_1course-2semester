def spy_game(nums):
    ok = False
    for i in range(len(nums)-1):
        if nums[i]==0:
            for j in range(i+1,len(nums)-1):
                if nums[j]==0:
                    for k in range(i+1, len(nums)-1):
                        if nums[k]==7:
                            ok = True
                            return ok
                            
    return ok

arr  = list(map(int, input().split()))

if spy_game(arr)==True:
    print("Yes")
else:
    print('No')
    