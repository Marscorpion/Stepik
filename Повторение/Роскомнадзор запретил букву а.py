def song_algorithm(word):
    # Russian alphabet without the letter 'ё'
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    # Concatenate the input word with the fixed phrase
    phrase = word + ' запретил букву '
    # Start with the full alphabet
    allowed_letters = alphabet
    # Initialize the list to collect phrases
    phrases = []

    # Go through each letter in the alphabet
    for letter in alphabet:
        # If the letter is in the phrase, proceed to create a line
        if letter in phrase:
            # Create a new line with the current state of the phrase and the letter
            new_line = phrase + letter
            # Append the new line to the phrases list
            phrases.append(new_line)
            # Update the phrase by removing the current letter
            phrase = phrase.replace(letter, '').replace('  ', ' ')
            # Update the allowed letters
            allowed_letters = allowed_letters.replace(letter, '')

    return phrases

# Example input
input_word = input()
# Generate the song
song_lyrics = song_algorithm(input_word)

# Print the song lyrics
for line in song_lyrics:
    print(line.strip())


