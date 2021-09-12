class sort1:
    def bubleSort(l:list):
        flag=1
        for i in range(len(l)-1):
            if flag==1:
                flag=0
                for j in range(len(l)-1):
                    if l[j]>l[j+1]:
                        l[j],l[j+1]=l[j+1],l[j]
                        flag=1
            else:
                return l

    a=bubleSort([1,10,35,61,89,36,55])
    print(a)
