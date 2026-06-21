# task - need to find 'an' in "can", "man", "fan", but not in "dan", "ran", "pan"

# теория. иногда использование дота избыточно - например, при проверке номера телефона. 
# для поиска символа из определенной последовательности используют "[]". 
# например, [abc] будет искать один из символов a, b, c в подстроке. 

import re

text1: str = "can"
text2: str = 'man'
text3: str = "fan"

nice_texts: list[str] = [text1, text2, text3]

stext1: str = "dan"
stext2: str = 'ran'
stext3: str = "pan"

shity_texts: list[str] = [stext1, stext2, stext3]

pattern: str = r"[cmf]an"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
