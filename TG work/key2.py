import csv

persondict = {
    "Name": input("What is your name? "),
    "Age": input("What is your age? "),
    "Race": input("What is your race? "),
    "Gender": input("What is your gender? "),
    "friend or foe": input("are you friend or foe? "),
}
def listdict():
    for key in persondict:
        print((key),":", persondict[key])

listdict()