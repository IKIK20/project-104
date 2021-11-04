import csv
from collections import Counter

with open('Weight.csv', newline= '') as f:
    reader = csv.reader(f)
    file_data= list (reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

data=Counter(new_data)

modedata={
    "95-105": 0,
    "105-115": 0,
    "115-125": 0,
    "125-135": 0,
    "135-145": 0,
    "145-155": 0,
    "155-165": 0,
    "165-175": 0,
    "175-185": 0,
}

for  weight, occurence in data.items():
    if 95<float(weight)<105:
        modedata["95-105"]+= occurence
    elif 105<float(weight)<115:
        modedata["105-115"]+= occurence
    elif 115<float(weight)<125:
        modedata["115-125"]+= occurence
    elif 125<float(weight)<135:
        modedata["125-135"]+= occurence
    elif 135<float(weight)<145:
        modedata["135-145"]+= occurence
    elif 145<float(weight)<155:
        modedata["145-155"]+= occurence
    elif 155<float(weight)<165:
        modedata["155-165"]+= occurence
    elif 165<float(weight)<175:
        modedata["165-175"]+= occurence
    elif 175<float(weight)<185:
        modedata["175-185"]+= occurence

modeRange, modeOccurence= 0,0
for range,occurence in modedata.items():
    if occurence>modeOccurence:
        modeRange, modeOccurence=[int(range.split("-")[0]), int(range.split("-")[1])],occurence

mode= float((modeRange[0]+modeRange[1])/2)

print(mode)