import re

text1: str = "3.14529"
text2: str = "-255.34"
text3: str = "128"
text4: str = "1.9e10"
text5: str = "123,340.00"

nice_texts: list[str] = [text1, text2, text3, text4, text5]

stext1: str = "	720p"

shit_texts: list[str] = [stext1]

pattern: str = r"^-?\d+(,\d+)*(\.\d+(e\d+)?)?$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shit_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

