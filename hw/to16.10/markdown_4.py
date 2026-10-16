def upper(a):
    upper_word = ''
    for n in a:
        upper_word += n.upper()
    return upper_word

text = input()
letters = list(text)
first_4 = []
if len(letters) >= 4:
    for i in range(4):
        first_4.append(letters[i])
    counter = 0
    for f in first_4:
        if f.isupper():
            counter += 1
    if counter >= 3:
        print(upper(letters))
    else:
        print(text)
else:
    counter = 0
    for f in letters:
        if f.isupper():
                counter += 1
    if counter == len(letters):
        print(upper(letters))
    else:
        print(text)
    
