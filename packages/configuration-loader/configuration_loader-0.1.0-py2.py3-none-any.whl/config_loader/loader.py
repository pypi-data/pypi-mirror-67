"""Configuration loader class."""

import ast
import logging
import os
import types
from operator import attrgetter

import pkg_resources

logger = logging.getLogger(__name__)


class Config(dict):
    """Configuration loader, it's like a normal dictionary with super-powers.

    It will load configuration in the following order:

        1. Load configuration from ``config_loader.module`` entry points
           group, following the alphabetical ascending order in case of
           multiple entry points defined.
        2. Load from file path, if provided via environment variable.
        3. Load from keyword arguments when provided.
        4. Load configuration from environment variables with the prefix
           ``env_prefix``.

    Once the object is created it can be updated, as a normal dictionary or,
    using any of the ``from_`` methods provided.

    :param env_var: Name of an environment variable pointing to a configuration
        file.
    :param env_prefix: Environment variable prefix, it will iterate over all
        environment variables and load the ones matching the prefix.
    :param entry_point_name: Name of the entry point used to add configuration
        files from outside modules.
    :param kwargs_config: Dictionary with ad-hoc configuration variables.
    """

    def __init__(
        self,
        env_var='CONFIG_SETTINGS',
        env_prefix='CONFIG_',
        entry_point_name='config_loader.module',
        **kwargs_config
    ):
        """Initialize new configuration loader instance."""
        self.from_entry_point(entry_point_name)
        self.from_envvar(env_var)
        self.update(**kwargs_config)
        self.from_env(env_prefix)

    def from_entry_point(self, entry_point_name):
        """Update values from module defined by entry point.

        Configurations are loaded in alphabetical ascending order.

        :param entry_point_name: The name of the entry point.
        """
        eps = sorted(
            pkg_resources.iter_entry_points(entry_point_name),
            key=attrgetter('name'),
        )
        for ep in eps:
            self.from_object(ep.load())

    def from_envvar(self, variable_name):
        """Update values from an env variable pointing to a configuration file.

        :param variable_name: The name of the environment variable.
        """
        filename = os.environ.get(variable_name, None)
        if filename:
            self.from_pyfile(filename)
        else:
            logger.debug('Cannot find env file')

    def from_pyfile(self, filename):
        """Update the values in the config from a Python file.

        :param filename: The filename of the config.
        """
        if not os.path.exists(filename):
            logger.warn('File %s does not exists', filename)
            return

        d = types.ModuleType('config')
        d.__file__ = filename
        with open(filename, mode='rb') as config_file:
            exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
        self.from_object(d)

    def from_object(self, obj):
        """Update the values from the given object.

        :param obj: An object to import cfg values from.
        """
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)

    def from_env(self, prefix):
        """Load configuration from environment variables.

        :param prefix: The prefix used to filter the environment variables.
        """
        prefix_len = len(prefix)
        for varname, value in os.environ.items():
            if not varname.startswith(prefix):
                continue
            # Prepare values
            varname = varname[prefix_len:]
            value = value or self.get(varname)

            # Evaluate value
            try:
                value = ast.literal_eval(value)
            except (SyntaxError, ValueError):
                pass

            # Set value
            self[varname] = value
