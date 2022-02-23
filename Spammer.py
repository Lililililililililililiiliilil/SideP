import socket
import time
import re


def Spammerino(_NICK, _PASS, _CHAN, MESSAGE):
    HOST = "irc.chat.twitch.tv"  # the twitch irc server
    PORT = 6667  # always use port 6667
    NICK = _NICK  # twitch username, lowercase
    PASS = "oauth:" + _PASS  # your twitch OAuth token
    CHAN = "#" + _CHAN  # the channel you want to join

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {}\r\n".format(PASS).encode())
    s.send("NICK {}\r\n".format(NICK).encode())
    s.send("JOIN {}\r\n".format(CHAN).encode())

    def sendMessage(s, mes):
        messageTemp = "PRIVMSG " + CHAN + " :" + mes
        s.send((messageTemp + "\r\n").encode())
        print("Sent: " + messageTemp)

    sendMessage(s, MESSAGE)
    time.sleep(30)