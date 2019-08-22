name = input("Pleas enter your name")
vowel_count = 0

for i in name:
    if i in "aeiouAEIOU":
        vowel_count += 1

print("Out of {} letters, {} has {} vowels".format(len(name), name, vowel_count))


