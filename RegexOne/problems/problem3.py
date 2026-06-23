import re

text1: str = "tom@hogwarts.com"
text2: str = "tom.riddle@hogwarts.com"
text3: str = "tom.riddle+regexone@hogwarts.com"
text4: str = "tom@hogwarts.eu.com"
text5: str = "potter@hogwarts.com"
text6: str = "harry@hogwarts.com"
text7: str = "hermione+regexone@hogwarts.com"

nice_texts: list[str] = [text1, text2, text3, text4, text5, text6, text7]

pattern: str = r"^([\w\.]+)[\+\w]*@[\w\.]+.com$"
# pattern: str = r"^([\w\.]*)$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1))
