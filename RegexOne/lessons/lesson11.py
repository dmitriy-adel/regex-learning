# task - need to detect "file_record_transcript.pdf" and "file_07241999.pdf" but skip "	testfile_fake.pdf.tmp". 
# Capture Groups for detected - 'file_record_transcript', 'file_07241999'

# теория. в регулярных выражениях есть метасимволы "(" и ")", которые позволяют создавать захваченные группы (Capture Groups) из строк.
# эти захваченные группы позволяют разделять вывод найденных совпадений. в примере ниже по заданию требуется найти файлы с определенным названием,
# основная часть которого (без постфикса), вынесена в круглые скобки. из вывода можно увидеть, что патерны в круглых скобках 
# ищутся в строке наравне со всем паттерном, только при этом есть возможность получить отдельно весь паттерн и отдельно паттерн круглых скобок/
# если говорить про поиск, сначала происходит поиск по всему паттерну, а после, в найденных строках, происходит поиск по группе

import re

text1: str = "file_record_transcript.pdf"
text2: str = "file_07241999.pdf"

nice_texts: list[str] = [text1, text2]

stext1: str = "testfile_fake.pdf.tmp"

shity_texts: list[str] = [stext1]

pattern: str = r"^(file[\d*a-z_]*)\.pdf$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1))

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
