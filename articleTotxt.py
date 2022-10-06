import os                   # 匯入 os 套件
import util6 as m     # 匯入自訂模組

sep = os.sep        # 作業系統的路徑分隔符號
root = os.getcwd()  # 取得當前路徑
root = root + sep + 'new2016zh'     # 問答資料最外層的資料夾 (webtext2019zh)

txtFile = open( 'w2vTrainData(new).txt', # 要寫入的txt檔案
                'w', encoding='utf-8')   

for fname in os.listdir(root):  # 迭代所有檔案名稱
    filePath = root + sep + fname   # 組成完整的檔案路徑
    with open(filePath, 'r',encoding='utf-8') as jsonFile:  # 開啟 json 檔    
        m.preprocessing(jsonFile, txtFile, 'content')   # 資料預處理
txtFile.close()     # 關閉檔案
