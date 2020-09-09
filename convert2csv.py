import serial
import csv   
f = open("logfile.txt", "rb")
file2 = open("logfile.csv", "w")
ba = bytearray(f.read())
cnt = -1
string = ""
for byte in ba:
	cnt+=1
	if(cnt==0):
		# print(str(byte))
		string+=str(byte)
		string+=','
		
	if(cnt==1):
		string+=str(byte)
		string+=','
	if(cnt==2):
		string+=str(byte)
		string+=','
	if(cnt==3):
		string+=str(byte)
		string+=','
	if(cnt==4):
		string+=str(byte)
		string+=','
	if(cnt==5):
		string+=str(byte)
		string+=','
	if(cnt==6):
		string+=str(byte)
		string+=','
	if(cnt==7):
		string+=str(byte)
		string+=','
	if(cnt==8):
		string+=str(byte)
		string+=','
	if(cnt==9):
		string+=str(byte)
		string+='\n'
		cnt=-1
		file2.write(string)
		string=""

f.close()
file2.close()