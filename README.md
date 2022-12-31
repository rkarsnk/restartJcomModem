# restartJcomModem
J:COMのKAON KCM-3100をWebGUI経由で再起動するプログラム

## 使い方
### 依存pythonライブラリのインストール
```
$ python3 -m pip install requests
```

### username/passwordの編集
ソースコードの以下の箇所に記載されている`admin`と`password`を自分の環境にあわせて編集する．
```
auth = {
    "username":"admin",
    "password":"password"
}
```

### 実行方法
```
$ python3 restartJcomModem.py
```
