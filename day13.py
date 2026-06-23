#basic dataframe understanding

#1.head()
#csv file import from github
#import pandas as pd
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#print (df.head(-2))
#head 
#print(df.head())
# head  -> 2 rows data
#print (df.head(-2)) 
# head -> negative number 


#2. tail()
#csv file import from github
#import pandas as pd
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#df 
# tail used for last 5 rows data
#df.tail(2)
# tail in negative 
#df.tail(-1)

# 3. shape
#import pandas as pd 
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#df.shape # rows -> 5 and columns -> 3




# 4. info()
#import pandas as pd
#import numpy as np
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#df["salary"]=[100,200,300,np.nan,500]
#df.info()




# 5. rename()
#import pandas as pd
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#df.rename(columns={"name":"student_name"}, inplace=True)
# original variable df -> value same
#print(df)


#import pandas as pd
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#df.describe()
#print(df.describe())








import pandas as pd

# Data
data = {
    "emp id": [101, 102, 103, 104, 105, 106],
    "name": ["amit", "riya", "raj", "sara", "john", "neha"],
    "department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "experience": [2, 3, 5, 4, 1, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Head
print("\nFirst 3 Rows (head):")
print(df.head(3))

# Tail
print("\nLast 3 Rows (tail):")
print(df.tail(3))

# Shape
print("\nShape of DataFrame:")
print(df.shape)

# Info
print("\nDataFrame Info:")
print(df.info())

# Describe
print("\nDescribe:")
print(df.describe())

# Rename Columns
df.rename(columns={
    "emp id": "Employee_ID",
    "name": "Employee_Name",
    "department": "Department",
    "experience": "Experience"
}, inplace=True)

print("\nDataFrame After Rename:")
print(df)

# New Column Names
print("\nColumn Names:")
print(df.columns)


