student = {"name": "Alice", "age": 25, "grade": "A"}

student["grade"]=26
student["major"] = "computer Science"
print(student)

del student["grade"]
print(student)

removed_major = student.pop("major")
print(removed_major)
print(student)