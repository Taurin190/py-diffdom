# py-diffdom
Pythonを用いたHTMLのdiff check tool.
DOM単位での比較を行い、毎回差分が出る部分は無視する。


## Description
以前、shellでdiffを使ってステージング環境と本番環境や、
プラットフォーム移設を行った時に、
同じ環境での差分を比較するツールを作成した。

以前のツールでは、広告やデータベースのデータや実行した時間による誤差が大量に出て、
狼ツール化してしまったので、その改良版として作成する。

以下の部分を作成しようと思う。
- 毎回diffとして出る部分は無視する
- 変化する部分はline単位で無く、dom単位で検知する
- 参考の環境も複数回htmlを取得する
- Seleniumとcurlの両方でhtmlを取得できるようにする

## ToDo
その前出来るか試す
- [x] domの構造をいい感じに比較する
- [x] domを比較するツールを分割する
先にやるもの
- [x] 設定ファイルを読み込んで各種設定を変更できる
  - [x] htmlを取得する方法を選択する設定を読み込む
  - [x] 比較する対象を選択する設置を読み込む
  - [x] 比較する方法を選択する設定を読み込む
  - [x] 比較した差分を保存するデータベースを読み込む
- [x] htmlを取得する
  - [x] Seleniumで対象のURLのhtmlを取得する
  - [x] Requestで対象のURLのhtmlを取得する
- [x] 比較する対象を取り出す
  - [x] ２つのファイルからURLを取り出す
- [x] 対象２つのhtmlを比較する
  - [x] Linuxのdiffツールのような感じに行毎に比較する
  - [x] DomをBeautifulSoupで取り出してDom構造に基づいた差分を比較する

## Usage
### install python3

    brew install python

### exec this cli

    python ./main.py


## Licence

[MIT]

## Author

[Taurin190](https://github.com/Taurin190)
