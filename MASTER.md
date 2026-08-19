# 切り替えスイッチ — MASTER

> **GitHub Source-of-Truth:** このファイルは販売施工の復元起点である。更新時は、下記の正本資料、対象コード、Git履歴を相互参照する。

| 項目 | 現在値 |
| --- | --- |
| Product | **切り替えスイッチ**（現行コード内表記: 「現場休憩スイッチ」） |
| Current Stage | **Stage 1/6 — 正本化完了、一次調査を継続中** |
| Repository | [`daimon-app/genba-break-switch`](https://github.com/daimon-app/genba-break-switch) |
| Branch | `main` |
| HEAD at start | `daaf6170220880c36da612935ba9c2dce11089ab` |
| GitHub Pages | `https://daimon-app.github.io/genba-break-switch/`（公開・HTTPS強制） |
| Latest QA | 未実施。`docs/qa/` に仕様・結果を作成予定。 |
| Latest Audit | 初期実装調査を `docs/research/2026-08-19_market_platform_research.md` に保存済み。販売最終監査は未実施。 |
| Blockers | 販売者情報、購入先・決済事業者、正式価格、返金ポリシーの本人確定が未了。OSバックグラウンド通知・OSアラームは現行未実装。 |
| Approval Required | 商品名最終確定、販売形態・価格、販売者名・住所・連絡先、問い合わせ窓口、返金条件、公開・販売開始可否。 |
| Next Action | 一次情報でのプラットフォーム・競合・法的表示調査を完了し、商品・販売仕様とDecision Logへ反映する。 |

## このリポジトリで作っているもの

切り替えスイッチは、現場作業者が**休憩を始め、短く整え、次の一手を確認して作業へ戻る**ためのモバイル優先PWAである。現行実装には通常・暑い日・重作業・時間休憩、30秒／1分／3分／5分のマイクロリセット、瞑想・整えタイマー、自然音、画面内の終了音、休憩終了30秒前の「次の一手」表示、端末内の記録がある。

> 製品は**医療機器、安全装置、熱中症予防を保証するツール、OSアラームの代替**ではない。実装・販売文言・最終監査では、この境界を維持する。

## 正本マップ

| 種別 | 正本パス | 状態 |
| --- | --- | --- |
| 受領施工仕様書 | [`docs/specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md`](docs/specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md) | 保存済み |
| GitHub正本ルール | [`docs/specs/2026-08-19_GITHUB_SOURCE_OF_TRUTH_MANDATORY_RULE.md`](docs/specs/2026-08-19_GITHUB_SOURCE_OF_TRUTH_MANDATORY_RULE.md) | 保存済み |
| 市場・OS・競合調査 | [`docs/research/2026-08-19_market_platform_research.md`](docs/research/2026-08-19_market_platform_research.md) | 初回調査済み・追記予定 |
| 商品・販売仕様 | `docs/sales/` | 未作成 |
| QA仕様・結果 | `docs/qa/` | 未作成 |
| 販売監査 | `docs/audits/` | 未作成 |
| Decision Log | `docs/decisions/` | 未作成 |

## 正本運用規則

この施工に関する情報は、チャットのみで完結させない。変更ごとに、要件、調査根拠、実装、QA、監査、判定、未決事項、次の一手をGitHub正本に保存する。各AIの出力は、そのまま事実として採用せず、対象コード・実画面・一次情報・QAとの照合結果をDecision Logに残す。

コミット時には**対象ファイルを明示してステージング**し、`git add .`、`git reset --hard`、force push、無関係変更のコミットを用いない。既存未コミット作業と安全に分離できない場合は、`GIT_COMMIT_HOLD` の理由をこのファイルとDecision Logに残す。

## マイルストーン

| Stage | 成果物 | 判定 |
| --- | --- | --- |
| 1 | GitHub正本確認、受領仕様書保存、MASTER作成 | 進行中 |
| 2 | 一次情報による市場・競合・プラットフォーム・表示要件調査 | 未完了 |
| 3 | 商品・価格・販売導線・差別化の仕様と意思決定 | 未開始 |
| 4 | LP・FAQ・規約・プライバシー・問い合わせ導線の施工 | 未開始 |
| 5 | 実装QA、販売監査、修正、再QA | 未開始 |
| 6 | HEAD／監査／QA／判定の確定、GitHub正本更新、最終報告 | 未開始 |

## 更新履歴

| 日付 | Stage | 変更 | 証拠 |
| --- | --- | --- | --- |
| 2026-08-19 | 1 | GitHub正本を確認し、施工仕様書、正本運用ルール、初回調査、MASTERを作成した。 | `docs/specs/`、`docs/research/`、Git履歴（コミット予定） |
