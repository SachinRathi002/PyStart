import webbrowser
import time

search_urls =["www.google.com", "www.yahoo.com", "www.bing.com"]
social_urls = ["https://twitter.com/", "www.facebook.com", "https://www.instagram.com/", "https://www.snapchat.com/",
                "https://in.linkedin.com/"]
news_urls = ["https://www.bbc.com/", "https://edition.cnn.com/world", "https://timesofindia.indiatimes.com/",
             "http://ddnews.gov.in/", "https://www.thehindu.com/"]
entrtmnt_urls = ["www.youtube.com", "www.netflix.com", "https://www.primevideo.com/"]
e_comm_urls = ["https://www.amazon.in/", "https://www.flipkart.com/"]

def open_tabs(urls_lists):
	for i in urls_lists:
		webbrowser.open_new_tab(i)
              
def main_search():
	open_tabs(search_urls)

def main_social():
	open_tabs(social_urls)

def main_news():
	open_tabs(news_urls)

def main_entrtmnt():
	open_tabs(entrtmnt_urls)

def main_ecomm():
    open_tabs(e_comm_urls)

print("Hello Good Moring!!!")
print("""Making your day more shiny....
Press ->1 for Search
Press ->2 for Social Media
Press ->3 for News
Press ->4 for Entertaiment
Press ->5 for eStore""")
userInput = int(input("Please enter your choice: "))
print("As you said we did it for you :)...")

if(userInput == 1):
    main_search()
elif(userInput == 2):
    main_social()
elif(userInput == 3):
    main_news()
elif(userInput == 4):
    main_entrtmnt()
elif(userInput == 5):
    main_ecomm()
else:
    print("Invalid option")
