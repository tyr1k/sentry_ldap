  sentryConfPy: |
    import os
    import ldap
    import hvac
    from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
    
    vault_token = os.getenv('CHANGED')
    
    client = hvac.Client(
        url='https://CHANGED',
        token=vault_token,
    )
    
    vault_secrets = client.secrets.kv.v2.read_secret_version(
        path='CHANGED',
        mount_point='CHANGED'
    )
    
    ldap_server_uri = vault_secrets['data']['data']['CHANGED']
    ldap_bind_dn = vault_secrets['data']['data']['CHANGED']
    ldap_bind_password = vault_secrets['data']['data']['CHANGED']
    
    AUTH_LDAP_SERVER_URI = ldap_server_uri
    AUTH_LDAP_BIND_DN = ldap_bind_dn
    AUTH_LDAP_BIND_PASSWORD = ldap_bind_password
    
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        'CHANGED',
        ldap.SCOPE_SUBTREE, '(sAMAccountName=%(user)s)',
    )
    
    AUTH_LDAP_USER_ATTR_MAP = {
        'username': 'CHANGED',
        'name': 'CHANGED',
        'email': 'CHANGED'
    }
    
    AUTH_LDAP_MAIL_VERIFIED = True
    
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        'CHANGED',
        ldap.SCOPE_SUBTREE,
        '(objectClass=CHANGED)'
    )
    
    AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
    
    AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        "is_active": "CHANGED",
        "is_staff": "CHANGED",
        "is_superuser": "CHANGED"
    }
    
    AUTH_LDAP_SENTRY_GROUP_ROLE_MAPPING = {
        'owner': ['CHANGED'],
        'admin': ['CHANGED'],
        'member': ['CHANGED', 'CHANGED']
    }

    AUTH_LDAP_MAIL_VERIFIED = True
    AUTH_LDAP_SENTRY_DEFAULT_ORGANIZATION = 'CHANGED'
    AUTH_LDAP_SENTRY_ORGANIZATION_ROLE_TYPE = 'CHANGED'
    AUTH_LDAP_SENTRY_ORGANIZATION_GLOBAL_ACCESS = True
    AUTH_LDAP_REQUIRE_GROUP = None
    AUTH_LDAP_DENY_GROUP = None
    AUTH_LDAP_FIND_GROUP_PERMS = False
    AUTH_LDAP_CACHE_GROUPS = True
    AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600 

    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
        'CHANGED',
    )

    CSRF_TRUSTED_ORIGINS = ["CHANGED","CHANGED","CHANGED","CHANGED","CHANGED"]
    SECURE_PROXY_SSL_HEADER = ('CHANGED', 'CHANGED')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

    SENTRY_FEATURES['organizations:profiling-view'] = True
