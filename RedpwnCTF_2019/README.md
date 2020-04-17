# RedpwnCTF_2019

## BabbyPwnB
## HARDMODE
## Rot26
4aバイト一気に書き込めばできるけど１バイトずつ書き換えようとするとできない??

## Bronze Ropchain
→ROPを組み立てる（ROPgadgetじゃダメなんだな）  
→自分で組み立てることができれば最強になる  
→レジスタにpopで0を代入できない❓  
→ROPgadgetでROPをつくって、0aを除く（gets関数で改行として認識されてしまうから）  
→それに代わるgadgetさがすのが難しい  
## Zipline
printfとputsの違い  
直接呼び出そうとしてもa0が含まれてるから改行されて実行できない❓ 
→グローバル変数を書き換える❓❗ 
→gets関数があってBOFがあれば、書き換えられる  
→getsとreadの違い  
