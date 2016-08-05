# SlackBot
A simple slack bot to answer some queries

First, create a virtual environment which python2:
```
virtualenv -p /usr/bin/python2.6 venv
source venv/bin/activate
pip install -r requirements.txt
```
Get your slack API_key and create a new bot. Run bot.py with api_key and name of bot as arguments.
```
python bot.py apikey slackbotname
```

You should see:
```
StarterBot connected and running!
```

What it does:
On slack, run:
```
@cocobot: calculate (2+2)   -> evaluates
@cocobot: find cat ->returns pictures of cats
@cocobot: when is lunch ->returns time until 12:30
```
Find commands are the most fun :)
