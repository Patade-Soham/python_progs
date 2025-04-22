# Students appearing for different entrance exams
cet_students = {"Aman", "Bhavna", "Chirag", "Divya", "Esha"}
jee_students = {"Bhavna", "Farhan", "Divya", "Gautam", "Harshit"}
neet_students = {"Ishita", "Chirag", "Farhan", "Divya", "Kabir"}

# 1. Students appearing for at least one exam (Union)
all_students = cet_students.union(jee_students, neet_students)
print("Students appearing for at least one exam (CET/JEE/NEET):")
print(all_students)
print()

# 2. Students appearing for both CET and JEE (Intersection)
cet_and_jee = cet_students.intersection(jee_students)
print("Students appearing for both CET and JEE:")
print(cet_and_jee)
print()

# 3. Students appearing for CET but not JEE (Difference)
cet_not_jee = cet_students.difference(jee_students)
print("Students appearing for CET but not JEE:")
print(cet_not_jee)
print()

# 4. Students appearing for all three exams (Intersection of all three)
all_three_exams = cet_students.intersection(jee_students, neet_students)
print("Students appearing for CET, JEE, and NEET:")
print(all_three_exams)
print()

# 5. Students who are only appearing for NEET (not in CET or JEE)
only_neet = neet_students.difference(cet_students.union(jee_students))
print("Students appearing only for NEET:")
print(only_neet)
