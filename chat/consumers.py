from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from urllib.parse import parse_qs
import json


@channel_session_user_from_http
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)

@channel_session_user
def ws_message(message):
    print(message.reply_channel.__dict__)
    Group("chat").send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.user.username,
        }),
    })

@channel_session_user
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
