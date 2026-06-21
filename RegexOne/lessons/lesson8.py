# task - need to detect "1 file found?", "2 files found?", "24 files found?" but skip "No files found."

# теория. к метасимволам относится и "?" который делает символ или последовательность перед ним опциональными. 
# например, паттерн "ab?c" задетектит и "ac", и "abc". 
# как и для остальных метасимволов, чтобы найти знак вопроса в строке, надо поставить \ перед ним

import re

text1: str = "1 file found?"
text2: str = '2 files found?'
text3: str = '24 files found?'

nice_texts: list[str] = [text1, text2, text3]

stext1: str = "No files found."

shity_texts: list[str] = [stext1]

pattern: str = r"\d+ files? found\?"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
