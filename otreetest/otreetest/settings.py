from os import environ


SESSION_CONFIGS = [
    dict(
        name = 'questionaire',
        # この構成の名前を設定します
        display_name = "はじめてのアンケート",
        # oTreeのデモ画面で表示される名前を設定します
        num_demo_participants = 1,
        # デモ画面に参加する人数を設定しておく必要があります
        app_sequence = ['questionnaire']
        # この構成で使用するアプリケーションを設定します
    ),
    dict(
        name = 'PG3',
        display_name = "はじめての公共財ゲーム",
        num_demo_participants = 7,
        app_sequence = ['publicgoods_trial']
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1314096243272'

ROOMS=[
    dict(
        name='label',
        display_name='Questionaire Room',
        participant_label_file='./_rooms/label.txt'
    )
]