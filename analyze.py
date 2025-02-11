from random_username.generate import generate_username


# welcome user
def welcomeuser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you provide")

# Get user name 
def getUsername():
    userNamefromInput = input("\nTo begin, please enter your username:\n")
    
    

    
    if len(userNamefromInput) < 5 or not userNamefromInput.isidentifier():
        print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces and cannot start with a number")
        userNamefromInput = generate_username()[0]
        print("Assigning new username: " + userNamefromInput)

    return userNamefromInput

# greet user
def greetUser(name):
    print("Hello, " + name)

welcomeuser()
userName = getUsername()
greetUser(userName)