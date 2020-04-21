import numpy as np

r=np.load('result.npy')
#print(r)

cat=np.load('categories.npy')
#print(cat)

# arr = np.array([11, 12, 13, 14, 15, 16, 17, 15, 11, 12, 14, 15, 16, 17])
# max=np.where(r == np.amax(r))
# print(max)
# index=np.where(r=np.amax(r))
# print(index)

m=np.amax(r)
print(m)

index=np.where(r==m)
print(index)

print(cat[index[1]])
