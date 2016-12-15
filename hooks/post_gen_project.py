import string
from subprocess import call
from random import SystemRandom

call(['git', 'clone', 'https://github.com/cybercommons/cybercom-portal', 'data/static/portal'])
call(['git', 'clone', 'https://github.com/cybercommons/cybercom-api', 'api_code']) # -v /api /usr/


# Generate keys on creation
with open(r'config/ssl/rabbitmq/keystoresecret', 'w') as f:
    f.write(''.join(SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(32)))

call(['run/genSSLKeys'])
