import math

try:
    sentence = input("Enter a sentence: ")

    words = sentence.split()
    unique_words = sorted(set(words))

    print("Unique Words:")
    for word in unique_words:
        print(word)

    total = len(unique_words)
    print("Total Unique Words:", total)
    print("Power of 2:", math.pow(total, 2))

except Exception as e:
    print("Error:", e)
