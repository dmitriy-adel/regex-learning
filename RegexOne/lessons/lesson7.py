# # task - need to detect "aaaabcc", "aabbbbc", "aacc" but skip "a"

# теория. иногда мы не знаем, сколько символов может быть в подстроке после определенного участка. 
# для поиска таких подстрок используются Клини Стар и Клини Плюс, которые добавляют (0 или более символов) и (1 и более символов) в подстроку.
# добавляемые символы следуют последним описанным правилам. например, \d+ захватит 5, 555, 5555555, а \d* захватит и пустую строку в том числе.
# если посмотреть на regex101.com, Kleene Star разбивает строку на символы и собирает результат по ним. 
# согласно сайту, для паттерна \d* в строке 555b4 будет найдено 4 строки: 555, пустая строка, 4, пустая строка

import re

text1: str = "aaaabcc"
text2: str = 'aabbbbc'
text3: str = 'aacc'

nice_texts: list[str] = [text1, text2, text3]

stext1: str = "a"

shity_texts: list[str] = [stext1]

pattern: str = r"a+[bc]+"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
