
##List
course = ["Math", "Military", "Science", "History"]

print(len(course))
print(course[-1])
print(course[0:2])

course.append("Art")

print(course)

for item in course:
    print(item)

for item in enumerate(course, start = 1):
    print(item)

course_str = " - ".join(course)
print(course_str)

newlist = course_str.split("-")
print(newlist)
### Tuple

list1 = ["Math", "Military", "Science", "History"]
list2 = list1

list2[1] = "Language"
print(list1)
print(list2)

### need tuple to keep original list

tuple1 = ("Math", "Military", "Science", "History")
tuple2 = tuple1
#tuple2[1] = "Language"
print(tuple1)
print(tuple2)

### set with no order, and combine same
set1 = {"Math", "Military", "Science", "History", "Math"}
set2 = {"Sport", "Art", "Calculus", "Math"}

print(set1)

print(set2.union(set1))
print(set2.intersection(set1))




