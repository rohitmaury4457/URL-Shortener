import pyshorteners

url = input("Enter the URL : ")

def shortenURL(url):
    s = pyshorteners.Shortener()
    print("Short ULR : ", s.tinyurl.short(url))


shortenURL(url)