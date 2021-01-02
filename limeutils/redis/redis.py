import redis as reds
from typing import Optional, Union, Any

from . import models
from .models import LT, V
from limeutils import byte_conv, parse_str
# from app.settings import settings as s



class Redis:
    ttl = 1209600  # seconds
    
    def __init__(self, **kwargs):
        self.pre = kwargs.pop('pre', '')
        self.ver = kwargs.pop('ver', '')
        self.r = reds.Redis(**kwargs)
    
    
    def _cleankey(self, data: models.StarterModel) -> str:
        """
        Create the final key name with prefix and/or version
        :param data: Contains the pre and ver data
        :return: Completed key
        """
        pre = data.pre and data.pre or self.pre.strip()
        ver = data.ver and data.ver or self.ver.strip()

        list_ = [pre, ver, data.key]
        list_ = list(filter(None, list_))
        return ":".join(list_)


    def _cleanmapping(self, mapping: Optional[dict] = None) -> dict: # noqa
        """
        Converts any None value to an empty string.
        :param mapping: Mapping values
        :return:        dict
        """
        if not mapping:
            return {}
        for k, v in mapping.items():
            mapping[k] = v is None and '' or v
        return mapping
        
    
    def hset(self, key: str, field: str, val: Optional[V] = '', mapping: Optional[dict] = None,
             ttl=None, pre=None, ver=None) -> int:
        """
        Add a single hash field using HSET
        :param key:     Hash key name
        :param field:   Field in the key
        :param val:     Value
        :param mapping: For multiple fields
        :param ttl:     Custom ttl
        :param pre:     Custom prefix
        :param ver:     Custom version
        :return:        Nubmer of items set. Updating an existing field counts as 0 not 1.
        """
        data = models.Hset(key=key, field=field, val=val, mapping=mapping,
                           ttl=ttl, pre=pre, ver=ver)
        key = self._cleankey(data)
        mapping = self._cleanmapping(data.mapping)
        ttl = data.ttl if data.ttl is not None else self.ttl

        ret = self.r.hset(key, data.field, data.val, mapping)
        self.r.expire(key, ttl)
        return ret
    

    def hmset(self, key: str, mapping: dict, ttl=None, pre=None, ver=None) -> int:
        """
        Add multiple hash fields. An alias for hset since hmset is deprecated.
        :param key:     Hash key name
        :param mapping: Fields in the key
        :param ttl:     Custom ttl
        :param pre:     Custom prefix
        :param ver:     Custom version
        :return:        Nubmer of items set. Updating an existing field counts as 0 not 1.
        """
        if not mapping:
            return 0
            
        data = models.Hmset(key=key, mapping=mapping, ttl=ttl, pre=pre, ver=ver)
        key = self._cleankey(data)
        mapping = self._cleanmapping(data.mapping)
        ttl = data.ttl if data.ttl is not None else self.ttl

        ret = self.r.hset(key, mapping=mapping)
        self.r.expire(key, ttl)
        return ret


    def hget(self, key: str, field: str, default: Any = '',
             pre=None, ver=None) -> Union[int, float, str]:
        """
        Get a single hash value from redis using HGET
        :param key:     Hash key name
        :param field:   Field in the key
        :param default: Default if !key
        :param pre:     Custom prefix
        :param ver:     Custom version
        :return:        Parsed string
        """
        data = models.StarterModel(key=key, pre=pre, ver=ver)
        key = self._cleankey(data)
        
        val = self.r.hget(key, field)
        val = byte_conv(val)
        return val if val or val == 0 else default


    def hmget(self, key: str, fields: Optional[LT] = None, pre=None, ver=None) -> dict:
        """
        Get multiple hash values form redis using HMGET
        :param key:     Hash key name
        :param fields:  Fields in the key. To get all keys just leave this empty.
        :param pre:     Custom prefix
        :param ver:     Custom version
        :return:        Parsed data in dict format
        """
        if isinstance(fields, list) and not len(fields):
            return {}
        
        data = models.Hmget(key=key, fields_=fields, pre=pre, ver=ver)
        key = self._cleankey(data)

        if fields is not None:
            val_list = self.r.hmget(key, data.fields_)
            v = map(lambda x: byte_conv(x), val_list)
            val_dict = dict(zip(fields, v))
        else:
            val_dict = self.r.hgetall(key)
            k = map(lambda x: byte_conv(x), val_dict.keys())
            v = map(lambda x: byte_conv(x), val_dict.values())
            val_dict = dict(zip(k, v))
        return val_dict


    # def hdel(key: str, *fields) -> int:
    #     """
    #     Delete a field from a a hash key
    #     Args:
    #         key (str): Key name with prefixes, if any
    #         *fields (str): Field names
    #
    #     Returns:
    #         Number of items deleted
    #     """
    #     prefix = get_cache_prefix()
    #     key = f'{prefix}:{key}'
    #
    #     count = redis.hdel(key, *fields)
    #
    #     return count