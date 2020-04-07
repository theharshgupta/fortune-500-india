import wikipedia
a = wikipedia.search("Reliance")[0]
print(wikipedia.page(a).content)

