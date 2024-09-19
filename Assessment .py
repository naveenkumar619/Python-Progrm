

#1 Program
word = 'Guvi Greeks Network Private Limited'
vowels = 'AEIOU'
#change word into uppercase
upper_case=word.upper()
#spliting the words into list 
wordSplit = upper_case.split()
#joining the words
i = "".join(wordSplit)

vowel_count = 0
for c in i:
    if c in vowels:    
        vowel_count += 1  

print("Total vowels:", vowel_count) 

#2 Program
num = 1
max_num = 20
row = 6
#executing for loop
for i in range(1, row + 1):
      print(' ' * (row - i), end='  ')
      for j in range(i):
          #loop will print 1 to 20
          if num <= max_num:
             print(num, end=' ')
             num += 1
      print()


#3 Program
word1 = 'Guvi Greeks Network Private Limited'
vowels1 = 'AEIOU'
word2 = word1.upper()
wordSplit2 = word2.split()
string1 = "".join(wordSplit)
#new string with vowels removed
new_string1 = ''.join(char for char in string1 if char not in vowels)
print(new_string1)


#4 Program
string = "Guvi Greeks Network Private Limited"
unique_char_count = len(set(string)) #It should will show the Unquie Character 
print(unique_char_count) 


#5 Program
Word_1 = 'madam'
word4 = Word_1.lower()
# using sliceing method reversing the word
if word4 == word4[0:0:-1]:
 print(f'{Word_1} its a palindrome')
else:
 print(f'{Word_1} its not a palindrome')

#6 Program
str1 = "hello world"
str2 = "world hello"
m, n = len(str1), len(str2) #Length of two string 
dp, max_length, result = [[0] * (n + 1) for _ in range(m + 1)], 0, ""
for i in range(1, m + 1): 
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                result = str1[i - max_length:i]
print("Longest common substring:", result)


 #7 Program
string = "Guvi Greeks Network Private Limited"
# changing the string to lowercase
string = string.lower()
letter_count = {}
# Iterate each character
for char in string:
        if char in letter_count:
            letter_count[char] += 1  
            # Increment the count if the letter exists in the dictionary
        else:
            letter_count[char] = 1   
            # Initialize the count if the letter is new
print(letter_count)
# Find the letter with the maximum count
max_letter = max(letter_count, key=letter_count.get)
max_count = letter_count[max_letter]
# Output the result
print(f"frequently used letter is '{max_letter}' with {max_count} occurrences.")

#8 Program
# Input strings
str1 = "listen"
str2 = "silent"

# Remove spaces and convert to lowercase
str1 = str1.lower()
str2 = str2.lower()
print(str1)
# Check if the sorted versions of the strings are the same
is_anagram = sorted(str1) == sorted(str2)

if is_anagram:
    print("True")  # They are anagrams
else:
    print("False")  # They are not anagrams


#9 program
input_string = "Write a program that takes a string and returns the number of words in it."
# Split the string into words
words = input_string.split()
# Count the number of words
word_count = len(words)
print("Number of words:", word_count)


