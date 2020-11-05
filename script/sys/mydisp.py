#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::ProjectName : ARK Backup
# ::github      : https://github.com/lucida3rd/ark_backup
# ::Admin       : Lucida（lucida3hai@twitter.com）
# ::TwitterURL  : https://twitter.com/lucida3hai
# ::Class       : ディスプレイ表示
# 
# ::Update= 2020/11/5
#####################################################
# Private Function:
#   __write( self, inLogFile, inDate, inMsg ):
#
# Instance Function:
#   __init__( self, inPath ):
#   Log( cls, inLevel, inMsg, inView=False ):
#
# Class Function(static):
#   (none)
#
#####################################################

from osif import CLS_OSIF
from filectrl import CLS_File
from gval import gVal
#####################################################
class CLS_MyDisp():
#####################################################

#####################################################
# インプリメント処理
#####################################################
	@classmethod
	def sDispInp( cls, inDisp, inLine, inIndex ):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_MyDisp"
		wRes['Func']  = "sDispInp"
		
		###メイン画面
		if inDisp=="MainConsole" :
			cls.__dispInp_Main( inLine, wRes )
		
		return wRes

	#####################################################
	# メイン画面
	@classmethod
	def __dispInp_Main( cls, inLine, outRes ):
		pRes = outRes
		#############################
		# インプリメント処理
		
		###インプリ：ユーザアカウント
		if "[@CIRCLE-BACKUP-LAST@]"==inLine :
			if gVal.FLG_Circle_Setted==True :
				wSet = str(gVal.CHR_Circle_LastDate)
			else :
				wSet = "(未バックアップ)"
			
			pRes['Responce'] = "                        最終更新日 : " + wSet
		
		###インプリ：ユーザアカウント
		elif "[@CIRCLE-BACKUP-TIME@]"==inLine :
			pRes['Responce'] = "                        周期間隔   : " + str(gVal.DEF_STR_TLNUM['circleBackupTime']) + "(分)"
		
		#############################
		# 正常
		pRes['Result'] = True
		return




#####################################################
# ディスプレイファイル 読み込み→画面表示
#####################################################
	@classmethod
	def sViewDisp( cls, inDisp, inIndex=-1 ):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_MyDisp"
		wRes['Func']  = "sViewDisp"
		
		#############################
		# ディスプレイファイルの確認
		wKeylist = gVal.DEF_STR_DISPFILE.keys()
		if inDisp not in wKeylist :
			###キーがない(指定ミス)
			wRes['Reason'] = "Display key is not found: inDisp= " + inDisp
			return wRes
		
		if CLS_File.sExist( gVal.DEF_STR_DISPFILE[inDisp] )!=True :
			###ファイルがない...(消した？)
			wRes['Reason'] = "Displayファイルがない: file=" + gVal.DEF_STR_DISPFILE[inDisp]
			return wRes
		
		#############################
		# ディスプレイファイルの読み込み
		wDispFile = []
		if CLS_File.sReadFile( gVal.DEF_STR_DISPFILE[inDisp], outLine=wDispFile, inStrip=False )!=True :
			wRes['Reason'] = "Displayファイルがない(sReadFile): file=" + gVal.DEF_STR_DISPFILE[inDisp]
			return wRes
		
		if len(wDispFile)<=1 :
			wRes['Reason'] = "Displayファイルが空: file=" + gVal.DEF_STR_DISPFILE[inDisp]
			return wRes
		
		#############################
		# 画面クリア(=通常モード時)
		if gVal.FLG_Test_Mode==False :
			CLS_OSIF.sDispClr()
		
		#############################
		# 画面に表示する
		for wLine in wDispFile :
			###コメントはスキップ
			if wLine.find("#")==0 :
				continue
			
			###インプリメント
			wResInp = cls.sDispInp( inDisp, wLine, inIndex )
			if wResInp['Result']!=True :
				wRes['Reason'] = "sDispInp is failed: reasin=" + wResInp['Reason']
				return wRes
			if wResInp['Responce']!=None :
				###インプリメントされていれば差し替える
				wLine = wResInp['Responce']
			
			#############################
			# print表示
			CLS_OSIF.sPrn( wLine )
		
		#############################
		# 正常処理
		wRes['Result'] = True
		return wRes



