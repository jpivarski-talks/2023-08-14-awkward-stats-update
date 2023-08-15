import requests
from bs4 import BeautifulSoup

repo = "scikit-hep/awkward"
url = 'https://github.com/{}/network/dependents'.format(repo)
nextExists = True
result = []
while nextExists:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    result = result + [
        "{}/{}".format(
            t.find('a', {"data-repository-hovercards-enabled":""}).text,
            t.find('a', {"data-hovercard-type":"repository"}).text
        )
        for t in soup.findAll("div", {"class": "Box-row"})
    ]
    nextExists = False
    for u in soup.find("div", {"class":"paginate-container"}).findAll('a'):
        if u.text == "Next":
            nextExists = True
            url = u["href"]

for r in result:
  print(r)
