from sklearn.neighbors import NearestCentroid
#database : gerbang logika AND
# x = data, Y = Target

x = [[0 , 0, 0], [0 , 3, 0], [0 , 0, 3], [0 , 3, 3], [3 , 3, 0], [3 , 0, 3], [3 , 3, 3], [1, 3, 3], [3 , 1, 3], [1, 1, 1]]
y = [0,0,0,3,3,3,1,1,3,0]

# Training and Classify
clf = NearestCentroid()
clf = clf.fit(x,y)

#prediksi
print ("logika AND Metode Neighbour")
print ("Logika = Prediksi")
print ("1 1 3  = ", clf.predict([[1,1,3]]))
print ("3 1 2  = ", clf.predict([[3,1,2]]))
print ("2 0 1  = ", clf.predict([[2,0,1]]))
print ("3 0 2  = ", clf.predict([[3,0,2]]))
print ("0 0 3  = ", clf.predict([[0,0,3]]))
print ("2 1 2  = ", clf.predict([[2,1,2]]))
print ("1 4 3  = ", clf.predict([[1,4,5]]))
print ("2 2 5  = ", clf.predict([[2,2,5]]))
print ("1 3 6  = ", clf.predict([[1,3,6]]))
