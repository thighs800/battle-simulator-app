from character import Character # character.py を別ファイルにした場合

class Hero(Character): # (Character) とすることで継承を指定
    """プレイヤーが操作するキャラクタークラス（回復能力を持つ）"""
    
    # 継承しているため、__init__ は定義しなくても使えるが、
    # 今回は Hero 独自の機能として 'max_mp' と 'mp' を追加する
    def __init__(self, name: str, hp: int, attack_power: int, mp: int):
        # 親クラス(Character)のコンストラクタを呼び出し、共通の属性を初期化
        super().__init__(name, hp, attack_power)
        
        # Hero独自の属性を追加
        self.mp = mp
        self.max_mp = mp
        
        print(f"[{self.name}] は特殊な勇者になりました。(MP: {self.mp})")

    def heal(self, target):
        """MPを消費してターゲットのHPを回復する（Hero独自の行動）"""
        mp_cost = 10
        heal_amount = 30
        
        if self.mp < mp_cost:
            print(f"[{self.name}]：MPが足りません！回復できませんでした。")
            return
        
        # MPを消費
        self.mp -= mp_cost
        
        # ターゲットのHPを回復（カプセル化の考えで、直接HPをいじるのではなくメソッドがあればそれを使うべきだが、
        # 今回はシンプルな実装として、直接HPに加算する）
        target.hp += heal_amount
        if target.hp > target.max_hp:
            target.hp = target.max_hp
            
        print(f"[{self.name}] は {target.name} を {heal_amount} 回復した！ (残りMP: {self.mp})")
        print(target)

    def __str__(self) -> str:
        """親クラスの __str__ を上書き（オーバーライド）し、MP情報も表示する"""
        # 親クラスのステータス情報と、独自のMP情報を結合して返す
        parent_status = super().__str__()
        return f"{parent_status}, MP: {self.mp}/{self.max_mp}"