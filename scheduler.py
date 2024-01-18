import sys, config, subprocess, os, error


def register():
    """install task to windows task scheduler"""
    pwd = os.getcwd()
    _config = config.load()
    hour = _config.run_time_24h
    minute = _config.delay_minute
    pythonw_path = os.path.join(pwd, "venv", "Scripts", "pythonw.exe")
    main_py_path = os.path.join(pwd, "main.py")
    delay = _config.random_delay
    powershell_script = (
        f"$Time = New-ScheduledTaskTrigger -Daily -At {hour}:{minute}:00 -RandomDelay (New-TimeSpan -Minutes {delay}) \n"
        f'$Action = New-ScheduledTaskAction -Execute "{pythonw_path}" -Argument "{main_py_path}" -WorkingDirectory "{pwd}" \n'
        f"$Setting = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -RunOnlyIfNetworkAvailable -MultipleInstances Queue -RestartCount 4 -RestartInterval (New-TimeSpan -Minutes 1) \n"
        f'Register-ScheduledTask -Force -TaskName "{_config.schedule_name}" -Trigger $Time -Action $Action -Settings $Setting -Description "Hoyolab Daily Check-In Bot" -RunLevel Highest'
    )

    try:
        completed_process = subprocess.run(
            ["powershell", "-Command", powershell_script],
            capture_output=True,
            text=True,
            check=True,
        )
        error_output = completed_process.stderr
        if error_output:
            error.crash(f"Error while setting up the scheduler: {error_output}")
        else:
            error.show_info("Scheduler set up successfully")
    except subprocess.CalledProcessError as e:
        error.crash(
            f"Error while setting up the scheduler. Return code: {e.returncode}, Output: {e.stdout}, Error: {e.stderr}"
        )
    except Exception as e:
        error.crash(f"Unknown error occurred: {e}")


def unregister():
    """remove task from windows task scheduler"""
    _config = config.load()
    ps_script = (
        f"Unregister-ScheduledTask -Confirm False -TaskName {_config.schedule_name}"
    )


file_name = os.path.basename(sys.argv[0])


def help():
    """print the help menu"""
    print(f"usage: {file_name} <Command>\n\nCommands:")
    values = globals()
    names = list(values.keys())
    names.sort()
    for name in names:
        if callable(values[name]):
            print(f"    {name: <12}{values[name].__doc__}")


if __name__ == "__main__":
    try:
        globals()[sys.argv[1]]()
    except IndexError as e:
        help()
    except KeyError as e:
        print(
            f"{file_name}: '{sys.argv[1]}' is not a valid command. See '{file_name} help'\n"
        )
