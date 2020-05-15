import json

#region access to parent folder of the solution
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
#endregion

from DataContext import DataContext
from Entities.User import User
from Util.DateTimeEncoder import DateTimeEncoder
from Util.ResourcesUtil import ResourcesUtil
from Util.Constant.SqlSentences import SqlSentences

class UserAccess(DataContext):

    def GetUsers(self):
        users = []
        data = self.Get(ResourcesUtil.GetEntryValue(SqlSentences.SELECT_USERS()))

        for obj in data:
            users.append(json.loads(json.dumps(obj, cls=DateTimeEncoder), object_hook=User))
        return users

    def GetUser(self, id):
        sql = ResourcesUtil.GetEntryValue(SqlSentences.SELECT_USER())
        data = self.GetById(sql, (id,))
        return json.loads(json.dumps(data, cls=DateTimeEncoder), object_hook=User)

    def InsertUser(self, user):
        val = (user.username, user.password, user.last_login, user.attempt, user.status, user.email)
        return self.Execute(ResourcesUtil.GetEntryValue(SqlSentences.INSERT_USER()), val)

    def UpdateUser(self, input):
        val = (input.username, input.password, input.last_login, input.attempt, input.status, input.email, input.id)
        return self.Execute(ResourcesUtil.GetEntryValue(SqlSentences.UPDATE_USER()), val)
    
    def DeleteUser(self, id):
        return self.Execute(ResourcesUtil.GetEntryValue(SqlSentences.DELETE_USER()), (id,))