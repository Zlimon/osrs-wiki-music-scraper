import requests
import urllib.request
from bs4 import BeautifulSoup

domain = "https://oldschool.runescape.wiki"
url = domain + "/w/Category:Music_composed_by_Ian_Taylor?pagefrom=Spirits+of+the+Elid+%28music+track%29#mw-pages"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

parentDiv = soup.find_all("div", {"class": "mw-category-group"})

for div in parentDiv:
	liTags = div.find_all("li")
	for li in liTags:
		aTags = li.find_all("a", href=True)
		for a in aTags:
			print(domain + a['href'])

			songUrl = domain + a['href']
			songPage = requests.get(songUrl)

			soup = BeautifulSoup(songPage.content, "html.parser")

			mediaDiv = soup.find_all("div", {"class": "mediaContainer"})

			for div in mediaDiv:
				audioTags = div.find_all("audio")
				for audioTag in audioTags:
					print(audioTag["data-mwtitle"])
					audioSources = audioTag.find_all("source")
					# for audioSource in audioSources:
					print(audioSources[0]["src"])
					doc = requests.get(domain + audioSources[0]["src"])
					with open(audioTag["data-mwtitle"], "wb") as f:
						f.write(doc.content)
