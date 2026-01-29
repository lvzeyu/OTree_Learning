from otree.api import *




doc = """
公共財ゲーム実験
"""




class C(BaseConstants):
    NAME_IN_URL = 'publicgoods_trial'
    PLAYERS_PER_GROUP = 7
    # 7人プレイヤー
    NUM_ROUNDS = 10
    # 10期繰り返し
    ENDOWMENT = cu(20)
    # 初期保有額は20ポイント
    MULTIPLIER = 1.6
    # 全員の貢献額の合計を1.6倍にします


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    # グループの貢献額を入れるオブジェクト
    individual_share = models.CurrencyField()
    # 各プレイヤーの個別の分配額を入れるオブジェクト


class Player(BasePlayer):
    contribution = models.CurrencyField(
        # プレイヤーの貢献額を入れるオブジェクト
        choices = currency_range(cu(0), C.ENDOWMENT, cu(1)),
        # 0から初期保有額（20ポイント）までの1ポイント刻みの選択肢を表示する
        label = 'あなたはいくら貢献しますか？'
        # 貢献額の選択肢の前に設問文を表示する
    )




def compute(group: Group):
    players = group.get_players()
    # groupクラスに所属するプレイヤーの情報を取得
    contrbutions = [p.contribution for p in players]
    # プレイヤーの貢献額をリストにまとめる
    group.total_contribution = sum(contrbutions)
    # グループの総貢献額を計算
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    # 各プレイヤーへの分配額を計算
    for p in players:
    # 各プレイヤーの獲得額を計算
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share
        # 各プレイヤーのpayoffは初期保有額から貢献額を引いて各プレイヤーへの分配額を加えたものである


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
    # もし第1期なら
        subsession.group_randomly()
        # ランダムにグループに割り当てる
    else:
        subsession.group_like_round(1)
        # 1期目と同じグループに割り当てる




# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['contribution']
    # プレイヤーが貢献額を入力する


class Page2(WaitPage):
    after_all_players_arrive = compute
    # 全プレイヤーがPage1で貢献額を入力したあとにcompute関数を実行する


class Page3(Page):
    pass




page_sequence = [Page1, Page2, Page3]
