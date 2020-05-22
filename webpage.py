import webbrowser
import time

social_urls = ["https://twitter.com/", "www.facebook.com", "www.youtube.com", "www.google.com"]

def open_tabs(urls_lists):
	for i in urls_lists:
		webbrowser.open_new_tab(i)

def main():
	open_tabs(social_urls)

main()