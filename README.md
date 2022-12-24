# pypipe

リアルタイムで実験パラメータを更新するサンプル

- policy_pipe.txt: 一行に一つ実験ポリシーが記載される　一番下が最新
- experimenter.py: ７秒ごとに実験を開始する
- miner.py: 11秒ごとに新しい実験ポリシーを発見する

## Run example

To run experimenter:

```shell
python experimenter.py
```

To run miner:

```shell
python miner.py
```
