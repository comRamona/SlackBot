import os
import sys
import time
from slackclient import SlackClient
import datetime
from duck import findImage
from bot_id import getBotId

API_key=sys.argv[1]
BOT_NAME=sys.argv[2]

slack_client = SlackClient(API_key)
BOT_ID = getBotId(API_key,BOT_NAME)

# constants
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"

    if "lunch" in command:
        lunch = datetime.time(12,30,0)
        current = datetime.datetime.now().time()
        lunch_time=lunch.hour*3600+lunch.minute*60+lunch.second
        current_time=current.hour*3600+current.minute*60+current.second
        add=""
        if(current_time>lunch_time):
            lunch_time=lunch_time+24*3600
            add="Try again tomorrow :( Lunch is in "
        time_diff=lunch_time-current_time
        h=int(time_diff/3600)
        m=int((time_diff-h*3600)/60)
        s=int(time_diff-h*3600-m*60)
        response = add+"%s hours, %s minutes and %s seconds" % (h,m,s)

    # returns an image link
    elif command.startswith('find'):
        search_for=command.split('find')[1].strip()
        response=str(findImage(search_for))

    elif command.startswith('calculate'):
        evaluate=command.split('calculate')[1].strip()
        x=eval(evaluate)
        response=str(x)

    else:
        response=str(findImage(command.strip()))

    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)





def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
