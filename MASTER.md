# 切り替えスイッチ — MASTER

> **GitHub Source-of-Truth:** このファイルは販売施工の復元起点である。更新時は、下記の正本資料、対象コード、Git履歴を相互参照する。

| 項目 | 現在値 |
| --- | --- |
| Product | **切り替えスイッチ**（現行コード内表記: 「現場休憩スイッチ」） |
| Current Stage | **Stage 5/6 — 公開GitHub Pages QA・販売監査・キャッシュ修正・再QA中** |
| Repository | [`daimon-app/genba-break-switch`](https://github.com/daimon-app/genba-break-switch) |
| Branch | `main` |
| HEAD at start | `daaf6170220880c36da612935ba9c2dce11089ab` |
| GitHub Pages | `https://daimon-app.github.io/genba-break-switch/`（公開・HTTPS強制） |
| Latest QA | 静的QA PASS、ローカル主要導線QA PASS、公開LP QA PASS。公開PWAで旧Service Workerキャッシュによる旧名称・旧導線を検出し、v10に修正・公開再QA待ち。iOS／Android実機QAは未実施。詳細は `docs/qa/2026-08-19_sales_ready_qa_result.md`。 |
| Latest Audit | 初期実装・市場・プラットフォーム調査、販売表示・個人情報調査、商品・販売仕様、GitHub Pages商取引制約、LP・法務・サポート施工を正本化済み。販売最終監査は未実施。 |
| Blockers | 有償販売はGitHub Pagesでは開始不可。無料公開ベータの外部告知はService Workerキャッシュ修正の公開再QAまで保留。販売者情報、商取引可能な販売基盤、決済事業者、正式価格、返金ポリシーの本人確定が未了。OSバックグラウンド通知・OSアラームは現行未実装。 |
| Approval Required | 商品名最終確定、販売形態・価格、販売者名・住所・連絡先、問い合わせ窓口、返金条件、公開・販売開始可否。 |
| Next Action | Service Workerキャッシュ修正をコミット・pushし、公開LP→PWAの再QA、全公開ページの到達確認、販売監査を行う。購入・決済は有効化しない。 |

## このリポジトリで作っているもの

切り替えスイッチは、現場作業者が**休憩を始め、短く整え、次の一手を確認して作業へ戻る**ためのモバイル優先PWAである。現行実装には通常・暑い日・重作業・時間休憩、30秒／1分／3分／5分のマイクロリセット、瞑想・整えタイマー、自然音、画面内の終了音、休憩終了30秒前の「次の一手」表示、端末内の記録がある。

> 製品は**医療機器、安全装置、熱中症予防を保証するツール、OSアラームの代替**ではない。実装・販売文言・最終監査では、この境界を維持する。

## 正本マップ

| 種別 | 正本パス | 状態 |
| --- | --- | --- |
| 受領施工仕様書 | [`docs/specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md`](docs/specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md) | 保存済み |
| GitHub正本ルール | [`docs/specs/2026-08-19_GITHUB_SOURCE_OF_TRUTH_MANDATORY_RULE.md`](docs/specs/2026-08-19_GITHUB_SOURCE_OF_TRUTH_MANDATORY_RULE.md) | 保存済み |
| 市場・OS・競合調査 | [`docs/research/2026-08-19_market_platform_research.md`](docs/research/2026-08-19_market_platform_research.md) | 初回調査済み・追記予定 |
| 販売表示・個人情報調査 | [`docs/research/2026-08-19_sales_legal_requirements_research.md`](docs/research/2026-08-19_sales_legal_requirements_research.md) | 初回調査済み |
| 商品・販売仕様 | [`docs/sales/2026-08-19_product_and_go_to_market_spec.md`](docs/sales/2026-08-19_product_and_go_to_market_spec.md)、[`2026-08-19_sales_assets_implementation.md`](docs/sales/2026-08-19_sales_assets_implementation.md)、[`2026-08-19_sns_launch_kit.md`](docs/sales/2026-08-19_sns_launch_kit.md) | 施工済み・有償化は本人承認待ち |
| QA仕様・結果 | [`docs/qa/2026-08-19_sales_ready_qa_spec.md`](docs/qa/2026-08-19_sales_ready_qa_spec.md)、[`2026-08-19_sales_ready_qa_result.md`](docs/qa/2026-08-19_sales_ready_qa_result.md) | ローカルQA済み・公開後／実機QA待ち |
| GitHub Pages商取引制約 | [`docs/research/2026-08-19_github_pages_hosting_constraints.md`](docs/research/2026-08-19_github_pages_hosting_constraints.md) | 調査済み |
| 販売監査 | `docs/audits/` | 未作成 |
| Decision Log | [`docs/decisions/2026-08-19_sales_execution_decision_log.md`](docs/decisions/2026-08-19_sales_execution_decision_log.md) | 初期判断を保存済み・継続更新 |

## 正本運用規則

この施工に関する情報は、チャットのみで完結させない。変更ごとに、要件、調査根拠、実装、QA、監査、判定、未決事項、次の一手をGitHub正本に保存する。各AIの出力は、そのまま事実として採用せず、対象コード・実画面・一次情報・QAとの照合結果をDecision Logに残す。

コミット時には**対象ファイルを明示してステージング**し、`git add .`、`git reset --hard`、force push、無関係変更のコミットを用いない。既存未コミット作業と安全に分離できない場合は、`GIT_COMMIT_HOLD` の理由をこのファイルとDecision Logに残す。

## マイルストーン

| Stage | 成果物 | 判定 |
| --- | --- | --- |
| 1 | GitHub正本確認、受領仕様書保存、MASTER作成 | 完了 |
| 2 | 一次情報による市場・競合・プラットフォーム・表示要件調査 | 完了 |
| 3 | 商品・価格・販売導線・差別化の仕様と意思決定 | 完了 |
| 4 | LP・FAQ・規約・プライバシー・問い合わせ導線の施工 | 完了（commit `f1ed9e57fd35a2f26eeacbff03d215ccc9e34d61`・push済み） |
| 5 | 実装QA、販売監査、修正、再QA | 進行中（キャッシュ修正・公開再QA待ち） |
| 6 | HEAD／監査／QA／判定の確定、GitHub正本更新、最終報告 | 未開始 |

## 更新履歴

| 日付 | Stage | 変更 | 証拠 |
| --- | --- | --- | --- |
| 2026-08-19 | 1 | GitHub正本を確認し、施工仕様書、正本運用ルール、初回調査、MASTERを作成・pushした。 | `docs/specs/`、`docs/research/`、commit `89e2bed3f3adc95d2c11160dea9a42a6a59050dd` |
| 2026-08-19 | 2 | 公開PWAの初期画面、OS／PWA制約、競合、販売表示・個人情報の一次情報調査を完了・pushした。 | `docs/research/`、commit `82f69c861f5483e559053b4841298f3236e34018` |
| 2026-08-19 | 3 | 商品価値、対象顧客、競合上の位置づけ、無料公開ベータ案、有償化条件、販売文言ガードレールを仕様化・pushした。 | `docs/sales/2026-08-19_product_and_go_to_market_spec.md`、commit `82eb228f4771f03f84970e830f5f8f90024d212d` |
| 2026-08-19 | 4 | GitHub Pagesを有償商取引に使わない方針を記録し、無料公開ベータ向けLP、FAQ、追加方法、利用規約、Privacy、販売案内、公開フィードバック、SNS素材、PWA本体からの導線を施工した。静的QAとローカル主要導線QAをPASS。 | `start.html`、`faq.html`、`install.html`、`terms.html`、`privacy.html`、`commerce.html`、`support.html`、`docs/sales/`、`docs/qa/`、commit `f1ed9e57fd35a2f26eeacbff03d215ccc9e34d61` |
| 2026-08-19 | 5 | 公開LP初回404はPagesビルド完了後に解消。公開PWAで既存Service Workerの旧HTML cache-first応答を検出し、v10・HTML network-first・バージョン付きPWAリンクへ修正、再QA待ち。 | `docs/qa/2026-08-19_sales_ready_qa_result.md`、D-015 |
