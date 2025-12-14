#!/bin/bash

# otreeという名前のconda環境が存在するかどうかをチェック
if conda env list | grep -q "^otree "; then
    echo "otree環境は既に存在します。作成をスキップします。"
else
    echo "otree環境が存在しません。作成中..."
    conda create -n otree python=3.10 -y

    # otree環境でotreeパッケージをインストール
    echo "otree環境でotreeをインストール中..."
    conda run -n otree pip install otree
fi

# scriptフォルダ内のファイルの権限を設定
echo "scriptフォルダ内のファイルの権限を設定中..."
chmod +x script/*.sh

echo "otree環境の設定が完了しました。この環境を使用するには、以下のコマンドを実行してください: conda activate otree"
