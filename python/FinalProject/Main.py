from CLI import CLI
import os

if __name__ == '__main__':
    user_interface = CLI(os.getcwd())
    cli = user_interface.create_cli()
    cli()