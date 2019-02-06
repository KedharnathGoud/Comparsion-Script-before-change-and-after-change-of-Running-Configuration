#$language = "python"
#$interface = "1.0"


#Written by: Kedharnath.E (goudkedharnath@gmail.com)

import os
import subprocess
import difflib


def Main():	

	def NN(number, digitCount):
		# Normalizes a single digit number to have digitCount 0s in front of it
		format = "%0" + str(digitCount) + "d"
		return format % number 
	def LaunchViewer(filename):
		try:
			os.startfile(filename)
		except AttributeError:
			subprocess.call(['open', filename])
	router=""
	opt=""
	crt.Screen.Synchronous = True  
	opt=crt.Dialog.Prompt('Please select your option \n\n 1= Before Change show run  \n \n 2=After Change show run  \n \n 3= Compare \n', 'Enter Your option', opt)
	LOG_DIRECTORY=""
	router=crt.Dialog.Prompt('Please Select the type of router \n\n 1=Cisco \n\n 2=Juniper  \n\n', 'Enter Your Option', router)
	y=''
	x=''
	if opt=='1':	
		LOG_DIRECTORY = os.path.join(
		os.path.expanduser('~'), 'C:\LogOut_beforechange')
		LOG_FILE_TEMPLATE = os.path.join(
		LOG_DIRECTORY, "Command_%(NUM)s_Results.txt")
		if not os.path.exists(LOG_DIRECTORY):
			os.mkdir(LOG_DIRECTORY)
			
		if not os.path.isdir(LOG_DIRECTORY):
			crt.Dialog.MessageBox(
			"Log output directory %r is not a directory" % LOG_DIRECTORY)
			return
	elif opt=='2':
		LOG_DIRECTORY = os.path.join(
		os.path.expanduser('~'), 'C:\LogOut_Afterchange')
		LOG_FILE_TEMPLATE = os.path.join(
		LOG_DIRECTORY, "Command_%(NUM)s_Results.txt")
		if not os.path.exists(LOG_DIRECTORY):
			os.mkdir(LOG_DIRECTORY)
			
		if not os.path.isdir(LOG_DIRECTORY):
			crt.Dialog.MessageBox(
			"Log output directory %r is not a directory" % LOG_DIRECTORY)
			return
	

	SCRIPT_TAB = crt.GetScriptTab()
	
		
	if not opt=='3':
		crt.Screen.Send("ter len 0\n" + chr(13))
		COMMANDS = [
	
	
			"sh run\n ",
			#	"",
			#	"",
		]
	
		COMMANDS2 = [
	
	
			"show configuration | no-more | display set    \n ",
		#	"",
		#	"",
		]
		
		if not SCRIPT_TAB.Session.Connected:
			crt.Dialog.MessageBox(
				"Not Connected.  Please connect before running this script.")
			return

	# Instruct WaitForString and ReadString to ignore escape sequences when
	# detecting and capturing data received from the remote (this doesn't
	# affect the way the data is displayed to the screen, only how it is handled
	# by the WaitForString, WaitForStrings, and ReadString methods associated
	# with the Screen object.
		SCRIPT_TAB.Screen.IgnoreEscape = True
		SCRIPT_TAB.Screen.Synchronous = True

	# If this script is run as a login script, there will likely be data
	# arriving from the remote system.  This is one way of detecting when it's
	# safe to start sending data. If this script isn't being run as a login
	# script, then the worst it will do is seemingly pause for one second
	# before determining what the prompt is.
	# If you plan on supplying login information by waiting for username and
	# password prompts within this script, do so right before this while loop.
		while True:
			if not SCRIPT_TAB.Screen.WaitForCursor(1):
				break
	# Once the cursor has stopped moving for about a second, we'll
	# assume it's safe to start interacting with the remote system.
	
	# Get the shell prompt so that we can know what to look for when
	# determining if the command is completed. Won't work if the prompt
	# is dynamic (e.g. changes according to current working folder, etc)
		rowIndex = SCRIPT_TAB.Screen.CurrentRow
		colIndex = SCRIPT_TAB.Screen.CurrentColumn - 1

		prompt = SCRIPT_TAB.Screen.Get(rowIndex, 0, rowIndex, colIndex)
		prompt = prompt.strip()
		if router=='1':
		
			for (index, command) in enumerate(COMMANDS):
				command = command.strip()

	# Set up the log file for this specific command
				logFileName = LOG_FILE_TEMPLATE % {"NUM" : NN(index + 1, 2)}
		
		# Send the command text to the remote
				SCRIPT_TAB.Screen.Send(command + '\r')

		# Wait for the command to be echo'd back to us.
				SCRIPT_TAB.Screen.WaitForString('\r', 1)
				SCRIPT_TAB.Screen.WaitForString('\n', 1)

		# Use the ReadString() method to get the text displayed while
		# the command was runnning.  Note also that the ReadString()
		# method captures escape sequences sent from the remote machine
		# as well as displayed text.  As mentioned earlier in comments
		# above, if you want to suppress escape sequences from being
		# captured, set the Screen.IgnoreEscape property = True.
				result = SCRIPT_TAB.Screen.ReadString(prompt)
				result = result.strip()
		
				filep = open(logFileName, 'wb+')

		# If you don't want the command logged along with the results, comment
		# out the very next line
			#filep.write("Results of command: " + command + os.linesep)

		# Write out the results of the command to our log file
				filep.write(result + os.linesep)
		
		# Close the log file
			filep.close()
			LaunchViewer(LOG_DIRECTORY)
	# Once we're complete, let's bring up the directory containing the
	# log files.
		elif router=='2':
			for (index, command) in enumerate(COMMANDS2):
				command = command.strip()

	# Set up the log file for this specific command
				logFileName = LOG_FILE_TEMPLATE % {"NUM" : NN(index + 1, 2)}
		
		# Send the command text to the remote
				SCRIPT_TAB.Screen.Send(command + '\r')

		# Wait for the command to be echo'd back to us.
				SCRIPT_TAB.Screen.WaitForString('\r', 1)
				SCRIPT_TAB.Screen.WaitForString('\n', 1)

		# Use the ReadString() method to get the text displayed while
		# the command was runnning.  Note also that the ReadString()
		# method captures escape sequences sent from the remote machine
		# as well as displayed text.  As mentioned earlier in comments
		# above, if you want to suppress escape sequences from being
		# captured, set the Screen.IgnoreEscape property = True.
				result = SCRIPT_TAB.Screen.ReadString(prompt)
				result = result.strip()
		
				filep = open(logFileName, 'wb+')

		# If you don't want the command logged along with the results, comment
		# out the very next line
			#filep.write("Results of command: " + command + os.linesep)

		# Write out the results of the command to our log file
				filep.write(result + os.linesep)
		
		# Close the log file
				filep.close()
			LaunchViewer(LOG_DIRECTORY)
		else :
				crt.Dialog.MessageBox("!! Wrong input !!\n" + chr(13))
				return "Wrong input"	
			
	# Once we're complete, let's bring up the directory containing the
	# log files.
		



	elif opt=='3':
		with open('C:\LogOut_beforechange\Command_01_Results.txt') as text1:
			with open('C:\LogOut_Afterchange\Command_01_Results.txt') as text2:
				d = difflib.Differ()
				diff = list(d.compare(text1.readlines(), text2.readlines()))
				with open('C:\Differance in Config with complete config.txt', 'w+') as diff_file:
					_diff = ''.join(diff)
					diff_file.write(_diff)
					ff=open('C:\Differance in Config with complete config.txt', 'r')
					_line = ''
					f= open("C:\Differance in Config.txt","w+")
					f.write("## Note:'+' Represents the line you have added,\n '-' Represents the line you have removed if you don’t see any line expect this\n Then you haven't made any changes# If a '-' is follwed '+' then you have replaced the line with - by + \n##" )
					for line in ff:
						if router=='2':
							if line.startswith('      '):
								if not line.startswith('       '):
									y=line
						if line.startswith('  '):
							if not line.startswith('   '):
								x=line
								#f.write(x)
						if line.startswith('-'):
							_d = '-'
							_line = line
							if router=="1":
								f.write(x)
								f.write(_line)
							else:
								f.write("on"+y)
								f.write(_line)
						elif line.startswith('+'):
							_d = '+'
							_line = line
							#f.write(x)
							f.write(_line)
					# if line.startswith('?'):
						#dp = line.find(_d)
						#dp=_line
						#f.write(_line)
						#if dp == -1:
							#_d = '+'
							#dp = line.find('^')
							#dpl = _line.rfind(',', 0, dp)
							#if dpl == -1:
							  # dpl = 2
							#else:
							#   dpl += 1
							 #  dpr = _line.find(',', dp)
							#   if dpr == dp:
								#   _d = ' '
								 #  dpl = dp
					              #  dpr = dp+1

				               # dpw = dpr - dpl
				               # line = line[:dpl] + _d*dpw + line[dpr:]
						#_line = line
				       # f.write(_line)
		LaunchViewer("C:\Differance in Config.txt")
	else :	
		crt.Dialog.MessageBox("!! Wrong input !!\n" + chr(13))
		return "Wrong input"
	#LaunchViewer("C:\Differance in Config with complete config.txt")
	

Main()
