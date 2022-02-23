# Config portion
import socket
import time
import re

HOST = "irc.chat.twitch.tv"  # the twitch irc server
PORT = 6667  # always use port 6667
NICK = "fuzzybottgaming"  # twitch username, lowercase
PASS = 'OAuth ' + 'obywswxi37w161vrcmyxqg02x38kx6'  # your twitch OAuth token
CHAN = "twilighi"  # the channel you want to join

# Message Rate
RATE = (20 / 30)  # messages per second

# BANN HAMMER
PATT = [
    r"swear",
    # ...
    r"some_pattern"
]

# bot.py portion
# Network functions go here

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))


def chat(sock, msg):
    '''
    Send a chat message to the server.
    sock -- the socket over which to send the message
    msg -- the message to be sent
    '''
    sock.send("PRIVMSG #{} :{}".format(CHAN, msg))


def ban(sock, user):
    '''
    Ban a user from the current channel.
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    '''
    chat(sock, ".ban {}".format(user))





# Make sure you prefix the quotes with an 'r'
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

s.send("PONG :tmi.twitch.tv \r\n".encode("utf-8"))
