import chord_cli
import conda.plugins
import sys


def conda_chord_cli(*args, **kwargs):
    note = sys.argv[-1]
    return chord_cli.main(note)


@conda.plugins.register
def conda_subcommands():
    yield conda.plugins.CondaSubcommand(
        name="chord-cli",
        summary="A subcommand that displays guitar chords",
        action=conda_chord_cli,
    )
