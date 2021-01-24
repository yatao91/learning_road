import ConfigParser
import os
import fcntl
import io


class Config(object):
    """
    Use it like use ConfigParser's methods:
    get
    getint
    getfloat
    etc.

    What we added is a get_items method which could interpret configs like:
    zookeeper=192.168.1.11,192.168.1.12,192.168.1.13

    and returns an array contains the items
    """

    def __init__(self, cfg):
        if not os.path.exists(cfg):
            raise RuntimeError("Config file " + cfg + " not found.")
        self.cfg = cfg
        cfg_str = ""

        with open(cfg, 'r') as f:
            fcntl.flock(f, fcntl.LOCK_SH)
            cfg_str = f.read()

        self.parser = ConfigParser.SafeConfigParser()
        self.parser.readfp(io.BytesIO(cfg_str))

    def get_items(self, section, key, seperator=','):
        value = self.parser.get(section, key)
        items = value.strip().split(seperator)
        return items

    # delegate all other calls
    def __getattr__(self, name):
        return getattr(self.parser, name)

    def get_local_data_ip(self):
        return self.get_items("network", "data_ip")

    def get_mongo_members(self, remove_port=False):
        """
        :return: ['10.0.0.17:27017', '10.0.0.15:27017', '10.0.0.16:27017']
        """
        result = self.get_items("cluster", "mongo")
        if remove_port:
            result = [host.split(":")[0] for host in result]
        return result

    def get_zk_members(self, remove_port=False):
        """
        :return: ['10.0.0.17:2181', '10.0.0.15:2181', '10.0.0.16:2181']
        """
        result = self.get_items('cluster', 'zookeeper')
        if remove_port:
            result = [host.split(":")[0] for host in result]
        return result

    def get_zbs_members(self):
        """
        :return: ['10.0.0.17', '10.0.0.15']
        """
        return self.get_items('cluster', 'members')

    def get_master_ips(self):
        return self.get_zbs_members()

    def get_cluster_mgt_ips(self):
        return self.get_items("cluster", "cluster_mgt_ips")

    def get_cluster_storage_ips(self):
        return self.get_items("cluster", "cluster_storage_ips")

    def save(self, cfg=None):
        if cfg is None:
            cfg = self.cfg
        with open(cfg, 'w+') as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            self.parser.write(f)


if __name__ == '__main__':
    cfg = Config("zbs-chunk")
    print cfg.get_items(section=None, key="CHUNK_SERVER_RPC_IP")
