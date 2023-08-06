from jeeves.core.actions.shell import ScriptAction
from jeeves.core.actions.docker import DockerBuildAction, DockerRunAction

__all__ = [
    # Shell
    ScriptAction,
    # Docker
    DockerBuildAction,
    DockerRunAction,
]

PROVIDED_ACTIONS = {action.id: action for action in __all__}
