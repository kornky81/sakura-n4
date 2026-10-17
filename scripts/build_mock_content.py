"""Original Sakura N4 mock content. Reproducible JSON export, no external question import."""
import json
from pathlib import Path
out=[]
def q(id,subject,kind,prompt,options,answer,explanation,**extra):
 out.append(dict(id=id,subject=subject,kind=kind,prompt=prompt,options=options,answer=answer,explanation=explanation,provenance='Sakura N4 original, AI-assisted; internal answer review',reviewStatus='internally-checked',**extra))
# Vocabulary: 7 reading, 5 spelling, 8 context, 4 paraphrase, 4 usage.
for i,(word,sentence,opts,ans,note) in enumerate([
('急行','この急行は、次の駅には止まりません。',['きゅうこう','きゅこう','きょうこう','きゅうごう'],0,'急行 is きゅうこう, an express train. The long vowel is required.'),
('住所','ここに住所を書いてください。',['じゅしょう','じゅしょ','じゅうしょ','じゅうしょう'],2,'住所 = じゅうしょ, address / adresse.'),
('運転','兄は毎日車を運転します。',['うんでん','うんてん','うてん','うんどう'],1,'運転 = うんてん, driving / kjøring; 運動 is a different word.'),
('説明','使い方の説明を聞きます。',['せつめ','せちめい','せつまい','せつめい'],3,'説明 = せつめい, explanation / forklaring.'),
('親切','駅員はとても親切でした。',['しんせつ','おやせつ','しんぜつ','しせつ'],0,'親切 = しんせつ, kind / vennlig.'),
('用意','出かける前に、切符を用意しました。',['よい','ようい','ようじ','ゆうい'],1,'用意 = ようい, preparation / forberedelse; 用事 is an errand.'),
('世界','世界のいろいろな国を旅行したいです。',['せいかい','せか','せっかい','せかい'],3,'世界 = せかい, world / verden.')]):
 q(f'fv{i+1}','Vocabulary','kanji-reading',sentence+'\n「'+word+'」の読み方はどれですか。',opts,ans,note)
for i,(word,sentence,opts,ans,note) in enumerate([
('きょうしつ','このきょうしつは広いです。',['教室','教屋','校室','学室'],0,'教室 means classroom / klasserom.'),
('かぞく','週末はかぞくと過ごします。',['家旅','家族','家庭','家屋'],1,'家族 means family members / familie.'),
('こうじょう','父はこうじょうで働いています。',['工所','公場','工場','工作'],2,'工場 is a factory / fabrikk.'),
('ちゅうい','車にちゅういしてください。',['中意','注目','主意','注意'],3,'注意する means to pay attention / være oppmerksom.'),
('けいかく','夏休みのけいかくを立てました。',['計画','計回','計書','計話'],0,'計画 = plan / plan; 計画を立てる means make a plan.')]):
 q(f'fv{i+8}','Vocabulary','orthography',sentence+'\n「'+word+'」を漢字で書くと、どれですか。',opts,ans,note)
for i,(p,opts,ans,note) in enumerate([
('雨が降りそうなので、（　）を持っていきます。',['財布','傘','地図','手紙'],1,'傘 is an umbrella / paraply, the item needed for rain.'),
('電車の時間まであと二分です。（　）ましょう。',['急ぎ','休み','眠り','遊び'],0,'急ぎましょう means let us hurry / la oss skynde oss.'),
('この問題は難しいので、先生に（　）します。',['運転','出発','質問','散歩'],2,'質問する means ask a question / stille et spørsmål.'),
('部屋が暗いので、電気を（　）ください。',['消して','閉めて','止めて','つけて'],3,'電気をつける means switch on the light / slå på lyset.'),
('すみません。この紙を十枚（　）してください。',['コピー','シャワー','ニュース','エアコン'],0,'コピーする means photocopy / kopiere. The other choices are not copying actions.'),
('熱があって頭が痛いので、今日は会社を（　）。',['着きます','休みます','直します','渡ります'],1,'会社を休む means take a day off work / være borte fra jobb.'),
('この料理は塩が多すぎて、（　）です。',['甘い','軽い','しょっぱい','静か'],2,'しょっぱい means salty / salt. Excess salt is the clue.'),
('友達の誕生日に花を（　）。',['拾いました','落としました','捨てました','贈りました'],3,'贈る means give as a gift / gi i gave; a birthday is the context.')]):q(f'fv{i+13}','Vocabulary','context',p,opts,ans,note)
for i,(p,opts,ans,note) in enumerate([
('このかばんは軽いです。',['重くありません。','大きくありません。','安くありません。','新しくありません。'],0,'軽い = not heavy / lett, ikke tung.'),
('もう一度説明してください。',['もっと速く話してください。','また説明してください。','説明しないでください。','一人で説明してください。'],1,'もう一度 means once more / en gang til.'),
('約束の時間に間に合いました。',['約束を忘れました。','時間が分かりませんでした。','遅れませんでした。','約束を変えました。'],2,'間に合う means be in time / rekke i tide, so the speaker was not late.'),
('この店はいつも込んでいます。',['いつも休みです。','いつも安いです。','いつも静かです。','いつも人が多いです。'],3,'込んでいる means crowded / fullt av folk.')]):q(f'fv{i+21}','Vocabulary','paraphrase','同じ意味に近い文を選んでください。\n'+p,opts,ans,note)
for i,(word,opts,ans,note) in enumerate([
('予約',['旅行の前にホテルを予約しました。','階段を予約して二階へ行きました。','雨を予約したのでぬれました。','この漢字を予約して覚えました。'],0,'予約 means reservation / bestilling. Booking a hotel is conventional usage.'),
('直す',['駅から会社まで直しました。','壊れた時計を直しました。','友達に本を直しました。','毎朝、牛乳を直しました。'],1,'直す means repair/correct / reparere, rette. A broken watch can be repaired.'),
('慣れる',['窓を慣れてください。','切符を三枚慣れました。','新しい仕事に慣れました。','雨が慣れています。'],2,'慣れる takes に for what one becomes accustomed to / venne seg til.'),
('残念',['駅まで残念に歩きます。','この机は残念を食べます。','残念を三つ買いました。','試合に負けて残念でした。'],3,'残念 describes regret/disappointment / skuffelse, appropriate after losing a match.')]):q(f'fv{i+25}','Vocabulary','usage','「'+word+'」の使い方が正しい文はどれですか。',opts,ans,note)
# Grammar: 13 selection.
for i,(p,opts,ans,note) in enumerate([
('日本へ行った（　）があります。',['こと','もの','よう','ため'],0,'た-form + ことがある expresses an experience / tidligere erfaring.'),
('音楽を（　）ながら料理を作ります。',['聞く','聞き','聞いて','聞いた'],1,'ながら follows the ます-stem: 聞きます → 聞き.'),
('明日は試験なので、勉強し（　）なりません。',['なくても','ないで','なければ','なかった'],2,'しなければなりません means must study / må studere.'),
('この本は子供でも（　）ます。',['読む','読んだ','読んで','読め'],3,'The potential form 読めます means can read / kan lese.'),
('出かける前に、窓を閉めて（　）ます。',['おき','いき','あり','み'],0,'ておく describes advance preparation / gjøre på forhånd.'),
('あの空を見てください。雨が（　）そうです。',['降る','降り','降った','降って'],1,'Visual conjecture そう follows the verb stem: 降りそう.'),
('友達が来る（　）、部屋を掃除しました。',['ながら','のに','ので','ても'],2,'ので supplies the reason: because a friend is coming, I cleaned.'),
('ここでは写真を（　）はいけません。',['撮る','撮り','撮った','撮って'],3,'てはいけない expresses prohibition: 撮ってはいけません.'),
('毎朝、野菜を食べる（　）しています。',['ように','ためで','ことが','そうで'],0,'ようにしている describes making a conscious effort / prøve å gjøre regelmessig.'),
('この町に住み（　）から、三年になります。',['始める','始めて','始めたら','始めながら'],1,'始めてから means since beginning. Three years have passed since moving here.'),
('道が分からない（　）、駅員に聞いてください。',['ても','まで','なら','しか'],2,'なら sets up the condition: if you do not know the way, ask station staff.'),
('一人（　）来ました。',['に','を','が','で'],3,'一人で means alone / alene; で marks the manner.'),
('この店は日曜日（　）開いています。',['も','を','へ','が'],0,'も means also/even: this shop is open on Sundays too.')]):q(f'fg{i+1}','Grammar','grammar-selection',p,opts,ans,note)
# Sentence ordering: answer is phrase in starred position, all choices used once.
for i,(p,opts,ans,order,note) in enumerate([
('私は ___ ___ ★ ___ あります。',['ことが','京都へ','行った','一度'],2,['京都へ','一度','行った','ことが'],'私は京都へ一度行ったことがあります。The third phrase is 行った.'),
('この本は ___ ___ ★ ___ 人におすすめです。',['ことが','日本語を','勉強した','ない'],0,['日本語を','勉強した','ことが','ない'],'この本は日本語を勉強したことがない人におすすめです。The fixed experience construction is 勉強したことがない; the third phrase is ことが.'),
('この町は ___ ___ ★ ___ 便利です。',['買い物に','駅が','近い','ので'],3,['駅が','近い','ので','買い物に'],'この町は駅が近いので買い物に便利です。The dependency is 駅が近い → ので → 買い物に便利; the third phrase is ので.'),
('私は ___ ___ ★ ___ 思います。',['なりたい','先生に','将来','と'],0,['将来','先生に','なりたい','と'],'私は将来先生になりたいと思います。Third phrase: なりたい.')]):
 q(f'fg{i+14}','Grammar','sentence-order',p+'\n★に入る言葉を選んでください。',opts,ans,note,orderedSolution=order)
# Text grammar, one coherent original paragraph.
text='先月、この町に引っ越してきました。最初は駅への道も（１）、困りました。でも、隣の人が親切に教えてくれました。今は一人で買い物に行ける（２）なりました。もっと町の人と話したいです。（３）、毎日少しずつ日本語を勉強しています。これからも、毎日勉強する（４）にしました。'
for i,(opts,ans,note) in enumerate([
(['分からなくて','分かるので','分かったら','分かりながら'],0,'分からなくて connects not knowing the way to being troubled. The following でも contrasts this difficulty.'),
(['ために','ように','ことに','そうに'],1,'Potential + ようになる describes acquiring an ability: 買い物に行けるようになった.'),
(['しかし','それでも','そのため','それなのに'],2,'そのため connects wanting to talk more with the purposeful daily study; the other conjunctions imply contrast.'),
(['ため','もの','こと','そう'],2,'Dictionary form + ことにする expresses a decision: decided to study every day.')]):q(f'fg{i+18}','Grammar','text-grammar',f'文章の（{i+1}）に入るものはどれですか。',opts,ans,note,passage=text)
# Reading: three short, two medium (2 q each), two information retrieval.
shorts=[
('鈴木さんへ。今日の会議は三時からの予定でしたが、部長が四時まで戻らないので、四時半からに変わりました。会議室はいつもの二階の部屋です。資料は私が用意しますから、持ってこなくてもいいです。佐藤','会議は何時に始まりますか。',['二時','三時','四時','四時半'],3,'The meeting was changed to 四時半, 4:30. Three was the original time; four is the manager’s return.'),
('私は毎朝、駅まで自転車で行きます。しかし、昨日は雨だったのでバスに乗りました。バスが遅れたため、いつもの電車に乗れませんでした。明日は晴れるそうなので、また自転車で行こうと思います。','昨日、いつもの電車に乗れなかったのはなぜですか。',['自転車が壊れたから','バスが遅れたから','寝坊したから','駅が休みだったから'],1,'The explicit cause is バスが遅れたため: the bus was late / bussen var forsinket.'),
('図書館からのお知らせ。来週の月曜日から水曜日まで、本棚の工事をします。この三日間、本を借りることはできません。返す本は入り口の箱に入れてください。木曜日からはいつもどおり利用できます。','工事中、本を返したい人はどうしますか。',['木曜日まで家に置きます。','二階で係の人に渡します。','入り口の箱に入れます。','本棚に自分で戻します。'],2,'返す本は入り口の箱に入れてください explicitly gives the return procedure.')]
for i,(p,prompt,opts,ans,note) in enumerate(shorts):q(f'fr{i+1}','Reading','short-reading',prompt,opts,ans,note,passage=p)
medium1='大学生の森さんは、去年から駅前のパン屋で働いています。最初は朝早く起きるのが大変で、何度もやめようと思いました。しかし、毎朝来るお客さんが「ここのパンを食べると元気になる」と言ってくれました。その言葉を聞いて、自分の仕事が誰かの役に立っていると分かりました。今では早起きにも慣れました。\n先月、店長に新しいパンのアイデアを聞かれました。森さんは、野菜がたくさん入ったパンを考えました。作るのに時間がかかるので、まだ毎日は売っていません。今は土曜日だけ売って、お客さんの意見を聞いています。森さんは、もっと多くの人に食べてもらいたいと思っています。'
q('fr4','Reading','medium-reading','森さんが仕事を続けようと思ったきっかけは何ですか。',['給料が上がったこと','朝遅く起きられるようになったこと','お客さんの言葉を聞いたこと','大学が休みになったこと'],2,'A customer’s words helped Mori realize the work was useful; this changed the initial desire to quit.',passage=medium1)
q('fr5','Reading','medium-reading','新しいパンについて、正しいものはどれですか。',['毎朝売っています。','今は土曜日だけ売っています。','野菜が入っていません。','作る時間が短いです。'],1,'今は土曜日だけ売って states Saturday-only sales; preparation takes time and the bread contains vegetables.',passage=medium1)
medium2='山田さんは、友達と日帰りの旅行を計画しています。二人とも山が好きなので、初めは山へ行くつもりでした。しかし、週末は雨が降るという天気予報を聞きました。山道は雨の日には危ないので、今度は海の近くの博物館へ行くことにしました。\n博物館は駅から歩いて二十分です。駅前からバスも出ていますが、一時間に一本しかありません。二人は九時に駅に着く予定です。九時五分のバスに乗れれば、九時十五分に着きます。乗れなかった場合は、次のバスを待たずに歩くことにしました。博物館の中には食堂がないので、駅でお弁当を買ってから行きます。'
q('fr6','Reading','medium-reading','山へ行く計画を変えたのはなぜですか。',['山が好きではないから','電車が動かないから','博物館が無料だから','雨の日の山道は危ないから'],3,'The weather forecast predicts rain and the text explicitly says wet mountain paths are dangerous.',passage=medium2)
info='市民センター・料理教室\nＡ：和食入門　火曜日１０時〜１２時　１回１５００円\nＢ：パン作り　土曜日１４時〜１６時　１回２０００円\nＣ：簡単な夕食　水曜日１８時〜２０時　１回１２００円\n対象：１８歳以上。材料費は料金に含まれます。\n申し込み：参加日の三日前までに電話してください。\n持ち物：エプロン、筆記用具。'
q('fr8','Reading','information-retrieval','平日は十七時まで働いています。平日の夜に参加できる教室はどれですか。',['Ａだけ','Ｂだけ','Ｃだけ','ＡとＢ'],2,'Only C meets on a weekday evening, Wednesday 18:00–20:00. B is Saturday afternoon.',passage=info)
q('fr9','Reading','information-retrieval','この料理教室について、正しいものはどれですか。',['材料費を別に払います。','参加する日に申し込みます。','何も持っていかなくていいです。','参加日の三日前までに電話で申し込みます。'],3,'The notice requires telephone registration by three days before attendance. Materials are included; an apron and writing tools are needed.',passage=info)
Path('src/mock-written.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Written questions:',len(out))
