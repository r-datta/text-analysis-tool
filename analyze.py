# welcome user
def welcomeuser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you provide")

# Get user name 
def getUsername():
    usernNamefromInput = input("\nTo begin, please enter your username:\n")
    return usernNamefromInput



# greet user
def greetUser(name):
    print("Hello, " + name)

welcomeuser()
userName = getUsername()
greetUser(userName)