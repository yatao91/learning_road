# -*- coding: utf-8 -*-
import click


@click.group()
def main():
    pass


@click.command(name="config_cgroup", help="change services cgroups config use service name and memory limit")
@click.option('--memory', '-m', type=(str, int), multiple=True, help='service memory limit, <service, limit>')
def config_cgroup(memory):

    input_config = {service: limit for service, limit in memory}
    print input_config
    for key, value in input_config.items():
        print key, type(key), value
    for service, limit in memory:
        print service, limit
    print "hello"

    try:
        a = 1 / 0
    except Exception:
        raise


main.add_command(config_cgroup)


if __name__ == '__main__':
    config_cgroup()
