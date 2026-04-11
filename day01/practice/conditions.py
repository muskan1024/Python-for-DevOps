# if-else conditions

env = input("Enter the environment: ")
print("User Environment is: ",env)

if env=="prod":
    print("Don't deploy on Friday")
elif env=="stg":
    print("Take backup and test well")
else:
    print("You can deploy anyday")