import guessing_game
import conda.plugins


def conda_guessing_game(*args, **kwargs):
    guessing_game.guess()


@conda.plugins.register
def conda_subcommands():
    yield conda.plugins.CondaSubcommand(
        name="guessing-game",
        summary="A subcommand that invokes a guessing game",
        action=conda_guessing_game,
    )
