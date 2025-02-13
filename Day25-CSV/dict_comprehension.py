
student_dict={
    "student":["Alice","Angela","Jacob"],
    "score":[89,98,99]
}
print(student_dict)

import  pandas

student_df=pandas.DataFrame(student_dict)
print(student_df)


for (index,row) in student_df.iterrows():
    print(index)

for (index,row) in student_df.iterrows():
    print(row.student)