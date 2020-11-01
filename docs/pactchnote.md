# Virtual2038のアップデート
## 2.0 GA

モジュールとしてインポートすることによって別のPythonスクリプトから現在の32bitUnix時刻を表示できるようになりました

```py
import Virtual2038

now=Virtual2038.now()
# 現在時刻の表示
print(now["RealTime"])
# Unix時間を10進法で
print(now["decimal"])
# Unix時間を2進法で
print(now["binary"])
```