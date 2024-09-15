def prod(nums):
    prod =1
    
    for product in nums:
        prod = prod * product 
     
     
    ans=[]
    for j in nums:
        ans = prod // j
        print(ans)
        
    
nums=[1,2,3,4]

prod(nums)
