# task - need to detect "1280x720" and "1920x1600" and "1024x768"
# Capture Groups for detected - "1280"-"720", "1920" | "1600", "1024" | "768"

# теория. ничего нового

import re

text1: str = "1280x720"
text2: str = "1920x1600"
text3: str = "1024x768"

nice_texts: list[str] = [text1, text2, text3]

pattern: str = r"^(\d+)x(\d+)$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1))
        print(matching.group(2))
