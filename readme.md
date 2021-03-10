# ARK バックアップ　～取扱説明書 兼 設計仕様書～
::ProjectName= ARK Backup (main)
::github= https://github.com/lucida3rd/ark_backup
::Admin= Lucida（lucida3hai@twitter.com）
::TwitterURL= https://twitter.com/lucida3hai

::Update= 2021/3/10
::Version= 1.2.0.0


<a id="iSystemSummary"></a>
## システム概要
Windows環境化でARK:Survival Evolvedのローカルプレイにおけるセーブ領域のバックアップをおこないます。
なおPythonで動作します。インストール方法はこのreadmeに記載しています。
　　[ARK:Survival Evolved(steam)](https://store.steampowered.com/app/346110/ARK_Survival_Evolved/)

実験してないので確証ないですが、Pythonで動作するのでPythonがインストールされているサーバでも動作する可能性はあります。




<a id="iRet"></a>
## 目次
* [システム概要](#iSystemSummary)
* [前提](#iPremise)
* [デフォルトエンコードの確認](#iDefEncode)
* [セットアップ手順](#iSetup)
* [アップデート手順](#iUpdate)
* [起動方法](#iStart)
* [運用方法](#iHowtoUnyo)
* [免責事項](#iDisclaimer)
* [謝辞](#iAcknowledgment)




<a id="iPremise"></a>
## 前提
* python3（v3.8.5で確認）
* Windows 10
* githubアカウント
* デフォルトエンコード：utf-8




<a id="iDefEncode"></a>
## デフォルトエンコードの確認　★初回のみ
本ソフトはデフォルトエンコード**utf-8**で動作することを前提に設計してます。
utf-8以外のエンコードでは誤動作を起こす場合があります。
pythonのデフォルトエンコードを確認したり、utf-8に設定する方法を示します。

```
# python
>>> import sys
>>> sys.getdefaultencoding()
'utf-8'
  utf-8が表示されればOKです。

>> exit
  ここでCtrl+Z を入力してリターンで終了します。
```

もしutf-8でなければWindowsの環境変数に PYTHONUTF8=1 を追加します。
「スタート」→「システムの詳細設定 で検索」→「詳細設定」→「環境変数」
ここに **変数名=PYTHONUTF8、変数値=1** を追加する。
設定したら上記エンコードの確認を再実行して確認しましょう。




<a id="iSetup"></a>
## セットアップ手順

1.pythonと必要なライブラリをインストールします。

インストーラを以下から取得します。基本的に * web-based installer を使います。
入手したインストーラで好きな場所にセットアップします。
  [python HP](https://www.python.org/)

Add Python x.x to Path はチェックしたほうがいいです。
その他はデフォルトか、環境にあわせてオプションを選択しましょう。
インストールが終わったらテストしてみます。

```
# python -V
Python 3.8.5
  ※Windowsの場合、python3ではなく、pythonらしいです

# pip3 list
～以下省略～
```

2.botソースの管理アプリとしてWindows版のgithubデスクトップを使います。

2-1.githubデスクトップをインストールします。
　　[githubデスクトップ](https://desktop.github.com)

2-2.githubの自分のアカウントに本家リポジトリをFork（コピー）する。
　　[Lucibotリポジトリ](https://github.com/lucida3rd/ark_backup)
  の右上あたりの[Fork]ボタンを押してください。
  すると、自分のアカウントに[自垢名 / lucibot_win]というリポジトリができます。

2-3.githubデスクトップで1項でForkしたリポジトリから自PCにクローンをダウンロードします。
  githubデスクトップのCurrent repository→Add→Cloneを選択します。
  任意のフォルダを選択してCloneを押してください。

2-4.自分のブランチを作ります。
  githubデスクトップのCurrent branch→New branchで任意の名前を入力します。




<a id="iUpdate"></a>
## アップデート手順
当方リポジトリのmasterから最新版をpullする方法です。  

1.githubデスクトップを起動します。

2.自分のark_backupリポジトリを選択し、Current branchをクリックします。

3.New branchをクリックし、バックアップ用のブランチを作成します。
  名前はわかりやすいように。

4.ブランチを[main]に切り替えます。

5.[Fetch Origin]をクリックします。

6.[Puch]をクリックします。

ここまでで、自分のリポジトリの[main]と、自PCのソースに最新が反映されてます。

もし不具合があったら...？
3項で保存したブランチに切り替えると、自PC側にアップデート前のソースが戻ってきます。
以後、アップデートがあったら[main]に切り替えて[Fetch]すれば、修正後のソースが反映されます。




<a id="iStart"></a>
## 起動方法
まずSteamクライアントのインストールフォルダを確認してください。
デフォルトだと以下のフォルダにインストールされてるはずです。
  C:/Program Files/Steam (x86)/

もし違っていたら、script/gval.pyの22行目を書き換えてください。


DOSのコマンドラインにて以下を入力します。

```
# cd [Lucibotのインストールフォルダ]
# python run.py
```

起動すると、コンソール画面が起動します。



<a id="iFunction"></a>
## 使い方
各機能を以下に説明します。
コマンドを実行するには、画面のプロンプトに指定のコマンドを入力します。
コマンドは全て\マークの後、半角英字を入力します。


<a id="iFunc_GetInfo"></a>
#### 手動バックアップ【 \mb 】
コマンド実行のタイミングでsavedフォルダをバックアップします。


<a id="iFunc_GetInfo"></a>
#### 定期バックアップ【 \cb 】
一定時間ごとにsavedフォルダをチェックし、データに更新があればバックアップします。
バックアップは、ARK側からコンソールコマンド SaveWorld を実施するか、ARKが定期セーブをおこなったタイミングでおこなわれます。
バックアップアーカイブは世代ごとに管理され、一定回数分は保持されます。




<a id="iDisclaimer"></a>
## 免責事項
* アーカイブなどに含まれるファイル類は消したりしないでください。誤動作の原因となります。
* 当ソースの改造、改造物の配布は自由にやってください。その際の著作権は放棄しません。
* 未改造物の再配布は禁止とします。
* 当ソースを使用したことによる不具合、損害について当方は責任を持ちません。全て自己責任でお願いします。
* 当ソースの仕様、不具合についての質問は受け付けません。自己解析、自己対応でお願いします。
* 使用の許諾、謝辞については不要です。
* その他、ご意見、ご要望については、Twitterに記載してある"マシュマロ"までお送りください。
* このアプリを使用してARKのセーブデータが破壊されても当方に責任はありません。自己責任でご使用ください。




<a id="iReference"></a>
## 参考記事　※敬称略
* [Windows 上の Python で UTF-8 をデフォルトにする（methane）](https://qiita.com/methane/items/9a19ddf615089b071e71)



