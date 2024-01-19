# to do: use windows installer via the installer sdk https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/
$cwd = Get-Location
$Time = New-ScheduledTaskTrigger -Daily -At 12:30:00 -RandomDelay (New-TimeSpan -Minutes 20)
$Action = New-ScheduledTaskAction -Execute "$cwd/checkin.exe" -WorkingDirectory "$cwd"
$Setting = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable -MultipleInstances Queue -RestartCount 4 -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -Force -TaskName "Hoyolab Check In" -Trigger $Time -Action $Action -Settings $Setting -Description "Hoyolab Daily Check-In Bot"