import configparser
import self as self
import json

configParser = configparser.RawConfigParser()
configParser.read(r'settings.py')
i = configParser.get('common', 'output')

print(i)
self.path = configParser.get('common', 'interval')
print(self.path)
newdict = {'success': True, 'data': "Hello"}
json.dumps(newdict)
print(json.dumps(newdict))
