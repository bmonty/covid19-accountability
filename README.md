# COVID-19 Accountability Reporter #

This script allows you to automate the submission of accountability reports while you self quarantine or shelter in place.  Reports are submitted using your email provider.

## Install ##
1. Get the script: `git clone https://github.com/bmonty/covid19-accountability.git`
1. Create a virtualenv: `python -m venv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install dependencies: `pip -r requirements.txt`
1. Create a configuration file.
1. _Optional:_ set up cron to run the tool.

## How to use ##

To submit a report:

```accountability.py -c config.yml```

## Configuration ##

Configuration of the tool is done using a YAML file.  The format of the configuration file is:

```
smtp:
  host: smtp.example.com     # this is your provider's SMTP hostname
  port: 587                  # check with your provider, likely 25 or 587
creds:
  username: test@example.com
  password: password1234
message:
  to:                        # this is where the report is sent
    - email1@work.com
    - email2@work.com
  from: test@example.com.    # your address
  subject: Accountability report for Bob
  body: |
    I am healthy!

    ---
    Bob
    test@example.com
```

NOTE: The tool will automatically append the current date to whatever value is provided for the subject line.

## Use with cron ##

Using `cron` allows for quick and easy automation of your accountability reporting.  Check your operating system's documentation for how to access and configure `cron`.

An example configuration to send a report once per day at 8:00AM on weekdays is:

`0 8 * * 1-5 /usr/bin/bash -c 'cd /home/user/project && source /home/user/project/.venv/bin/activate && ./accountability.py -c config.yml' > /dev/null 2>&1`
