
student = {"name":"Jimmy", "age":35, "course":["History", "CompSci"]}
student["phone"] ="555-5555"
student.update({"name":"John", "age":36})
print(student.get("phone", "Not Found"))
#del student["age"]
print(student)

print(student.pop("course"))

print(student.items())

for key, value in student.items():
    print("Dict:", key, value)