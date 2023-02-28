"""
Create a program that do a basic sentiment analysis, search for a few keywords
to see how bias the customers are. Write your findings as a note using print

Submitted by: Auradee Castro
"""
import re
from colorama import Fore as fg, Back as bg, Style as ef, init

init(autoreset=True)

POSITIVE_KEYWORDS = ('calming', 'relaxing', 'relaxes', 'soothing', 'nice', 'great', 'good', 'perfect', 'ok',
                     'happy', 'best', 'gentle', 'love', 'loved', 'satisfied', 'comforting', 'help', 'helps',
                     'helpful', 'favorite', 'favourite', 'lasting', 'amazing', 'excellent', 'fantastic',
                     'recommend', 'pretty', 'reliable')
NEGATIVE_KEYWORDS = ('scam', 'disappointed', 'bad', 'dislike', 'worse', 'worst', 'angry', 'waste',
                     'awful', 'gross', 'avoid', 'dissatisfied', 'cheap', 'poor', 'poorest', 'trash',
                     'atrocious', 'nauseous', 'stinky', 'ugly', 'disgusting', 'weak', 'horrible',
                     'rotten', 'garbage', 'terrible', 'sucks', 'smelly', 'smells', 'weird', 'sour')

def startApplication():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                     Basic Sentiment Analysis                     +")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("The NOW Lavender Oil has a fairly good ratings from the customers with 4.4 out of 5 stars in Amazon website.")
    print("One-fifty (150) reviews were randomly picked for basic sentimental analysis")
    print("Link: https://www.amazon.ca/Now-Lavender-Oil-Liquid-30ml/dp/B00IZ7WSXM\n")

    line_list = readFile("Reviews.txt")

    word_list = []
    for line in line_list:
        line_arr = line.split(" ")
        word_list.extend(line_arr)

    word_list_no_stop_keywords = list(filter(removeStopKeywords, word_list))
    word_list_no_special_chars = list(map(removeSpecialCharacters, word_list_no_stop_keywords))
    filtered_word_list = list(filter(removeStopKeywords, word_list_no_special_chars))

    print(f"{fg.CYAN}{ef.BRIGHT}FILTERED WORDS (removed stop keywords and special characters): {len(filtered_word_list)}")
    print(", ".join(filtered_word_list), '\n')

    positive_word_list = list(filter(filterPostiveKeywords, filtered_word_list))
    negative_word_list = list(filter(filterNegativeKeywords, filtered_word_list))

    total_positive_words = len(positive_word_list)
    total_negative_words = len(negative_word_list)
    total_words_for_analysis = total_positive_words + total_negative_words

    print(f"{fg.CYAN}{ef.BRIGHT}Total number of positive words used in the reviews: {total_positive_words}")
    countWords(POSITIVE_KEYWORDS, filtered_word_list)
    print(f"{fg.CYAN}{ef.BRIGHT}Total number of negative words used in the reviews: {total_negative_words}")
    countWords(NEGATIVE_KEYWORDS, filtered_word_list)

    print()
    print(f"{ef.BRIGHT}Percentage of total number of keywords against the total words used by the customers in the review:")
    print(f"{fg.GREEN}{ef.BRIGHT}Positive: {round((len(POSITIVE_KEYWORDS) / total_positive_words) * 100, 2)}%")
    print(f"{fg.RED}{ef.BRIGHT}Negative: {round((len(NEGATIVE_KEYWORDS) / total_negative_words) * 100, 2)}%")

    print("\nBased on the number of keywords against the usage of the word in the reviews, we can see that people tend to use ")
    print(f"various harsh words when they don’t like the item, which is {round((len(NEGATIVE_KEYWORDS) / total_negative_words) * 100, 2)}%. "
          f"This is to exaggerate their dislike on the product.")
    print("e.g. disgusting, stinky, gross")

    print()
    print(f"{ef.BRIGHT}Percentage of total positive/negative words used in the reviews against the total number of words used for "
          "sentimental analysis:")
    print(f"{fg.GREEN}{ef.BRIGHT}Positive: {round((total_positive_words / total_words_for_analysis) * 100, 2)}%")
    print(f"{fg.RED}{ef.BRIGHT}Negative: {round((total_negative_words / total_words_for_analysis) * 100, 2)}%")
    print("\nBased on the number of words usage against the totality of the words for sentimental analysis (sum of positive and negative words),")
    print(f"it is evident that more customers which is {round((total_positive_words / total_words_for_analysis) * 100, 2)}% still love the product. Though some might ")
    print("exaggerate it (words like perfect, best and excellent), majority provided their honest opinions.")


def removeStopKeywords(word):
    stop_keywords = readFile("StopKeywords.txt")

    if word.lower() in stop_keywords:
        return False
    return True

def removeSpecialCharacters(word):
    special_chars = ('.', ',', '!', '?', "'", '"', '(', ')', ':')
    return re.sub(r"["+"".join(special_chars)+"]", '', word)

def filterPostiveKeywords(word):
    if word.lower() in POSITIVE_KEYWORDS:
        return True
    return False

def filterNegativeKeywords(word):
    if word.lower() in NEGATIVE_KEYWORDS:
        return True
    return False

def countWords(word_list, src_word_list):
    for word in word_list:
        print(f"{word}: {src_word_list.count(word)}", end=", ")
    print()

def readFile(filename):
    try:
        with open(filename, "r") as file:
            line_list = file.readlines()

        for idx, line in enumerate(line_list):
            line_list[idx] = line.replace("\n", "")
    except EOFError:
        line_list = []
    except Exception as err:
        print(f"{fg.RED}Unexpected error: {err}")
        line_list = None

    return line_list

if __name__ == "__main__":
    startApplication()
