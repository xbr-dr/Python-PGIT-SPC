# Program to print different vowels present in the given word
word = input("Enter word to search for vowels: ")
s1 = set(word)
v1 = {'a', 'e', 'i', 'o', 'u'}
d1 = s1.intersection(v1)
print("The different vowel present in", word, "are", d1)
