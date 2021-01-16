
#import modules
import os
import re

#ask for file and open that file
file_title = input("What txt file would you like to analyse?  ")
input_file_path = os.path.join("raw_data", file_title)

#open, read, and extract contents of files
with open(input_file_path, "r") as pfile:

    content = pfile.read()

    words = content.split(" ")
    sentences = re.split("(?<=[.!?]) +", content)

#calculate approx letter total
total_char = 0
for word in words:
    total_char += len(word)

#calculate averages
average_letter = round(total_char/len(words),1)
average_sentence = round(len(words)/len(sentences),1)
    
#print results    
print("--------------------------------")
print("Paragraph Analysis")
print("--------------------------------")
print(f"Approximate Word Count: {len(words)}")
print(f"Approximate Sentences Count: {len(sentences)}")
print(f"Approximate Letter Count: {average_letter}")
print(f"Average Sentence Length: {average_sentence}")
print("--------------------------------")
