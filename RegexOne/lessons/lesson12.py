# task - need to detect "Jan 1987" and "May 1969" and "Aug 2011"
# Capture Groups for detected - "Jan 1987"-"1987", "May 1969" | "1969", "Aug 2011" | "2011"

# теория. помимо групп, существуют еще и подгруппы. для иъ обозначения надо использовать метазнкаи "()" с несколькими уровнями вложенности

import re

text1: str = "Jan 1987"
text2: str = "May 1969"
text3: str = "Aug 2011"

nice_texts: list[str] = [text1, text2, text3]

pattern: str = r"^([A-Z][a-z]+ (\d{4}))$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1))
        print(matching.group(2))
