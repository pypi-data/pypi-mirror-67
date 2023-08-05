from globus_sdk import IdentityMap

from globus_cli.parsing import command, endpoint_id_arg
from globus_cli.safeio import formatted_print
from globus_cli.services.auth import get_auth_client
from globus_cli.services.transfer import get_client


@command("list")
@endpoint_id_arg
def role_list(endpoint_id):
    """List of assigned roles on an endpoint"""
    client = get_client()
    roles = client.endpoint_role_list(endpoint_id)

    resolved_ids = IdentityMap(
        get_auth_client(),
        (x["principal"] for x in roles if x["principal_type"] == "identity"),
    )

    def principal_str(role):
        principal = role["principal"]
        if role["principal_type"] == "identity":
            try:
                return resolved_ids[principal]["username"]
            except KeyError:
                return principal
        if role["principal_type"] == "group":
            return (u"https://app.globus.org/groups/{}").format(principal)
        return principal

    formatted_print(
        roles,
        fields=[
            ("Principal Type", "principal_type"),
            ("Role ID", "id"),
            ("Principal", principal_str),
            ("Role", "role"),
        ],
    )
