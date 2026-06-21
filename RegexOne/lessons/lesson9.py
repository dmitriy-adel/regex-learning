# task - need to detect "1.   abc",  "2.	abc", "3.           abc" but skip "4.abc"

# теория. для определения табуляции в последовательности используется \t, для пробела - просто пробел, для переноса на следующую строку - \n.
# при этом \t никак не детектится пробелами

import re

text1: str = "1.   abc"
text2: str = '2.    abc'
text3: str = '3.           abc'

nice_texts: list[str] = [text1, text2, text3]

stext1: str = "4.abc"

shity_texts: list[str] = [stext1]

pattern: str = r"\d\.[ \t]+abc"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
