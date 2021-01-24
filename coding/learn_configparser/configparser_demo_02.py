# -*- coding: utf-8 -*-
import configparser

config = configparser.ConfigParser()
print(config.sections())

config.read("example.ini")
print(config.sections())

print('bitbucket.org' in config)
print('bytebong.com' in config)

print(config['bitbucket.org']['User'])
print(config['DEFAULT']['Compression'])

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])
print(topsecret['Port'])

for key in config['bitbucket.org']:
    print(key)

print(config['bitbucket.org']['ForwardX11'])

print(topsecret.getboolean('ForwardX11'))
print(config['bitbucket.org'].getboolean('ForwardX11'))
print(config.getboolean('bitbucket.org', 'Compression'))

print(topsecret.get('Port'))
print(topsecret.get('CompressionLevel'))
print(topsecret.get('Cipher'))
print(topsecret.get('Cipher', '3des-cbc'))
print(topsecret.get('CompressionLevel', '3'))

print(config.get('bitbucket.org', 'monster', fallback='No such things as monsters'))

print('BatchMode' in topsecret)
print(topsecret.getboolean('BatchMode', fallback=True))
config['DEFAULT']['BatchMode'] = 'no'
print(topsecret.getboolean('BatchMode', fallback=True))
