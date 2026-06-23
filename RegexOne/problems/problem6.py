import re

text1: str = "			The quick brown fox..."  # capture group "The quick brown fox..."
text2: str = "	   jumps over the lazy dog."  # capture group "	jumps over the lazy dog."

nice_texts: list[str] = [text1, text2]

pattern: str = r"^\s*([\w \.]*)$"
# pattern: str = r"^\s*(.*)\s*$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1), matching.group(2))

