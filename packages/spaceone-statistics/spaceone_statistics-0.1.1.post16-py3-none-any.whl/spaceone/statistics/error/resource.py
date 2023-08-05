from spaceone.core.error import *


class ERROR_NOT_SUPPORT_RESOURCE_TYPE(ERROR_INVALID_ARGUMENT):
    _message = 'Resource type not supported. (resource_type = {resource_type})'


class ERROR_STATISTICS_QUERY(ERROR_INVALID_ARGUMENT):
    _message = 'Statistics query failed. (reason = {reason})'


class ERROR_STATISTICS_JOIN(ERROR_INVALID_ARGUMENT):
    _message = 'Join key dose not exist. (resource_type = {resource_type}, join_keys = {join_keys})'


class ERROR_STATISTICS_FORMULA(ERROR_INVALID_ARGUMENT):
    _message = 'Statistics formula error: {formula}'
