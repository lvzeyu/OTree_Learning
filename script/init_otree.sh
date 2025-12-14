#!/bin/bash

# oTreeプロジェクトの初期化スクリプト

# .envファイルを読み込み
ENV_FILE="$(dirname "$0")/../.env"
if [ -f "$ENV_FILE" ]; then
    source "$ENV_FILE"
else
    echo ".envファイルが見つかりません: $ENV_FILE"
    exit 1
fi

# oTreeをインストール（既にインストールされている場合スキップ）
# pip install -U otree

# プロジェクトディレクトリを作成（.envのOTREE_WORKING_DIRを使用）
PROJECT_DIR=$OTREE_WORKING_DIR/otreetest
echo "プロジェクトディレクトリ: $PROJECT_DIR"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# otree環境をアクティブ化
conda activate otree

# oTreeプロジェクトを開始
otree startproject otreetest --noinput

# プロジェクトディレクトリに移動
cd otreetest

# テストアプリを作成
otree startapp testapp

# 開発サーバーを起動
otree devserver