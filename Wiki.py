import wikipedia
import traceback

while True:    
    page = input("What wikipedia page do you want? \n")
    number = input("How many sentences do you want from said wikipedia page? \n")

    try:
        print(wikipedia.summary(page, sentences=int(number)))
        break
    
    except ValueError:
        print("I don't think that's a valid number (or even a number).....please try again \n")

    except wikipedia.exceptions.PageError:
        print("Sorry, that doesn't seem to be a real page or something else messed up.......")

    except:
        print("Couldn't anticipate error, but you should be able to try again anyway....")



