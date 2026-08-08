# Hoyolab Daily Check-In

Automated daily sign-in for Genshin Impact, Honkai: Star Rail, and Zenless Zone Zero via the Hoyolab API.

## Features

- Automatic daily login reward claim for all three Hoyoverse games
- Persistent cookie storage to avoid re-login
- Systemd timer support for fully scheduled, hands-free operation
- Single dependency: `pywebview[qt]` to retrieve fresh cookies via login webview

## Installation

1. Install the dependency:

    **Arch Linux based**

    ```
    sudo pacman -S python-pywebview python-qtpy
    ```

    **Other distros / manual install**

    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install pywebview[qt]
    ```

2. (Recommended) Set up the systemd timer to run the check-in daily at noon:

   ```
   cp hoyolab-checkin.{service,timer} ~/.config/systemd/user/
   ```

   **Edit `~/.config/systemd/user/hoyolab-checkin.service`** and update the `WorkingDirectory` line to match the actual project path.

3. Enable and start the timer:

   ```
   systemctl --user enable --now hoyolab-checkin.timer
   ```

## Usage

Run the script manually:

```
python check_in.py
```

**First run** — A Qt webview window will open prompting you to log in to your Hoyolab account. After logging in, click **Actions → Get Cookies** in the window menu. The script will then attempt to claim daily rewards for each enabled game.

**Subsequent runs** — The saved cookie file is reused, so no browser window will appear.

With the systemd timer installed (see Installation above), the script runs automatically every day at 12:00.

## Configuration

Edited `config.json` to enable or disable sign-in per game:

```json
{
    "genshin": true,
    "star_rail": true,
    "zzz": true
}
```

Set any game to `false` to skip its daily claim. If `config.json` doesn't exist yet, the script creates one with all games enabled on first run.

## Uninstall

To remove the systemd timer, stop and disable it, then delete the unit files:

```
systemctl --user stop hoyolab-checkin.timer
systemctl --user disable hoyolab-checkin.timer
rm ~/.config/systemd/user/hoyolab-checkin.{service,timer}
```

## Cookies

- Cookies are stored in `./Cookies` in LWFormat format. They are git-ignored.
- `webview_storage/` and `logfile.log` are also git-ignored and contain no sensitive credentials.
- If the cookie expires or the API returns a `-100` retcode, the script will automatically re-open the webview to refresh them.
- Do not share or commit `./Cookies` as it contains your session cookies.
