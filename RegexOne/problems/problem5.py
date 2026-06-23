import re

text1: str = "img0912.jpg"  # capture group "img0912" and "jpg"
text2: str = "updated_img0912.png"  # capture group "updated_img0912" and "png"
text3: str = "favicon.gif"  # capture group "favicon" and "gif"

nice_texts: list[str] = [text1, text2, text3]

stext1: str = ".bash_profile"
stext2: str = "workspace.doc"
stext3: str = "documentation.html"
stext4: str = "img0912.jpg.tmp"
stext5: str = "access.lock"

shity_texts: list[str] = [stext1, stext2, stext3, stext4]

pattern: str = r"^([\w]+)\.(jpg|png|gif)$"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1), matching.group(2))

for t in shity_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
