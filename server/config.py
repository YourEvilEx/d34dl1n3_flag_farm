CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    # Подвести формат ip под нужный
    'TEAMS': {'Team #{}'.format(i): '10.0.0.{}'.format(i)
              for i in range(1, 29 + 1) if i != 'Namber_my_team'},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.
    # RuCTF(E) and VolgaCTF checksystems are supported out-of-the-box.
    # Изменить адрес чекера и его портю
    'SYSTEM_PROTOCOL': 'ructf_tcp',
    'SYSTEM_HOST': '127.0.0.1',
    'SYSTEM_PORT': 1337,

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',

    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    # Изменить время раунда и время жизни флага
    'SUBMIT_FLAG_LIMIT': 100,
    'SUBMIT_PERIOD': 0.5,
    'FLAG_LIFETIME': 5 * 120,
    
    

    # Password for the web interface. This key will be excluded from config
    # before sending it to farm clients.
    # Изменить пароль входа в ферму
    'SERVER_PASSWORD': '1234',
}
