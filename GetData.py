import httpx
import re
import sqlite3

def Get_Phigros_Data():
	url='https://mzh.moegirl.org.cn/index.php'
	headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
					  "Chrome/89.0.4389.128 Safari/537.36"}
	params={'title':'Phigros/谱面信息','action':'raw'}
	try:
		req=httpx.get(url, headers=headers, params=params, timeout=None)
		s=req.text
		return s
	except Exception as e:
		print(e)
		return None

def Find_Data_Temp(Data):
	Pattern=r'\|\| | \|.*?\n'
	return re.findall(Pattern,Data)

DBPath='C:/Users/Administrator/Desktop/nonebot2-2.0.0rc4/MihoBot/data/PhiData'

def Output_Dif(DifList,NoteList,CharterList,File):
	DifTot=['EZ','HD','IN','AT','SP']
	Len=len(DifList)
	for i in range(Len):
		File.write(DifList[i]+'('+DifTot[i]+')')
		if i==Len-1:
			break
		File.write(',')
	File.write('\n')
	for i in range(Len):
		File.write(CharterList[i]+'('+DifTot[i]+')')
		if i==Len-1:
			break
		File.write(',')
	File.write('\n')
	for i in range(Len):
		File.write(NoteList[i]+'('+DifTot[i]+')')
		if i==Len-1:
			break
		File.write(',')
	File.write('\n')


# 信息处理和输出
def Data_Process(DataList):
	File=open('ProcessResult.txt',mode='w',encoding='utf-8')
	List=[]
	DifList=[]
	NoteList=[]
	CharterList=[]
	Num=0
	for Text in DataList:
		Num+=1
		if (Text[2]!='|')&(Num>11):
			for Str in List:
				File.write(Str)
			Output_Dif(DifList,NoteList,CharterList,File)
			DifList.clear()
			CharterList.clear()
			NoteList.clear()
			Num=1
			List.clear()
		if Num==1:
			List.append(Get_String(Text))
		elif Num==2:
			List.append(Get_String(Text))
		elif Num==3:
			List.append(Get_String(Text))
		elif Num==4:
			List.append(Get_String(Text))
		elif Num==5:
			List.append(Get_String(Text))
		elif Num==7:
			List.append(Get_String(Text))
		elif Num>=9:
			TmpArg=Get_Dif(Text)
			CharterList.append(TmpArg[2].rstrip())
			NoteList.append(TmpArg[1].rstrip())
			DifList.append(TmpArg[0].rstrip())
	File.close()
			
			
def Get_String(Text):
	Text=Text.replace('-{','').replace('}-','')
	Text=Text.replace('<nowiki>','').replace('</nowiki>','')
	Pos=Text.rfind("| ")
	Str=Text[Pos+2:]
	Pos=Str.rfind("[[File:")
	if Pos!=-1:
		return Str[Pos+7:-9]+'\n'
	return Str

def Get_Dif(Text):
	TextArg=Text.split(' || ')
	TextArg.pop(0)
	TextArg.pop(0)
	if TextArg[2].find('ref name')!=-1:
		Start=TextArg[2].find('<ref name="')
		End=TextArg[2].find('" />')
		TextArg[2]=TextArg[2][:Start]+'<aka.'+TextArg[2][(Start+11):End]+'>'
	TextArg[2]=TextArg[2].replace('-{','').replace('}-','')
	if len(TextArg)!=3:
		print(TextArg)
	return TextArg
PhiData=Get_Phigros_Data()

TextArg=Find_Data_Temp(PhiData)

Data_Process(TextArg)