import json
class SettingsManager(object):
	def __init__(self):
		self.settings_file = 'settings.json'
	
	
	def get_settings(self):
		fp = open(self.settings_file, 'r')
		settings = json.load(fp)
		return settings
	
	def set_settings(self, settings):
		fp = open(self.settings_file, 'w')
		json.dump(settings, fp)
# 		settings = json.load(fp)
# 		return settings

