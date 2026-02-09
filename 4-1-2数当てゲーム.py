import random

def number_guessing_game():
    """
    1～100の間の数字を当てるゲーム
    """
    # 1～100の間のランダムな数字を生成
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("=" * 50)
    print("数当てゲームへようこそ！")
    print("1～100の間の数字を当ててください。")
    print("=" * 50)
    
    while True:
        try:
            # ユーザーからの入力を受け取る
            guess = int(input("\n数字を入力してください: "))
            attempts += 1
            
            # 入力値の範囲チェック
            if guess < 1 or guess > 100:
                print("⚠️  1～100の間の数字を入力してください。")
                continue
            
            # 正解かどうかを判定
            if guess == target_number:
                print(f"\n🎉 正解です！")
                print(f"答えは {target_number} でした。")
                print(f"\n✨ 試行回数: {attempts}回 ✨")
                break
            elif guess < target_number:
                # 正解との差を計算
                difference = target_number - guess
                if difference <= 2:
                    print(f"💡 もう少しだけ大きいです。")
                else:
                    print(f"💡 もっと大きいです。")
            else:
                # 正解との差を計算
                difference = guess - target_number
                if difference <= 2:
                    print(f"💡 もう少しだけ小さいです。")
                else:
                    print(f"💡 もっと小さいです。")
                
        except ValueError:
            print("⚠️  数字を入力してください。")
        except KeyboardInterrupt:
            print("\n\nゲームを終了します。")
            break

if __name__ == "__main__":
    number_guessing_game()

