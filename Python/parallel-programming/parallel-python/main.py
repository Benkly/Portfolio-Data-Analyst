import os
import requests
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from functools import reduce
import datetime

def cube(x):
  """Returns the cube of the argument"""
  print(f"Core {os.getpid()} processing {x}")
  return x * x * x

def download(url):
  print(f"{os.getpid()} downloading {url}")
  response = requests.get(url)
  return response.text

urls = ["https://www.gutenberg.org/files/2600/2600-0.txt", "https://www.gutenberg.org/files/2701/2701-0.txt", "https://www.gutenberg.org/files/2700/2700-0.txt"]

if __name__ == "__main__":
  with ProcessPoolExecutor(max_workers=24) as pool:
    now = datetime.datetime.now()
    values = range(1, 1001)
    result = pool.map(cube, values)
    
    print("")
    print(f"The sum of the first {len(values):,} cubes is {reduce(lambda x,y: x+y, result):,}")
    print(f"Completed in {datetime.datetime.now() - now}")

  with ThreadPoolExecutor() as pool:
    now = datetime.datetime.now()
    print("")
    result = pool.map(download, urls)
    
    print("")
    with open("books.txt", "w", encoding="utf-8") as f:
      for text in result:
        f.write(text)
    print(f"Finished downloading {len(urls):,} files")
    print(f"Completed in {datetime.datetime.now() - now}")