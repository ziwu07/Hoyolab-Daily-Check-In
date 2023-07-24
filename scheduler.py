import config
import subprocess
import os
import error

def setupScheduler():
    pwd = os.getcwd()
    _config = config.read_config()
    hour = _config['run_time(24h)']
    minute = _config['delay_minute']
    pythonw_path = os.path.join(pwd, 'venv', 'Scripts', 'pythonw.exe')
    main_py_path = os.path.join(pwd, 'main.py')
    delay = _config['random_delay']
    powershell_script = (
        f'$Time = New-ScheduledTaskTrigger -Daily -At {hour}:{minute}:00 -RandomDelay 00:{delay}:00 \n'
        f'$Action = New-ScheduledTaskAction -Execute "{pythonw_path}" -Argument "{main_py_path}" -WorkingDirectory "{pwd}" \n'
        f'$Setting = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable -MultipleInstances Parallel -Priority 3 -RestartCount 30 -RestartInterval (New-TimeSpan -Minutes 1) \n'
        f'Register-ScheduledTask -Force -TaskName "{_config["schedule_name"]}" -Trigger $Time -Action $Action -Settings $Setting -Description "Hoyolab Daily Check-In Bot" -RunLevel Highest'
    )

    try:
        completed_process = subprocess.run(['powershell', '-Command', powershell_script], capture_output=True, text=True, check=True)
        error_output = completed_process.stderr
        if error_output:
            error.show_error_message(f'Error while setting up the scheduler: {error_output}')
        else:
            error.show_info('Scheduler set up successfully')
    except subprocess.CalledProcessError as e:
        error.show_error_message(f'Error while setting up the scheduler. Return code: {e.returncode}, Output: {e.stdout}, Error: {e.stderr}')
    except Exception as e:
        error.show_error_message(f'Unknown error occurred: {e}')


if __name__ == "__main__":
    setupScheduler()