# write your code here
with open("users.json") as f:
    print(len(json.load(f)["users"]))
