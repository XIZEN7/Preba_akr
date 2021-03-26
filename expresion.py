import re
daft = re.compile(r"[A-Z][a-z_-]{2,30}")
r = input(str('Enter words: '))
x = daft.findall(r)
print(x)
