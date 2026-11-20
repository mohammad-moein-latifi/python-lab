print(
    "\n📝 Welcome to Text Analyzer! "
    "I'll analyze your text, count its characters and words, "
    "find the most frequent ones, and show their frequencies.\n"
)

text = input("Enter your text: ").strip()

if not text:
    print("Your text is empty. Please try again!")

else:
    normalized_text = text.lower()

    # Character count
    character_count = len(text)

    # Word count
    words = normalized_text.split()
    word_count = len(words)

    # Character frequencies
    characters = normalized_text.replace(" ", "")
    character_frequencies = {}

    for character in characters:
        character_frequencies[character] = characters.count(character)

    # Word frequencies
    word_frequencies = {}

    for word in words:
        word_frequencies[word] = words.count(word)

    # Most frequent character
    most_frequent_character = max(character_frequencies, key=character_frequencies.get)

    # Most frequent word
    most_frequent_word = max(word_frequencies, key=word_frequencies.get)

    # Display report
    print("\n========== TEXT ANALYSIS ==========")

    print(f"Total characters: {character_count}")
    print(f"Total words: {word_count}")

    print(
        f"Most frequent character: "
        f"{most_frequent_character} "
        f"({character_frequencies[most_frequent_character]} times)"
    )

    print(
        f"Most frequent word: "
        f"{most_frequent_word} "
        f"({word_frequencies[most_frequent_word]} times)"
    )

    print("\nCharacter Frequencies:")

    for character, count in character_frequencies.items():
        print(f"{character!r}: {count}")

    print("\nWord Frequencies:")

    for word, count in word_frequencies.items():
        print(f"{word}: {count}")

    print("\nThanks for using Text Analyzer!")
