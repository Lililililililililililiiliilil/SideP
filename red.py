# Config portion
import socket
import time
import re

HOST = "irc.chat.twitch.tv"  # the twitch irc server
PORT = 6667  # always use port 6667
NICK = "shariahwkd"  # twitch username, lowercase
PASS = "oauth:bqzb11yk44qtis56c3265owu2xd607"  # your twitch OAuth token
CHAN = "#twilighi"  # the channel you want to join

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
s.send("PASS {}\r\n".format(PASS).encode())
s.send("NICK {}\r\n".format(NICK).encode())
s.send("JOIN {}\r\n".format(CHAN).encode())


# def chat(sock, msg):
#     '''
#     Send a chat message to the server.
#     sock -- the socket over which to send the message
#     msg -- the message to be sent
#     '''
#     sock.send("PRIVMSG {} :{}".format(CHAN, msg))


def sendMessage(s, mes):
    messageTemp = "PRIVMSG " + CHAN + " :" + mes
    s.send((messageTemp + "\r\n").encode())
    print("Sent: " + messageTemp)



# Make sure you prefix the quotes with an 'r'
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:
    response = s.recv(1024).decode("utf-8")
    print(response)
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode())
        print("Pong")
    else:
        username = re.search(r"\w+", response).group(0)  # return the entire
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)

    # chat(s, 'sosi\r\n'.encode('utf-8'))

    sendMessage(s, 'привет')
    time.sleep(1 / RATE)


