#!/usr/bin/env python3
import json
from pathlib import Path
from jsonschema import ValidationError, validate

def validate_json(data: dict, schema: dict) -> tuple[bool, str | None]:
    try:
        validate(instance=data, schema=schema)
        return True, None

    except ValidationError as e:
        return False, f"Validation Error: {e.message}"

def validate_file(file_path: Path, schema_obj: Path | dict) -> tuple[bool, str | None]:
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        if isinstance(schema_obj, Path):
            schema = json.loads(schema_obj.read_text(encoding="utf-8"))
        else:
            schema = schema_obj
    except json.JSONDecodeError as e:
        return False, f"Decode Error: {e.msg}"

    return validate_json(data=data, schema=schema)

def validate_directory(directory_path: Path, schema_path: Path) -> tuple[bool, list[tuple[Path, str]]]:
    errors: list[tuple[Path, str]] = []

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append((schema_path, e))
        return False, errors
    
    for file_path in directory_path.glob("*.json"):
        valid, e = validate_file(file_path=file_path, schema_obj=schema)
        if not valid:
            errors.append((file_path, e))

    status = len(errors) == 0

    return status, errors