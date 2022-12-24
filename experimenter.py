from time import sleep
import json

# 7秒かかる実験 与えられたポリシーに従う
def experiment(policy: dict):
  print(f"実験開始 ポリシー: {policy}")
  for i in range(7):
    print(f'実験中... {i+1}/7', end='\r', flush=True)
    sleep(1)
  print('実験中... 完了', flush=True)

# 一行のJSON文字列を辞書型に変換
def generate_policy(line: str) -> dict:
  return json.loads(line)


def main(policy_filename: str = 'policy_pipe.txt'):
  policy = None
  try:
    f = open(policy_filename, 'r', encoding='utf-8')
    while True:
      # ファイルを最後まで読み、最新のポリシーを採用
      lines = f.readlines()
      if len(lines) > 0:
        policy = generate_policy(lines[-1])
      if policy is None:
        print('Found no policies. exit')
        exit(1)
      experiment(policy)

  except FileNotFoundError as e:
    print(e)

  finally:
    f.close()
  
main()