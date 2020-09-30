a= list(map(int, input().split()))
maxx=max(a)
minn=min(a)
maxi=a.index(maxx)
mini=a.index(minn)
a[maxi]=minn
a[mini]=maxx
print(a)
