from character import Character # character.py を別ファイルにした場合

class Monster(Character):
    """敵キャラクタークラス（特別な行動はシンプルにランダム攻撃のみ）"""

    def __init__(self, name: str, hp: int, attack_power: int):
        # 親クラスのコンストラクタを呼び出すだけでOK
        super().__init__(name, hp, attack_power)
        print(f"[{self.name}] が襲いかかってきた！")

    # Characterクラスの attack メソッドを上書き（オーバーライド）
    def attack(self, target):
        """攻撃の前に、モンスター独自のメッセージを表示する"""
        
        # 継承元のメソッドを呼び出さず、独自に実装することも可能
        if not self.is_alive():
            print(f"[{self.name}] は行動できない...")
            return
            
        print(f"[{self.name}] は雄叫びを上げながら攻撃してきた！")
        target.take_damage(self.attack_power)

    def act(self, target):
        """Monster独自の行動：単純な攻撃"""
        if not self.is_alive():
            return

        print("\n--- モンスターのターン ---")
        self.attack(target) # Monster独自のattack（メッセージ付き）を呼び出す