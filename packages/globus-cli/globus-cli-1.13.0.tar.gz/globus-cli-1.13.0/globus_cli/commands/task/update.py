import click

from globus_cli.parsing import command, task_id_arg
from globus_cli.safeio import formatted_print
from globus_cli.services.transfer import assemble_generic_doc, get_client


@command("update", short_help="Update a task")
@task_id_arg
@click.option("--label", help="New Label for the task")
@click.option("--deadline", help="New Deadline for the task")
def update_task(deadline, label, task_id):
    """Update label and/or deadline on an active task"""
    client = get_client()

    task_doc = assemble_generic_doc("task", label=label, deadline=deadline)

    res = client.update_task(task_id, task_doc)
    formatted_print(res, simple_text="Success")
