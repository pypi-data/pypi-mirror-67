CLI_CONFIG = {
    "unit": {"options": ["-u"], "subcommands": ["create", "get", "set", "migrate"],},
    "store": {"subcommands": ["create", "migrate"],},
    "cipher": {"options": ["-C"], "subcommands": ["create", "migrate"],},
    "seal": {"options": ["-S"], "subcommands": ["create", "migrate"],},
    "seal_raw": {"subcommands": ["set", "get"],},
    "path": {"options": ["-p"], "subcommands": ["set", "get"],},
    "string": {"options": ["-s"], "subcommands": "set",},
    "file": {"options": ["-f"], "subcommands": ["set"],},
    "data_dir": {"subcommands": ["create", "set", "get", "migrate"],},
    "unit_dir": {"subcommands": ["create", "set", "get", "migrate"],},
}
CONFIG = {
    "unit": {
        "default": "main",
        "help": 'The unit to work with, if empty the unit "main" is used',
    },
    "store": {"default": "file", "help": "Choose the storage medium to use",},
    "cipher": {
        "default": "fernet",
        "help": "When creating or cipher to use for storage of data for the new unit",
    },
    "seal": {
        "default": "passwd",
        "help": "The type of seal to use to secure the storage interface",
    },
    "seal_raw": {
        "default": None,
        "help": "DO NOT USE! This option allows you to pass secrets as command line arguments! This should only be used for testing!!",
    },
    "path": {"default": None, "help": "The path to store or retrive the desired data",},
    "string": {
        "defalt": None,
        "help": "Choose a string to set as the value for the given storage path",
    },
    "file": {
        "default": None,
        "help": "Choose a local file to set as the value to find for the given path",
    },
    "data_dir": {
        "default": "/var/takara/data",
        "help": "The directory to store data specific to the configuration of encrypted units when using local file storage systems",
    },
    "unit_dir": {
        "default": "/var/takara/unit",
        "help": "The directory to store encrypted data when using the local file storage system",
    },
}
GLOBAL = {}
SUBCOMMANDS = {
    "create": {
        "desc": "Create New Units",
        "help": "Use create to make new units to store encrypted data",
    },
    "set": {
        "desc": "Set data to a location",
        "help": "Use set to change or add a location for a given unit",
    },
    "get": {
        "desc": "Get data from a location",
        "help": "Use Get to retrive data from a given location",
    },
    "migrate": {
        "desc": "Migrate a unit to other stores, seals, and/or ciphers",
        "help": "Migrate a unit to other stores, seals, and/or ciphers",
    },
}
DYNE = {
    "takara": ["takara"],
}
