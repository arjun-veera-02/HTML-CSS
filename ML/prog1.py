import csv
h=['0' for i in range(6)]
with open("D:/veera/ML/training.csv")as f:
    data=csv.reader(f)
    data=list(data)
    print("Positive examples are:")
    for i in data:
        if len(i)==0:
            continue
        if i[-1]=="positive":
            print(i)
    print("\n Steps to find - S:")
    for i in data:
        if len(i)==0:
            continue
        if i[-1]=="positive":
            for j in range(6):
                if h[j]=='0':
                    h[j]=i[j]
                elif h[j] != i[j]:
                    h[j]='?'
                    print(h)
print("\n Final specific hypothesis :\n",h)

    