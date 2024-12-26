phone= input('Please input your phone number:  ')

digits= {
    "1": 'one', 
    "2": 'two', 
    "3": 'three', 
    "4": 'four'
}
output= ""
for ch in phone: 
    output+=digits.get(ch, '!') + " "
print(output)

print(' This is a new program: ')

mes= input("> ")
words= mes.split()
emojis= {
    ":)": "😂", 
    ":(": " 😒"
    }
output= " "
for word in words: 
    output+=emojis.get(word, word) + " "
print(output)

    