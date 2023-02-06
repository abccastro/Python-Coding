"""
Create a program for birdwatchers that stores a list of birds along with a count of the
number of times each bird has been spotted.

Created by: Auradee Castro
"""

import pickle


def startBirdCounter():
    print("Bird Counter Program")
    print("Enter 'x' to exit")

    filename = "birds.bin"
    birds_record = readBirdsRecord(filename)

    if birds_record is not None:

        while True:
            input_name = input("Enter name of the bird: ").strip().lower()
            if input_name != "x":
                bird_count = birds_record.get(input_name, 0)
                birds_record[input_name] = bird_count + 1
                writeBirdsRecord(birds_record, filename)
            else:
                break

        print("\nName Count")
        print("=================================")

        birds_record = readBirdsRecord(filename)

        if len(birds_record) != 0:
            for bird in birds_record.items():
                print(str(bird[0]).ljust(25), str(bird[1]).rjust(5))
        else:
            print("No record found")


def readBirdsRecord(filename):
    try:
        with open(filename, "rb") as output_file:
            birds_record = pickle.load(output_file)
    except EOFError:
        birds_record = {}
    except FileNotFoundError:
        print("File not found:", filename)
        birds_record = None
    return birds_record


def writeBirdsRecord(birds_record, filename):
    with open(filename, "wb") as input_file:
        pickle.dump(birds_record, input_file)


if __name__ == "__main__":
    startBirdCounter()
