import re

text1: str = "<a>This is a link</a>"  # capture group "a"
text2: str = "<a href='https://regexone.com'>Link</a>"  # capture group "a"
text3: str = "<div class='test_style'>Test</div>"  # capture group "div"
text4: str = "<div>Hello <span>world</span></div>"  # capture group "div"

nice_texts: list[str] = [text1, text2, text3, text4]

pattern: str = r"^<(\w+)"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1))
