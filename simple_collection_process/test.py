# li=[
#     {'Name': 'Akshay','Lastname': 'Gawali', 'Age':'27'},
#     {'Name': 'Yuvraj','Lastname':'Kadam', 'Age': '25'}
#     ]

li=[
    [ 'Akshay','Gawali',27],
    [ 'Yuvraj','Kadam',25]
    ]

import csv
import  pandas as pd
df = pd.DataFrame(li, columns=["Name", "LName", "Age"])
df.to_csv("li.csv", index=False)

# with open('test.csv', 'wb') as outcsv :
#     w = csv.writer(outcsv, lineterminator='\n')
#     for l in li:
#         w.writerow( l)




