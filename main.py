import requests
from bs4 import BeautifulSoup
import fake_useragent
user=fake_useragent.UserAgent().random
header ={'user-agent':user}
# основной блок
host = 'https://browser-info.ru/'
responce = requests.get(host).text
soup = BeautifulSoup(responce,'lxml')
blok = soup.find("div",id='center')
# чек джава
check_js = blok.find("div",id="javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript:{status_js}'
# чек флэщ
check_fv = blok.find("div",id="flash_version")
status_fv = check_fv.find_all('span')[1].text
result_fv = f"flash_version:{status_fv}"

print(result_js)
print(result_fv)
