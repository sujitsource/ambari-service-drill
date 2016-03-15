import sys, os, pwd, grp, signal, time
from resource_management import *

class drillbit(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Master'
        self.install_packages(env)
    def stop(self, env):
        print 'Stop the Master'
    def start(self, env):
        import params
        env.set_params(params)
        print 'Start the Master'
    def status(self, env):
        print 'Status of the Master'
if __name__ == "__main__":
    DummyMaster().execute()