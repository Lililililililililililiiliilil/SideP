import requests
import json
import socket
import time
import re
from Spammer import Spammerino


class TwitchFollower:
    def __init__(self, channel):
        self.channel = channel
        self.tokens_path = "tokens.txt"
        self.total_follows = 0
        self.HEADERS = {
            "content-type": "application/json",
            "accept": "application/json",
            "accept-charset": "utf-8",
            "accept-encoding": "br, gzip, deflate",
        }

    def _update_header(self, token):
        self.HEADERS['Authorization'] = 'OAuth ' + token

    def _get_tokens(self):
        with open(self.tokens_path, 'r', encoding='utf-8') as f:
            tokens = [line.strip('\n') for line in f]
        return tokens

    def _get_logins(self):
        with open('logins.txt', 'r', encoding='utf-8') as f:
            logins = [line.strip('\n') for line in f]
        return logins

    def _get_channel_id(self):
        access_token = "qecxhnjevnnfvskhhd07od91yliqti"
        self._update_header(access_token)
        url = f'https://api.twitch.tv/api/channels/{self.channel}/access_token?need_https=true&oauth_token={access_token}'

        channel_info = requests.get(url, headers=self.HEADERS)

        try:
            token_info = channel_info.json()['token']
            channel_id = json.loads(token_info)['channel_id']
            return str(channel_id)
        except KeyError:
            print("User not found")
            return False

    def run(self):
        channel_id = self._get_channel_id()
        payload = r'[{"operationName":"FollowButton_FollowUser",' \
                  r'"variables":{"input":{"disableNotifications":false,"targetID":"' + channel_id + r'"}},' \
                                                                                                    r'"extensions":{' \
                                                                                                    r'"persistedQuery":{"version":1,' \
                                                                                                    r'"sha256Hash' \
                                                                                                    r'":"51956f0c469f54e60211ea4e6a34b597d45c1c37b9664d4b62096a1ac03be9e6"}}}] '
        for token in self._get_tokens():
            self._update_header(token)
            r = requests.post('https://gql.twitch.tv/gql', data=payload, headers=self.HEADERS)
            self.total_follows += 1 if not "error" in r.text and not '"follow":null' in r.text else False
        print(f"Added {self.total_follows} followers to {self.channel}")

    def spam(self):
        channel_id = self._get_channel_id()

        for token, login in zip(self._get_tokens(), self._get_logins()):
            Spammerino(login, token, channel_name, 'sosi')


if __name__ == '__main__':
    channel_name = input("Twitch channel: ")
    TwitchFollower(channel_name).spam()
