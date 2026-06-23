import re

text1: str = "ftp://file_server.com:21/top_secret/life_changing_plans.pdf"  # capture group "ftp" and "file_server.com" and "21"
text2: str = "https://regexone.com/lesson/introduction#section"  # capture group "https" and "regexone.com""
text3: str = "file://localhost:4040/zip_file"  # capture group "file" and "localhost" and "4040"
text4: str = "https://s3cur3-server.com:9999/"  # capture group "https" and "s3cur3-server.com" and "9999"
text5: str = "market://search/angry%20birds"  # capture group "market" and "search"

nice_texts: list[str] = [text1, text2, text3]

pattern: str = r"^(\w+)://([\w\.-]+)(:(\d+))?"

for t in nice_texts:
    matching = re.search(string=t, pattern=pattern)
    if matching:
        print(matching.group())
        print(matching.group(1), matching.group(2))
