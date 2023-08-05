import click

from globus_cli.parsing import command, endpoint_id_arg
from globus_cli.safeio import FORMAT_TEXT_RAW, formatted_print
from globus_cli.services.transfer import assemble_generic_doc, get_client


@command("update")
@endpoint_id_arg
@click.argument("rule_id")
@click.option(
    "--permissions",
    required=True,
    type=click.Choice(("r", "rw"), case_sensitive=False),
    help="Permissions to add. Read-Only or Read/Write",
)
def update_command(permissions, rule_id, endpoint_id):
    """Update an access control rule, changing permissions on an endpoint"""
    client = get_client()

    rule_data = assemble_generic_doc("access", permissions=permissions)
    res = client.update_endpoint_acl_rule(endpoint_id, rule_id, rule_data)
    formatted_print(res, text_format=FORMAT_TEXT_RAW, response_key="message")
