__all__ = ['ACL']

ACL = {
    "developer": 1,
    "support": 2,
    "customer": 4,
}

ACL.update({k.upper(): v for k, v in ACL.items()})

DEFAULT_FORMAT = '%(name)s: (%(asctime)s) [%(levelname)s] -\n%(message)s'
