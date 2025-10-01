class Character:
    """戦闘に参加するすべてのキャラクターの基本クラス"""

    def __init__(self, name: str, hp: int, attack_power: int):
        # 属性（データ）の初期化
        self.name = name
        self.hp = hp
        self.max_hp = hp  # 最大HPを保持
        self.attack_power = attack_power
        
        # オブジェクトが生成されたことを確認
        print(f"[{self.name}] が生成されました。HP: {self.hp}, 攻撃力: {self.attack_power}")

    def is_alive(self) -> bool:
        """キャラクターが生きているか（HPが0より大きいか）を判定する"""
        return self.hp > 0

    def __str__(self) -> str:
        """print()関数でオブジェクトを表示したときに呼び出される（デバッグやステータス表示に便利）"""
        return f"[{self.name}] HP: {self.hp}/{self.max_hp}, 攻撃力: {self.attack_power}"

    def take_damage(self, damage: int):
        """ダメージを受けてHPを減少させる（カプセル化の概念）"""
        
        # ダメージが負の値でないことを保証
        if damage < 0:
            damage = 0

        # HPを減少
        self.hp -= damage
        print(f"[{self.name}] は {damage} のダメージを受けた！ (残りHP: {self.hp})")

        # 状態変化のロジック
        if self.hp <= 0:
            self.hp = 0 # HPがマイナスにならないようにする
            print(f"[{self.name}] は力尽きた...")

    def attack(self, target):
        """指定したターゲットに攻撃する"""
        if not self.is_alive():
            print(f"[{self.name}] は行動できない...")
            return

        print(f"[{self.name}] の攻撃！")
        # ターゲットの take_damage メソッドを呼び出す
        target.take_damage(self.attack_power)

    def act(self, target):
        """キャラクターの基本的な行動（攻撃）"""
        self.attack(target)

# 実行テスト (character.py の if __name__ == "__main__": ブロックを以下に置き換え)
if __name__ == "__main__":
    hero = Character("勇者", 100, 20)
    monster = Character("ゴブリン", 50, 10)

    print("\n--- 戦闘開始 ---")
    # 勇者がゴブリンを攻撃
    hero.attack(monster)
    print(monster)
    
    # ゴブリンが勇者を攻撃
    monster.attack(hero)
    print(hero)

    # 大ダメージテスト（カプセル化された take_damage の動作確認）
    print("\n--- オーバーキルテスト ---")
    monster.take_damage(100) # HP50のゴブリンに100ダメージ
    print(monster) # HPが0になっているか確認

# 実行テスト (Character.py のファイル末尾に追加して実行)
if __name__ == "__main__":
    # オブジェクトの生成
    hero = Character("勇者", 100, 20)
    monster = Character("ゴブリン", 50, 10)

    # __str__ メソッドのテスト
    print("\n--- 現在のステータス ---")
    print(hero)
    print(monster)

    print(f"\n勇者は生きているか？: {hero.is_alive()}")