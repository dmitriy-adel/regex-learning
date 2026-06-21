# task - need to detect "Mission: successful" but skip "No files found."

# теория. существует негласное праивло "писать настолько специфичные регулярные выражения, на сколько это возможно" для каждого случая.
# правило это существует, чтобы избежать обнаружения тех строк, что не должны быть обнаружены. 
# для этой цели служат уже знакомая каретка "^" и символ доллара "$". 
# обращу внимание, что каретка имеет разное поведение внутри квадратных скобочек "[]" при работе с последовательностью и во вне квадратных скобочек.
# "^" - начало строки, "$" - конец строки

import re

text1: str = "Mission: successful"

nice_texts: list[str] = [text1]

stext1: str = "Last Mission: unsuccessful"
stext2: str = "Next Mission: successful upon capture of target"

shity_texts: list[str] = [stext1, stext2]

pattern: str = r"^Mission: successful$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
