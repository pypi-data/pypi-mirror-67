from __future__ import print_function

from abc import ABCMeta

#@todo fix exception parameters
class HaloException(Exception):
    __metaclass__ = ABCMeta
    """
    The abstract exception is used as base class. app expects to handle exception. Accepts the following
    optional arguments:
    """
    def __init__(self, message, detail=None,data=None):
        super(HaloException,self).__init__()
        self.message = message
        self.detail = detail
        self.data = data

    def __str__(self):
        return str(
            self.message)  # __str__() obviously expects a string to be returned, so make sure not to send any other data types

class HaloError(HaloException):
    __metaclass__ = ABCMeta
    """
    The abstract error is used as base class. app does not expect to handle error. Accepts the following
    optional arguments:
    """
    pass

class AuthException(HaloException):
    pass


class ApiException(HaloException):
    pass


class MaxTryException(ApiException):
    pass


class MaxTryHttpException(MaxTryException):
    pass


class MaxTryRpcException(MaxTryException):
    pass


class ApiTimeOutExpired(ApiException):
    pass


class ApiError(HaloError):
    pass


class DbError(HaloError):
    pass


class DbIdemError(DbError):
    pass


class CacheError(HaloError):
    pass


class CacheKeyError(CacheError):
    pass


class CacheExpireError(CacheError):
    pass

class HaloHttpError(HaloError):
    """Custom exception class to be thrown when local request error occurs."""
    def __init__(self, message, detail=None,data=None, http_status=400):
        super(HaloHttpError,self).__init__(message, detail,data)
        self.status = http_status

class BadRequestError(HaloHttpError):
    """Custom exception class to be thrown when local request error occurs."""
    pass

class ServerError(HaloHttpError):
    """Custom exception class to be thrown when local server error occurs."""
    def __init__(self, message, detail=None, data=None, http_status=500):
        super(HaloHttpError, self).__init__(message, detail, data)
        self.status = http_status

class ProviderError(HaloError):
    pass

class NoLocalSSMClassError(HaloError):
    pass

class NoLocalSSMModuleError(HaloError):
    pass

class BusinessEventMissingSeqException(HaloException):
    pass

class HaloMethodNotImplementedException(HaloException):
    pass

class IllegalBQException(HaloException):
    pass

class NoApiDefinitionError(HaloError):
    pass

class ApiClassError(HaloError):
    pass

class NoApiClassException(HaloException):
    pass

class StoreException(HaloException):
    pass

class StoreClearException(HaloException):
    pass

class MissingHaloContextException(HaloException):
    pass

class NoCorrelationIdException(HaloException):
    pass

class ReflectException(HaloException):
    pass