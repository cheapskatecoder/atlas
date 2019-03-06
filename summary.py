"""
    Created @ - 1:53PM
    Created By - llama (Sahil)
    Created On - VSCode
    Created Under - llamasec [owned by Sahil (llama)]
    Lisence - GNU General Public License v3 (GPL-3)
"""
#!/bin/python3
import requests as r 
import re
from bs4 import BeautifulSoup as bs

# https://api.duckduckgo.com/?q=valley+forge+national+park&format=json&pretty=1
# https://en.wikipedia.org/wiki/

"""
    Summary is a simple module in a larger sceheme. 
    It get's any* topic summary and return the essentials, like, 
    what, who, when, where, (hopefully how), follow up links, . 
"""

class GetSummary:
    def __init__(self, query):
        self.query = query
        self.wiki_url = f"https://en.wikipedia.org/wiki/{self.query}"
        self.ducky_url = f"https://api.duckduckgo.com/?q={self.query}&format=json&pretty=1"
        self.get_summary_text()
    
    def get_summary_text(self):
        get_data = r.get(self.wiki_url)
        if get_data.status_code == 200:
            soup = bs(get_data.text, 'lxml')
            output_clener = re.compile(r'<[^>]+>')
            summary = str(soup.find_all('p')[1])
            print(output_clener.sub('', summary))
        else:
            print("it was a 404")
        
if __name__ == '__main__':
    while 1:
        classobj = GetSummary(input("Enter ").replace(" ", "_"))
