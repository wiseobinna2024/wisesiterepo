def emojis_convertor(messange):
    words= messange.split()
    emojis={
        ":)": "😍",
        ":(": "😒", 
        ":#": "😁"
    }
    output=''
    for word in words:
        output+= emojis.get(word, word) + " "
    return output 
    
    
messange= input(" > ")
result= emojis_convertor(messange)
print(result)

        