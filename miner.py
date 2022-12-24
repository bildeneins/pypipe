from time import sleep
import json
from datetime import datetime
from random import randint

def main(policy_filename: str = 'policy_pipe.txt'):
  try:
    f = open(policy_filename, 'a', encoding='utf-8')
    # 11秒に1回より良いポリシーを見つける
    while True:
      new_policy = {
        "updated": str(datetime.now()),
        "param_a": randint(0, 10)
      }
      new_policy_str = json.dumps(new_policy)
      print('Found new policy: ', new_policy_str)
      f.write(f'{new_policy_str}\n')
      f.flush()
      sleep(11)
  
  except FileNotFoundError as e:
    print(e)

  finally:
    f.close()

main()