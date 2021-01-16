def bubble_sort(numlist):
    N = len(numlist)
    
    for i in range(N-1):
        
        
        isChange = 0
        
        
        for j in range(N-i-1):
            
            if numlist[j]>numlist[j+1]:
                
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp
                
                isChange = 1
        
        if isChange == 0:
            break
            
list = [19,2,13,8,34,25,7]
bubble_sort(list)
print(list)
