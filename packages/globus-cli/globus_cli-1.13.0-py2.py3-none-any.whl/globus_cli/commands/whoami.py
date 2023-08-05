import click
from globus_sdk.exc import AuthAPIError

from globus_cli.parsing import command
from globus_cli.safeio import (
    FORMAT_TEXT_RECORD,
    formatted_print,
    is_verbose,
    print_command_hint,
)
from globus_cli.services.auth import get_auth_client


@command("whoami", disable_options=["map_http_status"])
@click.option(
    "--linked-identities",
    is_flag=True,
    help="Also show identities linked to the currently logged-in primary identity.",
)
def whoami_command(linked_identities):
    """Show the currently logged-in primary identity"""
    client = get_auth_client()

    # get userinfo from auth.
    # if we get back an error the user likely needs to log in again
    try:
        res = client.oauth2_userinfo()
    except AuthAPIError:
        click.echo(
            "Unable to get user information. Please try logging in again.", err=True
        )
        click.get_current_context().exit(1)

    print_command_hint(
        "For information on which identities are in session see\n"
        "  globus session show\n"
    )

    # --linked-identities either displays all usernames or a table if verbose
    if linked_identities:
        try:
            formatted_print(
                res["identity_set"],
                fields=[
                    ("Username", "username"),
                    ("Name", "name"),
                    ("ID", "sub"),
                    ("Email", "email"),
                ],
                simple_text=(
                    None
                    if is_verbose()
                    else "\n".join([x["username"] for x in res["identity_set"]])
                ),
            )
        except KeyError:
            click.echo(
                "Your current login does not have the consents required "
                "to view your full identity set. Please log in again "
                "to agree to the required consents.",
                err=True,
            )

    # Default output is the top level data
    else:
        formatted_print(
            res,
            text_format=FORMAT_TEXT_RECORD,
            fields=[
                ("Username", "preferred_username"),
                ("Name", "name"),
                ("ID", "sub"),
                ("Email", "email"),
            ],
            simple_text=(None if is_verbose() else res["preferred_username"]),
        )
