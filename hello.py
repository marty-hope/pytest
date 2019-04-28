msg =  1 + 2
print(msg)
msg = "Hello World"
print(msg)

number = 0
print("true" if number != 0 else "false")
print("   ")

student_names = ["Michael", "Jessica", 0, 1]
print("present" if "Jessica" in student_names else "not")
print(" ")
for s in student_names:
    print("Student name is {0}".format(s))

for index in range(len(student_names)):
    print("Range operation returns index {0} and value {1}".format(index,student_names[index]))
try:
    for s in student_names:
        if(0 == s):
            print("Found 0")
            raise Exception("This is an error")
        print("testing {0}".format(s))
except Exception as e:
    print ("Exception occurred. {0}".format(e))


