import requests
import os
import datetime

now = datetime.datetime.now()
def download(url):
  print(f"{os.getpid()} downloading {url}")
  response = requests.get(url)
  return response.text

urls = ["https://www.gutenberg.org/files/2600/2600-0.txt", "https://www.gutenberg.org/files/2701/2701-0.txt", "https://www.gutenberg.org/files/2700/2700-0.txt"]

result = [download(url) for url in urls]

with open("books.txt", "w", encoding="utf-8") as f:
      for text in result:
        f.write(text)

print(f"Finished downloading {len(urls):,} files")
print(f"Completed in {datetime.datetime.now() - now}")


