# Get the Stack Overflow Fanatic badge with Golden Bot :trophy:

This bot will help you to get the golden badge on Stack Overflow... and hopefully teach you 
something about Python!

Golden Bot:
1) Visits Stack Overflow and logs in to your account.
2) Views your profile and check the visits' consecutive days counter.
3) Sends you an email with a report:

![email screenshot](https://i.ibb.co/VN4nr3w/so-bot.png)

## Installation

If you're using AWS ec2 instance with the Amazon AMI image, you can run `installs_aws_ec2.sh` (with sudo) for steps 1 and 2.

Manual steps:

1. Install the Chrome browser.
2. Install chromedriver (must be available in your `PATH`). Useful [tutorial for Linux](https://makandracards.com/makandra/29465-install-chromedriver-on-linux).
3. Install Python modules:

``` sudo pip install -r requirements.txt```

4. Modify `config.json` with your credentials. Use a gmail account to send the email.

## Setup a cronjob
 
1. You can verify that the bot is working by running it directly with `python golden_bot.py` and
checking the specified receiver mailbox.
2. Setup a cronjob in your machine that will run the bot daily. Type `crontab -e` and add the following line at the end of the 
file (will run the bot at 9am in the machine's timezone):

```0 9 * * * source /home/ec2-user/.bash_profile && python /home/ec2-user/stackoverflow_golden_bot/golden_bot.py```

**NOTE:** Adjust the paths in the above line. `.bash_profile` (or other similar file) should contain all the
environmental variables.


