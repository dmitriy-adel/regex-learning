# task - match the dot in some texts

# теория. как было сказано в предыдущем уроке, каждый элемент строки - символ. 
# при этом существует набор специальных символов, которые используеются для обозначения набора символов. 
# например, \d используется для обозначения любой цифры от 0 до 9. 
# метазнак можно определить по '\', стоящему перед знаком

import re

text1: str = "abc123xyz"
text2: str = 'define "123"'
text3: str = "var g = 123;"
text4: str = "krya12"

texts: list[str] = [text1, text2, text3, text4]
pattern: str = r"\d\d\d"
# pattern: str = r"123"

for t in texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
