#!python3
#encoding:utf-8
import web.http.Response
import web.service.github.api.v3.Response
#import web.service.github.api.v3.RequestParam
import web.service.github.api.v3.RequestParameter
from web.service.github.api.v3.miscellaneous import Licenses
from web.service.github.api.v3.repositories import Repositories
class Client(object):
    def __init__(self, db, authentications, authData=None, repo=None):
        self.__db = db
        self.__repo = repo
        self.__authData = authData
#        self.__reqp = web.service.github.api.v3.RequestParam.RequestParam(self.__db, self.__authData)
        self.__reqp = web.service.github.api.v3.RequestParameter.RequestParameter(self.__db, authentications)
#        self.__reqp = web.service.github.api.v3.RequestParam.RequestParam(self.__db, self.__user)
        self.__response = web.service.github.api.v3.Response.Response()
        self.license = Licenses.Licenses(self.__reqp, self.__response)
        self.repo = Repositories.Repositories(self.__reqp, self.__response, self.__authData, self.__repo)
#        self.repo = Repositories.Repositories(self.__reqp, self.__response, self.__user, self.__repo)

