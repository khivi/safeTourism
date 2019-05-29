import pandas as pd 

data = pd.read_csv("/mnt/h/workSpace/news-project/wire_2018.csv") 
saved_column = data.title
print(len(saved_column))
print (type(saved_column[1]))
fp = open('politics.txt', 'w')
for i in range(len(saved_column)):
    data = saved_column[i].encode('ascii', 'ignore').decode('ascii')
    fp.write(data + "\n")
fp.close()
