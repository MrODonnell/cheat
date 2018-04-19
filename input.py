user_names = ["Tom", "Jane", "Jose"]
user_response = ''
user_name = ''
     
def validate(un, un_list):
    global user_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            user_name = list_item
            return False
        count += 1
    return True

while validate(user_response, user_names):
    user_response = input("What name would you like to use")

print("the user name is: " + user_response + " -- " + user_name)
print(user_names)
