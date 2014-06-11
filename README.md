vyos-users-jp.github.io-source
==============================

* [www.vyos-users.jp](http://vyos-users.jp/)のソースおよび設定用リポジトリです。
* [Pelican](http://docs.getpelican.com/)を利用しています。
* GitHub Pages リポジトリ [vyos-users-jp / vyos-users-jp.github.io](https://github.com/vyos-users-jp/vyos-users-jp.github.io)

編集方法
--------

* 必要な物
    * Python 2.7.x
    * pip
        * Pelican
        * Markdown
        * Fabric
1. Python 2.7.x と pip をインストール
2. 必要なパッケージをインストール `pip install -r requirements.txt`
3. ソースコードを取得 `git clone --recursive https://github.com/vyos-users-jp/vyos-users-jp.github.io-source.git`
4. テーマを取得 `git clone https://github.com/vyos-users-jp/vyos-users-jp.github.io-theme.git && pelican-themes -i vyos-users-jp.github.io-theme`
5. ディレクトリに移動 `cd vyos-users-jp.github.io-source`
6. ページを修正 `vi content/pages/index.md` (トップページを修正する場合)
7. 公開 `fab deploy`

ライセンス
----------

<p>
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a> Content licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution 4.0 International License</a>, except where indicated otherwise.
</p>
