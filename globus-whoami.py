#!/usr/local/bin/python 

import globus_cli as g

try: 
  import globus_cli 
  HAS_GLOBUSCLI = True
except ImportError:
  HAS_GLOBUSCLI = False

from ansible.module_utils.basic import AnsibleModule

module = AnsibleModule(argument_spec=None)

g.whoami_command()








