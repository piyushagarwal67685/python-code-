import pandas as pd
#url = "https://raw.githubusercontent.com/piyushagarwal67685/python-code-/main/file2.json"
#df = pd.read_json(url)
#df .rename (columns={"marks":"student_marks"}, inplace=True)
#print(df)


#d = {
#    "name": ["piyush", "shivangi", "satyam", "priyanshu", "priyansh"],
#    "salary": [100, 200, 300, 400, 500] # 3 rows
#}
#df = pd.DataFrame(data=d)
#df["holidays"] = df ["salary"] / 100
#df["decrements"]  = [10,20,30,40,50]
# delete column
#df.drop("salary", axis=1, inplace=True)
#print(df)

d = {
    "name": ["piyush", "shivangi", "satyam"], # 3 rows 
    "salary": [100, 200, 300] # 3 rows
}
df = pd.DataFrame(data=d)
#print(df)

#print(df.loc[2,"name"])
#print(df.iloc[2,0])

#get single row data
#print(df.iloc[1])

#get single row using loc
#print(df.loc[1])

#get multi rows
#print(df.iloc[0:3])

#get multi rows using loc
#print(df.loc[0:2])

#sub data get 
#df1 = df.iloc[0:2,[0]] # rows -> 0 to 1 and column -> 0 | name
#print(df1)

#sub data get using loc
#df2 = df.loc[0:1,["name"]] # rows -> 0 to 1 and column -> name
#print(df2)



#import pandas as pd 

#data = {
#"emp_id": [101, 102, 103, 104, 105],
#"name": ["piyush", "shivangi", "satyam", "priyanshu", "priyansh"],
#"department": ["IT", "HR", "finace", "HR", "sales"],
#"salary": [50000, 45000, 60000, 55000, 48000],
#"experience": [5, 3, 7, 4, 2]
#}   

#df = pd.DataFrame(data) 

#print(df.loc[2,"experience"]) 
#print(df.iloc[3,1])

#get single row data
#print(df.iloc[0])

#get single row using loc
#print(df.loc[0])

#get multi rows
#print(df.iloc[0:3])

#get multi rows using loc
#print(df.loc[0:2])

#subdata get using iloc
#df1 = df.iloc[0:6[2]]
#print(df1)

#subdata get using loc
#df2 = df.loc[0:5,["salary"]]
#print(df2)


import pandas as pd

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"

df = pd.read_json(url)

# Filter 1
#print("English = 95")
#print(df[df["english"] == 95])

# Filter 2
#print("\nMaths < 60")
#print(df[df["maths"] < 60])

# Filter 3
#print("\nMaths < 60 and English > 80")
#print(df[(df["maths"] < 60) & (df["english"] > 80)])

#physics values less than and equal to 56
#print("\nPhysics <= 56")
#print(df[df["physics"] <= 56])

# maths 90 and english 90
print(df[(df["maths"] > 90) & (df["english"] > 90)])

#df.loc[0:2]
#print(df.iloc[0:2])
#print(df)

#gender -> male
#male_students = df[df["gender"] == "Male"]

#print(male_students)