from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    # 1人の時はNoneと記述する
    NUM_ROUNDS = 1
    # 質問は1度だけ

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models.CharField(initial = None,
                                choices = ['男性', '女性', "回答しない"],
                                verbose_name = 'あなたの性別を教えてください',
                                widget = widgets.RadioSelect)
    # ラジオボタンを使うときはwidget = widgets.RadioSelectを記述する

    q_age = models.IntegerField(initial = None,
                                verbose_name = 'あなたの年齢を教えてください',
                                choices = range(0, 125)
                                )
    # 数字の場合は"choices"を使うことで範囲を指定できる
    # 0<= q_age < 125になるので，表示される最小値は0，最大値は124となる

    q_area = models.CharField(initial = None,
                              choices = ['北海道', '東北地方', '関東地方',
                                         '中部地方', '近畿地方', '中国地方', 
                                         '四国地方', '九州地方'],
                             verbose_name = 'あなたのお住まいの地域を教えてください'
                             )
    q_tanmatsu = models.CharField(initial = None,
                                  choices = ['パソコン', 
                                            'タブレット',
                                            'スマートフォン',
                                            'それ以外'],
                                            verbose_name = '解答端末を教えてください',
                                            widget = widgets.RadioSelect
                                            )
    living_alone = models.StringField(

        label='現在、一人暮らしですか？',

        choices=[

            ('はい', 'はい'),

            ('いいえ', 'いいえ')

        ]

    )
    
    is_student = models.BooleanField(

        label='あなたは学生ですか？',

        widget=widgets.RadioSelect,

        choices=[(True, 'はい'), (False, 'いいえ')]

    )


# PAGES
class Page1(Page):
    form_model = 'player'
    # 各フィールドはplayerクラスで定義されている
    form_fields = [
        'q_gender','q_age','q_area','q_tanmatsu',"living_alone","is_student"
    ]
    # 質問項目は4つある


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page1]