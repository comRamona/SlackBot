# SlackBot
A simple slack bot to answer some queries

First, create a virtual environment which python2:

virtualenv -p /usr/bin/python2.6 venv
source venv/bin/activate
pip install requirements

Update your slack api key in the print_bot_id file, get your bot id and update both
api key and bot id in bot.py. Then you can run
python bot.py.

What it does:
On slack, run:
@cocobot: calculate (2+2)   -> evaluates
@cocobot: find cat ->returns pictures of cats
@cocobot: when is lunch ->returns time until 12:30

Find commands are the most fun :)
