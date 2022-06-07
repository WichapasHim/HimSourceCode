f = open("output.txt", "a")
print("Hello stackoverflow!", file=f)
print("I have a question.", file=f)
f.close()