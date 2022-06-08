
# psdtoolkit-util

![](https://img.shields.io/badge/version-0.1.0-gray)
![](https://img.shields.io/badge/python-3.10-blue)
![](https://img.shields.io/github/license/tikubonn/psdtoolkit-util)

PSDToolKitが生成するパラメータ文字列を編集できるライブラリです。
私用で動的にPSDToolKitオブジェクトを作成する必要があったので書きました。
おまけの機能としてPSDファイルから、レイヤー可視情報を生成する機能もあります。
詳細は[Usage](#Usage)の項目をご参照ください。

このライブラリは自分用に書いたものです。
念のために簡単な動作テストを済ませていますが、ちゃんと動作する保証はございません。
迷惑になってしまうかもしれませんので、もし本ライブラリの生成した文字列が、PSDToolKitで動作しなかったとしても、
PSDToolKitの開発者様（oov氏）に問い合わせることのないようお願いいたします。
不具合がございましたら、自力で解決していただくか、再現性のある詳細な情報を私（ちくぼん）に報告してください。

```py
from psdtoolkit_util import Params

params = Params.deserialize("L.0 V.9E0AwmIBIEwMAQYIAA")
params #Params([('L.', Flip(0)), ('V.', Visibles([True, True, False, False, False, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False]))])
params.serialize() #L.0 V.9E0AwmIBIEwMAQYIAA
```

## Support Versions 

* [PSDToolKit 0.1.3](https://github.com/oov/aviutl_psdtoolkit/tree/d71bb83bc96025fa0e0bd43ca525b63a4ded1280) 

## Usage

### パラメータ文字列を読み込む・書き出す

PSDToolKitのパラメーター文字列を読み込むには`Params.deserialize`クラスメソッドを使用します。
逆に`Params`インスタンスをパラメータ文字列に変換するには`Params.serialize`メソッドを使用します。

```py
from psdtoolkit_util import Params

params = Params.deserialize("L.0 V.9E0AwmIBIEwMAQYIAA")
params #Params([('L.', Flip(0)), ('V.', Visibles([True, True, False, False, False, False, True, False, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False]))])
params.serialize() #L.0 V.9E0AwmIBIEwMAQYIAA
```

### レイヤー可視情報を編集する

レイヤー可視情報を編集するには`Visibles`インスタンス使います。
このクラスは組み込みクラスのリストを継承しているので、普通のリストのように使うことができます。
対象のレイヤー表示するならば`True`非表示ならば`False`を設定してください。

```py
from psdtoolkit_util import Params, Visibles

params = Params.deserialize("L.0 V.9E0AwmIBIEwMAQYIAA")
for index, visible in enumerate(params["V."]):
  params["V."][index] = False
params.serialize() #L.0 V._00LAA
```

### 表示を反転させる

表示を反転させるには`Flip`インスタンス使います。
`Flip.flip_x`メソッドを使用することで左右の反転を設定することができます。
`Flip.flip_y`メソッドを使用することで上下の反転を設定することができます。

```py
from psdtoolkit_util import Params, Flip 

params = Params.deserialize("L.0 V.9E0AwmIBIEwMAQYIAA")
params["L."] = params["L."].flip_x(True).flip_y(True) #similar as Flip.X | Flip.y
params.deserialize() #L.3 V.9E0AwmIBIEwMAQYIAA
```

### PSDからレイヤー可視情報を作成する

psdtoolkit-utilはPSDファイルからレイヤーの可視情報を生成する機能が用意されています。
この機能を使うには`PSDVisibles.open`クラスメソッドを使用します。

```py
from psdtoolkit_util import Params, Flip, PSDVisibles

#https://seiga.nicovideo.jp/seiga/im5342445

psdvisibles = PSDVisibles.open("./SDゆかり.psd", encoding="cp932")
psdvisibles #PSDVisibles([('ポーズ', True), ('ポーズ/1', True), ('ポーズ/2', False), ('ポーズ/3', False), ('ポーズ/4', False), ('ポーズ/5', False), ('他', True), ('他/影', False), ('他/照', False), ('口', True), ('口/他', True), ('口/他/べー', False), ('口/他/ぺろ', False), ('口/他/涎', False), ('口/開', True), ('口/開/ニヤ', False), ('口/開/悲', False), ('口/開/歯', False), ('口/開/。', False), ('口/開/○', False), ('口/開/∞', False), ('口/開/大▽', False), ('口/開/▽', False), ('口/開/ポーズ4用', True), ('口/開/ポーズ4用/○', False), ('口/開/ポーズ4用/大▽', False), ('口/閉', True), ('口/閉/膨', False), ('口/閉/ω', False), ('口/閉/く', False), ('口/閉/へ', False), ('口/閉/～', False), ('口/閉/⌒', False), ('口/閉/-', True), ('口/閉/、', False), ('口/閉/∪', False), ('眉', True), ('眉/- -', True), ('眉/^\u3000^', False), ('眉/^\u3000`', False), ('眉/`"´', False), ('眉/` ´', False), ('眉/´"`', False), ('眉/´ `', False), ('目', True), ('目/通常', True), ('目/ウィンク', False), ('目/逸', False), ('目/ジト目', False), ('目/白目', False), ('目/驚', False), ('目/点', False), ('目/涙目', False), ('目/泣2', False), ('目/泣1', False), ('目/閉', True), ('目/閉/＾＾', False), ('目/閉/´`', False), ('目/閉/`´', False), ('目/閉/--', False), ('目/閉/><', False), ('漫符', True), ('漫符/2', True), ('漫符/2/垂線', False), ('漫符/2/怒', False), ('漫符/2/涙', False), ('漫符/2/汗', False), ('漫符/2/絆創膏', False), ('漫符/1', True), ('漫符/1/Σ', False), ('漫符/1/電球', False), ('漫符/1/音符', False), ('漫符/1/キラキラ', False), ('漫符/1/ハート', False), ('漫符/1/焦', False), ('漫符/1/！', False), ('漫符/1/？', False)])
params = Params({
  "L.": Flip.None,
  "V.": psdvisibles, 
})
params.serialize() #L.0 V.9E0AwmIBIEwMAQYIAA
```

レイヤーの可視情報を変更するには`PSDVisibles.change_visible`メソッドを使用します。
変更先レイヤーの指定には`PSDPath`インスタンスを使用します。

このメソッドはPSDToolKitでレイヤーを選択したときと同じ振る舞いをするように書かれています。
例えば、レイヤー名の先頭が`!`ならば変更時にエラーを送出し、レイヤー名の先頭が`*`ならば選択されたレイヤー以外すべての`*`レイヤーを非表示に設定します。

```py
from psdtoolkit_util import Params, Flip, PSDPath, PSDVisibles

#https://seiga.nicovideo.jp/seiga/im5342445

psdvisibles = PSDVisibles.open("./SDゆかり.psd", encoding="cp932")
psdvisibles.change_visible(PSDPath("ポーズ/1"), False)
psdvisibles.change_visible(PSDPath("ポーズ/5"), True)
params = Params({
  "L.": Flip.None,
  "V.": psdvisibles, 
})
params.serialize() #L.0 V.9E0AhmIBIEwMAQYIAA
```

## Install

```txt
python setup.py install
```

```txt
python setup.py test
```

## Require Package

* psd-tools: https://github.com/psd-tools/psd-tools

## License 

[The MIT License](./LICENSE).

* psd-tools: [The MIT License](./LICENSE_PSD_TOOLS).
* PSDToolKit: [The MIT License](./LICENSE_PSDTOOLKIT).
