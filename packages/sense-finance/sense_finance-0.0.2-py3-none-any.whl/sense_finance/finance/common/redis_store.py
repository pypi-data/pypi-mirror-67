import sense_core as sd
import redis
from sense_core import Encryption
from sense_finance.finance.util import parse_config

REDIS_DB_FINANCE_COMPANY = 10
REDIS_DB_FINANCE_CUSTOM_PARAM = 11
REDIS_DB_OPINION_INDUSTRY_COMPANY = 9
REDIS_DB_OPINION_INDUSTRY_RISK = 8
REDIS_DB_PLEDGE = 12
REDIS_DB_BACKSTAGE = 7
REDIS_DB_FINANCE_REPORT = 13
REDIS_DB_FINANCE_FACTOR = 14
REDIS_DB_ESTATE = 6


def get_redis_client(db=0, label='redis', config_map=None):
    if config_map:
        redis_host = config_map['host']
        redis_port = int(config_map['port'])
        redis_pass = config_map['pass'] if config_map.get('pass') else config_map['password']
    else:
        redis_host = sd.config(label, 'host')
        redis_port = int(sd.config(label, 'port'))
        redis_pass = sd.config(label, 'pass', '')
        if redis_pass == '':
            redis_pass = sd.config(label, 'password', '')
    client = redis.Redis(host=redis_host, port=redis_port, password=redis_pass, db=db)
    return client


def get_finance_company_key(uid, type, model_class=None):
    if model_class:
        return '{0}_{1}_{2}'.format(uid, type, model_class)
    return '{0}_{1}'.format(uid, type)


def get_finance_custom_param_key(uid, model_class):
    return '{0}_{1}'.format(uid, model_class)


class RedisStore(object):

    def __init__(self, db, time_out=3600 * 24 * 7):
        config_map = {
            'host': sd.config('redis', 'host'),
            'port': sd.config('redis', 'port'),
            'password': parse_config('redis', 'password')
        }
        self.config_en_map = Encryption.decrypt_dict(config_map, ignore=['host', 'port'])
        self.time_out = time_out
        self.db = db
        self.clients = None

    def get_redis_data(self, key):
        try:
            self.clients = get_redis_client(self.db, 'redis', self.config_en_map)
            val = self.clients.get(key)
            data = sd.load_json(val)
            self.clients.close()
            if data is None:
                sd.log_info("get_redis_data data is none with val={0} for {1}".format(val, key))
            return data
        except Exception as ex:
            sd.log_exception(ex)
            return None

    def update_data(self, key, data):
        try:
            self.clients = get_redis_client(self.db, 'redis', self.config_en_map)
            self.clients.set(key, sd.dump_json(data), ex=self.time_out)
            sd.log_info("update redis db={0} key={1}".format(self.db, key))
            self.clients.close()
        except Exception as ex:
            sd.log_exception(ex)

    def update_hash_data(self, name, key, value):
        try:
            self.clients = get_redis_client(self.db, 'redis', self.config_en_map)
            self.clients.hset(name, key, value)
            sd.log_info("update redis db={0} name={1}, key={2}".format(self.db, name, key))
            self.clients.close()
        except Exception as ex:
            sd.log_exception(ex)

    def bulk_hash_data(self, name, map_data):
        try:
            self.clients = get_redis_client(self.db, 'redis', self.config_en_map)
            self.clients.hmset(name, map_data)
            sd.log_info("bulk_hash_data redis db={0} name={1}".format(self.db, name))
            self.clients.close()
        except Exception as ex:
            sd.log_exception(ex)

    def get_hash_data(self, name, key):
        try:
            self.clients = get_redis_client(self.db, 'redis', self.config_en_map)
            data = sd.load_json(self.clients.hget(name, key))
            self.clients.close()
            return data
        except Exception as ex:
            sd.log_exception(ex)
            return None
