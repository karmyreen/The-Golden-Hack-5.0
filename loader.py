import configparser

configParser = configparser.RawConfigParser()

def read_settings():
    configFilePath = r'./settings.cfg'
    configParser.read(configFilePath)
    settings_options = dict(configParser.items('Settings'))

    #SETTINGS

    WIDTH = settings_options['width']
    HEIGHT = settings_options['height']
    FPS = settings_options['fps']

    return int(WIDTH), int(HEIGHT), int(FPS)

def read_character():
    configFilePath = r'./character.cfg'
    configParser.read(configFilePath)
    settings_options = dict(configParser.items('Settings'))

read_settings()