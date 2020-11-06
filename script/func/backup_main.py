#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::ProjectName : ARK Backup
# ::github      : https://github.com/lucida3rd/ark_backup
# ::Admin       : Lucida（lucida3hai@twitter.com）
# ::TwitterURL  : https://twitter.com/lucida3hai
# ::Class       : バックアップ
# 
# ::Update= 2020/11/5
#####################################################
# Private Function:
#   (none)
#
# Instance Function:
#   __init__(self):
#   Init(self):
#   GetCope(self):
#   GetNewFollower(self):
#   Run(self):
#   ViewFavo(self):
#   RunFavo(self):
#   ViewFollower(self):
#
# Class Function(static):
#   (none)
#
#####################################################

from osif import CLS_OSIF
from filectrl import CLS_File
from gval import gVal
#####################################################
class CLS_BackupMain():
#####################################################

###	CHR_ARK_LastDate = "1901-01-01 00:00:00"		#ARK側 更新日時

	ARR_CircleFileList = {}							#定期バックアップファイル一覧
###	CHR_Circle_LastDate = "1901-01-01 00:00:00"		#定期バックアップ 最新日時
	CHR_Circle_LastFile = ""						#定期バックアップ 最新ファイル名



#####################################################
# Init
#####################################################
	def __init__(self):
###		self.OBJ_BackupMan = CLS_BackupMan( parentObj=self )
		return



#####################################################
# 初期化
#####################################################
	def Init(self):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_BackupMain"
		wRes['Func']  = "Init"
		
		#############################
		# ARK最終更新日 取得
###		if self.GetARKdate()!=True :
###			wRes['Reason'] = "GetARKdate is failed"
###			return wRes
		self.GetARKdate()
		
		#############################
		# 手動バックアップ 最終更新日 取得
		self.UpdateManualDate()
		
		self.ARR_CircleFileList = {}
		#############################
		# バックアップ一覧の作成
		wList = CLS_File.sFs( gVal.DEF_USERDATA_PATH )
		for wFile in wList :
			if wFile=="Saved.zip" or wFile=="Saved_befour.zip" :
				###手動バックアップは除く
				continue
			
			wDate = CLS_File.sGetTimedate( gVal.DEF_USERDATA_PATH + wFile )
			if wDate=="" :
				continue
			
			wCell = {}
			wCell.update({ "File" : wFile })
			wCell.update({ "Date" : wDate })
			self.ARR_CircleFileList.update({ wFile : wCell })
			
			###最新更新日の更新
			self.UpdateCircleDate( wFile, wDate )




		
		#############################
		# 完了
		wRes['Result'] = True
		return wRes



#####################################################
# ARK最終更新日 取得
#####################################################
	def GetARKdate(self):
		wDate = CLS_File.sGetTimedate( gVal.DEF_STR_FILE['ARKcheck_file'] )
		if wDate=="" :
			gVal.FLG_ARK_Setted = False
			return False
		
###		self.CHR_ARK_LastDate = wDate
		gVal.CHR_ARK_LastDate = wDate
		gVal.FLG_ARK_Setted = True
		return True



#####################################################
# 手動バックアップ 最新日時更新
#####################################################
	def UpdateManualDate(self):
		wDate = CLS_File.sGetTimedate( gVal.DEF_STR_FILE['BackupMan_file'] )
		if wDate=="" :
			gVal.FLG_Manual_Setted = False
			return False
		
		gVal.CHR_Manual_LastDate = wDate
		gVal.FLG_Manual_Setted = True
		return True



#####################################################
# 定期バックアップ 最新日時更新
#####################################################
	def UpdateCircleDate( self, inFile, inDate ):
		if gVal.CHR_Circle_LastDate < inDate :
			gVal.CHR_Circle_LastDate = inDate
			self.CHR_Circle_LastFile = inFile
			gVal.FLG_Circle_Setted   = True
		return



#####################################################
# 手動バックアップ
#####################################################
	def ManualBackup(self):
		#############################
		# 応答形式の取得
		#   "Result" : False, "Class" : None, "Func" : None, "Reason" : None, "Responce" : None
		wRes = CLS_OSIF.sGet_Resp()
		wRes['Class'] = "CLS_BackupMan"
		wRes['Func']  = "ManualBackup"
		
		#############################
		# ARKのローカルプロファイルの存在チェック
		if CLS_File.sExist( gVal.DEF_STR_FILE['ARKcheck_file'] )!=True :
			## ファイルがない
			wRes['Reason'] = "ARKのローカルプロファイルが確認できません: path=" + gVal.DEF_STR_FILE['ARKcheck_file']
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# ユーザフォルダの存在チェック
		if CLS_File.sExist( gVal.DEF_USERDATA_PATH )!=True :
			## フォルダがない
			wRes['Reason'] = "フォルダがありません: path=" + gVal.DEF_USERDATA_PATH
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# 画面クリア(=通常モード時)
		if gVal.FLG_Test_Mode==False :
			CLS_OSIF.sDispClr()
		
		#############################
		# ヘッダ表示
		wStr = "--------------------" + '\n'
		wStr = wStr + " 手動バックアップ" + '\n'
		wStr = wStr + "--------------------" + '\n'
		wStr = wStr + '\n'
		wStr = wStr + "手動バックアップを開始します......" + '\n'
		CLS_OSIF.sPrn( wStr )
		
		#############################
		# 処理開始
		wStr = "バックアップファイル退避中......" + '\n'
		CLS_OSIF.sPrn( wStr )
		
		#############################
		# 前回バックアップしていればファイルを退避する
		wFLG_Escape = False
		if CLS_File.sExist( gVal.DEF_STR_FILE['BackupMan_file'] )==True :
			wFLG_Escape = True
			## 退避コピー
			if CLS_File.sCopy( gVal.DEF_STR_FILE['BackupMan_file'], gVal.DEF_STR_FILE['BackupMan_befour_file'] )!=True :
				## 失敗
				wRes['Reason'] = "ファイルの退避コピーに失敗しました: path=" + gVal.DEF_STR_FILE['BackupMan_file']
				CLS_OSIF.sErr( wRes )
				return wRes
			
			## 前回バックアップ削除
			if CLS_File.sRemove( gVal.DEF_STR_FILE['BackupMan_file'] )!=True :
				## 失敗
				wRes['Reason'] = "前回バックアップの削除に失敗しました: path=" + gVal.DEF_STR_FILE['BackupMan_file']
				CLS_OSIF.sErr( wRes )
				return wRes
		
		#############################
		# アーカイブリストの取得
		wStr = "アーカイブ中......" + '\n'
		CLS_OSIF.sPrn( wStr )
		
		#############################
		# 作業フォルダ変更
		wSrcCurr = CLS_File.sGetCurrentPath()
		wArcPath = wSrcCurr + "/" + gVal.DEF_STR_FILE['BackupMan_file']
		CLS_File.sChgFolder( gVal.DEF_STR_FILE['ARKsave_path'] )
		
		#############################
		# アーカイブリストの作成
		wArcList = self.__get_ArcList()
		if len(wArcList)==0 :
			## 失敗
			wRes['Reason'] = "アーカイブリストの取得 list=0"
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# バックアップ(savedアーカイブ)
		if CLS_File.sFolderArcive( wArcPath, wArcList )!=True :
			## 失敗
			wRes['Reason'] = "アーカイブに失敗しました: path=" + gVal.DEF_STR_FILE['ARKsave_path'] + "/" + gVal.DEF_STR_FILE['ARKsave_folder']
			CLS_OSIF.sErr( wRes )
			return wRes
		
		#############################
		# フォルダを戻す
		CLS_File.sChgFolder( wSrcCurr )
		
		#############################
		# 退避ファイルの削除
		if wFLG_Escape==True :
			if CLS_File.sRemove( gVal.DEF_STR_FILE['BackupMan_befour_file'] )!=True :
				## 失敗
				wRes['Reason'] = "退避ファイルの削除に失敗しました: path=" + gVal.DEF_STR_FILE['BackupMan_befour_file']
				CLS_OSIF.sErr( wRes )
				return wRes
		
		#############################
		# ARK最終更新日 取得
		# 手動バックアップ 最終更新日 取得
		self.GetARKdate()
		self.UpdateManualDate()
		
		#############################
		# 完了
		wStr = "バックアップが完了しました。"
		CLS_OSIF.sPrn( wStr )
		
		wRes['Result'] = True
		return wRes



#####################################################
# アーカイブリスト作成
#####################################################
	def __get_ArcList(self):
		wArcList = []
		
		### Saved以下のリスト
		wCurrList = CLS_File.sLs( gVal.DEF_STR_FILE['ARKsave_folder'] )
		if len(wCurrList)==0 :
			## 失敗
			return wArcList
		
		for wCurrFolder in wCurrList :
			### Config以下
			if wCurrFolder=="Config" :
				wCurrPath = gVal.DEF_STR_FILE['ARKsave_folder'] + wCurrFolder
				wArcList.append( wCurrPath )
				
				### サブフォルダ
				wSubList = CLS_File.sLs( gVal.DEF_STR_FILE['ARKsave_folder'] + wCurrFolder )
				for wFile in wSubList :
					wSubPath = gVal.DEF_STR_FILE['ARKsave_folder'] + wCurrFolder + "/" + wFile
					wArcList.append( wSubPath )
					
					### フォルダ内のファイル
					wInFiles = CLS_File.sFs( wSubPath + "/" )
					for wFile in wInFiles :
						wFilePath = wSubPath + "/" + wFile
						wArcList.append( wFilePath )
			
			### それ以外
			else:
				### フォルダ
				wCurrPath = gVal.DEF_STR_FILE['ARKsave_folder'] + wCurrFolder
				wArcList.append( wCurrPath )
				
				### フォルダ内のファイル
				wInFiles = CLS_File.sFs( wCurrPath + "/" )
				for wFile in wInFiles :
					wFilePath = wCurrPath + "/" + wFile
					wArcList.append( wFilePath )
		
		return wArcList



