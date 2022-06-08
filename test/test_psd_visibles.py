
from unittest import TestCase 
from psdtoolkit_util import PSDPath, PSDVisibles, Visibles

class TestPSDVisibles (TestCase):

  def test_psd_visibles (self):
    psdvisibles = PSDVisibles({
      "a": False,
      "a/b": False,
      "a/b/c": False,
    })
    self.assertEqual(psdvisibles["a"], False)
    self.assertEqual(psdvisibles["a/b"], False)
    self.assertEqual(psdvisibles["a/b/c"], False)
    self.assertEqual("a" in psdvisibles, True)
    self.assertEqual("a/b" in psdvisibles, True)
    self.assertEqual("a/b/c" in psdvisibles, True)
    self.assertEqual("a/b/c/d" in psdvisibles, False)

  def test_change_visible (self):
    psdvisibles = PSDVisibles({
      "a": False,
      "a/b": False,
      "a/b/c": False,
    })
    self.assertEqual(psdvisibles["a"], False)
    self.assertEqual(psdvisibles["a/b"], False)
    self.assertEqual(psdvisibles["a/b/c"], False)
    psdvisibles.change_visible("a", True)
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/b"], False)
    self.assertEqual(psdvisibles["a/b/c"], False)

  def test_change_visible2 (self):
    psdvisibles = PSDVisibles({
      "a": False,
      "a/b": False,
      "a/b/c": False,
    })
    self.assertEqual(psdvisibles["a"], False)
    self.assertEqual(psdvisibles["a/b"], False)
    self.assertEqual(psdvisibles["a/b/c"], False)
    psdvisibles.change_visible("a/b", True)
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/b"], True)
    self.assertEqual(psdvisibles["a/b/c"], False)

  def test_change_visible3 (self):
    psdvisibles = PSDVisibles({
      "a": False,
      "a/b": False,
      "a/b/c": False,
    })
    self.assertEqual(psdvisibles["a"], False)
    self.assertEqual(psdvisibles["a/b"], False)
    self.assertEqual(psdvisibles["a/b/c"], False)
    psdvisibles.change_visible("a/b/c", True)
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/b"], True)
    self.assertEqual(psdvisibles["a/b/c"], True)

  def test_change_visible4 (self):
    psdvisibles = PSDVisibles({
      "a": False,
      "a/b": False,
      "a/b/c": False,
    })
    self.assertEqual(psdvisibles["a"], False)
    self.assertEqual(psdvisibles["a/b"], False)
    self.assertEqual(psdvisibles["a/b/c"], False)
    with self.assertRaises(KeyError):
      psdvisibles.change_visible("a/b/c/d", True)

  def test_change_visible_asterisk (self):
    psdvisibles = PSDVisibles({
      "a": True,
      "a/*b1": True,
      "a/*b1/c": True,
      "a/*b2": False,
      "a/*b2/c": False,
      "a/*b3": False,
      "a/*b3/c": False,
    })
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/*b1"], True)
    self.assertEqual(psdvisibles["a/*b1/c"], True)
    self.assertEqual(psdvisibles["a/*b2"], False)
    self.assertEqual(psdvisibles["a/*b2/c"], False)
    self.assertEqual(psdvisibles["a/*b3"], False)
    self.assertEqual(psdvisibles["a/*b3/c"], False)
    psdvisibles.change_visible("a/*b1/c", True)
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/*b1"], True)
    self.assertEqual(psdvisibles["a/*b1/c"], True)
    self.assertEqual(psdvisibles["a/*b2"], False)
    self.assertEqual(psdvisibles["a/*b2/c"], False)
    self.assertEqual(psdvisibles["a/*b3"], False)
    self.assertEqual(psdvisibles["a/*b3/c"], False)

  def test_change_visible_asterisk2 (self):
    psdvisibles = PSDVisibles({
      "a": True,
      "a/*b1": True,
      "a/*b1/c": True,
      "a/*b2": False,
      "a/*b2/c": False,
      "a/*b3": False,
      "a/*b3/c": False,
    })
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/*b1"], True)
    self.assertEqual(psdvisibles["a/*b1/c"], True)
    self.assertEqual(psdvisibles["a/*b2"], False)
    self.assertEqual(psdvisibles["a/*b2/c"], False)
    self.assertEqual(psdvisibles["a/*b3"], False)
    self.assertEqual(psdvisibles["a/*b3/c"], False)
    psdvisibles.change_visible("a/*b2/c", True)
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/*b1"], False)
    self.assertEqual(psdvisibles["a/*b1/c"], True)
    self.assertEqual(psdvisibles["a/*b2"], True)
    self.assertEqual(psdvisibles["a/*b2/c"], True)
    self.assertEqual(psdvisibles["a/*b3"], False)
    self.assertEqual(psdvisibles["a/*b3/c"], False)

  def test_change_visible_asterisk3 (self):
    psdvisibles = PSDVisibles({
      "a": True,
      "a/*b1": True,
      "a/*b1/c": True,
      "a/*b2": False,
      "a/*b2/c": False,
      "a/*b3": False,
      "a/*b3/c": False,
    })
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/*b1"], True)
    self.assertEqual(psdvisibles["a/*b1/c"], True)
    self.assertEqual(psdvisibles["a/*b2"], False)
    self.assertEqual(psdvisibles["a/*b2/c"], False)
    self.assertEqual(psdvisibles["a/*b3"], False)
    self.assertEqual(psdvisibles["a/*b3/c"], False)
    psdvisibles.change_visible("a/*b3/c", True)
    self.assertEqual(psdvisibles["a"], True)
    self.assertEqual(psdvisibles["a/*b1"], False)
    self.assertEqual(psdvisibles["a/*b1/c"], True)
    self.assertEqual(psdvisibles["a/*b2"], False)
    self.assertEqual(psdvisibles["a/*b2/c"], False)
    self.assertEqual(psdvisibles["a/*b3"], True)
    self.assertEqual(psdvisibles["a/*b3/c"], True)

  def test_change_visible_exclamation_mark (self):
    psdvisibles = PSDVisibles({
      "!a1": True, 
      "!a1/b": True, 
      "!a1/b/c": True, 
      "!a2": False, 
      "!a2/b": False, 
      "!a2/b/c": False, 
    })
    self.assertEqual(psdvisibles["!a1"], True)
    self.assertEqual(psdvisibles["!a1/b"], True)
    self.assertEqual(psdvisibles["!a1/b/c"], True)
    self.assertEqual(psdvisibles["!a2"], False)
    self.assertEqual(psdvisibles["!a2/b"], False)
    self.assertEqual(psdvisibles["!a2/b/c"], False)
    psdvisibles.change_visible("!a1/b/c", True)
    psdvisibles.change_visible("!a2/b/c", False)
    self.assertEqual(psdvisibles["!a1"], True)
    self.assertEqual(psdvisibles["!a1/b"], True)
    self.assertEqual(psdvisibles["!a1/b/c"], True)
    self.assertEqual(psdvisibles["!a2"], False)
    self.assertEqual(psdvisibles["!a2/b"], False)
    self.assertEqual(psdvisibles["!a2/b/c"], False)

  def test_change_visible_exclamation_mark2 (self):
    psdvisibles = PSDVisibles({
      "!a1": True, 
      "!a1/b": True, 
      "!a1/b/c": True, 
      "!a2": False, 
      "!a2/b": False, 
      "!a2/b/c": False, 
    })
    self.assertEqual(psdvisibles["!a1"], True)
    self.assertEqual(psdvisibles["!a1/b"], True)
    self.assertEqual(psdvisibles["!a1/b/c"], True)
    self.assertEqual(psdvisibles["!a2"], False)
    self.assertEqual(psdvisibles["!a2/b"], False)
    self.assertEqual(psdvisibles["!a2/b/c"], False)
    with self.assertRaises(ValueError):
      psdvisibles.change_visible("!a1/b/c", False)
    with self.assertRaises(ValueError):
      psdvisibles.change_visible("!a2/b/c", True)

  #https://seiga.nicovideo.jp/seiga/im6232152

  def test_serialize (self):
    psdvisibles = PSDVisibles([('うしろ', False), ('うしろ/ピクミソ', False), ('うしろ/ゴーレム', True), ('ゆかりさん', True), ('ゆかりさん/本体', True), ('ゆかりさん/本体/制服', True), ('ゆかりさん/本体/制服/左手', True), ('ゆかりさん/本体/制服/左手/通常', False), ('ゆかりさん/本体/制服/左手/上向き', True), ('ゆかりさん/本体/制服/左手/下向き', True), ('ゆかりさん/本体/制服/左手/残像', True), ('ゆかりさん/本体/制服/リュック', True), ('ゆかりさん/本体/制服/本体', True), ('ゆかりさん/本体/制服/ リュックパーツ', True), ('ゆかりさん/本体/通常服', False), ('ゆかりさん/顔パーツ', True), ('ゆかりさん/顔パーツ/口', True), ('ゆかりさん/顔パーツ/口/む', False), ('ゆかりさん/顔パーツ/口/あわわ', False), ('ゆかりさん/顔パーツ/口/波線ほほえみ', False), ('ゆかりさん/顔パーツ/口/ほほえみ', False), ('ゆかりさん/顔 パーツ/口/ほほえみ(舌)', False), ('ゆかりさん/顔パーツ/口/笑い', False), ('ゆかりさん/顔パーツ/口/よだれ', False), ('ゆかりさん/顔パーツ/口/ねこ', True), ('ゆかりさん/顔パーツ/口/悔しい', False), ('ゆかりさん/顔パーツ/口/わっ', False), ('ゆかりさん/顔パーツ/口/あ', False), ('ゆかりさん/顔パーツ/口/よだれ', False), ('ゆかりさん/顔パーツ/口/むう', False), ('ゆかりさん/顔パーツ/口/おっ', False), ('ゆかりさん/顔パーツ/口/お', False), ('ゆかりさん/顔パーツ/口/肉', False), ('ゆかりさん/顔パーツ/口/むぐ', False), ('ゆかりさん/顔パーツ/頬紅、汗', True), ('ゆかりさん/顔パーツ/頬紅、汗/頬紅', True), ('ゆかりさん/顔パーツ/頬紅 、汗/頬紅/頬線', True), ('ゆかりさん/顔パーツ/頬紅、汗/頬紅/頬紅', True), ('ゆかりさん/顔パーツ/頬紅、汗/頬紅/頬紅(2)', True), ('ゆかりさん/顔パーツ/頬紅、 汗/頬紅/赤面', False), ('ゆかりさん/顔パーツ/頬紅、汗/頬紅/赤面', False), ('ゆかりさん/顔パーツ/頬紅、汗/汗1', False), ('ゆかりさん/顔パーツ/頬紅、汗/汗2', False), ('ゆかりさん/顔パーツ/目', True), ('ゆかりさん/顔パーツ/目/開き目', True), ('ゆかりさん/顔パーツ/目/開き目/通常', False), ('ゆかりさん/顔パーツ/目/ 開き目/病み', False), ('ゆかりさん/顔パーツ/目/開き目/おどろき', False), ('ゆかりさん/顔パーツ/目/開き目/おどろき２', False), ('ゆかりさん/顔パーツ/目/開き 目/ぐるぐる', False), ('ゆかりさん/顔パーツ/目/開き目/じと', True), ('ゆかりさん/顔パーツ/目/開き目/じと(病み)', False), ('ゆかりさん/顔パーツ/目/開き目/な みだ', False), ('ゆかりさん/顔パーツ/目/開き目/クマ', False), ('ゆかりさん/顔パーツ/目/閉じ目', False), ('ゆかりさん/顔パーツ/目/閉じ目/○○', False), ('ゆ かりさん/顔パーツ/目/閉じ目/なみだ', False), ('ゆかりさん/顔パーツ/目/閉じ目/なみだ', False), ('ゆかりさん/顔パーツ/目/閉じ目/閉じ', False), ('ゆかりさん/顔パーツ/目/閉じ目/ーー', False), ('ゆかりさん/顔パーツ/目/閉じ目/＾＾', True), ('ゆかりさん/顔パーツ/目/閉じ目/特殊', False), ('ゆかりさん/顔パーツ/目/閉じ目/特殊/白目', False), ('ゆかりさん/顔パーツ/目/閉じ目/特殊/三白眼', True), ('ゆかりさん/顔パーツ/目/閉じ目/特殊/なみだ', True), ('ゆかりさん/顔パーツ/目/閉じ目/＞＜', False), ('ゆかりさん/顔パーツ/目/閉じ目/＞＜/なみだ', False), ('ゆかりさん/顔パーツ/目/閉じ目/＞＜/＞＜', True), ('ゆかりさん/顔パーツ/眉', True), ('ゆかりさん/顔パーツ/眉/通常', True), ('ゆかりさん/顔パーツ/眉/おこ', False), ('ゆかりさん/顔パーツ/眉/かなしみ', False), ('ゆかりさん/顔パーツ/眉/むむ', False), ('ゆかりさん/顔パーツ/闇', False), ('ゆかりさん/顔パーツ/闇/闇', True), ('ゆかりさん/顔パーツ/闇/闇(2)', False), ('ゆかりさん/顔パーツ/闇/青ざめ', False), ('影', False), ('アイコン', True), ('アイコン/！', False), ('アイコン/？', False), ('アイコン/！？', False), ('アイコン/＝３', False), ('アイコン/き らん', False), ('アイコン/きらきら', True), ('アイコン/はっ', False), ('アイコン/はっ２', False), ('アイコン/ぞくぞく', False), ('アイコン/ぶるぶる', False), ('アイコン/草', False), ('アイコン/むか', False), ('アイコン/吐息', False), ('アイコン/あせあせ', False), ('アイコン/あせ', False), ('アイコン/おっ', False), ('アイコン/あわ', False), ('あたま', True), ('あたま/弦巻マキ', True), ('あたま/弦巻マキ/制服', True), ('あたま/弦巻マキ/通常服', False), ('あたま/弦巻 マキ/頬紅、汗', True), ('あたま/弦巻マキ/頬紅、汗/頬線', True), ('あたま/弦巻マキ/頬紅、汗/頬紅', True), ('あたま/弦巻マキ/頬紅、汗/赤面', False), ('あたま/弦巻マキ/頬紅、汗/あせ', False), ('あたま/弦巻マキ/口', True), ('あたま/弦巻マキ/口/お', False), ('あたま/弦巻マキ/口/にっこり', False), ('あたま/弦巻マキ/ 口/あ', False), ('あたま/弦巻マキ/口/よだれ', False), ('あたま/弦巻マキ/口/む', False), ('あたま/弦巻マキ/口/む', False), ('あたま/弦巻マキ/口/ω', False), ('あたま/弦巻マキ/口/へへ', False), ('あたま/弦巻マキ/口/笑い', False), ('あたま/弦巻マキ/口/笑い(八重歯)', False), ('あたま/弦巻マキ/口/わ', True), ('あた ま/弦巻マキ/目', True), ('あたま/弦巻マキ/目/通常', True), ('あたま/弦巻マキ/目/じと', False), ('あたま/弦巻マキ/目/縦長', False), ('あたま/弦巻マキ/目/驚き', False), ('あたま/弦巻マキ/目/ーー', False), ('あたま/弦巻マキ/目/＾＾', False), ('あたま/弦巻マキ/目/なみだ', True), ('あたま/弦巻マキ/眉', True), ('あたま/弦巻マキ/眉/通常', True), ('あたま/弦巻マキ/眉/おこ', False), ('あたま/弦巻マキ/眉/八', False), ('あたま/弦巻マキ/闇', True), ('あたま/弦巻マキ/アイコン', True), ('あたま/弦巻マキ/アイコン/！', False), ('あたま/弦巻マキ/アイコン/？', False), ('あたま/弦巻マキ/アイコン/！？', False), ('あたま/弦巻マキ/アイコ ン/はっ', False), ('あたま/弦巻マキ/アイコン/おっ', False), ('あたま/弦巻マキ/アイコン/草', False), ('あたま/弦巻マキ/アイコン/ぶるぶる', True), ('あたま/弦巻マキ/アイコン/ほっ', False), ('あたま/弦巻マキ/アイコン/むか', False), ('あたま/弦巻マキ/アイコン/あせ', False), ('あたま/弦巻マキ/アイコン/もや', False), ('あたま/影', False), ('あたま/小物いろいろ', True), ('あたま/小物いろいろ/ｾﾔﾅｰ', False), ('あたま/小物いろいろ/マイク', False), ('あたま/小物いろいろ/うさ', False), ('あたま/小物いろいろ/ヘルメット', False), ('あたま/小物いろいろ/けが', False), ('あたま/小物いろいろ/ミカン', False), ('あたま/小物いろいろ/ヘアピン', False), ('あたま/小物いろいろ/めがね', False), ('あたま/小物いろいろ/リボン', True), ('あたま/小物いろいろ/花', True), ('あたま/小物いろいろ/生肉', False), ('あたま/小物いろいろ/目玉焼き', False), ('あたま/小物いろいろ/きのこ', False), ('あたま/小物いろいろ/鼻ちょうちん', False), ('あたま/小物いろいろ/提督帽', False), ('あたま/小物いろいろ/ぼうし', False), ('あたま/小物いろいろ/いつもの', False), ('あたま/小物とか2', True), ('あたま/小物とか2/ほか', False), ('あたま/小物とか2/ほか/ぷよ', False), ('あたま/小物とか2/ほか/角', False), ('あたま/小物とか2/ほか/手紙', True), ('あたま/小物とか2/Thaumcraft', False), ('あたま/小物とか2/Thaumcraft/それっぽいマント', False), ('あたま/小物とか2/Thaumcraft/ゴーグル', True), ('あたま/小物とか2/Thaumcraft/ソーモノミコン', True), ('あたま/小物とか2/Thaumcraft/ソーモメーター', False), ('あたま/小物とか2/Thaumcraft/グレートウッドワンド', False), ('あたま/小物とか2/Thaumcraft/きのこ', False), ('あたま/小物とか2/ごちうさ', False), ('あたま/小物とか2/ごちうさ/さくらのヘアピン', False), ('あたま/小物とか2/ごちうさ/ヘアピン', False), ('あた ま/小物とか2/ごちうさ/花', False), ('あたま/小物とか2/ごちうさ/ロップイヤー', False), ('あたま/小物とか2/ごちうさ/コーヒーカップ', True), ('あたま/小物とか2/ごちうさ/ティッピー', False), ('あたま/包丁', True), ('あたま/包丁/包丁', True), ('あたま/包丁/血', True), ('あたま/ずん', True)])
    self.assertEqual(psdvisibles.serialize(), "_LgAPv0CgPY-GCAJnCIIAO5AAg75YEEAwETALw")
  
  #https://seiga.nicovideo.jp/seiga/im5342445

  def test_serialize2 (self):
    psdvisibles = PSDVisibles([('ポーズ', True), ('ポーズ/1', True), ('ポーズ/2', False), ('ポーズ/3', False), ('ポーズ/4', False), ('ポーズ/5', False), ('他', True), ('他/影', False), ('他/照', False), ('口', True), ('口/他', True), ('口/他/べー', False), ('口/他/ぺろ', False), ('口/他/涎', False), ('口/開', True), ('口/開/ニヤ', False), ('口/開/悲', False), ('口/開/歯', False), ('口/開/。', False), ('口/開/○', False), ('口/開/∞', False), ('口/開/大▽', False), ('口/開/▽', False), ('口/開/ポーズ4用', True), ('口/開/ポーズ4用/○', False), ('口/開/ポーズ4用/大▽', False), ('口/閉', True), ('口/閉/膨', False), ('口/閉/ω', False), ('口/閉/く', False), ('口/閉/へ', False), ('口/閉/～', False), ('口/閉/⌒', False), ('口/閉/-', True), ('口/閉/、', False), ('口/閉/∪', False), ('眉', True), ('眉/- -', True), ('眉/^\u3000^', False), ('眉/^\u3000`', False), ('眉/`"´', False), ('眉/` ´', False), ('眉/´"`', False), ('眉/´ `', False), ('目', True), ('目/通常', True), ('目/ウィンク', False), ('目/逸', False), ('目/ジト目', False), ('目/白目', False), ('目/驚', False), ('目/点', False), ('目/涙目', False), ('目/泣2', False), ('目/泣1', False), ('目/閉', True), ('目/閉/＾＾', False), ('目/閉/´`', False), ('目/閉/`´', False), ('目/閉/--', False), ('目/閉/><', False), ('漫符', True), ('漫符/2', True), ('漫符/2/垂線', False), ('漫符/2/怒', False), ('漫符/2/涙', False), ('漫符/2/汗', False), ('漫符/2/絆創膏', False), ('漫符/1', True), ('漫符/1/Σ', False), ('漫符/1/電球', False), ('漫符/1/音符', False), ('漫符/1/キラキラ', False), ('漫符/1/ハート', False), ('漫符/1/焦', False), ('漫符/1/！', False), ('漫符/1/？', False)])
    self.assertEqual(psdvisibles.serialize(), "9E0AwmIBIEwMAQYIAA")
  
  #https://seiga.nicovideo.jp/seiga/im10788496

  def test_serialize3 (self):
    psdvisibles = PSDVisibles([('尻尾的なアレ', True), ('パーカー裏地', False), ('*服装2', False), ('*服装2/*素体', False), ('*服装2/*ぱんつ', False), ('*服装2/*スク水', False), ('*服装2/*バスタオル', True), ('*服装2/!右腕', True), ('*服装2/!右腕/*(非表示)', False), ('*服装2/!右腕/*胸元', False), ('*服装2/!右腕/*マイク', False), ('*服装2/! 右腕/*指差し', False), ('*服装2/!右腕/*口元', False), ('*服装2/!右腕/*手を挙げる', False), ('*服装2/!右腕/*腰', False), ('*服装2/!右腕/*基本', True), ('*服 装2/!左腕', True), ('*服装2/!左腕/*(非表示)', False), ('*服装2/!左腕/*ひそひそ', False), ('*服装2/!左腕/*胸元', False), ('*服装2/!左腕/*考える', False), ('*服装2/!左腕/*口元', False), ('*服装2/!左腕/*手を挙げる', False), ('*服装2/!左腕/*腰', False), ('*服装2/!左腕/*基本', True), ('*服装1', True), ('*服装1/*制服', False), ('*服装1/*いつもの服', True), ('*服装1/!左腕', True), ('*服装1/!左腕/*(非表示)', False), ('*服装1/!左腕/*ひそひそ', False), ('*服装1/!左腕/*考え る', False), ('*服装1/!左腕/*口元', False), ('*服装1/!左腕/*手を挙げる', False), ('*服装1/!左腕/*腰', True), ('*服装1/!左腕/*基本', False), ('*服装1/!右腕', True), ('*服装1/!右腕/*(非表示)', False), ('*服装1/!右腕/*マイク', False), ('*服装1/!右腕/*指差し', False), ('*服装1/!右腕/*口元', False), ('*服装1/!右腕/*手を挙げる', False), ('*服装1/!右腕/*腰', True), ('*服装1/!右腕/*基本', False), ('!口', True), ('!口/*ほあー', True), ('!口/*ほあ', False), ('!口/*ほー', False), ('!口/*むふ', False), ('!口/*△', False), ('!口/*んあー', False), ('!口/*んへー', False), ('!口/*んー', False), ('!口/*お', False), ('!口/*ゆ', False), ('!口/*むー', False), ('!顔色', True), ('!顔色/かげり', False), ('!顔色/*(非表示)', False), ('!顔色/*青ざめ', False), ('!顔色/*ほっぺ赤め', False), ('!顔 色/*ほっぺ2', False), ('!顔色/*ほっぺ', True), ('!目', True), ('!目/*ぐるぐる', False), ('!目/*〇〇', False), ('!目/*><', False), ('!目/*UU', False), ('!目/*にっこり2', False), ('!目/*にっこり', False), ('!目/*なごみ目', False), ('!目/*ジト目', False), ('!目/*細め目', False), ('!目/*上向き2', False), ('!目/*上 向き', False), ('!目/*目セット', True), ('!目/*目セット/*見開き白目', False), ('!目/*目セット/*ジト白目', False), ('!目/*目セット/*普通白目', True), ('!目/*目セット/!黒目', True), ('!目/*目セット/!黒目/*目逸らし2', False), ('!目/*目セット/!黒目/*目逸らし', False), ('!目/*目セット/!黒目/*カメラ目線2', False), ('!目/*目セット/!黒目/*カメラ目線', False), ('!目/*目セット/!黒目/*普通目2', False), ('!目/*目セット/!黒目/*普通目', True), ('!眉', True), ('!眉/*困り眉2', False), ('!眉/*困り眉1', False), ('!眉/*上がり眉', False), ('!眉/*怒り眉', True), ('!眉/*普通眉', False), ('!枝豆', True), ('!枝豆/*枝豆萎え', False), ('!枝豆/*枝豆通常', True), ('!枝豆/*パーカー(裏地とセットで使用)', False), ('記号など', True), ('記号など/汗3', False), ('記号など/汗2', False), ('記号など/汗1', False), ('記号など/涙', False), ('記号など/アヒルちゃん', False)])
    self.assertEqual(psdvisibles.serialize(), "8WYAgwGA2CgsAIMAEwYqIA")
