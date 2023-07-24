import config
import subprocess
import os
import error

def setupScheduler():
    pwd = os.getcwd()
    _config = config.read_config()
    hour = _config['run_time(24h)']
    minute = _config['delay_minute']
    reset_timezone = str(_config['reset_timezone(UTC)'])
    pythonw_path = os.path.join(pwd, 'venv', 'Scripts', 'pythonw.exe')
    main_py_path = os.path.join(pwd, 'main.py')
    ret_code = subprocess.call((
        f'powershell',
        f'$Time = New-ScheduledTaskTrigger -Daily -At {hour}:{minute}:00+{reset_timezone} \n',
        f'''$Action = New-ScheduledTaskAction -Execute "{pythonw_path}" -Argument "{main_py_path}" -WorkingDirectory "{pwd}" \n''',
        f'$Setting = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable -MultipleInstances Parallel -Priority 3 -RestartCount 30 -RestartInterval (New-TimeSpan -Minutes 1) \n',
        f'Register-ScheduledTask -Force -TaskName "{_config["schedule_name"]}" -Trigger $Time -Action $Action -Settings $Setting -Description "Hoyolab Daily Check-In Bot" -RunLevel Highest'
    ), creationflags=0x08000000)
    if ret_code != 0:
        error.show_error_message(f'at setupScheduler(), return code is {ret_code}')
    elif ret_code == 0:
        error.show_info('Scheduler set up successful')

if __name__ == "__main__":
    setupScheduler()