import re

number = "+(380)001234567"
result = re.search(r"(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?", number)
print(result[0])
