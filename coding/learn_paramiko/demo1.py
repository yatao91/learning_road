# -*- coding: utf-8 -*-
import os
import socket
import paramiko


def manual_auth(username, hostname):

    path = os.path.join(os.environ["HOME"], ".ssh", "id_rsa")

    key = paramiko.RSAKey.from_private_key_file(path)

    t.auth_publickey(username, key)


username = 'root'
hostname = '39.104.104.210'

# now connect
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, 22))
except Exception as e:
    print("*** Connect failed: " + str(e))

try:
    t = paramiko.Transport(sock)
    try:
        t.start_client()
    except paramiko.SSHException:
        print("*** SSH negotiation failed.")

    try:
        keys = paramiko.util.load_host_keys(
            os.path.expanduser("~/.ssh/known_hosts")
        )
    except IOError:
        try:
            keys = paramiko.util.load_host_keys(
                os.path.expanduser("~/ssh/known_hosts")
            )
        except IOError:
            print("*** Unable to open host keys file")
            keys = {}

    # check server's host key -- this is important.
    key = t.get_remote_server_key()
    if hostname not in keys:
        print("*** WARNING: Unknown host key!")
    elif key.get_name() not in keys[hostname]:
        print("*** WARNING: Unknown host key!")
    elif keys[hostname][key.get_name()] != key:
        print("*** WARNING: Host key has changed!!!")
    else:
        print("*** Host key OK.")

    manual_auth(username, hostname)
    if not t.is_authenticated():
        print("*** Authentication failed. :(")
        t.close()

    chan = t.open_session()
    chan.get_pty()
    chan.invoke_shell()
    print("*** Here we go!\n")
    chan.close()
    t.close()

except Exception as e:
    print("*** Caught exception: " + str(e.__class__) + ": " + str(e))
    try:
        t.close()
    except:
        pass
