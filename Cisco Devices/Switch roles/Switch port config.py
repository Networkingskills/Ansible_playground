import csv
from pipes import Template
from jinja2 import template

source_file = "switch-ports.csv"
interface_template_file = "switchport-interface-template.j2"

interface_configs = ""

with open(interface_template_file) as f:
        interface_template = Template(f.read(), keep_trailing_newline=True)
        
with open(source_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            vlan = row["VLAN"]
            server = row["Server"]
            link = row["Link"]
            purpose = row["Purpose"]
        )
        interface_configs += interface_config
        
with open("interface_config.txt", "w") as f:
    f.write(interface_configs)