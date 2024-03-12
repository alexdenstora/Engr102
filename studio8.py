import requests
import time
from bs4 import BeautifulSoup as bs

class Quote:
    def __init__(self, text, author, tags):
            self.text = text
            self.author = author
            self.tags = tags

def main():
        url = "https://quotes.toscrape.com"
        r = requests.get(url)
        soup = bs(r.content, "html.parser")

        #scrape_quotes(soup)
        quotes = []

        while True:
            time.sleep(1)
            relative_url = get_next_url(soup)
            if relative_url is None:
                   break
            next_page = url + relative_url
            
            r = requests.get(next_page)
            soup = bs(r.content, "html.parser")
            quotes.extend(scrape_quotes(soup))
        
        get_popular_tags(quotes)
        print("----------------------")
        print("Answer to question 2 and 3:")
        get_shortest_and_longest(quotes)
        print("----------------------")
        

        return

def get_popular_tags(quotes):
    list_of_tags = []
    top_ten = []
    
    
    for quote in quotes:
        list_of_tags.extend(quote.tags)

    sorted_list_tags = sorted(list_of_tags)

    #print(sorted_list_tags)

    #sorted_frequency_tags = []

    #count = 20
    #for tag in sorted_list_tags:
        #if sorted_list_tags.count(tag) > 


        #if list_of_tags.count(tag) > count:
              #list_of_tags.append(tag)
              #count = count - 1
              #for i in list_of_tags:
                    #if i == tag:
                        #list_of_tags.remove()
              

    #print("LIST:", list_of_tags)
              
            
    #for tag in list_of_tags:
        #curr_frequency = list_of_tags.count(tag)
        #if curr_frequency > counter and len(top_ten) < 10:
            #counter = curr_frequency
            #top_ten.append(tag)
            #for i in list_of_tags:
                #if i == tag:
                    #list_of_tags.remove(i)
            

    #for tag in list_of_tags:
        #curr_frequency = list_of_tags.count(tag)
        #if curr_frequency > counter:
            #counter = curr_frequency
            #num_1_tag = tag

    #print("number of love tags: ", list_of_tags.count("love"))
    #print("number of tags:", len(list_of_tags))
    #print("list of ALL tags: ", list_of_tags)
    #print("-----------------------------------")
    #print("List of top ten tags: ", top_ten)
    return

      
def get_shortest_and_longest(quotes):
    longest = 0
    shortest = 1000000
    longest_quote = ""
    shortest_quote = ""

    for quote in quotes:
        if len(quote.text) > longest:
            longest = len(quote.text)
            longest_quote = quote.text

        if len(quote.text) < shortest:
            shortest = len(quote.text)
            shortest_quote = quote.text

    print(longest_quote, longest)
    print(shortest_quote, shortest)
    return 

def get_next_url(soup: bs):
        list_item = soup.find("li", {"class": "next"})
        if list_item is None:
               return None
        anchor = list_item.find("a")
        url = anchor['href']
        

        
        return url
       
       

def scrape_quotes(soup: bs):
        
        quotes = soup.find_all("div", {"class": "quote"})

        quotes_list = []

        for quote in quotes:
                text = quote.find("span", {"class": "text"}).get_text(strip = True)
                #print(text)

                author = quote.find("small", {"class": "author"}).get_text(strip = True)
                #print(author)
               
                tags = quote.find_all("a", {"class": "tag"})
                tags_text = []
                for tag in tags:
                        tags_text.append(tag.get_text(strip = True))

                quotes_list.append(Quote(text, author, tags_text))
                #print(tags_text)

        return quotes_list


if __name__ == "__main__":
        main()