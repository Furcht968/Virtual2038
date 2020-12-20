# Virtual2038のアップデート
## 2.1 GA

このPythonスクリプトをモジュールとしてインポートして出力した場合、配列によっていろいろ制御する必要がありましたが、Classで置き換え可能です！

```py
import Virtual2038

now=Virtual2038.now()
# 現在時刻の表示
print(now.RealTime)
# Unix時間を10進法で
print(now.decimal)
# Unix時間を2進法で
print(now.binary)
# オーバーフローまでの時間
print(now.until)
```