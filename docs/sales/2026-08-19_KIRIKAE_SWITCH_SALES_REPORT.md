# KIRIKAE SWITCH SALES REPORT

> **報告日:** 2026-08-19 JST
>
> **判定時点の正本HEAD:** `aaab82bce5824dc230ea2c68cd580df002444885`（本報告書のcommit前）
>
> **最終結論:** **CONDITIONAL — 無料公開ベータは本人承認後にGO。有償販売はNO GO。**

## Repository

| 項目 | 内容 |
| --- | --- |
| Repository | [`daimon-app/genba-break-switch`](https://github.com/daimon-app/genba-break-switch) |
| Public PWA | [切り替えスイッチ](https://daimon-app.github.io/genba-break-switch/index.html?v=20260819) |
| Public LP | [無料公開ベータ案内](https://daimon-app.github.io/genba-break-switch/start.html) |
| Branch | `main` |
| GitHub Source-of-Truth | 本リポジトリを唯一の施工正本とし、仕様、調査、QA、監査、Decision Log、進行台帳を保存済み。 |

## Commit

| 施工単位 | Commit | 状態 |
| --- | --- | --- |
| 仕様・初期正本化 | `89e2bed3f3adc95d2c11160dea9a42a6a59050dd` | push済み |
| 市場・法的表示調査 | `82f69c861f5483e559053b4841298f3236e34018` | push済み |
| 商品・無料ベータ戦略 | `82eb228f4771f03f84970e830f5f8f90024d212d` | push済み |
| LP・FAQ・規約・Privacy・サポート・QA | `f1ed9e57fd35a2f26eeacbff03d215ccc9e34d61` | push済み |
| PWA更新キャッシュ修正 | `9db6d2118cf5d7fd4cdc4983955118d0a7a3e785` | push済み |
| 最終監査・QA・Decision Log | `ef4797a3d5c0fd2b5375a9bdacea10e2152e7186` | push済み |
| MASTER最終ステージ更新 | `aaab82bce5824dc230ea2c68cd580df002444885` | push済み |

## Latest Product

**切り替えスイッチ**は、現場作業者が休憩を始め、30秒から短く整え、休憩後の「次の一手」を一つだけ見て作業へ戻るためのモバイル優先PWAである。現行コードで、通常／暑い日／重作業／時間休憩、30秒／1分／3分／5分のマイクロリセット、瞑想・整えタイマー、自然音、端末内記録、次の一手の入力・再表示を確認した。

## Platform Constraints

| 項目 | 現行状態 | 販売文言の扱い |
| --- | --- | --- |
| OS Push通知・OSアラーム | 未実装 | 約束しない。端末標準タイマー／アラーム併用を案内。 |
| バックグラウンド終了通知・音 | 保証不可 | 「画面を開いている間のタイマー」に限定。 |
| 画面消灯防止 | 対応環境で試行 | 端末・設定・画面の非表示化により解除・非対応となり得ることを明示。 |
| Android／iPhone追加 | 導入案内を実装 | 端末・OS・ブラウザ差を明示。実機QAは未実施。 |
| 端末間同期 | 未実装 | 履歴・設定・次の一手はブラウザ・端末内保存と説明。 |
| GitHub Pages | 無料公開ベータ案内・PWAに限定 | 有償取引・決済・機微情報フォームに使わない。 |

一次情報と詳細根拠は[市場・プラットフォーム調査](../research/2026-08-19_market_platform_research.md)、[GitHub Pages制約調査](../research/2026-08-19_github_pages_hosting_constraints.md)、[最終販売監査](../audits/2026-08-19_kirikae_switch_sales_audit.md)に保存した。

## Market

最初の対象は、一人親方および少人数チームの内装・建築系作業者とする。現場で短い休憩を取り、休憩後に何から戻るかが散る状況に、「休憩から次の一手へ戻る型」を提供する。無料公開ベータでは、利用頻度ではなく、現場語彙、操作の分かりやすさ、端末ごとの使いにくさ、再始動の実感を検証する。

## Competition

| 競合群 | 強み | 本プロダクトの対応 |
| --- | --- | --- |
| OS標準タイマー・アラーム | 通知・アラームの信頼性、無料 | 代替しない。終了時刻を確実に知る用途では併用を推奨。 |
| 一般作業タイマー | ポモドーロ等の集中反復 | 現場語彙と休憩後の次の一手に焦点を置く。 |
| 大規模瞑想アプリ | 音源・ガイド・睡眠コンテンツ | コンテンツ量で競わず、30秒からの再始動操作に集中。 |

## Differentiation

差別化は、**現場の短い休憩を、次の一手への再始動に接続すること**である。一般タイマーにない「次の一手」の一言入力・終了時表示、現場向けモード、30秒から始める短い整えを、一画面に収めている。瞑想効果、安全効果、アラーム信頼性の保証では差別化しない。

## Price

**現在の価格は0円。無料公開ベータ。** 現行PWAは公開リポジトリで、有料機能・決済・アカウント・個別サポートを持たないため、有償化は実体のある別商品（導入キット、チーム支援、継続チーム版等）を定義してから検討する。

有償化の参考価格案は[商品・販売仕様](2026-08-19_product_and_go_to_market_spec.md)に保存しているが、本人承認前の案であり、公開価格ではない。

## LP

施工済みの公開ページは次のとおりである。

| ページ | URL | 状態 |
| --- | --- | --- |
| LP | [start.html](https://daimon-app.github.io/genba-break-switch/start.html) | 公開QA PASS |
| PWA | [index.html](https://daimon-app.github.io/genba-break-switch/index.html?v=20260819) | 公開QA PASS |
| FAQ | [faq.html](https://daimon-app.github.io/genba-break-switch/faq.html) | 公開QA PASS |
| 追加方法 | [install.html](https://daimon-app.github.io/genba-break-switch/install.html) | 公開QA PASS |
| 利用規約 | [terms.html](https://daimon-app.github.io/genba-break-switch/terms.html) | 公開到達確認 PASS |
| Privacy | [privacy.html](https://daimon-app.github.io/genba-break-switch/privacy.html) | 公開到達確認 PASS |
| 販売案内 | [commerce.html](https://daimon-app.github.io/genba-break-switch/commerce.html) | 公開到達確認 PASS |
| サポート | [support.html](https://daimon-app.github.io/genba-break-switch/support.html) | 公開到達確認 PASS |

LPは「疲れる前に、戻る。」を核にし、無料公開ベータ、標準アラーム非代替、安全・体調判断非代替を明示する。購入・決済・料金表示は設けていない。

## Legal

無料公開ベータ向けに、利用規約、販売案内、サポート注意、公開フィードバックの注意を施工した。現時点の販売案内は、**有償取引が存在しないことを説明するページ**であり、特定商取引法に基づく表記ではない。有償販売は、販売者情報、商品、価格、支払、提供時期、返金・解約、正式問い合わせ先、決済前確認を実情報で確定し、GitHub Pages外の適切な商取引基盤に移行してから開始する。

## Privacy

現行PWA本体は、休憩履歴、音設定、次の一手をブラウザのローカルストレージに保存し、現行コードにアカウント、広告SDK、行動分析SDK、位置情報、連絡先、決済はない。GitHub Pagesのアクセス時にGitHubがIPアドレスを記録する点と、公開フィードバックのGitHub Issuesは公開され得る点をPrivacyページに明示した。

## SNS

SNS用のプロフィール文案、X、Instagram／Threads、LinkedIn、15秒動画台本、投稿前チェック、禁止表現を[ SNSローンチキット](2026-08-19_sns_launch_kit.md)として保存済みである。**SNS投稿、広告出稿、DM、事例掲載は一切実行していない。** 投稿者、日時、素材、投稿文は本人承認が必要である。

## Technical Fix Required

| 状態 | 内容 | 対応 |
| --- | --- | --- |
| RESOLVED | 初回GitHub Pages 404 | Pagesビルド完了後に再確認し解消。 |
| RESOLVED | 既存Service Workerが旧HTMLを表示 | `kirikae-v10`、HTML network-first、バージョン付きPWA導線に修正し公開再QA PASS。 |
| RESOLVED | 未参照の旧 `icons/service-worker.js` | 参照確認後に削除。 |
| TECH_FIX_REQUIRED（低） | 音源・アイコンの重複資産 | 販売文言に直結しない。参照確認後に別施工単位で整理。 |
| LIMITATION | iOS／Android実機QA未実施 | 実機でインストール、復帰、Wake Lock、低電力状態を確認する。 |

## Final Audit

最終監査は[2026-08-19_kirikae_switch_sales_audit.md](../audits/2026-08-19_kirikae_switch_sales_audit.md)に全文を保存した。静的QA、ローカルブラウザQA、公開GitHub Pages QA、販売文言、法務・Privacy・サポート・商取引境界を照合している。Claude、Gemini、Codexの独立した調査・監査・施工結果は本施工時点で存在しないため、作成・引用していない。

## Decision

**CONDITIONAL**。無料公開ベータの技術公開は、本人承認後に進められる。現行GitHub Pages上での有償販売は開始しない。

## SALES READY

| 販売状態 | 判定 |
| --- | --- |
| 無料公開ベータ | **CONDITIONAL SALES READY** — 本人承認後にGO。実機QAは強く推奨。 |
| 有償販売 | **NOT SALES READY / NO GO** — 商取引基盤、販売者情報、価格、返金、決済、正式窓口、実機QAが未了。 |

## 本人承認 Required

1. 正式な商品名を「切り替えスイッチ」として確定するか。
2. 無料公開ベータを外部へ告知・開始するか。
3. SNSローンチキットのうち使用する投稿文、投稿者、日時、素材を承認するか。
4. 可能であれば、Android ChromeとiPhone Safariの実機QAを誰がいつ実施するか。
5. 将来有償化する場合、販売者名・住所・連絡先、商品、税込価格、返金・解約、決済・販売基盤を確定するか。

## Next Action

本人が無料公開ベータの開始を承認する場合、承認済みのSNS文案とURLだけを使って公開告知を行う。実機QAが可能なら、Android ChromeとiPhone Safariでホーム画面追加、画面復帰、音、表示、端末標準アラーム併用を確認してQA結果を追記する。有償販売を検討する場合は、GitHub Pagesとは別に商取引可能な販売基盤を選定し、販売者情報・決済・返金・プライバシー・正式窓口を確定したうえで、新規の販売施工として再開する。

## 正本保存・最終引継ぎ

| 項目 | 内容 |
| --- | --- |
| Spec Saved | Yes |
| GitHub Source-of-Truth | [`daimon-app/genba-break-switch`](https://github.com/daimon-app/genba-break-switch) |
| Spec Path | [`docs/specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md`](../specs/2026-08-19_M05_SALES_READY_EXECUTION_SPEC.md) |
| Audit Path | [`docs/audits/2026-08-19_kirikae_switch_sales_audit.md`](../audits/2026-08-19_kirikae_switch_sales_audit.md) |
| QA Path | [`docs/qa/2026-08-19_sales_ready_qa_result.md`](../qa/2026-08-19_sales_ready_qa_result.md) |
| Decision Log | [`docs/decisions/2026-08-19_sales_execution_decision_log.md`](../decisions/2026-08-19_sales_execution_decision_log.md) |
| Branch | `main` |
| Commit | 本報告書のcommit後に、`MASTER.md`へ最終HEADを追記する。 |
| Push | 本報告書のcommit後に、`origin/main`との一致を確認する。 |
| Next Action | 上記「本人承認 Required」を確定する。 |
