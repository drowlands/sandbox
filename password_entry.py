'''
Daniel Rowlands Molpeceres
'''

min_length = int(10)
password = ""
done = False

while not done:
    password = input("Input a password: ")
    if len(password) < min_length:
        print("Password is too short. Please try again.")
    else:
        output = ""
        for step in range(len(password)):
            output += "*"
        print(output)
        done = True