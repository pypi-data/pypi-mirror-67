# -*- coding: utf-8 -*-
"""
:Module:            khoros.utils.helper
:Synopsis:          Module that allows the khoros library to leverage a helper configuration file
:Usage:             ``from khoros.utils import helper``
:Example:           ``helper_settings = helper.get_settings('/tmp/helper.yml', 'yaml')``
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     26 Apr 2020
"""

import json

import yaml

from .. import errors
from .core_utils import get_file_type


# Define function to import a YAML helper file
def import_helper_file(file_path, file_type):
    """This function imports a YAML (.yml) or JSON (.json) helper config file.

    .. versionchanged:: 2.2.0
       Changed the name and replaced the ``yaml.load`` function call with ``yaml.safe_load`` to be more secure.

    :param file_path: The file path to the YAML file
    :type file_path: str
    :param file_type: Defines the file type as either ``yaml`` or ``json``
    :type file_type: str
    :returns: The parsed configuration data
    :raises: :py:exc:`FileNotFoundError`, :py:exc:`khoros.errors.exceptions.InvalidHelperFileTypeError`
    """
    with open(file_path, 'r') as cfg_file:
        if file_type == 'yaml':
            helper_cfg = yaml.safe_load(cfg_file)
        elif file_type == 'json':
            helper_cfg = json.load(cfg_file)
        else:
            raise errors.exceptions.InvalidHelperFileTypeError
    return helper_cfg


# Define function to covert a YAML Boolean value to a Python Boolean value
def _convert_yaml_to_bool(_yaml_bool_value):
    """This function converts the 'yes' and 'no' YAML values to traditional Boolean values."""
    true_values = ['yes', 'true']
    if _yaml_bool_value.lower() in true_values:
        _bool_value = True
    else:
        _bool_value = False
    return _bool_value


# Define function to get the connection information
def _get_connection_info(_helper_cfg):
    """This function parses any connection information found in the helper file.

    .. versionchanged:: 2.2.0
       Removed one of the preceding underscores in the function name
    """
    _connection_info = {}
    _connection_keys = ['community_url', 'tenant_id', 'default_auth_type']
    for _key in _connection_keys:
        if _key in _helper_cfg['connection']:
            _connection_info[_key] = _helper_cfg['connection'][_key]

    # Parse OAuth 2.0 information if found
    if 'oauth2' in _helper_cfg['connection']:
        _connection_info['oauth2'] = _get_oauth2_info(_helper_cfg)

    # Parse session authentication information if found
    if 'session_auth' in _helper_cfg['connection']:
        _connection_info['session_auth'] = _get_session_auth_info(_helper_cfg)
    return _connection_info


def _get_oauth2_info(_helper_cfg):
    """This function parses OAuth 2.0 information if found in the helper file.

    .. versionchanged:: 2.2.0
       Removed one of the preceding underscores in the function name
    """
    _oauth2 = {}
    _oauth2_keys = ['client_id', 'client_secret', 'redirect_url']
    for _key in _oauth2_keys:
        if _key in _helper_cfg['connection']['oauth2']:
            _oauth2[_key] = _helper_cfg['connection']['oauth2'][_key]
        else:
            _oauth2[_key] = ''
    return _oauth2


def _get_session_auth_info(_helper_cfg):
    """This function parses session authentication information if found in the helper file.

    .. versionchanged:: 2.2.0
       Removed one of the preceding underscores in the function name
    """
    _session_auth = {}
    _session_info = ['username', 'password']
    for _key in _session_info:
        if _key in _helper_cfg['connection']['session_auth']:
            _session_auth[_key] = _helper_cfg['connection']['session_auth'][_key]
        else:
            _session_auth[_key] = None
    return _session_auth


def _get_construct_info(_helper_cfg):
    """This function parses settings that can be leveraged in constructing API responses and similar tasks.

    .. versionchanged:: 2.2.0
       Removed one of the preceding underscores in the function name
    """
    _construct_info = {}
    _top_level_keys = ['prefer_json']
    for _key in _top_level_keys:
        if _key in _helper_cfg:
            _key_val = _helper_cfg[_key]
            if _key_val in HelperParsing.yaml_boolean_values:
                _key_val = HelperParsing.yaml_boolean_values.get(_key_val)
            _construct_info[_key] = _key_val
        else:
            _construct_info[_key] = None
    return _construct_info


# Define function to retrieve the helper configuration settings
def get_helper_settings(file_path, file_type='yaml'):
    """This function returns a dictionary of the defined helper settings.

    .. versionchanged:: 2.2.0
       Added support for JSON formatted helper configuration files

    :param file_path: The file path to the helper configuration file
    :type file_path: str
    :param file_type: Defines the helper configuration file as a ``yaml`` file (default) or a ``json`` file
    :type file_type: str
    :returns: Dictionary of helper variables
    :raises: :py:exc:`khoros.errors.exceptions.InvalidHelperFileTypeError`
    """
    # Initialize the helper_settings dictionary
    helper_settings = {}

    if file_type != 'yaml' and file_type != 'json':
        file_type = get_file_type(file_path)

    # Import the helper configuration file
    helper_cfg = import_helper_file(file_path, file_type)

    # Populate the connection information in the helper dictionary
    if 'connection' in helper_cfg:
        helper_settings['connection'] = _get_connection_info(helper_cfg)

    # Populate the construct information in the helper dictionary
    helper_settings['construct'] = _get_construct_info(helper_cfg)

    # Return the helper_settings dictionary
    return helper_settings


# Define class for dictionaries to help in parsing the configuration files
class HelperParsing:
    """This class is used to help parse values imported from a YAML configuration file."""
    # Define dictionary to map YAML Boolean to Python Boolean
    yaml_boolean_values = {
        True: True,
        False: False,
        'yes': True,
        'no': False
    }
