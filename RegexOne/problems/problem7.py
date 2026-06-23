import re

text1: str = "E/( 1553):   at widget.List.makeView(ListView.java:1727)"  # capture group "makeView" and "ListView.java" and "1727"
text2: str = "E/( 1553):   at widget.List.fillDown(ListView.java:652)"  # capture group "fillDown" and "ListView.java" and "652"
text3: str = "E/( 1553):   at widget.List.fillFrom(ListView.java:709)"  # capture group "fillFrom" and "ListView.java" and "709"

nice_texts: list[str] = [text1, text2, text3]

stext1: str = "W/dalvikvm( 1553): threadid=1: uncaught exception"
stext2: str = "E/( 1553): FATAL EXCEPTION: main"
stext3: str = "E/( 1553): java.lang.StringIndexOutOfBoundsException"

shity_texts: list[str] = [stext1, stext2, stext3]

pattern: str = r"^./[\w+]?[\( \d\)]+:\s*[\w ]*.[\w]*.(\w*)\(([\w\.]*):(\d*)\)$"
# pattern: str = r"^(\w+)\(([\w\.]+):(\d+)\)$"  - не понял, почему этот вариант работает и проходит тест кейсы. надо посидеть с ллм над ним

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1), matching.group(2))

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
