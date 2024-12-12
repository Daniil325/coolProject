from dishka import Provider, Scope, provide

from infra.usecases import TakeCommand


class CommandsProvider(Provider):
    scope = Scope.REQUEST

    take_command = provide(TakeCommand)
