#!python

import argparse
from datetime import datetime
import yaml
from smtplib import SMTP
from email.message import EmailMessage

def create_msg(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

if __name__ == '__main__':
    # parse command line arg
    parser = argparse.ArgumentParser(description="COVID-19 Accountability Reporter")
    parser.add_argument("-c", "--config",
                        required=True,
                        dest="config_file",
                        help="YAML file with configuration settings")
    args = parser.parse_args()

    # parse configuration
    with open(args.config_file, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)

    # send message
    with SMTP(config["smtp"]["host"], config["smtp"]["port"]) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(config["creds"]["username"], config["creds"]["password"])
        smtp.send_message(
          create_msg(
            from_address=config["message"]["from"],
            to_address=",".join(config["message"]["to"]),
            subject=f'{config["message"]["subject"]} ({datetime.now().strftime("%d %b %Y")})',
            body=config["message"]["body"]
          )
        )

    print('Email sent successfully')

