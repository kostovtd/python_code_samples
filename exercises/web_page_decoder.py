"""

 Extracts the article titles from www.nytimes.com

"""


import requests
from lxml import html


def main():
    page = requests.get("http://www.nytimes.com/")
    tree = html.fromstring(page.content)
    print(page.text)
    article_titles = tree.xpath('//h2[@class="story-heading"]//text()')
    filtered_articles = []

    for x in range(0, len(article_titles)):
        if article_titles[x] != ' ':
            filtered_articles.append(article_titles[x].strip())

    print(filtered_articles)


if __name__ == "__main__":
    main()