#!-- coding:utf-8 --
# github上でのファイル操作を学ぶためのサンプルデータ
# 後ほど消します
# 
import shapefile
import csv
import glob
import os.path
def lp2shp(fd,flg):
    # ファイルリストの作成
    flist = glob.glob(fd + "*.txt")
    # ファイルリスト毎に繰り返し処理
    for i in flist:
        # カンマ区切りテキストファイルの読み込み
        cobj = csv.reader(open(i, "rb"))
        # ESRI shapefile(point)をつくる
        w = shapefile.Writer(shapefile.POINT)
        # 属性フィールド elev(標高値)を float　"F",15桁, 精度5, で作成する
        w.field("elev", "F", 15, 5)
        # 属性フィールド flagを integer "N" 5　桁　で作成する
        w.field("flag", "N", 5)
        # テキストの行毎にポイント作成        
        for j in cobj:
            # 2列目をx座標 3列目をy座標としてポイント作成
            w.point(float(j[1]),float(j[2]))
            # 最初の属性フィールド(elev) に　4列目の情報を入力
            # 2番目の属性フィールド(flag) に 5列目の情報を入力
            w.record(float(j[3]),int(j[4]))
        # テキストファイルのフルパス情報からファイル名のみ抽出
        os.path.basename(i)
        # ESRI Shapefileの保存(テキストファイルのファイル名に"_p"を追加した名称を付与)
        w.save(str(i)[0:-4] + "_p.shp")
    print "finished"
    if flg == 1:
        files = glob.glob(fd + "*.shp")
        w = shapefile.Writer()
        for f in files:
            r = shapefile.Reader(f)
            w._shapes.extend(r.shapes())
            w.records.extend(r.records())
        w.fields = list(r.fields)
        w.save(fd + "mergedall.shp")
        print "All processes has been finished(convert shp & merge)"
    else:
        print "All processes has been finished(convert shp only)"
        
if __name__ == '__main__':
    print "this is code block"
