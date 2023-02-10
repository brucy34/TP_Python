import re

text="I'm a #champion if i play in #Real_Madrid"
test=re.findall(r"#\w+",text)

for li in test:
    text = text.replace(li, f"<a href=\' \' >{li}</a>")

print(text) 