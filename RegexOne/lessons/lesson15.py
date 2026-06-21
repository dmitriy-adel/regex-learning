# да когда же это кончится. ЭКСТРА УРОК! 

# task - need to detect "The quick brown fox jumps over the lazy dog." and "There were 614 instances of students getting 90.0% or above." and "The FCC had to censor the network for saying &$#*@!.	To be completed"

# теория. есть такое понятие, как back-referencing. 
# можно сказать, что это обращения к захваченным группам через метасимволы "\n", где n - порядковый номер группы


import re

text1: str = "The quick brown fox jumps over the lazy dog."
text2: str = "There were 614 instances of students getting 90.0% or above."
text3: str = "The FCC had to censor the network for saying &$#*@!."

nice_texts: list[str] = [text1, text2, text3]

pattern: str = r"^([A-Za-z \d %&$#\*@!\.])+$"
# pattern: str = r".*"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
