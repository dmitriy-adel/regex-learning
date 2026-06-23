import re

text1: str = "415-555-1234"
text2: str = "650-555-2345"
text3: str = "(416)555-3456"
text4: str = "202 555 4567"
text5: str = "4035555678"
text6: str = "1 416 555 9292"

nice_texts: list[str] = [text1, text2, text3, text4, text5, text6]

pattern: str = r"^\d?[\s]?\(?(\d{3})\)?[\s-]?\d{3}[\s-]?\d{4}$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1))
