# -*- coding: utf-8 -*-
import click
import subprocess
import os


@click.group()
def main():
    pass


@main.command(name="hello")
def hello():
    process = subprocess.Popen("systemctl daemon-reload", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout + stderr
    process.poll()
    if process.returncode == 0:
        print output
        print "hello"
    else:
        print "fail hello"


@main.command(name="world")
def world():
    code = os.system("systemctl daemon-reload")
    if code == 0:
        print "world"
    else:
        print "fail world"


main.add_command(hello)
main.add_command(world)


if __name__ == '__main__':
    main()
