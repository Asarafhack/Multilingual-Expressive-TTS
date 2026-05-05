from app.cli import run_cli

mode = input("Choose mode (cli/ui): ")

if mode == "cli":
    run_cli()
else:
    from app.ui import app