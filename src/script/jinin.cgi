#!/usr/bin/perl
use Image::Magick;
use Digest::MD5;
use CGI qw(:standard);

my $script="/";

my $seed=Digest::MD5::md5_hex("$ENV{HTTP_USER_AGENT}$ENV{REMOTE_ADDR}$ENV{QUERY_STRING}");
$seed=~s/[abcdef]//g;
$seed=int(substr($seed,0,8));
srand($seed);

$qCGI=new CGI;
&init_form;

if($ENV{REQUEST_URI}=~/wakashin/) {
	$ENV{REDIRECT_STATUS}=500;
	$ENV{REDIRECT_REQUEST_METHOD}="GET";
	$ENV{REDIRECT_URL}="http://wakashin.com/";
	require "error/error.cgi";
	exit;
}

$imagehtml=<<EOM;
Content-type: text/html

<!DOCTYPE html>
<html>
<head>
<!--
　　　　　　　　　　　　 ,,,,,,,,,,,
　　　　　　　　　　　／": : : ::::::＼
　　　　　　　　　 　/-q-,,_: : ::::::＼
　　　　　　　　　　/　　　''-,,: ::::::i
　　　　　　　　　 /、　　　　/: : :::::i
　　　　　　　　　r-、 ,,,,　/: : ::::::i
　　　　　　　　　L_, ,　 、 ＼: :::::::i
　　　　　　　　 /●) (●>　　 |::_=-::/
　　　　　　　　l ｲ　 '-　　　 |:/tbﾉﾉ
　　　　　　　　l ,`-=-'＼　　 `l ι;/
　　　　　　　　ヽﾄｪ-ｪｪ-:）　　 -r'
　　　　　　　　　ヾ＝-'　　　／　/
　　　　　　＿＿＿_ヽ:.　　 ／:::|
　　　　　／:::::::l`qq'''　:::|
-->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>@{[$ENV{HTTP_USER_AGENT}=~/MSIE|Trident/ ? "neet.co.jp" : qq(NAME.jpg(640x480))]}</title><meta name="description" content="ニートによるニートの株式会社" /><meta name="keywords" content="ニート株式会社,NEET株式会社,ニート,NEET,ニート,働かない,ニー株,ニート(株),全員取締役,中小企業共和国,若新雄純" /><link href="/favicon.ico" type="image/x-icon" rel="icon" /><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon" />
<style type="text/css">
body{color:#000;}a:link,a:active,a:visited,a:hover{color:#000;text-decoration:none;cursorpointer;}
</style>
<script type="text/javascript">
var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-46303321-1']);_gaq.push(['_trackPageview']);(function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);})();</script></head><body><a href="index.html"><img src="ENCNAME.JPG"></a><audio autoplay><source src="audio/hotaru.mp3"><source src="audio/hotaru.ogg"></audio></body><!--ｲﾁｵｰｷｮｳﾊ2015ｴｲﾌﾟﾘｰﾙﾌｰﾙﾅﾝﾃﾞｽｶﾞ--></html>
EOM

$html=<<EOM;
Content-type: text/html

<!DOCTYPE html>
<html>
<head>
<!--
　　　　　　　　　　　　 ,,,,,,,,,,,
　　　　　　　　　　　／": : : ::::::＼
　　　　　　　　　 　/-q-,,_: : ::::::＼
　　　　　　　　　　/　　　''-,,: ::::::i
　　　　　　　　　 /、　　　　/: : :::::i
　　　　　　　　　r-、 ,,,,　/: : ::::::i
　　　　　　　　　L_, ,　 、 ＼: :::::::i
　　　　　　　　 /●) (●>　　 |::_=-::/
　　　　　　　　l ｲ　 '-　　　 |:/tbﾉﾉ
　　　　　　　　l ,`-=-'＼　　 `l ι;/
　　　　　　　　ヽﾄｪ-ｪｪ-:）　　 -r'
　　　　　　　　　ヾ＝-'　　　／　/
　　　　　　＿＿＿_ヽ:.　　 ／:::|
　　　　　／:::::::l`qq'''　:::|
-->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>ニート株式会社｜NEET株式会社</title>
<meta name="description" content="ニートによるニートの株式会社" /><meta name="keywords" content="ニート株式会社,NEET株式会社,ニート,NEET,ニート,働かない,ニー株,ニート(株),全員取締役,中小企業共和国,若新雄純" /><link href="/favicon.ico" type="image/x-icon" rel="icon" /><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon" />
<style type="text/css">
body{color:#000;}a:link,a:active,a:visited,a:hover{color:#000;text-decoration:none;cursor：pointer;}
</style>
<script type="text/javascript">
var _gaq = _gaq || [];_gaq.push(['_setAccount', 'UA-46303321-1']);_gaq.push(['_trackPageview']);(function() {var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);})();
</script>
</head>
<body><div align="right"><img src="images/neetkun_.jpeg" /><br />平成２７年４月１日</div><p>各位</p><div align="right">NEET株式会社<br>代表者名 代表取締役社長 <a href="http://wakashin.com/" onclick="location.href='/http://wakashin.com/'; return false;">若新勇純</a></div><p>&nbsp;</p><div align="center"><font size="+1"><strong>当社役員の異動、及び、辞任に関するお知らせ</strong></font></div><p>&nbsp;</p><p>平素は格別のご愛顧を賜り、厚く御礼を申し上げます。</p><p>この度、平成２７年２月１０日に開催されました臨時株主総会の決定におきまして、当社取締役全員が同年４月１日付で辞任することとなりましたことをお知らせ致します。</p><strong>１．当社代表取締役の異動</strong><p>（１）異動の内容</p><table><tr><th>氏名&nbsp;</th><th>新&nbsp;</th><th>旧</th></tr><tr><td><a href="http://wakashin.com/" onclick="location.href='/http://wakashin.com/'; return false;">若新勇純</a>&nbsp;</td><td>代表取締役<u>社長</u>&nbsp;</td><td>代表取締役<u>会長</u></td></tr></table><p>（２）異動の理由</p><p>当社全取締役が辞任するため、社長職が不在となるため</p><p>（３）異動日</p><p>平成２７年４月１日</p><p><strong>２．当社役員の役職辞任</strong>（いずれも平成２７年４月１日付）</p><p>（１）取締役の役職辞任者</p><table><tr><th>氏名&nbsp;</th><th>理由</th></tr>TRIS</table><p>（２）辞任の理由</p><p>当社株主総会上にて、全員が辞任する意向を示し、全株主の承認を得たため</p><p>&nbsp;</p><div align="right">以上</div></body><!--ｲﾁｵｰｷｮｳﾊ2015ｴｲﾌﾟﾘｰﾙﾌｰﾙﾅﾝﾃﾞｽｶﾞ--></html>
EOM

$trihtml=qq(<tr><td><a href="@{[$script]}ENCNAME.jpg">NAME</a></td><td>&nbsp;（NEET株式会社辞任のため）</td></tr>);

$jinin["m"]=<<EOM;
North:10:30:70:辞任届
North:10:180:39:@{[&randword("私","私","私","私","私","私","私","わたし")]}は、このたび一身上の都合により、@{[&randword("貴社","貴社","御社")]}の取締役を
North:10:250:40:辞任いたしたく、お届けいたします。
SouthWest:10:300:42:平成２７年４月１日
SouthEast:10:230:34:ADDRESS2
SouthEast:10:180:34:ADDRESS3
SouthEast:70:100:60:NAME
SouthWest:10:10:50:ＮＥＥＴ株式会社　御中
EOM

$jinin["w"]=<<EOM;
North:10:30:70:辞任届
North:10:180:39:@{[&randword("私","私","私","私","私","私","わたし")]}は、このたび一身上の都合により、@{[&randword("貴社","貴社","御社")]}の取締役を
North:10:250:40:辞任いたしたく、お届けいたします。
SouthWest:10:300:42:平成２７年４月１日
SouthEast:10:230:35:ADDRESS2
SouthEast:10:180:35:ADDRESS3
SouthEast:70:100:60:NAME
SouthWest:10:10:50:ＮＥＥＴ株式会社　御中
EOM

$itext=<<EOM;
SouthEast:10:125:40:INKAN1
SouthEast:10:95:40:INKAN2
EOM

@wfonts=(
	"aquafont.ttf",
	"APJapanesefont.ttf",
	"APJapanesefontT.ttf",
	"MakibaFontB13.ttf",
	"MakibaFontP13.ttf",
	"TAKUMISFONT_L.ttf",
	"TAKUMISFONT_LP.ttf",
	"851tegaki_zatsu.ttf",
	"OhisamaFontB11.ttf",
#	"RiiTN_R.otf",
	"mikachan-p.ttf",
	"mikachan-pb.ttf",
	"mikachan-ps.ttf",
	"mikachan.ttf",
);

@mfonts=(
	"aquafont.ttf",
	"APJapanesefont.ttf",
	"APJapanesefontT.ttf",
	"falconfontb_1.1.ttf",
	"falconfont_1.1.ttf",
	"MakibaFontB13.ttf",
	"MakibaFontP13.ttf",
	"TAKUMISFONT_L.ttf",
	"TAKUMISFONT_LP.ttf",
	"851tegaki_zatsu.ttf",
);

@ifonts=(
	"hkinsoukk.ttf",
	"hktenkk.ttf",
#	"hksoukk.ttf",
#	"hkreikk.ttf",
#	"hkkoinkk.ttf",
);

@jimage=(
	"P3250020.JPG,2",
	"P3260037.JPG,1",
	"P3260083.JPG,0",
	"P3260116.JPG,0",
);

my $tri=0;
@tris=(
"あたらしいせきちや,w,ちせ,やき",
"trlster,m,すと,たれ",
"新しくない中学生,m,生中,印学",
"samno,m,ノさ,印む",
"ゅぃ,w,ノゅ,印ぃ",
"片丘和希,m,おか,かた",
"mewdow,m,どめ,ぅう",
"キツパ,m,パキ,印ツ",
"かつぱちやん,w,ぱか,印つ",
"kyoku,w,曲,印の",
"sayatti,m,っさ,ちや",
"yavatti,m,ちや,印ば",
"トミィ,m,ィト,印ミ",
"ぼち,m,のぼ,印ち",
"髭男爵,m,ノひ,印げ",
"Mayuminmin,w,みま,んゆ",
"Lucy,m,ｃＬ,ｙｕ",
"悟空,m,うご,印く",
"満月,m,ノ満,印月",
"プレイ,m,イプ,印レ",
"オズワンコ。,m,ノオ,印ズ",
"おどるぽんぽこぽん,m,ぽぽ,こん",
"e-zima,m,ノ良,印島",
"まろうど まろい,m,うま,どろ",
"Right45,m,印右,五四",
"予備,m,ノ予,印備",
"あゆみちゃん,w,みあ,印ゆ",
"ちこちこ,m,ちち,ここ",
"優助,m,ノ優,印助",
"さつまいも,m,まさ,印つ",
"黒玉,m,ノ黒,印玉",
"しょうさん,m,ノし,印ょ",
"ピロシ,m,シピ,印ロ",
"ケイ素,m,素ケ,印イ",
"bugiemonn,m,ノぶ,印ぎ",
"あまざけ,m,ざあ,けま",
"海羊,m,ノ海,印羊",
"マミー,w,｜マ,印ミ",
"さやたん,w,たさ,んや",
"SALAD10弱士,m,ノ弱,印士",
"末,m,印末,　の",
"太郎丸,m,丸太,印郎",
"りん,m,ノり,印ん",
"路部ナオ,w,ナ路,オ部",
"賞,m,ノ賞,印",
"類字,m,ノ類,印",
"ちよろい,m,ろち,いよ",
"なかちや,w,ちな,やか",
"土産ノ原エス夫,m,ノ土,原産",
"良山,m,の良,印山",
"なおこ,w,こな,印お",
"大豆もあい,m,最大,相豆",
"†漆白の昇天使ゆぅたん,m,たゆ,んぅ",
"飽きた,m,たあ,印き",
"信希,m,ノ信,印希",
"ヤヒー,m,｜ヤ,印ヒ",
"うぐぐ,m,ぐう,印う",
"ノック,m,クノ,印ッ",
"レオパ,m,パレ,印オ",
"あんぱん,m,ぱあ,んん",
"馬梅,m,ノ馬,印梅",
"グッドモーニング,m,よお,うは",
"育田海希,m,海育,希田",
"富士桜　衣織,w,桜富,印士",
"歯に虎　ニート,w,ト歯,ラに",
"パスへイ,m,へパ,イス",
"俺,m,ノお,印れ",
"てくてく,m,てて,くく",
"小間選３,w,選小,３印",
"都留,w,ノ都,印留",
"すずろ,m,ずす,印ろ",
"生村,m,ノ生,印村",
"球由良,m,良玉,印由",
"意思革,m,革意,印思",
"佐久良優,m,良砂,優久",
"エヌジェー,m,ジエ,ェヌ",
"突発王子,w,ノ王,印子",
"育間,w,ノ育,印間",
"万枝トロ,m,ト万,ロ枝",
"１ｔ,w,ン一,印ト",
"ロート,m,トロ,印｜",
"ヒーロー,m,ロヒ,｜｜",
"ニートさん,m,ＡＮ,ＴＥ",
"ちゃんた,m,んち,たゃ",
"幼一,m,ノ幼,印一",
"まるまる優しい石,m,い優,石し",
"村下,m,ノ村,印下",
"丸,m,印丸,章ノ",
"市場,m,ノ市,印場",
"ふすま,m,まふ,印す",
"司法書士,m,書司,士法",
"正鬼,m,おま,にさ",
"高昭,m,ノ高,印昭",
"原ノ町,m,町原,印ノ",
"紅茶,m,ノ紅,印茶",
"温水,m,ノ温,印水",
"紐様,w,様ひ,印も",
"棒くん,m,ノ棒,印棒",
"野良ねこ,m,ね野,こ良",
"松野,m,ノ松,印野",
"時事通信,m,通時,信事",
"エムケー,m,ケエ,｜ム",
"氷野太郎,m,ノ氷,印野",
"私の開放,m,開私,放の",
"ゆーく,w,くゆ,印｜",
"勝くん,m,ノ勝,印君",
"雨世美花,w,美雨,花世",
"ルンナス,m,ナル,スン",
"山家,m,ノ山,印家",
"qasefujiko,w,子不,印二",
"ぷぅたん,w,たぷ,んぅ",
"束子,w,ノ束,印子",
"遊医,w,ノ遊,印医",
"肉の万代,m,万肉,代の",
"ハチ犬,m,犬ハ,印チ",
"キム三世,m,三キ,世キ",
"なにょこ,m,ょな,こに",
"青希友緒,m,友青,緒希",
"桃色植物,w,植桃,物色",
"ハタオ,w,オハ,印タ",
"レタス,m,スレ,印タ",
"里絵里,w,里里,印絵",
"ジェントルマン,m,ノ神,印士",
"squid-proxy,m,いす,どく",
"カンパ,m,パカ,印ン",
"几帳面な広島,m,きす,りっ",
"一人,w,ノ一,印人",
"暗い人,m,人暗,印い",
"2001年HALの旅,w,九ハ,千ル",
"中洋助,m,助中,印洋",
"今日,w,ノ今,印日",
"無の形式,m,形無,式の",
"時雪,m,ノ時,印雪",
"純水,m,ノ純,印水",
"ほこり,m,りほ,印こ",
"富士,w,ノ富,印士",
"たくさんあってな,m,さた,んく",
"石口純平,m,純石,平口",
"全部,m,ノ全,印部",
"上代,m,ノ上,印代",
"多中,m,ノ多,印中",
"無理無理,m,無無,理理",
"異東,m,ノ異,印東",
"真性ニート,m,ニ真,ト性",
"赤いの,m,ノ赤,印い",
"ポンコツ,m,コポ,ツン",
"引退,m,ノ引,印退",
"LEAVE,m,ノ退,印出",
"野原,m,ノ野,印原",
"丸丸,m,ノ丸,印丸",
"見城,m,ノ見,印城",
"くまもん,m,もく,んま",
"陸作修介,m,ノ陸,印作"
);

@randam_parks=(
"プラザ,",
",ロイヤル",
",パーク",
",ステーション",
"リバーサイド,",
"グリーン,",
",ガーデン",
"シティ,",
",アパート",
",フォレスト",
",ヒル",
"メゾン,",
"ガーデン,",
"コーポ,",
"プレイス,",
"グランド,",
"テラス,",
",ゴールデン",
",荘",
"スィート,",
"プラチナ,",
",シーサイド",
",ランド",
"コーポ",
",テラス",
",庵",
"ヴィレッジ,",
",ヴィレッジ",
"スカイ,",
",ハウス",
"ハイツ,",
",ハイツ",
"ステーション,",
"パレス,",
"ザ　,",
);

$moji=<<EOM;
あ い う え お か き く け こ さ し す せ そ た ち つ て と な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を ん ぁ ぃ ぅ ぇ ぉ ゃ ゅ ょ
が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ
ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ワ ヲ ン ァ ィ ゥ ェ ォ ャ ュ ョ
ガ ギ グ ゲ ゴ ザ ジ ズ ゼ ゾ ダ ヂ ヅ デ ド バ ビ ブ ベ ボ パ ピ プ ペ ポ
１ ２ ３ ４ ５ ６ ７ ８ ９ ０
Ａ Ｂ Ｃ Ｄ Ｅ Ｆ Ｇ Ｈ Ｉ Ｊ Ｋ Ｌ Ｍ Ｎ Ｏ Ｐ Ｑ Ｒ Ｓ Ｔ Ｕ Ｖ Ｗ Ｘ Ｙ Ｚ
ａ ｂ ｃ ｄ ｅ ｆ ｇ ｈ ｉ ｊ ｋ ｌ ｍ ｎ ｏ ｐ ｑ ｒ ｓ ｔ ｕ ｖ ｗ ｘ ｙ ｚ
ー 〒 －
一 右 雨 円 王 音 下 火 花 貝 学 気 九 休 玉 金 空 月 犬 見 五 口 校 左 三 山 子 四 糸 字 耳 七 車 手 十 出 女 小 上 森 人 水 正 生 青 夕 石 赤 千 川 先 早 草 足 村 大 男 竹 中 虫 町 天 田 土 二 日 入 年 白 八 百 文 木 本 名 目 立 力 林 六引 羽 雲 園 遠 何 科 夏 家 歌 画 回 会 海 絵 外 角 楽 活 間 丸 岩 顔 汽 記 帰 弓 牛 魚 京 強 教 近 兄 形 計 元 言 原 戸 古 午 後 語 工 公 広 交 光 考 行 高 黄 合 谷 国 黒 今 才 細 作 算 止 市 矢 姉 思 紙 寺 自 時 室 社 弱 首 秋 週 春 書 少 場 色 食 心 新 親 図 数 西 声 星 晴 切 雪 船 線 前 組 走 多 太 体 台 地 池 知 茶 昼 長 鳥 朝 直 通 弟 店 点 電 刀 冬 当 東 答 頭 同 道 読 内 南 肉 馬 売 買 麦 半 番 父 風 分 聞 米 歩 母 方 北 毎 妹 万 明 鳴 毛 門 夜 野 友 用 曜 来 里 理 話
悪 安 暗 医 委 意 育 員 院 飲 運 泳 駅 央 横 屋 温 化 荷 界 開 階 寒 感 漢 館 岸 起 期 客 究 急 級 宮 球 去 橋 業 曲 局 銀 区 苦 具 君 係 軽 血 決 研 県 庫 湖 向 幸 港 号 根 祭 皿 仕 死 使 始 指 歯 詩 次 事 持 式 実 写 者 主 守 取 酒 受 州 拾 終 習 集 住 重 宿 所 暑 助 昭 消 商 章 勝 乗 植 申 身 神 真 深 進 世 整 昔 全 相 送 想 息 速 族 他 打 対 待 代 第 題 炭 短 談 着 注 柱 丁 帳 調 追 定 庭 笛 鉄 転 都 度 投 豆 島 湯 登 等 動 童 農 波 配 倍 箱 畑 発 反 坂 板 皮 悲 美 鼻 筆 氷 表 秒 病 品 負 部 服 福 物 平 返 勉 放 味 命 面 問 役 薬 由 油 有 遊 予 羊 洋 葉 陽 様 落 流 旅 両 緑 礼 列 練 路 和
愛 案 以 衣 位 囲 胃 印 英 栄 塩 億 加 果 貨 課 芽 改 械 害 街 各 覚 完 官 管 関 観 願 希 季 紀 喜 旗 器 機 議 求 泣 救 給 挙 漁 共 協 鏡 競 極 訓 軍 郡 径 型 景 芸 欠 結 建 健 験 固 功 好 候 航 康 告 差 菜 最 材 昨 札 刷 殺 察 参 産 散 残 士 氏 史 司 試 児 治 辞 失 借 種 周 祝 順 初 松 笑 唱 焼 象 照 賞 臣 信 成 省 清 静 席 積 折 節 説 浅 戦 選 然 争 倉 巣 束 側 続 卒 孫 帯 隊 達 単 置 仲 貯 兆 腸 低 底 停 的 典 伝 徒 努 灯 堂 働 特 得 毒 熱 念 敗 梅 博 飯 飛 費 必 票 標 不 夫 付 府 副 粉 兵 別 辺 変 便 包 法 望 牧 末 満 未 脈 民 無 約 勇 要 養 浴 利 陸 良 料 量 輪 類 令 冷 例 歴 連 老 労 録
圧 移 因 永 営 衛 易 益 液 演 応 往 桜 恩 可 仮 価 河 過 賀 快 解 格 確 額 刊 幹 慣 眼 基 寄 規 技 義 逆 久 旧 居 許 境 均 禁 句 群 経 潔 件 券 険 検 限 現 減 故 個 護 効 厚 耕 鉱 構 興 講 混 査 再 災 妻 採 際 在 財 罪 雑 酸 賛 支 志 枝 師 資 飼 示 似 識 質 舎 謝 授 修 述 術 準 序 招 承 証 条 状 常 情 織 職 制 性 政 勢 精 製 税 責 績 接 設 舌 絶 銭 祖 素 総 造 像 増 則 測 属 率 損 退 貸 態 団 断 築 張 提 程 適 敵 統 銅 導 徳 独 任 燃 能 破 犯 判 版 比 肥 非 備 俵 評 貧 布 婦 富 武 復 複 仏 編 弁 保 墓 報 豊 防 貿 暴 務 夢 迷 綿 輸 余 預 容 略 留 領
異 遺 域 宇 映 延 沿 我 灰 拡 革 閣 割 株 干 巻 看 簡 危 机 揮 貴 疑 吸 供 胸 郷 勤 筋 系 敬 警 劇 激 穴 絹 権 憲 源 厳 己 呼 誤 后 孝 皇 紅 降 鋼 刻 穀 骨 困 砂 座 済 裁 策 冊 蚕 至 私 姿 視 詞 誌 磁 射 捨 尺 若 樹 収 宗 就 衆 従 縦 縮 熟 純 処 署 諸 除 将 傷 障 城 蒸 針 仁 垂 推 寸 盛 聖 誠 宣 専 泉 洗 染 善 奏 窓 創 装 層 操 蔵 臓 存 尊 宅 担 探 誕 段 暖 値 宙 忠 著 庁 頂 潮 賃 痛 展 討 党 糖 届 難 乳 認 納 脳 派 拝 背 肺 俳 班 晩 否 批 秘 腹 奮 並 陛 閉 片 補 暮 宝 訪 亡 忘 棒 枚 幕 密 盟 模 訳 郵 優 幼 欲 翌 乱 卵 覧 裏 律 臨 朗 論
EOM

&main;

sub imagehtml {
	$l=$::form{tri};
	$imagehtml=~s/ENCNAME/@{[&encode($l)]}/g;
	$imagehtml=~s/NAME/$l/g;
	print $imagehtml;
}

sub main {
	if($::form{mode} eq "") {
		&html;
		exit;
	}
	if($::form{mode} eq "html") {
		&imagehtml;
		exit;
	}

	my $env=$::form{tri};
	$env=~s/\.jpg//g;
	my $triname=$env;
	my $tri=0;
	my $tflg=0;
	foreach(@tris) {
		my($l,$r)=split(/,/,$_);
		if($l eq $triname) {
			$tflg=1;
			last;
		}
		$tri++;
	}
	exit if(!$tflg);

	my $canvas = Image::Magick->new;
	$canvas->Set(size=>"1024x768");
	$canvas->ReadImage('xc:white');
	$canvas->Transparent(color=>'White');

	my($addr1,$addr2,$addr3);
	do {
		($addr1,$addr2,$addr3)=split(/\n/,&randamaddress);
	} while(length($addr2) > 84 || length($addr3) > 84);
	my ($name,$sex,$inkan1,$inkan2)=split(/,/,$tris[$tri]);
	my $jinin=$jinin[$sex];
	$jinin=~s/ADDRESS1/$addr1/g;
	$jinin=~s/ADDRESS2/$addr2/g;
	$jinin=~s/ADDRESS3/$addr3/g;
	$jinin=~s/FONT/$font/g;
	$jinin=~s/NAME/$name/g;
	$itext=~s/INKAN1/$inkan1/g;
	$itext=~s/INKAN2/$inkan2/g;
	my $font=$sex eq "m"
		? "./font/" . $mfonts[int(rand(1)*($#mfonts+1))]
		: "./font/" . $wfonts[int(rand(1)*($#wfonts+1))];
	my $ifont="./font/" . $ifonts[int(rand(1)*($#ifonts+1))];

	my $randblack=int(rand(4));
	foreach(split(/\n/,$jinin)) {
		my($gravity, $geo_x, $geo_y, $size, $text)=split(/:/,$_);
		my $ret = $canvas->Annotate(
			font=>$font,
			pointsize=>&rand($size,3),
			fill=>sprintf("#%d%d%d",$randblack,$randblack,$randblack),
			text=>$text,
			gravity => $gravity,
			geometry =>"+@{[&rand($geo_x,2)]}" . "+@{[&rand($geo_y,2)]}",
		);
	}

	my $randred=int(rand(4)+11);
	foreach(split(/\n/,$itext)) {
		my($gravity, $geo_x, $geo_y, $size, $text)=split(/:/,$_);
		my $ret = $canvas->Annotate(
			font=>$ifont,
			pointsize=>&rand($size,2),
			fill=>sprintf("#%x00",$randred),
			text=>$text,
			gravity => $gravity,
			geometry =>"+@{[&rand($geo_x,2)]}" . "+@{[&rand($geo_y,2)]}",
		);
	}
	foreach(
		'925,596 1019,596',
		'925,680 1019,680',
		'925,596 925,680',
		'1019,596 1019,680') {
		$canvas->Draw(
			primitive=>'line',
			points=>$_,
			stroke=>sprintf("#%x00",$randred),
			strokewidth=>2
		);
	}

	$canvas->Resize(
		width  =>480,
		height =>360,
		blur   => 0.8,
	);
	my $back = Image::Magick->new;
	my ($jimage,$rotate)=split(/,/,$jimage[int(rand($#jimage+1))]);
	$back->Read("./jimage/@{[$jimage]}");
#	$back->Resize(
#		width  =>640,
#		height =>480,
#		blur   => 0.8,
#	);
	$back->Rotate(-$rotate);
#	$back->Resize(
#		width  =>1440,
#		height =>1080,
#		blur   => 0.8,
#	);

#	$canvas->Distort(virtual-pixel=>"transparent", distort=>"Perspective", points=>"0,0,511,511 0,90,0,90 90,0,70,25 90,90,90,65");
#	$back->Composite(image=>$canvas,compose=>'Over', x=>(1440-1024)/2, y=>(1080-768)/2);
	$back->Composite(image=>$canvas,compose=>'Over', x=>(640-480)/2, y=>(480-360)/2);

	$back->Rotate($rotate);
	$back->Resize(
		width  =>640,
		height =>480,
		blur   => 0.8,
	);

	$back->Comment( 'copy="NO" kddi_copyright=on (C)2015 NEET co ltd.');
	print "Content-type: image/jpeg\n\n";
	binmode(STDOUT);
	$ret=$back->Write("jpeg:-");
}

sub html{
	my $thtml;
	foreach(@tris) {
		my($l,$r)=split(/,/,$_);
		$l=~s/\t//g;
		my $h=$trihtml;
		$h=~s/ENCNAME/@{[&encode($l)]}/g;
		$h=~s/NAME/$l/g;
		$thtml.=$h;
	}
	$html=~s/TRIS/$thtml/g;;
	print $html;
}

sub decode {
	$s=shift;
	$s =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/chr(hex($1))/eg;
	$s;
}

sub encode {
	my $encoded=shift;
	$encoded=~s/(\W)/'%' . unpack('H2', $1)/eg;
	$encoded;
}

sub rand {
	my($value,$range)=@_;
	if(rand(1) < 0.5) {
		return $value + int(rand($range));
	} else {
		return $value - int(rand($range));
	}
}

sub amain {
	my $testmoji=$moji;
	$testmoji=~s/\n/ /g;

	foreach(@tris) {
		while(1) {
			my ($tri,$inkan)=split(/,/,$_);
			my $test=$inkan;
			print "$test ";
			foreach(split(/ /,$testmoji)) {
				$test=~s/$_//g;
			}
			last if($test eq "");
			print "test $test\n";
		}
	}
	my $addr;
	$addr=&randamaddress;
	print $addr;
}

sub randamaddress {
	open my $fh,"<KEN_ALL.CSV.txt" || die("can't open KEN_ALL.CSV.txt\n");
	foreach(<$fh>) {
		chomp;
		push(@add, $_);
	}
	close($fh);

	my($yubin, $ken, $city, $town);
	my ($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime;
	while(1) {
		($yubin, $ken, $city, $town)=split(/\t/,$add[int(rand($#add))]);
		next if($hour % 2 eq 0 && $ken!~/山口都|岩国県|下関府|長門県/);
		next if($town=~/センター/);
		next if($town=~/タワー/);
		next if($town=~/ビル/);
		next if($town=~/インターシティー/);
		next if($town=~/シティセンター/);
		next if($town=~/モノリス/);
		next if($town=~/オペラシティ/);
		next if($town=~/ＴｈｉｎｋＰａｒｋＴｏｗｅｒ/);
		next if($town=~/ガーデンプレイス/);
		next if($town=~/サンシャイン/);
		next if(length($town)>20);
		last if($town ne "");
	}
	$yubin=sprintf("%07d",$yubin);
	$yubin=substr($yubin, 0, 3) . "－" . substr($yubin, 3, 4);

	my ($aza, $banch);
	if($city=~/郡/) {
		$aza="大字" if(rand(1) < 0.5);
		$banch=&randbanch(9949) . "番地";
	} else {
		$banch=&randbanch(149) . "丁目" . &randbanch(449) . "番地" . &randbanch(449) . "号";
	}
	my ($bill,$billflg);
	if($ken eq "東京都") {
		$billflg=0.8;
	} elsif($ken eq "大阪府") {
		$billflg=0.7;
	} elsif($city=~/区/) {
		$billflg=0.7;
	} elsif($city=~/市/) {
		$billflg=0.6;
	} else {
		$billflg=0.3;
	}
	if($billflg > rand(1)) {
		my($l, $r)=split(/,/,$randam_parks[int(rand($#randam_parks))]);
		$bill="$l$town$r" . &randbanch(9940) . "号室";
	}
	my $address="〒$yubin\n$ken$city$aza$town$banch\n$bill\n";
	$address=~s/0/０/g;
	$address=~s/1/１/g;
	$address=~s/2/２/g;
	$address=~s/3/３/g;
	$address=~s/4/４/g;
	$address=~s/5/５/g;
	$address=~s/6/６/g;
	$address=~s/7/７/g;
	$address=~s/8/８/g;
	$address=~s/9/９/g;
	$address;
}

sub randbanch {
	my($rand)=shift;
	my $banch;

	$banch=int(rand($rand)) + 50;
	$banch;
}

sub randword {
	my @words=@_;
	return $words[int(rand($#words + 1))];
}

sub init_form {
	if ($qCGI->param()) {
		foreach my $var ($qCGI->param()) {
			$::form{$var} = $qCGI->param($var);
		}
	} else {
		$ENV{QUERY_STRING} = $::FrontPage;
	}

	# Thanks Mr.koizumi. v0.1.4							# comment
	my $query = $ENV{QUERY_STRING};
	if ($query =~ /&/) {
		my @querys = split(/&/, $query);
		foreach (@querys) {
			$_ = &decode($_);
			$::form{$1} = $2 if (/([^=]*)=(.*)$/);
		}
	} else {
		$query = &decode($query);
	}
}
