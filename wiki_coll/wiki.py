import wikipedia

wikipedia.set_lang("en")
content = wikipedia.page("cricket").content
# print(content[:])

with open("cricket.txt", "w") as f:
    f.write(content)

