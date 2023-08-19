def two_sums(nums,target):
    prev_maps={}
    for i,n in enumerate(nums):
        diff = target - n
        
        if diff in prev_maps:
            print(prev_maps)
            return[prev_maps[diff],i]
        prev_maps[n]=i
        

print(two_sums([1,2,3],4))
