# 切り替えスイッチ — SALES READY QA結果

> **実施日:** 2026-08-19 JST
> **対象ワークツリー:** `main`（販売施工の未コミット変更を含むローカル検証）
> **QA仕様:** [2026-08-19_sales_ready_qa_spec.md](2026-08-19_sales_ready_qa_spec.md)
> **実機境界:** iOS／Androidの物理端末検証、低電力状態、バックグラウンド音、インストール後の実機挙動は未実施。

## 総合暫定結果

| 区分 | 結果 | 注記 |
| --- | --- | --- |
| 静的QA | PASS | 必須ファイル、名称整合、ローカルリンク、販売境界、表現ガード、Service Workerキャッシュ、Privacy文言を自動検査。詳細JSONは `2026-08-19_sales_ready_static_result.json`。 |
| ローカルLP画面 | PASS | `http://localhost:4173/start.html` でLPのタイトル、無料公開ベータ表記、主要CTA、制約・安全注意、フッター導線を確認。 |
| LP→PWA導線 | PASS | LPの「無料で試す」から `http://localhost:4173/index.html` へ遷移し、ホーム画面を確認。 |
| PWAホーム名称・導線 | PASS | 「切り替えスイッチ」の表示、既存機能、案内LPとFAQへのリンクを確認。 |
| モバイル実機 | NOT RUN | 実機確認が必要。 |
| 公開GitHub Pages | PASS | LP、キャッシュ修正後のPWA、FAQを公開URLで確認。初回404はビルド待ちで解消。旧Service Workerキャッシュ問題はv10・HTMLネットワーク優先・バージョン付き導線の公開反映後に、`index.html?v=20260819` で新名称・新導線を確認して解消。 |

## 実施したQA

| ID | 方法 | 結果 | 証拠・所見 |
| --- | --- | --- | --- |
| Q-01 | `validate_sales_ready.py` | PASS | HTML、CSS、manifest、Service Worker、キャッシュ対象の存在を確認。 |
| Q-02 | `validate_sales_ready.py`＋ローカル実画面 | PASS | `index.html` title、Apple Web App title、manifest `name`／`short_name`、ホーム表示を「切り替えスイッチ」に整合。 |
| Q-03 | ローカル実画面・クリック | PASS | LPに「無料で試す」があり、PWA本体へ遷移。無料公開ベータ・有償購入なしを表示。 |
| Q-04 | `validate_sales_ready.py` | PASS | LP、FAQ、追加方法、規約、Privacy、販売案内、サポートのローカルリンクが全て解決。 |
| Q-05 | `validate_sales_ready.py`＋LP実画面 | PASS | OSアラーム、必ず通知、バックグラウンド保証、熱中症予防、安全保証、効果保証を販売約束として含めず、端末標準タイマー併用と安全上の注意を表示。 |
| Q-06 | `validate_sales_ready.py` | PASS | `kirikae-v9` のService WorkerキャッシュにPWA本体、案内・法務・サポートページ、共通CSS、音源・アイコンを含めた。Push APIは実装していない。 |
| Q-07 | ローカル実画面 | PASS | ホーム画面に「使い方・無料公開ベータ」「FAQ・安全上の注意」を表示し、到達できる。 |
| Q-10 | ローカル実画面 | PASS WITH LIMITATION | LPは対象表示領域でCTAと見出しが視認でき、PWAホームでは主要操作と追加導線が縦一画面に収まる。iOS／Android実機の視認性は未確認。 |
| Q-12 | `validate_sales_ready.py`＋LP実画面 | PASS | ローカルフォームなし。販売案内に有償販売・決済なしを明示。 |

## 追加の手動ブラウザQA（ローカル）

| ID | 操作 | 結果 | 所見 |
| --- | --- | --- | --- |
| Q-07-A | PWAホームで「30秒リセット」を選択 | PASS | 「30秒リセット」設定画面へ遷移し、次の一手の入力欄、プリセット、開始ボタンを表示した。 |
| Q-07-B | 「ボードを1枚貼る」を次の一手に入力 | PASS | 入力欄へテスト文が反映された。 |
| Q-08-A | 「30秒でスタート」を選択 | PASS | 30秒リセットのタイマー画面へ遷移し、残り時間、チェックリスト、一時停止、終了を表示した。 |
| Q-08-B | 実行中に「一旦止める」を選択 | PASS | 残り `00:21` の状態で「一時停止中」と「再開する」を表示した。 |
| Q-08-C | 「再開する」を選択し、経過を確認 | PASS | 「整える」「一旦止める」に戻り、残り時間が `00:19` から `00:10` へ進行した。 |
| Q-08-D | 30秒の終了を待機 | PASS | 完了画面で「まず」「ボードを1枚貼る」を表示し、入力した次の一手を復元した。 |
| Q-08-E | 「現場に戻る」を選択 | PASS | ホームへ戻り、今日・今週の集計が各1回へ更新された。 |
| Q-08-F | 瞑想・整えタイマーで30秒「断ち切り」を選択 | PASS | 「断ち切り30秒」、残り時間、固定の再始動メッセージ「次の一手だけ見る」、自然音切替、一時停止・終了を表示した。標準アラーム併用の注意も表示。 |
| Q-08-G | 瞑想・整えタイマーで1分「一息リセット」を選択 | PASS | 「一息リセット1分」、残り `00:59`、固定の再始動メッセージ「肩の力を抜く」、自然音切替、一時停止・終了を表示した。 |
| Q-11-A | GitHub PagesのLPを初回確認 | FAIL→PASS | push直後はPagesが `building` でLPが404。build success（run `32204066051`）後に `start.html` は公開・表示を確認。 |
| Q-11-B | 公開LPからPWAへ遷移 | FAIL（修正済み・公開再QA待ち） | 既存のキャッシュ利用環境では旧「現場休憩スイッチ」画面・旧ホーム導線が表示された。旧Service Workerのcache-first HTML応答が原因。 |
| Q-06-R | キャッシュ修正の静的再QA | PASS | `kirikae-v10`、HTMLのnetwork-first取得、PWAリンクの `?v=20260819` 付与、全ローカルリンク整合を自動検証。 |
| Q-11-C | キャッシュ修正後の公開PWAを `index.html?v=20260819` で確認 | PASS | 新名称「切り替えスイッチ」、LP・FAQ導線、既存のモード・マイクロリセット・瞑想導線を確認。旧名称・旧画面を再現しなかった。 |
| Q-11-D | 公開PWAからFAQへ遷移 | PASS | FAQを公開URLで表示し、無料公開ベータ、アファメーション専用機能の未実装、OS通知／中断／画面消灯／Android・iPhone／オフライン／記録／暑い日モード／公開フィードバックの制約説明を確認。 |

## FAIL／TECH_FIX_REQUIRED

初回のLP 404はGitHub Pagesのビルド完了後に解消した。既存Service Workerの旧HTML cache-first問題は、v10・HTML network-first・バージョン付きPWAリンクの公開反映後に再QAし、解消を確認した。未解消の技術監査項目と実機検証範囲は下表に残す。

| 区分 | 内容 | 対応 |
| --- | --- | --- |
| RESOLVED | `https://daimon-app.github.io/genba-break-switch/start.html` の初回GitHub Pages 404。 | Pages build success後に公開LPを再確認し、正常表示を確認。初回404はビルド反映待ちとしてクローズ。 |
| RESOLVED | 既存Service Workerがcache-firstで旧 `index.html` を返し、既存利用者が旧名称・旧導線を見る。 | `kirikae-v10`、HTMLのnetwork-first応答、LP等からのバージョン付きPWAリンクに修正。公開再QAで新名称・新導線を確認。 |
| RESOLVED | `icons/service-worker.js` はルートのアクティブService Workerとは別に存在し、旧キャッシュ名を持つ。 | ルート登録経路のみであることを確認し、未参照の旧ファイルを削除した。 |
| TECH_FIX_REQUIRED（監査対象） | ルートに音源・アイコンの重複ファイルがあり、アクティブ実装は `assets/sounds/` と `icons/` を使用する。 | 配布容量・更新誤認を避けるため、利用有無を確認して別施工単位で整理する。 |
| LIMITATION | OS通知、OSアラーム、バックグラウンド終了通知、Wake Lockの恒常成功、端末別の追加体験は保証不可。 | LP、FAQ、規約に明示済み。実機QAで挙動を記録する。 |
| APPROVAL_REQUIRED | 有償販売の販売者情報、商取引基盤、価格、返金条件、決済、正式窓口が未確定。 | 無料公開ベータに限定し、有償販売は開始しない。 |

## 次のQA

1. 追加方法、利用規約、Privacy、販売案内、サポートの公開到達を確認する。
2. Android ChromeとiPhone Safariで、ホーム画面追加、画面消灯防止の表示、復帰時の残時間再計算を実機検証する。
3. 販売監査で、有償販売の禁止・無料公開ベータの表現・特商法／問い合わせの未確定状態・販売導線を確認する。
