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
    character_options = dict(configParser.items('character options'))
    character_colours = dict(configParser.items('colours'))

    # Unfinished


def read_save():
    configFilePath = r'./save.cfg'
    configParser.read(configFilePath)
    game_options = dict(configParser.items('Options'))
    game_progress = dict(configParser.items('Progress'))

    DIFFICULTY = game_options['difficulty']
    #we could use this to determine the speed the player moves at (faster being more difficult) and other things relating to the difficulty

    STEPS = game_progress['steps']
    MINIGAMES_CLEARED = game_progress['minigames_cleared']

    return DIFFICULTY, int(STEPS), int(MINIGAMES_CLEARED)