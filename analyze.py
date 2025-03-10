from random_username.generate import generate_username
import nltk 
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
wordLemmatizer = WordNetLemmatizer()
import re 




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

# extract sectences from raw text body
def tokenizeSentences(rawText):
    return sent_tokenize(rawText)

# extract words from list of sentences
def tokenizeWords(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words 

# get the key sentences based on search pattern of key words
def extractKeySentences(sentences):
    matchedSentences = []
    for sentence in sentences:
        # if sentences matches desired pattern, add to matchedSentences
        if re.search("[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss", sentence.lower()):
            matchedSentences.append(sentence)
    return matchedSentences

# Get the average words per sentence, excluding punctuation
def getWordsPerSentence(sentences):
    numSentences = len(sentences)
    if numSentences == 0:
        return 0
    totalWords = 0
    for sentence in sentences:
        totalWords += len(sentence.split(" "))
    return totalWords / numSentences

# Filter raw tokenized words list to only include valid english words
def cleanseWordList(words):
    cleansedWords = []
    invalidWordPattern = "[^a-zA-Z-+]"
    for word in words:
        cleansedWord = word.replace(".", "").lower()
        if (not re.search(invalidWordPattern, cleansedWord)) and len(cleansedWord) > 1:
            cleansedWords.append(wordLemmatizer.lemmatize(cleansedWord))

    return cleansedWords

# get user details
# welcomeUser()
# userName = getUsername()
# greetUser(userName)

# extract and tokenize text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)


# get analytics 
stockSearchPattern = "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences)
wordsPerSentence = getWordsPerSentence(articleSentences)

# Get Word Analytics
articleWordsCleansed = cleanseWordList(articleWords)


# print for testing
print("GOT:")
print(articleWordsCleansed)