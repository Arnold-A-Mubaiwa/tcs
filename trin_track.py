N = int(input('Enter number of trains :'))
trains = []
if 1 <= N <= 5.10**4 :
    for train in range(N):
        T, A, I = input('Train No | A.Time | S.Time :').split()
        if 1000 < int(T) < 10**8 and 0 <= int(A) <= 86400 and 0 < int(I) < 86400:
            trains.append([T,A,I])
    
    new_list = sorted(trains,key=lambda l:l[1])
    print(new_list)
    platfor=[]
    total =0
    count=[]
    F = input()
    f_index =0
    
    for current in new_list:
        if platfor:
            for values in platfor:
                total = int(current[1])+ int(current[2])
                if total > int(values[1]):
                    platfor.append([current[1],total])
                    count.append(1) 
                    if F == current[0]:
                        f_index = platfor.index(values)+1
                else:
                    index = platfor.index(values)
                    platfor.remove(values) 
                    platfor.insert(index,[current[1],total])
                    count[index] +=1 
                    if F == current[0]:
                        f_index = platfor.index(values)+1
        else:
            platfor.append([current[1],int(current[1])+ int(current[2])])
            if F == current[0]:
                f_index = 1
            count.append(1)
                
    print(count)            
    print(f_index)