import config
import subprocess
import os
import error

def setupScheduler():
    pwd = os.getcwd()
    _config = config.read_config()
    hour = _config['run_time(24h)']
    minute = _config['delay_minute']
    ret_code = subprocess.call((
        f'powershell',
        f'$Time = New-ScheduledTaskTrigger -Daily -At {hour}:{minute}:00 \n',
        f'''$Action = New-ScheduledTaskAction -Execute "{os.path.join(pwd,'main.py')}" -WorkingDirectory "{pwd}" \n''',
        f'$Setting = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable -MultipleInstances Parallel -Priority 3 -RestartCount 30 -RestartInterval (New-TimeSpan -Minutes 1) \n',
        f'Register-ScheduledTask -Force -TaskName "{_config["schedule_name"]}" -Trigger $Time -Action $Action -Settings $Setting -Description "Hoyolab Daily Check-In Bot" -RunLevel Highest'
    ), creationflags=0x08000000)
    if ret_code != 0:
        error.show_error_message(f'at setupScheduler(), return code is {ret_code}')
    elif ret_code == 0:
        error.show_info('Scheduler set up successful')