from collections import Counter

input = "Test abc def abc"

input = input.split(" ")
for i in range(0, len(input)):
    input[i] = "".join(input[i])
    
UniqW = Counter(input)
    
s = " ".join(UniqW.keys())
# print (s)
print (UniqW)

# print (input)