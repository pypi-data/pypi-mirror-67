import click
from globus_sdk import DeleteData

from globus_cli.parsing import (
    ENDPOINT_PLUS_OPTPATH,
    TaskPath,
    command,
    delete_and_rm_options,
    shlex_process_stdin,
    task_submission_options,
)
from globus_cli.safeio import (
    FORMAT_TEXT_RECORD,
    err_is_terminal,
    formatted_print,
    term_is_interactive,
)
from globus_cli.services.transfer import autoactivate, get_client


@command("delete", short_help="Submit a delete task (asynchronous)")
@task_submission_options
@delete_and_rm_options
@click.argument("endpoint_plus_path", type=ENDPOINT_PLUS_OPTPATH)
def delete_command(
    batch,
    ignore_missing,
    star_silent,
    recursive,
    enable_globs,
    endpoint_plus_path,
    label,
    submission_id,
    dry_run,
    deadline,
    skip_activation_check,
    notify,
):
    """Delete a file or directory from one endpoint as an asynchronous task"""
    endpoint_id, path = endpoint_plus_path
    if path is None and (not batch):
        raise click.UsageError("delete requires either a PATH OR --batch")

    client = get_client()

    # attempt to activate unless --skip-activation-check is given
    if not skip_activation_check:
        autoactivate(client, endpoint_id, if_expires_in=60)

    delete_data = DeleteData(
        client,
        endpoint_id,
        label=label,
        recursive=recursive,
        ignore_missing=ignore_missing,
        submission_id=submission_id,
        deadline=deadline,
        skip_activation_check=skip_activation_check,
        interpret_globs=enable_globs,
        **notify
    )

    if batch:
        # although this sophisticated structure (like that in transfer)
        # isn't strictly necessary, it gives us the ability to add options in
        # the future to these lines with trivial modifications
        @click.command()
        @click.argument("path", type=TaskPath(base_dir=path))
        def process_batch_line(path):
            """
            Parse a line of batch input and add it to the delete submission
            item.
            """
            delete_data.add_item(str(path))

        shlex_process_stdin(process_batch_line, "Enter paths to delete, line by line.")
    else:
        if not star_silent and enable_globs and path.endswith("*"):
            # not intuitive, but `click.confirm(abort=True)` prints to stdout
            # unnecessarily, which we don't really want...
            # only do this check if stderr is a pty
            if (
                err_is_terminal()
                and term_is_interactive()
                and not click.confirm(
                    'Are you sure you want to delete all files matching "{}"?'.format(
                        path
                    ),
                    err=True,
                )
            ):
                click.echo("Aborted.", err=True)
                click.get_current_context().exit(1)
        delete_data.add_item(path)

    if dry_run:
        formatted_print(delete_data, response_key="DATA", fields=[("Path", "path")])
        # exit safely
        return

    res = client.submit_delete(delete_data)
    formatted_print(
        res,
        text_format=FORMAT_TEXT_RECORD,
        fields=(("Message", "message"), ("Task ID", "task_id")),
    )
