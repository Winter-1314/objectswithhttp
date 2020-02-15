"""

"""
import requests


class Coding_Langs:
    def __init__(self, name, url):
        """

        :param name:
        :type name:
        :param url:
        :type url:
        """
        self.name = name
        self.url = url
        self.html = requests.get(self.url).text
