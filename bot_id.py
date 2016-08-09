import os
from slackclient import SlackClient


def getBotId(API_key, BOT_NAME):
    slack_client = SlackClient(API_key)
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                return user.get('id')
    else:
        return ""
