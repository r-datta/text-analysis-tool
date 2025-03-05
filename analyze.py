from random_username.generate import generate_username

# welcome user
def welcomeuser():
    print("\nWelcome to the text analysis tool, I will mine and analyze a body of text from a file you provide")

# Get user name 
def getUsername():

    maxAttempts = 3
    attempts = 0

    while attempts < maxAttempts:
        # print message prompting user to input their name
        inputPrompt = ""
        if attempts == 0:
            inputPrompt = "\nTo begin, please enter your username:\n"
        else: 
            inputPrompt = "\nPlease try again:\n"
        userNamefromInput = input(inputPrompt)

#validate username
        if len(userNamefromInput) < 5 or not userNamefromInput.isidentifier():
             print("Your username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9), have no spaces and cannot start with a number")
        else: 
            return userNamefromInput
        attempts += 1
    
    print("\nExhausted all " + str(maxAttempts) + " attempts, assigning new username: ")
    return generate_username()[0]
    
    

    
    
        
        

# greet user
def greetUser(name):
    print("Hello, " + name)

# Get text from file
def getArticleText():
    f = open("files/article.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "")


welcomeuser()
userName = getUsername()
greetUser(userName)

articleTextRaw = getArticleText()
print("GOT:")
print(articleTextRaw)