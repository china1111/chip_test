a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
l = [sum([a[i][j] for i in range(len(a))])/len(a) for j in range(len(a[0]))]
# b = [1, 2,3 , 4, 5]
# l = sum(b)
print(l)