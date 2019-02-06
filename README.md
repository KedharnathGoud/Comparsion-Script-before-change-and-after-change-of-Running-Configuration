# Comparsion-Script-before-change-and-after-change-of-Running-Configuration
Comparison-Script-before-change-and-after-change of Running Configuration

Script – –Changes Applied .py –

Author: Kedharnath E (goudkedharnath@gmail.com)

Language: Python

Devices supported: Cisco and Juniper Switches, Routers, WLCS
 
Q. Why do we need this script?
	
This script helps us with the changes which were made on the device before and after the scheduled   Change or MACDs. We already have the applications which does the same thing also which need a lot of time and keen observation line by line .This all can be done with the single click.


Q. What does this script do?

 This script will take the command output of show running (running configuration) for cisco or show configuration | no-more for Juniper devices and saves them as a txt file in the H drive under the folder names of LogOut_beforechange and LogOut_Afterchange , before and after change respectively.  Compares them and gives the output in detail. The scripts even prompts the outputs at each phase.

Q .How to use it?



Step 1: Please save (Changes applied.py) the below file in a folder 

Open secure CRT (script only works on secure CRT)

Step 2: Login to any of the device and get in to enable mode.
Step 3: Go to scripts tab-> Select Run- Choses the Changes applied.py file.
Step 4: Please select option 1 to take the Running configuration before change.

 
Step 5: Please chose the type of the router.
	1 for cisco 
	2 for juniper
 
Step 6: This Script will create a folder in C drive with Log output before change with the configuration. We can use this as a backup to.

After the change please take after change show run.

Step 7: Please select option 2 This Script will create a folder in C drive with Log output After change with the configuration.

Again run the same script with option 2

Step 8: Please chose the type of the router.
	1 for cisco 
	2 for juniper

Again run the same script with option 3

This script will compare two Configuration will provide the output.


There will be output generated in C drive as  
	Difference in Config: This will give you the output of what lines you have added and removed. 
	Differance in Config with complete config: This will give you complete config with the changes where you have made and what are the changes you have made.

Note:
'+' Represents the line you have added,
'-' Represents the line you have removed 
if you don’t see any line Then you haven't made any changes

if you’re working with more than 1 device please save the sh run config of the devices  and copy past them in the respective folders in the filename of LogOut_Afterchange and LogOut_Beforechange compare them. 




