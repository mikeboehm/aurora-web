from settings_manager import SettingsManager

my_settings = SettingsManager()

settings = my_settings.get_settings()
print settings
# my_settings.set_settings(settings)