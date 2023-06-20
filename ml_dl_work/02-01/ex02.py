'''

[10,11,12,13]

'''

from sklearn.neighbors import KNeighborsClassifier

knr =  KNeighborsClassifier(n_neighbors=1)
data = [10,11,12,13,14,15]+[100,101,102,106,104,105]
data = [[item] for item in data]

knr.fit(([[10],[11],[12],[13],[14],[15]]), ['A','A','A','A','A','A'])

result =  knr.pedict([16])
print(result)