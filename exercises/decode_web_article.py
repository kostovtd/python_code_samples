"""

Decodes a simple web page and prints it's content
to the user

"""

import requests
from lxml import html


def main():
    page = requests.get("http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
    tree = html.fromstring(page.content)
    article_intros = tree.xpath('//div[@class="dek"]//text()')
    paragraphs_list = tree.xpath('//p//text()')

    for x in range(0, len(article_intros)):
        print(article_intros[x])
        print('\n')

    for y in range(0, len(paragraphs_list)):
        print(paragraphs_list[y])
        print('\n')

if __name__ == "__main__":
    main()