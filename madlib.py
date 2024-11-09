with open("Textfile.text", "r") as file:
    story = file.read()

word_start = "<"
word_end = ">"
startingindex = 0
endindex = 0
word_list = set()

for index, character in enumerate(story):
    if character == word_start:
        startingindex = index
    

    if character == word_end:
        endindex = index

    
        word = story[startingindex: endindex + 1]
        word_list.add(word)

print(word_list)

answers = {} 

for words in word_list:
    answer = input(f"Enter a word for {words}: ")

    answers[words] = answer

for words in word_list:
    story = story.replace(words, answers[words])

print(story)
