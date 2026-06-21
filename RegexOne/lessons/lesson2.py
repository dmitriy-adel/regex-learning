# task - 

# теория. иногда приходится искать в тексте подстроки, часть которых неизвестна или не очень важна. 
# для этого существует символ '.', который считается метазнаком и представляет собой 
# совершенно любой один знак, будь то буква, число, пробел, спец. символ и так далее. 
# если же требуется найти в тексте точку, надо использовать последовательность '\.'

import re

text1: str = "	cat."
text2: str = '896.'
text3: str = "?=+."
text4: str = "krya12"

texts: list[str] = [text1, text2, text3, text4]
pattern: str = r"\."
# pattern: str = r"123"

for t in texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())