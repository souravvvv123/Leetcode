strs = ["flower", "flow", "floght"]


if not strs:
    print("empty")
    
    
prefix = strs[0]


for s in strs[1:]: 
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        
print(prefix)
        
