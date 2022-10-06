num = input("Enter a Value = ", )

result = 0

i=1

# This is a Big O or O(n) Notation

for i in range(int(num)+1):
    result = result + i
    i = i + 1

print(result)
