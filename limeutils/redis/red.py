from redis import Redis
from typing import Optional, Union, Any, Literal
from pydantic import BaseModel
from redis.client import list_or_args
from redis.exceptions import ResponseError

from . import models
from icecream import ic
from .models import LIST, VAL, StarterModel
from limeutils import byte_conv, ValidationError




class Red(Redis):
    
    def __init__(self, *args, **kwargs):
        self.pre = kwargs.pop('pre', '')
        self.ver = kwargs.pop('ver', '')
        self.ttl = kwargs.pop('ttl', -1)
        self.clear_wrongtype = kwargs.pop('wrongtype', True)
        super().__init__(*args, **kwargs)

    
    def formatkey(self, key: str) -> str:
        """
        Create the final key name with prefix and/or version
        :param key: The key to format
        :return:    str
        """
        pre = self.pre.strip()
        ver = self.ver.strip()

        list_ = [pre, ver, key]
        list_ = list(filter(None, list_))
        return ":".join(list_)

    # TODO: How can they change the datatype if the datatype is set by the existing variable?
    def set(self, key: str, val: Union[VAL, LIST, set, dict], **kwargs):
        """
        Set and updates a key
        :param key:     Key name
        :param val:     Value to save. Could be any valid value inc dict or list
        :param kwargs:  Checks for clear and insert
        :return:
        """
        key = self.formatkey(key)
        clear = kwargs.pop('clear', False)
        insert = kwargs.pop('insert', 'end')
        
        if clear:
            self.delete(key)
        
        if isinstance(val, (str, int, float, bytes)):
            if self.clear_wrongtype and self._get_type(key) != 'string':
                self.delete(key)
            return super().set(key, val, **kwargs)
        
        elif isinstance(val, (list, tuple)):
            if self.clear_wrongtype and self._get_type(key) != 'list':
                self.delete(key)
                    
            if insert == 'end':
                return self.rpush(key, *val)
            elif insert == 'start':
                return self.lpush(key, *val)
            else:
                raise ValidationError(choices=['start', 'end'])
            
        elif isinstance(val, dict):
            if self.clear_wrongtype and self._get_type(key) != 'hash':
                self.delete(key)
            return self.hset(key, mapping=val)
        
        elif isinstance(val, set):
            if self.clear_wrongtype and self._get_type(key) != 'set':
                self.delete(key)
            return self.sadd(key, *val)
    
    
    def get(self, key: str, **kwargs):
        start = kwargs.pop('start', 0)
        end = kwargs.pop('end', -1)
        only = kwargs.pop('only', None)
        
        key = self.formatkey(key)
        datatype = byte_conv(super().type(key))
        
        if datatype == 'string':
            return byte_conv(super().get(key))
        
        elif datatype == 'list':
            data = super().lrange(key, start, end)
            return [byte_conv(i) for i in data]
        
        elif datatype == 'hash':
            if only:
                only = [only] if isinstance(only, str) else list(only)
                data = super().hmget(key, only)
                data = [byte_conv(i) for i in data]
                d = dict(zip(only, data))
            else:
                data = super().hgetall(key)
                d = {byte_conv(k):byte_conv(v) for k, v in data.items()}
            # ic(d)
            return d
        elif datatype == 'set':
            data = super().smembers(key)
            return {byte_conv(v) for v in data}


    def exists(self, *keys):
        keys = [self.formatkey(i) for i in keys]
        return super().exists(*keys)
    
    
    def _get_type(self, key: str):
        return byte_conv(super().type(key))
        # data = models.Set(key=key, val=val, xx=xx, keepttl=keepttl, ttl=ttl, pre=pre, ver=ver)
        # key = self.formatkey(data)
        # ttl = data.ttl if data.ttl is not None else self.ttl
        #
        # self.pipe.set(key, data.val, xx=data.xx, keepttl=data.keepttl)
        # self.pipe.expire(key, ttl)
        # [set_ret, _] = self.pipe.execute()
        # return set_ret

# class Redis:
#     def __init__(self, **kwargs):
#         self.conn = reds.Redis(**kwargs)
#
#
#
#
#
#     def hset(self, key: str, field: str, val: Optional[V] = '', mapping: Optional[dict] = None,
#              ttl=None, pre=None, ver=None) -> int:
#         """
#         Add a single hash field using HSET
#         :param key:     Hash key name
#         :param field:   Field in the key
#         :param val:     Value
#         :param mapping: For multiple fields
#         :param ttl:     Custom ttl
#         :param pre:     Custom prefix
#         :param ver:     Custom version
#         :return:        Number of fields set. Updating an existing field counts as 0 not 1.
#         """
#         data = models.Hset(key=key, field=field, val=val, mapping=mapping,
#                            ttl=ttl, pre=pre, ver=ver)
#         key = self.cleankey(data)
#         ttl = data.ttl if data.ttl is not None else self.ttl
#
#         self.pipe.hset(key, data.field, data.val, data.mapping)
#         self.pipe.expire(key, ttl)
#         [hset_ret, _] = self.pipe.execute()
#         return hset_ret