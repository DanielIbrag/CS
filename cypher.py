#Name: Daniel Ibragimov
#Email: daniel.ibragimov74@myhunter.cuny.edu
#Date: Sept 7th, 2023
#This program cyphers a message

message = input("Please enter a message")
new_message = " "
coded_word = " "
for ch in message:
    offset = ord(ch) - ord('a') + 13
    wrap = offset % 26
    new_char = chr(ord('a')+ wrap)
    coded_word = coded_word + new_char

print('your word in code is', coded_word)