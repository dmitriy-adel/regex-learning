# task - detect "hog" and "dog", but skip "bog"

# теория. иногда требуется избегать опредленных символов, для этого используется метасимвол "^".  
# например, паттерн [^abc] будет находить все одиночные символы, кроме a, b, c

import re

text1: str = "hog"
text2: str = 'dog'

nice_texts: list[str] = [text1, text2]

stext1: str = "bog"

shity_texts: list[str] = [stext1]

pattern: str = r"[^b]og"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
