from functions import get_json_from_string, get_json_age_squared

initial_string =  '{ "Name":"Dennis", "Class":"Intermediate", "Age":9 }'

print("\Initial string: ",initial_string)

python_obj = get_json_from_string(initial_string)

assert python_obj["Name"] == "Dennis"
print("\nName: ",python_obj["Name"])
assert python_obj["Class"] == "Intermediate"
print("Class: ",python_obj["Class"])
assert python_obj["Age"] == 9
print("Age: ",python_obj["Age"]) 

python_obj = get_json_age_squared(initial_string)

assert python_obj["Name"] == "Dennis"
print("\nName: ",python_obj["Name"])
assert python_obj["Class"] == "Intermediate"
print("Class: ",python_obj["Class"])
assert python_obj["Age"] == 81
print("Age: ",python_obj["Age"]) 