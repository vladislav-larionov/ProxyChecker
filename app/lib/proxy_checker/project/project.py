import os
from datetime import datetime
from os.path import normpath, join

from app.lib.proxy.proxy import Proxy


class Project:

    def __init__(self):
        self.__project_path = normpath(join(os.getcwd(), datetime.now().strftime('Project [%d_%m_%Y]/Results [%H_%M_%S]')))
        os.makedirs(self.project_path)

    @property
    def project_path(self):
        return self.__project_path

    def store_good_proxy(self, proxy: Proxy):
        with open("{project_path}\{proxy_type}.txt".format(project_path=self.project_path, proxy_type=proxy.proxy_type),
                  "a") as proxy_file:
            proxy_file.write(str(proxy))
            proxy_file.write("\n")
