import re
text="Hello everyone,I am studying at KBTU"

pattern=r"[ ,.]"
new_text=re.sub(pattern,";",text)
print(new_text)