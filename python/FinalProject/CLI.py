import click
from Repository import Repository
import requests

class CLI:
    def __init__(self,path):
        self.re = Repository(path)
    def create_cli(self):
        @click.group()
        def cli():
            """Management user interface repository"""
            pass

        @cli.command()
        def init():
            try:
                self.re.init()
                click.echo("Initialized repository succeed.")
            except Exception as e:
                click.echo("Error:\t"+str(e))

        @cli.command()
        @click.argument("files",nargs =-1)
        def add(files):
            try:
                for file1 in files:
                    self.re.add(file1)
                    click.echo("file added successfully.")
                files_to_send = []
                for filepath in files:
                    path = self.re.path + "\\add\\" + filepath
                    files_to_send.append(("files", open(path, "rb")))
                response = requests.post("http://127.0.0.1:8000/analyze", files=files_to_send, data={"path": self.re.path})

                click.echo("Response from server:")
                click.echo(response.text)
            except Exception as e:
                click.echo("Error:\t" + str(e))

        @cli.command()
        @click.argument("message")
        def commit(message):
            try:
                self.re.commit(message)
                click.echo("Commited successfully.")
            except Exception as e:
                click.echo("Error:\t" + str(e))

        @cli.command()
        def log():
            try:
                self.re.log()
            except Exception as e:
                click.echo("Error:\t" + str(e))

        @cli.command()
        def status():
            try:
                self.re.status()
            except Exception as e:
                click.echo("Error:\t" + str(e))

        @cli.command()
        @click.argument("id1")
        def checkout(id1):
            try:
                self.re.checkout(id1)
                click.echo("return to commit successfully.")
            except Exception as e:
                click.echo("Error:\t" + str(e))

        return cli