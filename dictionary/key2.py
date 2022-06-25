import csv

persondict = {
    "Name": input("What is your name? "),
    "Age": input("What is your age? "),
    "Race": input("What is your race? "),
    "Gender": input("What is your gender? "),
    "friend or foe": input("are you friend or foe? "),
    "pokemon": input("who is your favorite pokemon? ")
}

keys = persondict.keys()
filename = "dictionary.csv"

with open(filename, "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = keys)

    writer.writeheader()

    writer.writerow(persondict)