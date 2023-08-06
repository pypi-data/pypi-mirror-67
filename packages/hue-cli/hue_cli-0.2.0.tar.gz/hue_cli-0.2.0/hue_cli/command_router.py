from hue_cli.command_types import (IdentifiableCommand,
                                   ValueCommand,
                                   EnumeratedCommand,
                                   InitializingCommand)

# Init is handled differently from the other commands
COMMANDS = {
    'init': (InitializingCommand, ['create_new_user', 'save_api_key']),
    'load': (InitializingCommand, ['load_existing', 'fetch_lights', 'fetch_groups', 'fetch_scenes']),
    'debug': (IdentifiableCommand, 'print_debug_info'),
    'list': (EnumeratedCommand, {
        'lights': 'list_lights',
        'groups': 'list_groups',
        "scenes": "list_scenes",
        'scene groups': 'list_scene_groups',
        '__default': 'list_lights'
    }),
    'on': (IdentifiableCommand, 'turn_on'),
    'off': (IdentifiableCommand, 'turn_off'),
    'toggle': (IdentifiableCommand, 'toggle_on'),
    'brightness': (ValueCommand, 'set_brightness'),
    'color': (ValueCommand, 'set_color')
}

class CommandRouter:

    def __init__(self, api):
        self.api = api

    def route_command(self, command, args):
        api = self.api
        if command == 'init':
            InitType, init_methods = COMMANDS.get('init')
            init_command = InitType(api, actions=init_methods, args=args)
            init_command()
            return
        InitType, init_methods = COMMANDS.get('load')
        init_command = InitType(api, actions=init_methods)
        Type, methods = COMMANDS.get(command)
        command = Type(api, actions=methods, args=args, init_command=init_command)
        command()
