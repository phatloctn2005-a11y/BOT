System Architecture
1. Overview
Fate/Grand Order AI Botはゲームが自動化され、YOLOの物体を発見する技術と近接ポリシー最適化（Proximal Policy Optimization - PPO）アルゴリズムが含まれるプロジェクトです。
システムが設計されたのは画面の観察、関係のある物体の認識と行動を選んで、その行動を通してゲームをコントロールします。
2. System Components
2.1 Screen Capture
エミュレータを通して連続に撮影します。
入力：画面
出力：写真フレーム
2.2 YOLO Object Detection
ゲームの中の諸物体の発見：
敵や敵の㏋
サーヴァントやサーヴァントの㏋
カード
スキルのボタン
攻撃のボタン
他のUI
入力：画面フレーム
出力：発見された諸物体、座標、分類と信頼度 (confidence score)
2.3 Reinforcement Learning Environment
Gymnasiumという環境はゲームの各操作とPPOの選んだ行動を管理します。
各責任：
・各観察を制作します。
・コントロールを通して選ばれた行動を実現します。
・ポイントを計算します。
・一周りの終わりを確認します。
・できる時、環境を再生します。
2.4 PPO Agent
近接ポリシー最適化（Proximal Policy Optimization - PPO) アルゴリズムを使って、行動を選ぶポリシーを学びます。
入力：環境の観察
出力：選ばれた行動
2.5 ゲームのコントロール
各操作をマウスのクリックとかエミュレータの画面のタッチとかに変換します。
3. Data Flow

Fate/Grand Order
       |
       v
Screen Capture
       |
       v
YOLO Detection
       |
       v
Observation Processing
       |
       v
PPO Agent
       |
       v
Game Controller
       |
       v
Fate/Grand Order

環境が学習中に各観察を集めるとかポイントを計算するとかも実現します。
5. Reinforcement Learning Design

環境の確認する要因：
・観察の空間：特徴の数の形をゲームの発見された各成分から抽出します。
・動く空間：行動を一つずつはゲームのコントロールの一つです。
・ポイント：正しい行動と間違えた行動を評価します。
・学習の終了：各要件が達成したら、学習の一回を終了します。
観察の空間についての各パラメータ、行動の価値とポイントの価値を開発環境に記録する必要があります。
6. Future Improvements
・YOLOの発見する能力を改善します。
・PPOアルゴリズムにポイントの設計を最適化にします。
・プレイ中に成功率を評価します。
・学習の各バラメータとテスト歴史を追加します。
・手順にテストが自動にするのを改善します。
