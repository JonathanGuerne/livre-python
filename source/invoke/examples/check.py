"""Module pour lancer les checks."""


from invoke import task, run


@task
def checks(ctx):
    """Check du code et de la doc."""
    ctx.run("pycodestyle source")
    ctx.run("pydocstyle source")
