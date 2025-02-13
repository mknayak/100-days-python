student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
total_score=0

for score in student_scores:
    total_score+=score

print(f"Total Score using loop:{total_score}")
#using built-in function
print(f"Total Score using built in function:{sum(student_scores)}")

max_score=0
for score in student_scores:
    if max_score<score:
        max_score=score

print(f"Max Score using loop:{max_score}")
#using built-in function
print(f"Max Score using built in function:{max(student_scores)}")
