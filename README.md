# Hoyolab-Daily-Check-In



## Files

**checkin.exe**: the main exe
**scheduler.ps1**: create a task register to run at 12:30:00 with a random delay of 20 mins
**uninstall_scheduler.ps1**: remove the created task scheduler
**config.json**: config file, edit this before runing the task scheduler script
**logfile.log**: log file

## info

**This project is in beta!**
this uses microsoft webview2 to get your login cookie, it will save the cookie whenever it can

## Install

run **MicrosoftEdgeWebview2Setup.exe**
then **scheduler.ps1** to setup scheduler

### uninstall

**uninstall_scheduler.ps1** to remove the scheduler
if you want to uninstall webview2 then go to settings and uninstall the app from there