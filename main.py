import time
import random
import os
import sys

TYPE_FIRE = "ほのお"
TYPE_WATER = "みず"
TYPE_GRASS = "くさ"

TYPE_CHART = {
    TYPE_FIRE: TYPE_GRASS,
    TYPE_WATER: TYPE_FIRE,
    TYPE_GRASS: TYPE_WATER
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_bar(current, max_val, length=20, color_char="#"):
    ratio = current / max_val
    filled_len = int(length * ratio)
    bar = color_char * filled_len + "-" * (length - filled_len)
    return f"[{bar}] {current}/{max_val}"

class Pokemon:
    def __init__(self, name, p_type, max_hp, attack_power):
        self.name = name
        self.type = p_type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_power = attack_power

    def is_fainted(self):
        return self.current_hp <= 0

    def heal(self):
        heal_amount = 30
        self.current_hp = min(self.max_hp, self.current_hp + heal_amount)
        slow_print(f"\n✨ {self.name} は きずぐすり をつかった！")
        slow_print(f"   HPが {heal_amount} かいふくした！")
        time.sleep(1)

    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)

    def attack(self, target):
        slow_print(f"\n⚔️  {self.name} の こうげき！")
        time.sleep(0.5)

        base_damage = self.attack_power + random.randint(-5, 5)
        multiplier = 1.0
        message = ""

        if TYPE_CHART.get(self.type) == target.type:
            multiplier = 2.0
            message = "🎯 こうかは ばつぐんだ！"
        elif TYPE_CHART.get(target.type) == self.type:
            multiplier = 0.5
            message = "🛡️ こうかは いまひとつのようだ..."

        damage = int(base_damage * multiplier)
        target.take_damage(damage)

        print(f"   {target.name} に {damage} のダメージ！")
        if message:
            print(f"   {message}")
        time.sleep(1)

def show_start_screen():
    clear_screen()
    print("=" * 40)
    print(r"""
    ____        __  __                  
   / __ \__  __/ /_/ /_  ____  ____     
  / /_/ / / / / __/ __ \/ __ \/ __ \    
 / ____/ /_/ / /_/ / / / /_/ / / / /    
/_/    \__, /\__/_/ /_/\____/_/ /_/     
      /____/                            
       TERMINAL BATTLE EDITION
    """)
    print("=" * 40)
    print("\n      ENTERキー をおして スタート！")
    input()

def select_pokemon():
    clear_screen()
    slow_print("オーキド博士: 「ここに 3びきの ポケモンが おる。」")
    slow_print("「さあ、すきな ポケモンを えらぶのじゃ！」\n")
    
    starters = [
        Pokemon("ヒトカゲ", TYPE_FIRE, 100, 22),
        Pokemon("ゼニガメ", TYPE_WATER, 110, 18),
        Pokemon("フシギダネ", TYPE_GRASS, 120, 16)
    ]

    print("1. ヒトカゲ   (タイプ: ほのお)")
    print("2. ゼニガメ   (タイプ: みず)")
    print("3. フシギダネ (タイプ: くさ)")

    while True:
        choice = input("\n>> 番号を入力してください (1-3): ")
        if choice in ["1", "2", "3"]:
            selected = starters[int(choice) - 1]
            slow_print(f"\nオーキド博士: 「{selected.name} に決めたのじゃな！ よし！」")
            time.sleep(1)
            return selected
        else:
            print("1から3の数字で選んでね。")

def battle_scene(player_poke, enemy_poke):
    clear_screen()
    slow_print(f"あ！ 野生の {enemy_poke.name} が とびだしてきた！\n")
    time.sleep(1)
    
    slow_print(f"ゆけっ！ {player_poke.name}！")
    time.sleep(1)

    while True:

        clear_screen()
        print(f"🔻 敵: {enemy_poke.name} ({enemy_poke.type})")
        print(draw_bar(enemy_poke.current_hp, enemy_poke.max_hp))
        print("\n" + "-"*30 + "\n")
        print(f"🟢 自分: {player_poke.name} ({player_poke.type})")
        print(draw_bar(player_poke.current_hp, player_poke.max_hp))
        print("-" * 30)

        print("\nどうする？")
        print("1. たたかう")
        print("2. かいふく (HP30回復)")
        print("3. にげる")
        
        action = input(">> ")

        if action == "1":
            player_poke.attack(enemy_poke)
        elif action == "2":
            player_poke.heal()
        elif action == "3":
            slow_print("\n🏃 うまく にげきれた！")
            return "run"
        else:
            continue # 無効な入力はスキップ

        if enemy_poke.is_fainted():
            slow_print(f"\n🌟 {enemy_poke.name} は たおれた！")
            slow_print("   勝負に かった！")
            return "win"

        enemy_action = random.choice(["attack", "attack", "attack", "wait"]) # 3/4で攻撃
        if enemy_action == "attack":
            enemy_poke.attack(player_poke)
        else:
            slow_print(f"\n👀 {enemy_poke.name} は 様子をみている...")
            time.sleep(1)

        if player_poke.is_fainted():
            slow_print(f"\n💀 {player_poke.name} は たおれた...")
            slow_print("   目の前が まっくらに なった...")
            return "lose"

def main():
    while True:
        show_start_screen()
        
        player_mon = select_pokemon()
        
        rival_idx = random.randint(0, 2)
        enemies = [
            Pokemon("ブースター", TYPE_FIRE, 105, 20),
            Pokemon("シャワーズ", TYPE_WATER, 115, 17),
            Pokemon("リーフィア", TYPE_GRASS, 125, 15)
        ]
        enemy_mon = enemies[rival_idx]

        result = battle_scene(player_mon, enemy_mon)
        
        print("\n" + "="*30)
        if result == "win":
            print("🏆 CONGRATULATIONS! 🏆")
        elif result == "lose":
            print("GAME OVER...")
        print("="*30)

        retry = input("\nもういちど あそぶ？ (y/n): ")
        if retry.lower() != 'y':
            print("またあそんでね！")
            break

if __name__ == "__main__":
    main()