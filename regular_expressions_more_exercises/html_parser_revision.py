import re

title_pattern = r"<title>(.+?)</title>"
content_pattern = r"<body>(.+?)</body>"
ignored_symbols_pattern = r"<.+?>"
remove_signs = r"\\n|\\t"

text = input()

title_match = re.findall(title_pattern, text, re.DOTALL)
content_match = re.findall(content_pattern, text, re.DOTALL)

if title_match and content_match:
    title = title_match[0]
    content = re.sub(ignored_symbols_pattern, "", content_match[0])
    content = re.sub(remove_signs, "", content)

    print(f"Title: {title}")
    print(f"Content: {content}")
else:
    print("No title or content found.")
