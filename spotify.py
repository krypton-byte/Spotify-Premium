#!/usr/bin/python2
import os,requests,json,time
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
def ulang():
	b=raw_input(u+'apakah ingin ngulang lagi bep:V y/t : '+p)
	if(b=='y' or b== 'Y'):
		inp()
	elif(b=='T' or b=='t'):
		exit()
	else:
		print('Y/y = iya , T/t = tidak')
		ulang()
def spotify(jumlah):
	try:
		logo()
		ambil=json.loads(requests.get('http://n1ghthax0r.000webhostapp.com/api/spotify/?jumlah='+str(jumlah)).text)
		n=0
		while n<len(ambil):
			print(u+'-----------------------------------------')
			print(m+'['+k+'*'+m+']'+b+' Type akun \t\t:'+h+' %s' % ambil[n]['Account Type'])
			print(m+'['+k+'*'+m+']'+b+' Email \t\t: '+h+'%s' % ambil[n]['Email'])
			print(m+'['+k+'*'+m+']'+b+' kata sandi \t\t:'+h+' %s' % ambil[n]['Password'])
			print(m+'['+k+'*'+m+']'+b+' Negara \t\t:'+h+' %s' % ambil[n]['Country'])
			print(m+'['+k+'*'+m+']'+b+' masa berlaku \t:'+h+' %s' % ambil[n]['Expired'])
			n+=1
		print(u+'-----------------------------------------'+p)
		ulang()
	except requests.exceptions.ConnectionError:
		print(k+'[!] yank coba hidupkan datamu pasti bisa'+p)
def inp():
	try:
		logo()
		jum=input('\t'+m+'['+k+'?'+m+']'+h+' jumlah : '+k)
		spotify(jum)
	except (NameError,SyntaxError):
		print(m+'[x] pake angka ya yank')
		time.sleep(1)
		inp()
def logo():
	os.system('clear')
	os.system('toilet -f slant -F gay "   SPOTIFY"')
	print(h+'Author :'+k+' Krypton')
try:
	inp()
except (KeyboardInterrupt,EOFError):
	print(m+'\n['+k+'!'+m+']'+h+' selamat tinggal bep :V'+p)
