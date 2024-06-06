import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import os

def exec_process():
    # フォルダの中のpng画像ファイルパスリストを取得
    # 画像ファイルがあるフォルダ名は"Z_7000um"の形式でその画像を取得したときのZ座標を示す
    # Z_7000um, Z_0umのようにZ座標ごとに分かれたフォルダの中の画像ファイルパスのリストを取得し"ファイルパス"とZ座標のカラムを持つDataFrameを作成
    # 画像をグレースケールで読み込み、その画像のリストを作成し"画像"カラムを追加
    # 画像の平均輝度を計算し"平均輝度"カラムを追加
    # 作成したDataFrameを返す
    root_dir_path = "" # 画像ファイルがあるフォルダのパス
    folder_list = os.listdir(root_dir_path)
    df_list = []
    for folder in folder_list:
        path_list = glob.glob(f'{root_dir_path}/{folder}/*.png')
        df = pd.DataFrame()
        # 画像のタイムスタンプをカラムに追加
        df['timestamp'] = [path.split('_')[1].split('.')[0] for path in path_list]
        df['path'] = path_list
        df['Z'] = folder
        img_list = [cv2.imread(path, 0) for path in path_list]
        df['img'] = img_list
        avg_brightness_list = [np.mean(img) for img in img_list]
        df['avg_brightness'] = avg_brightness_list
        df_list.append(df)
    
    # 指定したZ座標における時刻と平均輝度のグラフを描画
    df = pd.concat(df_list)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    z_list = df['Z'].unique()
    for z in z_list:
        df_z = df[df['Z'] == z]
        plt.plot(df_z['timestamp'], df_z['avg_brightness'], label=z)
    plt.legend()
    plt.show()
    return df
    