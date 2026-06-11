# import package pandas
import pandas as pd

#ld -> method Series
#example 1 
l = [65, 78, 90]
df = pd.Series(data=l)

#print(df)

#exampel 2
#d = {"Name": "Piyush", "Age": "19", "Roll-no": 73}
#df = pd.Series(data=d, index=["Name", "Age", "Roll-no"])
#print(df)

import pandas as pd

#d = {
 #   "name": ["Shivangi", "Piyush", "Yashshvi", "Ishita", "Aarav"],
  #  "roll-no": [20, 19, 28, 26, 24]
#}
#df = pd.DataFrame(data=d)
#print(df)

#csv file imoort from github
import pandas as pd

url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2%20-%20Sheet1.csv"

df = pd.read_csv(url)

print(df)