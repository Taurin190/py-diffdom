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
- [] 設定ファイルを読み込んで各種設定を変更できる
  - [] htmlを取得する方法を選択する設定を読み込む
  - [] 比較する対象を選択する設置を読み込む
  - [] 比較する方法を選択する設定を読み込む
  - [] 比較した差分を保存するデータベースを読み込む
- [] データベースの操作をする
  - [] MongoDBの操作をする
    - [] MongoDBにデータを保存する
    - [] MongoDBからデータを取り出す
  - [] MySQLの操作をする
    - [] MySQLにデータを保存する
    - [] MySQLからデータを取り出す
  - [] データをファイルで入出力する
    - [] ファイルに出力する
    - [] ファイルを読み込んで対象のデータを取り出す
- [] htmlを取得する
  - [] Seleniumで対象のURLのhtmlを取得する
  - [] Requestで対象のURLのhtmlを取得する
- [] 比較する対象を取り出す
  - [] ２つのファイルからURLを取り出す
  - [] １つのファイルのURLリストを複数のプロキシで比較する
- [] 対象２つのhtmlを比較する
  - [] Linuxのdiffツールのような感じに行毎に比較する
  - [] DomをBeautifulSoupで取り出してDom構造に基づいた差分を比較する

## Usage
### install python3

    brew install python

### exec this cli

    python ./main.py


## Licence

[MIT]

## Author

[Taurin190](https://github.com/Taurin190)
