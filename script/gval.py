#!/usr/bin/python
# coding: UTF-8
#####################################################
# ::ProjectName : ARK Backup
# ::github      : https://github.com/lucida3rd/ark_backup
# ::Admin       : Lucida（lucida3hai@twitter.com）
# ::TwitterURL  : https://twitter.com/lucida3hai
# ::Class       : グローバル値
# 
# ::Update= 2020/11/5
#####################################################

#####################################################
class gVal() :

#############################
# ※ユーザ自由変更※
	DEF_USERDATA_PATH   = '../ark_backup_data/'				#ユーザデータフォルダ
	DEF_TIMEZONE = 9										# 9=日本時間 最終更新日補正用
	DEF_MOJI_ENCODE = 'utf-8'								#文字エンコード

	DEF_STEAM_PATH   = 'C:/steam/'							#Steamインストールフォルダ
	###  C:\\Program Files\\Steam (x86)\\SteamApps\\Common

#############################
# システム情報
	#データversion(文字)
	DEF_CONFIG_VER = "1"

	STR_SystemInfo = {
		"Client_Name"	: "ARK Backup",
		"ProjectName"	: "",
		"github"		: "",
		"Admin"			: "",
		"TwitterURL"	: "",
		"Update"		: "",
		"Version"		: "",
		
		"PythonVer"		: 0,
		"APIrect"		: ""
	}

#############################
# ユーザ情報
	STR_UserInfo = {
		"UserFolder_path"	: ""	#ユーザフォルダパス
	}

#############################
# Timeline調整数
	DEF_STR_TLNUM = {
		"circleBackupTime"	: 5,						#定期バックアップ時間(分)
		"circleBackupNum"	: 30,						#定期バックアップ数
		"(dummy)"			: ""
	}

#############################
# ファイルパス
#   ファイルは語尾なし、フォルダは_path

	DEF_STR_FILE = {
		"Readme"				: "readme.md",
		
		"ARKsave_path"			: DEF_STEAM_PATH + "SteamApps/Common/ARK/ShooterGame/",
		"ARKcheck_file"			: DEF_STEAM_PATH + "SteamApps/Common/ARK/ShooterGame/Saved/LocalProfiles/PlayerLocalData.arkprofile",
		"ARKsave_folder"		: "Saved/",
		
		"BackupMan_file"		: DEF_USERDATA_PATH + "Saved.zip",
		"BackupMan_befour_file"	: DEF_USERDATA_PATH + "Saved_befour.zip",
		
		"(dummy)"				: 0
	}

	DEF_DISPPATH = "script/disp/"

	DEF_STR_DISPFILE = {
		"MainConsole"			: DEF_DISPPATH + "main_console.disp",
		"SearchConsole"			: DEF_DISPPATH + "search_console.disp",
		"KeyuserConsole"		: DEF_DISPPATH + "keyuser_console.disp",
		
		"(dummy)"				: 0
	}

#############################
# 定数
	DEF_TEST_MODE     = "test"								#テストモード(引数文字)
	DEF_DATA_BOUNDARY = "|,|"



#############################
# 変数
	FLG_Console_Mode = False								#画面出力の有無
	FLG_Test_Mode    = False								#テストモード有無

	CHR_Circle_LastDate = "1901-01-01 00:00:00"				#定期バックアップ 最新日時
	FLG_Circle_Setted   = False								#最新日時 設定済み


#####################################################
# Init
#####################################################
##	def __init__(self):
##		return
##
##

#####################################################
# Delete
#####################################################
##	def __del__(self):
##		return
##
##

