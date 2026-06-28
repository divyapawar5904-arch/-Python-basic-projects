def analyze_string(s):
    if s == "":
        print("Empty string is not allowed.")
        return

    print("Length:", len(s))
    print("Reverse:", s[::-1])

    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1

    print("Number of vowels:", count)

    print("\nCharacter | Positive Index | Negative Index")
    for i in range(len(s)):
        print(s[i], "\t", i, "\t\t", i - len(s))

text = input("Enter a string: ")
analyze_string(text)
