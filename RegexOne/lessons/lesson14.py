# task - need to detect "I love cats" and "I love dogs" but skip "I love logs" and "I love cogs"

# теория. регулярные выражения также поддерживают логические операторы. например, метазнак "|" обозначает "или".
# при его использовании в последовательности (bread|milk|juice) будет произведен поиск по всем 3-м элементам

import re

text1: str = "I love cats"
text2: str = "I love dogs"

nice_texts: list[str] = [text1, text2]

stext1: str = "I love logs"
stext2: str = "I love cogs"

shity_texts: list[str] = [stext1, stext2]

pattern: str = r"^I love (cats|dogs)$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
