#!/usr/bin/python3
import sys
import os
from time import sleep
os.system('clear')

logo = ('''
    \033[0;1m+\033[36;1m----------------------\033[0;1m+\033[0;1m
    \033[36;1m| \033[32mYOUTUBE \033[33;1m| \033[32mDOWNLOADER \033[36;1m|
    \033[0;1m+\033[36;1m----------------------\033[0;1m+''')

def main():
	try:
		print ('')
		print (logo)
		print ('')
		print ('\033[36;1m-------------------\033[0;1m')
		print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m MENU\033[0;1m:          ')
		print ('\033[36;1m-------------------\033[0;1m')
		print ('\033[0;1m[\033[31m1\033[0;1m]\033[32m install package')
		print ('\033[0;1m[\033[31m2\033[0;1m]\033[32m Youtube        ')
		print ('\033[0;1m[\033[31m0\033[0;1m]\033[31m Exit           ')
		print ('\033[36;1m-------------------\033[0;1m')
		print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Enter Number\033[0;1m:  ')
		choose = input('\033[34m=\033[31m>\033[0;1m: ')
		if choose == '1':
			print ('')
			sleep(2)
			os.system('cd test;sh install.sh')
			print ('')
			quit()
		elif choose == '2':
			os.system('clear')
			print ('')
			print (logo)
			print ('')
			print ('\033[0;1m[\033[31m?\033[0;1m]\033[32m Please insert a valid Video URL\033[0;1m: ')
			url = input('\033[34m=\033[31m>\033[0;1m: ')
			os.system('clear')
			print ('')
			print (logo)
			print ('')
			print ('\033[36;1m-----------------\033[0;1m')
			print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m MENU\033[0;1m:        ')
			print ('\033[36;1m-----------------\033[0;1m')
			print ('\033[0;1m[\033[31m1\033[0;1m]\033[32m Download MP3 ')
			print ('\033[0;1m[\033[31m2\033[0;1m]\033[32m Download MP4 ')
			print ('\033[36;1m-----------------\033[0;1m')
			print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Enter Number\033[0;1m:')
			download = input('\033[34m=\033[31m>\033[0;1m: ')
			def mp3():
				print ('')
				print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Downloading\033[31m...\033[0;1m')
				sleep(2)
				os.system('clear')
				os.system('youtube-dl --extract-audio --audio-format mp3 {0}'.format(url))
				print ('\033[36;1m---------------------------------')
				print ('\033[0;1m[\033[31m√\033[0;1m]\033[32m File Saved At ~/\033[33;1mDownloader')
				print ('')
				quit()

			def mp4():
				print ('')
				print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Downloading\033[31m...\033[0;1m')
				sleep(2)
				os.system('clear')
				os.system('youtube-dl -f mp4 --no-check-certificate {0}'.format(url))
				print ('\033[36;1m---------------------------------')
				print ('\033[0;1m[\033[31m√\033[0;1m]\033[32m File Saved At ~/\033[33;1mDownloader')
				print ('')
				quit()
			if '1' in download:
				mp3()
			if '2' in download:
				mp4()
			else:
				pass
		elif choose == '0':
			print ('')
			print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Thank you\033[0;1m')
		else:
			print ('\033[0;1m[\033[31m!\033[0;1m]\033[31m Wrong input')
			print ('')
			quit()
	except KeyboardInterrupt:
		print ('\033[0;1m[\033[31m!\033[0;1m]\033[31m Berhenti\033[0;1m')

def quit():
	cb = input('\033[0;1m[\033[31m?\033[0;1m]\033[32m Back to the Menu \033[32m(\033[0;1my\033[31m/\033[0;1mt\033[32m)\033[0;1m: ')
	if cb[0].upper() == 'T':
		print ('\033[0;1m[\033[31m+\033[0;1m]\033[32m Created By Edi ID\033[0;1m')
		sys.exit()
	else:
		os.system('clear')
		main()

if __name__ == '__main__':
	main()
