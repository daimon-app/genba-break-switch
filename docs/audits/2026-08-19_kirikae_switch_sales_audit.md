# KIRIKAE SWITCH SALES AUDIT

> **監査日:** 2026-08-19 JST
> **監査対象:** `daimon-app/genba-break-switch` の `main`、公開GitHub Pages、無料公開ベータ向け案内・法務・サポート導線
> **監査者:** Manus AI
> **監査状態:** 最終施工監査。法的助言・法的適合性の最終保証ではない。
> **結論:** **CONDITIONAL — 無料公開ベータは本人承認後に開始可能。有償販売は開始不可。**

## 1. 監査の結論

切り替えスイッチは、**現場の休憩から次の一手へ戻るための無料公開ベータPWA**として、商品価値、モバイル導線、制約表示、プライバシー、利用規約、公開フィードバック、公開QAの必要最小限を施工した。LP、PWA、FAQ、追加方法、規約、Privacy、販売案内、サポートはGitHub Pagesで公開済みであり、主要導線・静的QA・ローカル手動QA・公開再QAは合格した。

ただし、現行のGitHub Pagesは、EC、商取引の促進を主目的とするサイト、商用SaaSの運営に用いることを意図・許可していない。[1] 現在は販売者情報、商取引可能な販売基盤、価格、返金条件、決済、個別問い合わせ窓口が未確定である。このため、**有償購入、決済、サブスクリプション、導入支援の申込みを開始することはNO GO**とする。無料公開ベータにも、外部告知や公開開始についての本人承認が必要である。

| 対象 | 判定 | 根拠 |
| --- | --- | --- |
| 無料公開ベータの技術公開 | **CONDITIONAL GO** | 公開LP・PWA・FAQ・規約・Privacy・サポートを実装し、主要QAに合格。本人承認と可能なら実機確認を条件とする。 |
| 無料公開ベータのSNS外部告知 | **APPROVAL REQUIRED** | 投稿文案は用意済みだが、公式アカウント、投稿者、日時、素材、本人承認が未確定。 |
| 有償デジタル販売 | **NO GO** | GitHub Pagesの用途制約、特商法の実情報未確定、決済・返金・問い合わせ未確定。 |
| チーム向け導入支援・継続サポートの販売 | **NO GO** | 提供範囲、販売者、契約、連絡先、納期、データ取扱い、商取引基盤が未確定。 |

## 2. GitHub正本と実装証跡

| 項目 | 確認結果 |
| --- | --- |
| Repository | [`daimon-app/genba-break-switch`](https://github.com/daimon-app/genba-break-switch) |
| Branch | `main` |
| HEAD at audit | `9db6d2118cf5d7fd4cdc4983955118d0a7a3e785` |
| 施工コミット | `f1ed9e57fd35a2f26eeacbff03d215ccc9e34d61` — 無料公開ベータの販売準備ページ、文書、QAを追加。 |
| 修正コミット | `9db6d2118cf5d7fd4cdc4983955118d0a7a3e785` — Service WorkerのHTML更新とキャッシュ回避導線を修正。 |
| 公開URL | [PWA](https://daimon-app.github.io/genba-break-switch/index.html?v=20260819) / [LP](https://daimon-app.github.io/genba-break-switch/start.html) |
| 仕様書 | [`docs/specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md`](../specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md) |
| Decision Log | [`docs/decisions/2026-08-19_sales_execution_decision_log.md`](../decisions/2026-08-19_sales_execution_decision_log.md) |
| QA | [`docs/qa/2026-08-19_sales_ready_qa_result.md`](../qa/2026-08-19_sales_ready_qa_result.md) |

## 3. 現行商品と価値

本プロダクトは、通常／暑い日／重作業／時間休憩、30秒／1分／3分／5分のマイクロリセット、30秒／1分を含む瞑想・整えタイマー、自然音、端末内の利用記録、休憩後の「次の一手」入力・再表示を提供する。差別化は「一般タイマー」や「瞑想コンテンツの量」ではなく、**現場の短い休憩を、次の一手への再始動へ接続する操作の型**にある。

| 価値 | 実装で確認した事実 | 言ってよいこと | 言ってはいけないこと |
| --- | --- | --- | --- |
| 短い切替 | 30秒からのマイクロリセットと瞑想・整えタイマー。 | 「30秒から整えるためのメニュー」 | 集中・疲労・ストレスが改善する保証。 |
| 再始動 | 次の一手を入力し、終盤・完了時に表示。 | 「戻る作業を一つだけ確認する」 | 作業効率・生産性が向上する保証。 |
| 時間の目安 | 画面内カウント、終了音、一時停止。 | 「画面を開いている間のタイマー」 | 必ず鳴る、OSアラームの代替、バックグラウンド通知。 |
| 暑い日の休憩提案 | 固定の休憩時間・チェック項目。 | 「暑い日向けの固定メニュー」 | 熱中症予防、診断、安全確保、法令遵守の保証。 |

## 4. 競合とポジショニング

無料のOS標準タイマー・アラームと一般作業タイマーは、時間管理と確実な通知における強力な代替である。大規模瞑想アプリは豊富なガイド・音源を提供し、Insight Timerは日本のApp Storeに月額1,150円／年額6,800円の価格を表示している。[2] 切り替えスイッチは、これらと通知の信頼性やコンテンツ量で競わず、**現場語彙、短いリセット、次の一手、再始動**に焦点を置く。

| 比較軸 | 標準タイマー | 一般作業タイマー | 大規模瞑想アプリ | 切り替えスイッチ |
| --- | --- | --- | --- | --- |
| 中核用途 | 時間・アラーム | 集中反復 | 瞑想・睡眠・音源 | 休憩から再始動 |
| 次の一手 | なし | 一般タスク | 通常なし | 現場の一言入力 |
| OS通知 | 強い | ネイティブなら強い | ネイティブなら強い | 現行では非提供 |
| 現場言葉 | なし | 限定的 | なし | 現行UIに反映 |
| 価格状態 | 多くは無料標準搭載 | 無料代替あり | サブスクリプションが主流 | 現在0円ベータ |

## 5. プラットフォーム・OS制約

Appleは、iOS/iPadOS 16.4以降でホーム画面に追加したWebアプリにWeb Pushを提供しているが、これは利用者の明示的許可とPush実装を前提にする。[3] 現行コードにはPush購読、サーバー送信、通知表示処理がない。Webの画面消灯防止はWake Lock APIによるベストエフォートで、ページの非表示化等により解除され得る。[4] PWAのホーム画面追加・インストールは端末・OS・ブラウザ条件に依存する。[5]

| 項目 | 現行状態 | 販売表示の扱い |
| --- | --- | --- |
| OS Push通知 | 未実装 | 提供すると約束しない。 |
| OSアラーム | 未実装 | 端末標準タイマー／アラームの併用を案内する。 |
| バックグラウンド終了音 | 保証不可 | 画面を開いている間のタイマーに限定して説明する。 |
| 画面消灯防止 | 対応環境で試行 | 端末・設定で解除／不使用となる可能性を明示する。 |
| Android／iPhoneへの追加 | 導入案内を実装 | 対応・手順・挙動の端末差を明示する。 |
| データ同期 | 未実装 | 端末・ブラウザ内保存と説明する。 |

## 6. 公開・QA結果

静的QAは、必須ファイル、名称整合、ローカルリンク、無料公開ベータ境界、禁止表現、Service Workerキャッシュ、Privacy説明を検査してPASSとなった。ローカルブラウザではLP→PWA、30秒リセット、入力した次の一手、一時停止・再開・完了、瞑想30秒、瞑想1分を確認した。公開GitHub PagesではLP、修正後PWA、FAQ、追加方法、利用規約、Privacy、販売案内、サポートの到達・内容を確認した。

| QA論点 | 判定 | 結果 |
| --- | --- | --- |
| 商品名整合 | PASS | title、ホーム、manifest、Apple Web App titleを「切り替えスイッチ」に整合。 |
| PWA主要操作 | PASS | 30秒リセット、次の一手、一時停止、再開、完了、瞑想30秒／1分を確認。 |
| 旧キャッシュ | RESOLVED | 旧HTML cache-firstを検出後、`kirikae-v10`とHTML network-first、バージョン付きURLで修正・公開再QA。 |
| LP・販売境界 | PASS | 無料公開ベータ、購入・決済なし、OS制約、安全上の注意を表示。 |
| Privacy | PASS | localStorage、GitHub Pages IPログ、公開Issues、未導入SDKを説明。 |
| 法務・販売 | CONDITIONAL | 無料ベータの案内文書はある。有償販売に必要な実情報は未確定。 |
| iOS／Android実機 | NOT RUN | 本監査環境では物理端末確認を実施していない。 |

## 7. 法務・プライバシー・サポート

日本の通信販売で有償申込みを受ける場合、消費者庁は広告表示、誇大広告の禁止、申込み段階の表示等を案内している。[6] 現行は有償取引がないため、販売案内は「特定商取引法に基づく表記」ではなく、有償販売を開始していないことと、開始前に確定すべき事項を説明するページに限定した。

GitHub Pagesは訪問時のIPアドレスをセキュリティ目的で記録・保存する。[7] PWA本体の休憩履歴、音設定、次の一手は、現行コード上ではブラウザのローカルストレージに保存され、サーバー送信・アカウント同期・広告SDK・分析SDKは実装していない。公開フィードバックはGitHub Issuesで受け付け、公開されるため個人情報・機密情報を記載しないよう明示した。

| 項目 | 無料公開ベータ | 有償販売開始時 |
| --- | --- | --- |
| 利用規約 | 実装済み（暫定） | 取引条件に合わせて改定・専門家確認。 |
| Privacy | 実装済み | 決済・問い合わせ・分析・アカウントの実態を追記。 |
| 問い合わせ | 公開Issuesのみ | 非公開の正式連絡先、対応時間、個人情報取扱いを設置。 |
| 特商法表記 | 有償取引なしのため未掲載 | 販売者、住所、連絡先、価格、支払、提供、返金を実情報で掲載。 |
| 決済 | なし | GitHub Pages外の適切な商取引基盤で実装。 |

## 8. 未解消のTECH_FIX_REQUIRED

| 優先度 | 内容 | 販売への影響 | 推奨対応 |
| --- | --- | --- | --- |
| 解消済み | `icons/service-worker.js` がルートのアクティブService Workerとは別に残り、旧キャッシュ名を含む。 | ルート登録経路のみであることを確認し、未参照の旧ファイルを削除済み。 | 再発時はルートの `service-worker.js` だけを正本とする。 |
| 低 | ルート直下に音源・アイコンの重複資産がある。 | 現時点で販売文言・機能に直接影響しないが、更新・容量の混乱要因。 | 参照確認後、不要資産を別コミットで整理する。 |
| 中 | iOS／Android実機QA未実施。 | インストール、Wake Lock、バックグラウンド、表示の品質を保証できない。 | 主要端末で導入・再開・時間経過・低電力状態を検証する。 |
| 高（有償化） | 決済、販売者、価格、返金、正式サポート、商取引基盤未確定。 | 有償販売は開始不可。 | 有償商品の実体を確定し、GitHub Pages外に販売基盤を構築する。 |

## 9. 本人承認待ち

| 承認事項 | 無料公開ベータ | 有償販売 |
| --- | --- | --- |
| 商品名「切り替えスイッチ」の最終確定 | 必須 | 必須 |
| 無料公開ベータの外部告知開始 | 必須 | — |
| SNS投稿文・投稿者・日時・素材 | 必須 | 必須 |
| 販売者の正式名称・住所・連絡先 | 推奨（正式サポート開始前は必須） | 必須 |
| 商品内容・税込価格・提供時期 | — | 必須 |
| 返金・解約条件 | — | 必須 |
| 決済事業者・商取引基盤 | — | 必須 |
| 実機QAの受容または実施 | 強く推奨 | 必須 |

## 10. Decision

> **Decision: CONDITIONAL**
>
> **SALES READY: 無料公開ベータに限り、本人承認後にGO。**
>
> **有償販売: NO GO。GitHub Pages上では開始せず、必要な実情報・商取引基盤・本人承認が揃うまで保留。**

無料公開ベータの公開URL・LP・アプリ・FAQ・規約・Privacy・サポートは施工済みで、外部告知を除く技術的公開準備は整った。本人が無料公開ベータの開始を承認する場合、SNS投稿は[`docs/sales/2026-08-19_sns_launch_kit.md`](../sales/2026-08-19_sns_launch_kit.md)の案から承認済み文面のみを使用する。有償化は、別ステージとして販売基盤・法定表示・決済・返金・個別窓口・実機QAを完了してから再監査する。

## 参照

[1] [GitHub Docs「GitHub Pages limits」](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

[2] [App Store「Insight Timer - 瞑想アプリ」](https://apps.apple.com/jp/app/insight-timer-%E7%9E%91%E6%83%B3%E3%82%A2%E3%83%97%E3%83%AA/id337472899)

[3] [Apple Developer Documentation「Sending web push notifications in web apps and browsers」](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers)

[4] [MDN Web Docs「Screen Wake Lock API」](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Wake_Lock_API)

[5] [web.dev「What does it take to be installable?」](https://web.dev/articles/install-criteria)

[6] [消費者庁「通信販売のルール」](https://www.no-trouble.caa.go.jp/what/mailorder/rule.html)

[7] [GitHub Docs「What is GitHub Pages?」](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
