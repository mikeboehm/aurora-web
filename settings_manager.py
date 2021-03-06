import json


class SettingsManager(object):
    def __init__(self):
        import sys

        self.settings_file = sys.path[0] + '/settings.json'


    def get_settings(self):
        try:
            fp = open(self.settings_file, 'r')
            settings = json.load(fp)
        except:
            fp = open(self.settings_file + '.default', 'r')
            settings = json.load(fp)
            self.set_settings(settings)

        return settings

    def set_settings(self, settings):
        fp = open(self.settings_file, 'w')
        json.dump(settings, fp)
