import json
from pathlib import Path
from typing import Dict
from enum import Enum
from collections import namedtuple

import click
from poetry.factory import Factory
from poetry.utils.env import EnvManager


class Target(Enum):
    VSCODE = "vscode"
    COC = "coc"


Config = namedtuple("Config", ["dir_name", "file_name", "commands"])


COMMANDS = {
    "python.pythonPath": "python",
    "python.jediPath": "jedi",
    "python.dataScience.ptvsdDistPath": "ptvsd",
    "python.formatting.blackPath": "black",
    "python.formatting.autopep8Path": "autopep8",
    "python.formatting.yapfPath": "yapf",
    "python.linting.banditPath": "bandit",
    "python.linting.flake8Path": "flake8",
    "python.linting.mypyPath": "mypy",
    "python.linting.prospectorPath": "prospector",
    "python.linting.pycodestylePath": "pycodestyle",
    "python.linting.pylamaPath": "pylama",
    "python.linting.pydocstylePath": "pycodestyle",
    "python.linting.pylintPath": "pylint",
    "python.sortImports.path": "isort",
    "python.testing.nosetestPath": "nosetest",
}


def write_settings(
    path_to_root: Path, dir_name: str, file_name: str, settings: Dict[str, str]
) -> None:
    setting_dir_path = path_to_root / dir_name
    setting_dir_path.mkdir(exist_ok=True)

    setting_json_path = setting_dir_path / file_name
    try:
        cur_settings = json.loads(setting_dir_path.read_text())
    except OSError:
        cur_settings = {}

    settings = {**cur_settings, **settings}
    settings_json_str = json.dumps(settings, indent=4)
    setting_json_path.write_text(settings_json_str)


def detect_commands(env_manager, target_commands: Dict[str, str]) -> Dict[str, str]:
    settings = {}
    for key, command in target_commands.items():
        command_path = env_manager.get().path / "bin" / command
        if command_path.exists():
            settings[key] = str(command_path)
    return settings


def get_config(target: Target) -> Config:
    if target == Target.VSCODE:
        return Config(".vscode", "settings.json", COMMANDS)
    elif target == Target.COC:
        return Config(".vim", "coc-settings.json", COMMANDS)

    raise NotImplemented(f"{target} is not supported.")


def cast_target(ctx, param, value: str) -> Target:
    return Target(value)


@click.command()
@click.option(
    "--target",
    type=click.Choice(["vscode", "coc"]),
    default="vscode",
    callback=cast_target,
)
def main(target: Target) -> None:
    poetry = Factory().create_poetry(Path.cwd())
    env_manager = EnvManager(poetry)

    config = get_config(target)

    settings = detect_commands(env_manager, config.commands)

    path_to_root = poetry.file.path.parent
    write_settings(path_to_root, config.dir_name, config.file_name, settings)

    settings_json_str = json.dumps(settings, indent=4)
    click.echo(settings_json_str)
