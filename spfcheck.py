#!/usr/bin/python
try:
	import spf
	import socket
except ImportError:
	print("Failed loading dependencies")

# info
def info():
    print("    #-- Author : cipher0x30        --#")
    print("    #-- Version : 1.0.0            --#")
    print("    #-- Type : SPF Record Checker  --#")

info()

domain = raw_input('Hostname: ')
domainIP = socket.gethostbyname(domain)
attackerIP = "104.219.248.97"

print("Victim IP: "+domainIP)
print("Attacker IP: "+attackerIP)
print("Checking SPF record...")
result = spf.check2(attackerIP,"postmaster@"+domain,domain)

if result[0] == "none":
	evaluation = "FAILED"
	msg = "The domain does not have an SPF record or the SPF record does not evaluate to a result. "+str(result[1])
elif result[0] == "fail":
	evaluation = "PASSED"
	msg = "The SPF record has designated the host as NOT being allowed to send, "+str(result[1])+"."
elif result[0] == "softfail":
	evaluation = "PASSED but consider fixing"
	msg = "The SPF record has designated the host as NOT being allowed to send but is in transition, "+str(result[1])+"."
elif result[0] == "nuetral":
	evaluation = "PASSED"
	msg = "The SPF record specifies explicitly that nothing can be said about validity, "+str(result[1])+"."
elif result[0] == "permerror":
	evaluation = "UNSPECIFIED"
	msg = "A permanent error has occured (eg. badly formatted SPF record), "+str(result[1])+"."	
elif result[0] == "temperror":
	evaluation = "UNSPECIFIED"
	msg = "A transient error has occured, "+str(result[1])+"."		
elif result[0] == "pass":
	evaluation = "PASSED"
	msg = "The SPF record designates the host to be allowed to send, "+str(result[1])+"."
else:
	print("An error has occured. Please check your input or email contact@jaymarkpestano.ninja for more info.")

print("===== Result ===== ")
print("SPF Record is set to \""+result[0]+"\"")
print("Validation Test: "+evaluation)
print("Explanation: "+msg)
