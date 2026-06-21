# task - need to find all strings with 3 'z' letters in it

# теория. разговор пойдет про повторения. если есть необходимость найти в строке подстроку из 10-ти символов 'z', не надо писать 10 раз символ 'z'.
# достаточно просто указать в паттерне z{10}. в данном случае фигруные скобки с цифрой обозначают количество искомых элементов друг за другом в строке.
# если, например, надо найти сразу 3 цифры, можно написать \d\d\d, а можно - [0-9]{3}.

import re

text1: str = "wazzzzzup"
text2: str = 'wazzzup'

nice_texts: list[str] = [text1, text2]

stext1: str = "wazup"

shity_texts: list[str] = [stext1]

pattern: str = r"z{3}"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
