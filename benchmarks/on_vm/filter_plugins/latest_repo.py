#!/usr/bin/python
import os

class FilterModule(object):
    def filters(self):
        return {
            'latest_repo': self.latest_repo
        }
    def latest_repo(self, a_variable):
        cdir= "cd " + a_variable + " &&"
        git_command= cdir  + " git describe --tags $(git rev-list --tags --max-count=10)"
        val= os.system(git_command)
        return val


