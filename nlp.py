import wikipediaapi as wiki
from string import Template
import pandas

def test():
    wikipedia = wiki.Wikipedia('en')
    page = wikipedia.page('Reliance Industries')
    templ = Template("Title: $(title) \n $(summary)")
    if page.exists():
        print(page.title)
        print(page.summary)
        print(page.fullurl)
        print(page.canonicalurl)
        print(page.canonicalurl)


def main():
    wiki_wiki = wiki.Wikipedia(
        language='en',
        extract_format=wiki.ExtractFormat.WIKI
    )
    df = pandas.read_csv("fortune.csv", delimiter=',')
    for company in df['company']:
        p_wiki = wiki_wiki.page(str(company))
        if "family" in p_wiki.text:
            print(p_wiki.title)
            print("\t" + p_wiki.summary)
        # else:
            # print(p_wiki.title + " Keyword not found. ")


main()

