import requests, time, re
from bs4 import BeautifulSoup

def generate_user_agents(url):
  headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/337.1.0.11.118;]"}
  try:
    response=requests.get(url, headers=headers, timeout=10)
  except requests.exceptions.Timeout:
    print("requests timeout!")
  else:
    return response.text

def get_list_agents():
  soup=BeautifulSoup(generate_user_agents(url), "html.parser")
  find = soup.find('ul', attrs={"class":"agents_list"})
  mozilla_sections = re.split(r"(Mozilla/5\.0 .+?)Mozilla/5\.0", find.text)
  
  result_text = "\n\n".join(section.strip() for section in mozilla_sections if section.strip())
  print(result_text)
  
if __name__=="__main__":
  url = "https://user-agents.net/applications/instagram-app"
  get_list_agents()