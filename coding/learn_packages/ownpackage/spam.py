# -*- coding: utf-8 -*-
import pkgutil

data = pkgutil.get_data("ownpackage", 'somedata.dat')
print(data.decode("utf-8"))
