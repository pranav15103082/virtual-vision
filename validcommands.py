from Commands.mswordcommands import mswordcommandset
from Commands.systemcommands import systemcommandset
from Commands.browsercommands import browsercommandset

class commands:
    mswordActivator = False
    browserActivator = False
    systemcommandsActivator = False

    systemcommands = systemcommandset
    mswordcommands = mswordcommandset
    browsercommands = browsercommandset

    @staticmethod
    def activatesystemcommandset():
        commands.mswordActivator = False
        commands.browserActivator = False
        commands.systemcommandsActivator = True

    @staticmethod
    def activatemswordcommandset():
        commands.activatesystemcommandset()
        commands.systemcommandsActivator = False
        commands.mswordActivator = True

    @staticmethod
    def activatebrowsercommandset():
        commands.activatesystemcommandset()
        commands.systemcommandsActivator = False
        commands.browserActivator = True

    @staticmethod
    def givecommands():
        if commands.mswordActivator is True:
            return commands.mswordcommands
        elif commands.systemcommandsActivator is True:
            return commands.systemcommands
        elif commands.browserActivator is True:
            return commands.browsercommands
