import os
from configparser import ConfigParser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini")
conf = ConfigParser.ConfigParser()
conf.read(configPath)

smtp_server = conf.get("email", "smtp_server")

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")


# from configparser import ConfigParser
#
# class ReadConfig:
#     def __init__(self):
#         self.config = ConfigParser()
#         self.config.read('./config.ini')
#
#     def get_server(self, name):
#         print(self.config.sections())
#         values = self.config.get('testServer', name)
#         return values
#
#     def db_server(self, name):
#         print(self.config.sections())
#         values = self.config.get('DBServer', name)
#         return values


