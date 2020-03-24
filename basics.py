import datetime

print(datetime.datetime.now())

x = 10
y = "10"

# print(str(x), y)

student_grades = [9.1, 8.8, 7.5]
print(student_grades)
# print(dir(student_grades))


print(sum(student_grades) / len(student_grades))

student_grades_dict = {
    'Marry': 9.1,
    'Sim': 8.8,
    'John': 7.5
}
print(student_grades_dict)

monday_temp_tuple = (1, 2, 3)  # un-mutable
print(monday_temp_tuple)


def mean_list(some_list):
    return sum(some_list) / len(some_list)


print(mean_list(student_grades))

name = input("Enter name: ")
surname = input("Enter surname: ")

message = "Hello %s %s" % (name, surname)
message = f"Hello {name} {surname}"  # only with Python 3..
print(message)

# print("String  plus var %s" % student_grades)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for phone in phone_numbers.items():
    print(f"{phone[0]}: {phone[1]}")
    print("%s: %s" % (phone[0], phone[1]))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for phone in phone_numbers.values():
    print(phone.replace('+', '00'))



