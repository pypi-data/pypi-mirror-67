import click

from globus_cli.parsing import command, endpoint_id_arg
from globus_cli.safeio import FORMAT_TEXT_RECORD, formatted_print
from globus_cli.services.auth import lookup_identity_name
from globus_cli.services.transfer import get_client


def _shared_with_keyfunc(rule):
    if rule["principal_type"] == "identity":
        return lookup_identity_name(rule["principal"])
    elif rule["principal_type"] == "group":
        return u"https://app.globus.org/groups/{}".format(rule["principal"])
    else:
        return rule["principal_type"]


@command("show")
@endpoint_id_arg
@click.argument("rule_id")
def show_command(endpoint_id, rule_id):
    """Show a permission on an endpoint"""
    client = get_client()

    rule = client.get_endpoint_acl_rule(endpoint_id, rule_id)
    formatted_print(
        rule,
        text_format=FORMAT_TEXT_RECORD,
        fields=(
            ("Rule ID", "id"),
            ("Permissions", "permissions"),
            ("Shared With", _shared_with_keyfunc),
            ("Path", "path"),
        ),
    )
