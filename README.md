# PhiDataGet
Get charts information of Phigros from MoegirlWiki

从萌娘百科爬取Phigros谱面信息

使用httpx库

程序会生成两个文件，一个名为 ```html.txt``` 的文件，存储了爬出来的源文件，方便查错。

一个名为 ```ProcessResult.txt``` 的文件，里面的谱面信息按照类似于

	Glaciaxion
	Glaciaxion_Phigros.png
	Chapter Legacy 过去的章节
	140
	SunsetRay
	艾若拉
	1.0(EZ),6.5(HD),12.5(IN)
	Barbarianerman(EZ),Arenn Saki(HD),Barbarianerman vs. NerSAN(IN)
	66(EZ),418(HD),729(IN)

的方式存储

可以用sqlite3存储，不过开发者比较懒，大家可以来pull一波
