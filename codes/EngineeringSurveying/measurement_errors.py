n = int(input("How many measurements were made? : "))
u = int(input("How many variables are there?      : "))

LList = []
print("__________________________________________________________________________")
print("Measurments")
print("__________________________________________________________________________")
for i in range(1,n+1):
    l = float(input("l%s : " %(i)))
    LList.append(l)
print("__________________________________________________________________________")
mostProbableValue = sum(LList) / n
print("Most probable value(X): ",round(mostProbableValue, 4))
print("__________________________________________________________________________")
vList = []
absoluteVList = []
rootMeanSquareVList = []
for i in range(0,n):
    v = mostProbableValue - LList[i]
    vList.append(v)
    absoluteVList.append(abs(v))
    rootMeanSquareVList.append(abs(v**2))
    print("V{} = {}".format((i+1), round(v, 4)))
print("__________________________________________________________________________")
print("[V]= ", round(sum(vList), 4))
print("__________________________________________________________________________")
print("Avarage Error/Second Way: ±", round(sum(absoluteVList) / n, 4))
print("__________________________________________________________________________")
m = (sum(rootMeanSquareVList) / (n-u))**(1/2)
print("RMSE(m): ±", round(m,5))
print("__________________________________________________________________________")
M = m / (n**(1/2))
print("RMSE of most probable value(M): ±", round(M, 5))
