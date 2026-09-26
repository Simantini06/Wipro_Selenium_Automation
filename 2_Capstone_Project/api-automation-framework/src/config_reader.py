"""
Loads config/config.yaml and resolves which environment to run against.

Priority for choosing the environment:
  1. explicit env_name argument (e.g. passed from behave -D env=<name>)
  2. API_ENV environment variable
  3. default_env value inside config.yaml
"""

import os
import yaml

DEFAULT_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "config", "config.yaml"
)


class ConfigReader:
    _config_cache = None

    @classmethod
    def load(cls, config_path=None):
        if cls._config_cache is not None:
            return cls._config_cache

        path = config_path or DEFAULT_CONFIG_PATH
        with open(path, "r") as f:
            cls._config_cache = yaml.safe_load(f)
        return cls._config_cache

    @classmethod
    def get_environment(cls, env_name=None):
        config = cls.load()
        resolved_name = env_name or os.environ.get("API_ENV") or config.get("default_env")
        environments = config.get("environments", {})

        if resolved_name not in environments:
            raise ValueError(
                f"Environment '{resolved_name}' not found in config.yaml. "
                f"Available environments: {list(environments.keys())}"
            )
        return environments[resolved_name]
