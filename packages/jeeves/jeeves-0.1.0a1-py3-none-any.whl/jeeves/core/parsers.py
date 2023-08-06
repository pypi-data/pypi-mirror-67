import json
from typing import Any, Text, MutableMapping
from pathlib import Path

import toml

from jeeves.core.objects import Flow, BaseObject


class ObjectParser:
    object: BaseObject = None

    @classmethod
    def from_dict(cls, serialized: MutableMapping[str, Any]) -> BaseObject:
        return cls.object.parse_obj(serialized)

    @classmethod
    def to_dict(cls, obj: BaseObject) -> dict:
        return obj.dict()

    @classmethod
    def from_json(cls, serialized: Text) -> BaseObject:
        return cls.object.parse_raw(serialized)

    @classmethod
    def from_json_file(cls, path: Path) -> BaseObject:
        return cls.object.parse_file(path)

    @classmethod
    def to_json(cls, obj: BaseObject) -> Text:
        return json.dumps(cls.to_dict(obj))

    @classmethod
    def from_toml(cls, serialized: Text) -> BaseObject:
        dct = toml.loads(serialized)
        return cls.from_dict(dct)

    @classmethod
    def from_toml_file(cls, path) -> BaseObject:
        dct = toml.load(path)
        return cls.from_dict(dct)

    @classmethod
    def to_toml(cls, obj: BaseObject) -> Text:
        return toml.dumps(cls.to_dict(obj))


class FlowParser(ObjectParser):
    object = Flow
