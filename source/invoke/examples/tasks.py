"""Module de taches pour l'automatisation de la creation de rst."""


from invoke import run, task

# html start


@task
def clean(ctx):
    """Nettoyage du dossier de destination."""
    ctx.run("rm -rf build/html")


@task(clean)
def html(ctx):
    """Generation de l'html."""
    result = ctx.run("sphinx-build -b html source build/html")

# fetch start


@task
def do_i_need_to_rebase(ctx):
    """Rebase si necaissaire."""
    if(ctx.run("git fetch")):
        print("ok")


# checks start


@task
def checks(ctx):
    """Fait les différents checks du programme."""
    ctx.run("pycodestyle source")
    ctx.run("pydocstyle source")
