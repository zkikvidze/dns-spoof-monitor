import dns.resolver
import time
import smtplib
import base64
import logging

#silk 87.253.32.130, 87.253.32.131

logging.basicConfig(filename='dnsmonitor.log',level=logging.DEBUG)


def emailreport(input):
        username = "user@domain.mail"
	password = base64.b64decode("BASEENCODEDPASS")
        FROM = "FROMMAIL@DOMAIN.MAIL"
        TO  = "TOMAIL@DOMAIN.MAIL"
        SUBJECT = "DNS Monitor"
        TEXT = input
        msg = """\      
From: %s
To: %s
Subject: %s

%s
""" % (FROM, "".join(TO), SUBJECT, TEXT)


        server = smtplib.SMTP('MAIL.SERVER.DOMAIN:PORT')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(FROM, TO, msg)
        server.quit()
        return



domains = [line.strip() for line in open('domains.txt')]
servers = [line.strip() for line in open('servers.txt')]


realserver = '8.8.8.8'

reallist = []
resolver = dns.resolver.Resolver()


resolver.nameservers=[realserver]
for realdomain in domains:
	try:
        	#time.sleep(5)
		realanswer = resolver.query(realdomain, "A")
	except:
		print 'server not answers' + ' ' + server
		logging.warning('server not answers' + ' ' + server) 
		break
        for realdata in realanswer:
                realaddress = realdata.address
		reallist.append([realdomain, realaddress])


for server in servers:
	resolver.nameservers=[server]
	for dynlist in xrange(len(servers)):
		dynlist = []
	for domain in domains:
		try:
			#time.sleep(5)
			answer = resolver.query(domain, "A")
		except:
			print 'server not answers' + ' ' + server
			logging.warning('server not answers' + ' ' + server)
			break
		for rdata in answer:
			address = rdata.address
		dynlist.append([domain, address])
		
	for a, b in zip(reallist, dynlist):
		if a != b:
			print 'Spoofing Detected! server:' +  ' '  + server + ' ' + 'Record:', b, 'Must Be:',  a
			report = 'Spoofing Detected! server:' +  ' '  + server + ' ' + 'Record:', b, 'Must Be:',  a
			emailreport(report)
