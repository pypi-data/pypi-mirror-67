#! /usr/bin/env python3.7

'''
This file contains every allowable argument and keyword argument. Anything
defined here will be permissable to pass into the 'Initializer' class.
'''

inventory = """
Specify an inventory config file. See Nornir
for inventory documentation:

https://nornir.readthedocs.io/en/stable/index.html

Args:
  A string.

Examples:
  Shell:
    '--inventory ./inventory/config.yaml'

  Python:
    foo = "./inventory/config.yaml"
    object(inventory=foo)

"""

devices = """
Filter devices using hostnames.

Args:
  A string or list. A string must contain comma separated hostnames. A list
  must be strings of devices.

Examples:
  Shell:
    '--devices chnddsrj01,chndbbrj02'

  Python:
    foo = ["chnddsrj01", "chndbbrj01"]
    object(devices=foo)

"""

device_groups = """
Filter devices using inventory attributes.

Args:
  A string or dictionary. A string must contain comma separated key/value pairs
  where in equal sign denotes the key/value relationship. The equivilent in
  dictionary format is required.

Examples:
  Shell:
    '--device_groups device_type=bbr,domain=backbone'

  Python:
    foo = {'device_type': 'bbr','domain':'backbone'}
    object(device_group=foo)

"""

confirm = """
Perform a commit confirm.

Args:
  A string.

Examples:
  Shell: --confirm

  Python: object(confirm)

"""

tests_file = """
Jsnapy test file used for all devices.

Args:
  A string.

Examples:
  Shell:
    '--tests_file ./PATH/FILE.yaml'

  Python:
    foo = "./PATH/FILE.yaml"
    object(tests_file=foo)

"""

comment = """
Add a comment ahead of time to avoid prompting at each node.

Args:
  A string.

Examples:
  Shell:
    '--comment "MY COMMENT"'

  Python:
    foo = "MY COMMENT"
    object(comment=foo)

"""

schemas = """
Schemas / YANG models to pull from device.

Args:
  A string or list. A string must be the path to the YAML file. A list must be
  strings of YANG models.

Examples:

  Shell:
    '--schemas ./DIR/FILE.yaml'

  Python:

    String:
      object(schemas='./DIR/FILE.yaml')

    List:
      foo = ["ietf-interfaces","openconfig-lldp"]
      object(schemas=foo)

      or

      foo = "./DIR/FILE.yaml"
      object(schemas=foo)

"""

rpcs = """
'Get' requests to pull operational or configuration data from node.

Args:
  A string or dictionary. A string must be the path to the YAML file. A
  dictionary must be constructed in an identical way to the YAML file.

Examples:
  Shell:
    $ more ./DIR/FILE.yaml
    ---
    MPLS: show mpls interface
    ISIS: show isis interface

    '--rpcs ./DIR/FILE.yaml'

  Python:
    foo = { "MPLS": "show mpls interface" ,
            "ISIS": "show isis interface" }

    object(rpcs=foo)

    or

    foo = "./DIR/FILE.yaml'"
    object(rpcs=foo)

"""

jsnapy = """
Specify jsnapy operation ('check' or 'compare').  This should align with the
test file's functionality.

Args:
  A string.

Examples:
  Shell:
    '--jsnapy check'

  Python:
    foo = "check"
    object(jsnapy=foo)

"""

config = """
A single configuration for all devices.

Args:
  A string.

Examples:
  Shell:
    '--config ./DIR/FILE.txt'

  Python:
    foo = "./DIR/FILE.txt"
    object(config=foo)

"""

host_configs = """
Specific configurations per host.

Args:
  A string or dictionary. A string must be the path to the directory containing
  the configuration '.txt' files.  A dictionary must be key/value pair where
  the key is the hostname and its values is the configuration.

Examples:
  Shell:
    '--host_configs ./DIR'

  Python:
    foo = { {"CHNDDSRJ01": "set system hostname CHNDDSRJ01"},
            {"CHNDBBRJ01": "set system hostname CHNDBBRJ01"} }
    object(host_configs=foo)

    or

    foo = "./DIR"
    object(host_configs=foo)

"""

host_rpcs= """
Specific rpcs per host.

Args:
  A string or dictionary. A string must be the path to the directory containing
  the rpc '.yaml' files.  A dictionary must be key/value pair where the key is
  the hostname and its values are the rpcs.

Examples:
  Shell:
    '--host_rpcs ./DIR'

  Python:
    foo = { "D01-BBRJ01": { "ISIS" "show isis adjacency",
                            "RSVP":"show rsvp interface" },
            "D02-BBRJ02": { "BGP": "show bgp summary" } }

    object(host_rpcs=foo)

    or

    foo = "./DIR"
    object(host_rpcs=foo)

"""

host_rollbacks = """
Specific rollbacks per host.

Args:
  Dictionary only. The dictionary must be key/value pair where the key is the
  hostname and its value is the commit number to rollback to.

Examples:
  Shell:
    NOT SUPPORTED

  Python:
    foo = {"D01-BBRJ01": 1,
           "D02-BBRJ02": 2}

    object(host_rollbacks=foo)

"""

host_tests = """
Specific Jsnapy tests per host.

Args:
  String only. A string must be the path to the directory containing the jsnapy
  '.yaml' files.

Examples:
  Shell:
    '--host_tests ./DIR'

  Python:
    foo = "./DIR"
    object(host_tests=foo)

"""

dir_name = """
A custom directory name.

Examples:
  Shell:
    '--dir_name MY_NAME'

  Python:
    foo = "MY_NAME"
    object(dir_name=foo)

"""

timer = """
Amount of time to sleep after configuration changes are made but before Jsnapy
post tests are executed.  This is required with performing a commit confirm.
Time supplied should be in seconds.

Examples:
  Shell:
    '--timer 10'

  Python:
    foo = 10
    object(timer=foo)

"""

rollback = """
Provide the rollback number.

Examples:
  Shell:
    '--rollback 1'

  Python:
    foo = "1"
    object(rollback=foo)

"""

skip_pre_check = """
When performing a jsnapy check (not a 'compare'), skip the pre-check and only
perform a post-check operation. This is useful for when you want to apply a
configuration that didn't exist beforehand and need to test it afterwards.

Examples:
  Shell:
    '--skip_pre_check'

  Python:
    object('skip_pre_check')

"""

skip_post_check = """
When performing a jsnapy check (not a 'compare'), skip the post-check and only
perform a post-check operation.

Examples:
  Shell:
    '--skip_post_check'

  Python:
    object('skip_pre_check')

"""

skip_pre_rpcs = """
When performing executing rpcs, only execute the pre rpcs (a config change must
occur).

Examples:
  Shell:
    '--skip_pre_rpcs'

  Python:
    object('skip_pre_rpcs')

"""

skip_post_rpcs = """
When performing executing rpcs, only execute the post rpcs (a config change
must occur). This is useful for clearing counters prior to a change.

Examples:
  Shell:
    '--skip_post_rpcs'

  Python:
    object('skip_post_rpcs')

"""

# available arguments
available_args = [ { "desc": "Collect NETCONF capabilities.",
                     "name": "capabilities",
                     "flag": "q" },
                   { "desc": "Eliminate commit prompt.",
                     "name": "commit",
                     "flag": "c" },
                   { "desc": "Skip a jsnapy pre-check and only perform post",
                     "name": "skip_pre_check",
                     "flag": "sc" },
                   { "desc": "Skip a jsnapy post-check and only perform pre",
                     "name": "skip_post_check",
                     "flag": "sc" },
                   { "desc": "Skip a pre rpcs and only perform post rpcs",
                     "name": "skip_pre_rpcs",
                     "flag": "sd" },
                   { "desc": "Skip a post rpcs and only perform pre rpcs",
                     "name": "skip_post_rpcs",
                     "flag": "sp" },
                   { "desc": "Do not write logging information to disk",
                     "name": "log_saving_off",
                     "flag": "dn" },
                   { "desc": "Display the inventory.",
                     "name": "show_inventory",
                     "flag": "n" },
                   { "desc": "Disable stdout and perform multithreading.",
                     "name": "silent",
                     "flag": "k" },
                   { "desc": "Perform a confirm commit.",
                     "name": "confirm",
                     "flag": "cm" },
                   { "desc": "Perform a config diff (disallows commit).",
                     "name": "diff",
                     "flag": "r" },
                   { "desc": ("Save and return get responses as XML "
                              "(default=JSON)."),
                     "name": "xml",
                     "flag": "x" } ]

available_kwargs = [ { "desc": inventory,
                       "name": "inventory",
                       "flag": "i" },
                     { "desc": devices,
                       "name": "devices",
                       "flag": "d" },
                     { "desc": device_groups,
                       "name": "device_groups",
                       "flag": "g" },
                     { "desc": tests_file,
                       "name": "tests_file",
                       "flag": "j" },
                     { "desc": comment,
                       "name": "comment",
                       "flag": "l" },
                     { "desc": timer,
                       "name": "timer",
                       "flag": "tm" },
                     { "desc": schemas,
                       "name": "schemas",
                       "flag": "s" },
                     { "desc": rpcs,
                       "name": "rpcs",
                       "flag": "p" },
                     { "desc": jsnapy,
                       "name": "jsnapy",
                       "flag": "w" },
                     { "desc": config,
                       "name": "config",
                       "flag": "y" },
                     { "desc": host_configs,
                       "name": "host_configs",
                       "flag": "hc" },
                     { "desc": host_rpcs,
                       "name": "host_rpcs",
                       "flag": "hg" },
                     { "desc": host_rollbacks,
                       "name": "host_rollbacks",
                       "flag": "hr" },
                     { "desc": host_tests,
                       "name": "host_tests",
                       "flag": "ht" },
                     { "desc": dir_name,
                       "name": "dir_name",
                       "flag": "h" },
                     { "desc": rollback,
                       "name": "rollback",
                       "flag": "u" } ]

available_args = sorted(available_args, key = lambda i: i['name'])
available_kwargs = sorted(available_kwargs, key = lambda i: i['name'])

'''
This docstring will be imported into the 'Initializer'
module and will allow the users to view the available
args and kwargs defined here.
'''
arg_docstring = ""

arg_docstring += (f"{'Arguments (args)':<30}{'Descriptions':<75}\n"
                  f"{'-'*105}\n")
for entry in available_args:
    arg_docstring += f"{entry['name']:<30}{entry['desc']:<75}\n"

arg_docstring += (f"\n{'Keyword Arguments (kwargs)':<30}"
                  f"{'Descriptions':<75}\n"
                  f"{'-'*105}\n")
for entry in available_kwargs:
    arg_docstring += f"{entry['name']:<30}{entry['desc']:<75}\n"

def terminal_input():
    from argparse import ArgumentParser, RawTextHelpFormatter

    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)

    for entry in available_args:
        parser.add_argument(f"--{entry['name']}",
                            f"--{entry['flag']}",
                            help=entry["desc"],
                            action="store_true")

    for entry in available_kwargs:
        parser.add_argument(f"--{entry['name']}",
                            f"--{entry['flag']}",
                            help=entry["desc"])

    user_input = parser.parse_args()

    # convert to dict
    usr_input = vars(user_input)

    # convert to tuple
    args = tuple( [ k for k,v in usr_input.items()
                       if isinstance(v, bool) and v is True ] )

    # convert to dict
    kwargs = { k:v for k,v in usr_input.items()
                       if not isinstance(v, bool) }

    # remove empty
    kwargs = { k:v for k,v in kwargs.items()
                       if v }

    return args, kwargs
