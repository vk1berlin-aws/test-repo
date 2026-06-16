from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


def format_response(
    data: Any = None, message: str = "Success", status: str = "ok"
) -> dict:
    """Format a standard API response envelope.

    Args:
        data: The response payload. If None, the 'data' key is set to None.
        message: A human-readable message describing the result.
        status: A short status indicator (e.g. 'ok', 'error').

    Returns:
        A dictionary with 'status', 'message', and 'data' keys.

    Raises:
        ValueError: If message or status is None.
    """
    if message is None:
        raise ValueError("message must not be None")
    if status is None:
        raise ValueError("status must not be None")

    return {
        "status": status,
        "message": message,
        "data": data,
    }


def parse_config(config_path: str | Path | None = None) -> dict:
    """Parse a YAML configuration file.

    Reads and parses a config.yaml file. If no path is provided, it defaults
    to 'config.yaml' in the project root directory (parent of the 'app' package).

    Args:
        config_path: Optional path to the YAML configuration file.

    Returns:
        A dictionary containing the parsed configuration.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the configuration file is empty or contains invalid YAML.
    """
    if config_path is None:
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config.yaml"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r") as f:
        content = f.read()

    if not content.strip():
        raise ValueError(f"Configuration file is empty: {config_path}")

    try:
        config = yaml.safe_load(content)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in configuration file: {e}")

    if not isinstance(config, dict):
        raise ValueError(
            f"Configuration file must contain a YAML mapping, got {type(config).__name__}"
        )

    return config
