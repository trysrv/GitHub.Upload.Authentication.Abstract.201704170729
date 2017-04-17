# このソフトウェアについて

GitHubアップローダの認証処理を抽象化した。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite](https://www.sqlite.org/) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 課題

HTTPリクエスト抽象化について。

## できたこと

* GitHubAPIの認証用requestsライブラリ引数生成を抽象化した
    * 認証なし, Basic, TwoFactor, OAuth
    * DBからTokenを取得する
    * APIでTokenを生成してDBに登録する
* APIごとに認証方法を使い分ける
    * `RequestParameter.py`
* 認証クラス配列を生成する
    * `AuthenticationsCreator.py`
        * DBとユーザ名から以下の認証クラス配列を生成する
        * OAuth, TwoFactor/Basicの優先順に作成できるものがあれば作る
* HTTPメソッド文字列からリクエストメソッドを識別して実行する

## できないこと

* APIごとに必要なHttpHeadersの`Accept`指定を抽象化する
    * たとえばLicenseAPIはすべて`application/vnd.github.drax-preview+json`が必要である
* GETの引数であるparamsを抽象化する
* POSTの引数であるdataを抽象化する

paramsやdataはAPIごとに異なる。Pythonの名前付き引数にしたい。それをどのように抽象化すればいいのか。
辞書引数`**kwargs`ならできそうだが、名前や初期値を指定して何を渡せばいいかわかるようにしたい。
引数のバリデートが必要だから抽象化は難しいか。

理想はAPIごとのdataやparamsの代入やバリデート処理を一切書かない上、以下のようにAPIを呼び出せること。

* `GitHubUploader.py`
    * `Client(AuthenticationCreator(db, username).Create())`
        * `client.repo.create(name='', desc='', url='', ..., sort='', direct='', per_page=100)`
* `GitHubUserRegister.py`
    * `Client([BasicAuthentication(username, password)])`
        * `client.auth.create(scopes)`
        * `client.sshkeys.create()`
    * `client.SetAuthentications([OAuthAuthentication(token), BasicAuthentication(username, password)])`
        * `client.users.get(username)`
        * `client.repo.gets()`

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)
[furl](https://github.com/gruns/furl)|[Unlicense](http://unlicense.org/)|[gruns/furl](https://github.com/gruns/furl/blob/master/LICENSE.md)
[PyYAML](https://github.com/yaml/pyyaml)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2006 Kirill Simonov](https://github.com/yaml/pyyaml/blob/master/LICENSE)

