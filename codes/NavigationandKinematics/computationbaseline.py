dx_1 = float(input("DX 1st Obs: "))
dy_1 = float(input("DY 1st Obs: "))
dz_1 = float(input("DZ 1st Obs: "))

dx_2 = float(input("DX 2st Obs: "))
dy_2 = float(input("DY 2st Obs: "))
dz_2 = float(input("DZ 2st Obs: "))

liste1 = [dx_1, dy_1, dz_1]
liste2 = [dx_2, dy_2, dz_2]


dif_list = []
ppm_list = []
base = []
for i,j in zip(liste1, liste2):
    
    base.append(round((i+j)/2,4))
    
    difference = round(abs(i-j),4)
    dif_list.append(difference)
    
base_2 = 0
dif_2 = 0
for i,j in zip(base,dif_list):
    base_2 += i**2
    dif_2 += j**2
    
total_dif = round(dif_2**(1/2),4)
baseline = round(base_2**(1/2),3)
total_ppm = round(total_dif/ baseline * 1000000,3)


for i in dif_list:
    ppm = i / baseline * 1000000
    ppm_list.append(round(ppm,2))

print("Baseline: ", baseline)
print("Diferrence: ", total_dif)
print("Total PPM: ", total_ppm)
print("------------------------")
title = ["Dif (m): ", "  PPM: "]

for i, j in zip(dif_list, ppm_list):
    print(title[0],i,title[1],j)