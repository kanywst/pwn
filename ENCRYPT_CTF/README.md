# ENCRYPT_CTF_2019

## pwn2
bssに書き込むときに0x100書き込むときと書き込まないときの違い  
あとNX disabledだったからシェルコードを使おうとしたけど、できなかった  

## pwn3
libc databaseからlibcをもってきて、libcのオフセットを求めてsystem関数を使う。  
 “/bin/sh”もlibcにある  
libc database searchの使い方わからん  
lddコマンドで自分の環境で使ってる共有ライブラリを表示する  
libc database searchってなんで必要  
リターンアドレスを_startにするともう1回実行できる  
->なんでmainじゃダメなのか  
_startは.textセクションにある  
e.symbols['puts']: 0x8048340  
e.got['puts']: 0x80497b0  
putでGOTのアドレスにかかれているメモリを出力  
libc.symbols[‘puts’]とのオフセットを求める  
readelf -rで再配置されてる関数はオフセットを求めるのに使える  

## pwn4
pwntoolsのfmtstr_payloadは今後64ビットへの対応や、書き込み対象アドレスにnullバイトが入っている際の対応してない  
 __stack_chk_failってなんだ  
-> スタックオーバフロー検出時に呼ばれる  
-> SSP有効でcanaryが書き換えられたときに呼ばれる  