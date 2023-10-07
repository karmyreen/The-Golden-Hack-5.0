import configparser
def read_config():
    configParser = configparser.RawConfigParser()
    configFilePath = r'./codeguesser.cfg'
    configParser.read(configFilePath)
    fixes_options = dict(configParser.items('Fixes'))
    dev_options = dict(configParser.items('Dev'))
    settings_options = dict(configParser.items('Settings'))

    #FIXES
    global is_iterm2
    is_iterm2 = fixes_options['is_iterm2']

    #DEV
    global enable_debugging_check
    global enable_debugging
    enable_debugging_check = dev_options['enable_debugging']
    if enable_debugging_check == "True":
        enable_debugging = True
    else:
        enable_debugging = False

    #SETTINGS
    
    global start_screen_check
    global start_screen
    start_screen_check = settings_options['start_screen']
    if start_screen_check == "True":
        start_screen = True

    global viewing_lenght
    viewing_lenght = settings_options['viewing_timer_lenght']

    global num_turns
    num_turns = settings_options['number_of_turns']

    global snippet_color
    snippet_color = settings_options['snippet_text_color']
