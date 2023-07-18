class solution:
    def column_sum(self,array,row):
        n=len(array[0])
        b=[]
        for i in range (n):
            sum=0
            for j in range (row):
                sum+=array[j][i]
            b.append(sum)
        return b
a1=solution()
arr=[]
row =int(input())
for i in range (row):
    column=list(map(int,input().split()))
    arr.append(column)
print(a1.column_sum(arr,row))