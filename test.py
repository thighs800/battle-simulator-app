# テストコード
from character import Character
from hero import Hero
from monster import Monster

if __name__ == "__main__":
    hero = Hero("アレス", 120, 25, 50) # Heroクラスのインスタンス
    goblin = Monster("ゴブリン", 40, 15) # Monsterクラスのインスタンス

    print("\n--- 継承機能の確認 ---")
    
    # HeroはCharacterのメソッド（attack）を使える
    hero.attack(goblin)
    
    # Hero独自のメソッド（heal）を使える
    hero.heal(hero)
    
    # Monsterは独自のattackメソッドを使う
    goblin.attack(hero)
    
    print("\n--- 現在のステータス ---")
    print(hero)
    print(goblin)