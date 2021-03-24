import time , secrets , uuid , webbrowser , requests
from colorama import Fore
import sys as n
import time as mm
uuid = uuid.uuid4()
r = requests.session()
cookies =secrets.token_hex()
y=Fore.LIGHTYELLOW_EX
po = '\033[1;38m'
ree='\033[1;39m'
g=Fore.LIGHTGREEN_EX
#dev @Filza_507 ______________ ch @TweakPY
def slow(M):
 for c in M + '\n':
  n.stdout.write(c)
  n.stdout.flush()
  mm.sleep(1. / 5070)
####################dev filza#####################
webbrowser.open('https://t.me/TweakPY')
slow("𝑫𝒆𝒗𝒆𝒍𝒐𝒑 𝒃𝒚-->𝑭𝒊𝒍𝒛𝒂")
slow("𝖇𝖔𝖙 𝖘𝖕𝖆𝖒 𝖎𝖓𝖘𝖙𝖆 𝖎𝖘 𝖈𝖔𝖒𝖎𝖓𝖌..")
print(y+'========================================')
print("Enter YOUR User ")
filza445=input(po+">> ")
print("Enter YOUR PASSWORD")
FLOZ20=input(po+">> ")
print(y+'========================================')
def filza507():
 url = 'https://www.instagram.com/accounts/login/ajax/'

 headers = {
     'accept': '*/*',
     'accept-encoding': 'gzip, deflate, br',
     'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
     'content-length': '296',
     'content-type': 'application/x-www-form-urlencoded',
     'origin': 'https://www.instagram.com',
     'referer': 'https://www.instagram.com/',
     'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
     'sec-ch-ua-mobile': '?0',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
     'x-csrftoken': 'MPicCBRW0thEKbRdX9DhiTL6UB0nGtqV',
     'x-ig-app-id': '936619743392459',
     'x-ig-www-claim': 'hmac.AR1Y1dEsDcV-xq-u_7U0XISuyjCpWSS-VvmOhVU2N6rp9zg7',
     'x-instagram-ajax': 'f65d2f981648',
     'x-requested-with': 'XMLHttpRequest'}

 data = {
         'username': f'{filza445}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{FLOZ20}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'
         }

 filza5448 = r.post(url, headers=headers, data=data)

 if '"authenticated":true' in filza5448.text:
  print(g+'Done login ..')
  r.headers.update({'x-csrftoken': filza5448.cookies['csrftoken']})

  print('========================================')
  print(y+"Enter The target ")
  floz70 = input(po+">> ")
  print(y+"Sleep")
  sl=int(input(po+">> "))
  print(y+'========================================')

  url_id = 'https://www.instagram.com/{}/?__a=1'.format(floz70)

  req_id = r.get(url_id).json()
  user_id = str(req_id['logging_page_id'])
  ffilza2000 =user_id.split('_')[1]
  done=0

  while True:
   url_spam = 'https://www.instagram.com/users/{}/report/'.format(ffilza2000)
   data_spam = {
           'source_name':'',
           'reason_id': 1,
           'frx_context':''}

   solo = r.post(url_spam, data=data_spam)
   print(g+f'done spam {done}')
   time.sleep(sl)
   done+=1

 elif ('checkpoint_required') in filza5448.text:
     print(y+'SECURE')

 elif ('"user":true,"authenticated":false') in filza5448.text:
     print(ree+'WRONG PASSWORD')

 elif filza5448.status_code == "429":
     print(ree+'YOU BAN NICE')

 elif ('"user":false') in filza5448.text:
     print(ree+'USERNAME WAS NOT FOUND')
 else:
     print(ree+'>>\nUNKNOWN ERROR..')
filza507()