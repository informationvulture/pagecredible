"""
The main app file
"""

# imports
from urllib.request import urlopen
import re

def get_pages():
    """
    Gets page urls from a text file,
    and return a list of HTTPResponse objects.
    """
    raw_pages = []
    with open("to_get.txt", "r", encoding="utf-8") as get_web_pages:
        for page in get_web_pages:
            
            # Finds stuff in-between the first and second '.'
            page_name = [match.start() for match in re.finditer("\\.", page)]

            raw_pages.append([urlopen(page), page[page_name[0]+1:page_name[1]]])
    return raw_pages

def extract_html(pages):
    """
    Takes in HTTPResponse objects and creates HTML files.
    """
    for indx, page in enumerate(pages):

        raw_page = page[0] # HTTPResponse object
        page_name = page[1] # Main page name
        
        with open(f"pages/{page_name}_{indx}.html", "w", encoding="utf-8") as index_page:
            html_bytes = raw_page.read()
            html = html_bytes.decode("utf-8")
            index_page.write(html)
            
def main():
    raw_pages = get_pages()
    extract_html(raw_pages)



if __name__ == "__main__":
    main()