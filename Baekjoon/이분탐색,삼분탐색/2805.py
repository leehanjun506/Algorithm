n,m = map(int,input().split())
tree = list(map(int,input().split()))

def get_tree(tree,mid):
    sum = 0
    for i in range(len(tree)):
        if tree[i]-mid<0:
           continue
        else:
            sum+= (tree[i]-mid) 
    return sum
start = 0
end = max(tree)
while start<=end:
    mid = (start+end)//2
    if get_tree(tree,mid)>=m:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)