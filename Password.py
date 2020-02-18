import string
import random
kw = input("Enter an Keyword : ")
x = [c for c in kw]
J = random.sample(x, len(x))
final = ''.join(str(x) for x in J)
print(final)
