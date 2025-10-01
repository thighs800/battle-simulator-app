from hero import Hero
from monster import Monster

def start_battle(hero: Hero, monster: Monster):
    """戦闘のメインループを実行する"""
    print("===================================")
    print(f" 戦闘開始！ {hero.name} VS {monster.name} ")
    print("===================================")

    # 戦闘が続く条件: 両者が生きている間
    turn = 1
    while hero.is_alive() and monster.is_alive():
        print(f"\n>>>> ターン {turn} <<<<")
        
        # ------------------------------------------------
        # 💡 ポリモーフィズムの核心
        # ------------------------------------------------
        # heroはHeroクラスのact()が実行され、ユーザー入力を処理する
        hero.act(monster)
        
        # monsterはMonsterクラスのact()が実行され、単純攻撃を実行する
        # 同じ act() という名前でも、オブジェクトの種類によって振る舞いが異なる！
        if monster.is_alive(): # ヒーローの攻撃で倒れていないかチェック
            monster.act(hero) 
        
        print("\n--- ターン終了後のステータス ---")
        print(hero)
        print(monster)
        
        turn += 1

    # 戦闘終了後の結果表示
    print("\n===================================")
    if hero.is_alive():
        print(f" 🎊 {hero.name} の勝利！ 🎊")
    elif monster.is_alive():
        print(f" 💀 {monster.name} の勝利... 💀")
    else:
        print(" 両者とも力尽きた！引き分け。 ")
    print("===================================")

# メイン処理
if __name__ == "__main__":
    # オブジェクトの生成
    player = Hero("アレス", 120, 25, 50)
    enemy = Monster("オーガ", 90, 18)

    # 戦闘開始
    start_battle(player, enemy)