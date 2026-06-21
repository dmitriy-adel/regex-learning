# task - match abc in some texts
# теория. регулярки обрабатывают все элементы в строке как символы. 
# символы или последовательности символов ищутся при помощи паттернов, которые, в основном, 
# используют набор ASCII, но при этом можно использовать и кодировку unicode 

import re

text1: str = "abcdefg"
text2: str = "abcde"
text3: str = "abc"
text4: str = "krya"

texts: list[str] = [text1, text2, text3, text4]


pattern: str = r"abc"

for t in texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
