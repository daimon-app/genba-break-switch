# GITHUB SOURCE-OF-TRUTH — MANDATORY RULE

> **正本区分:** 受領施工仕様書（原文保存）
>
> **受領日:** 2026-08-19 JST
>
> **対象リポジトリ:** `daimon-app/genba-break-switch`
>
> **対象ブランチ:** `main`

## 受領仕様書（原文）

```text
GITHUB SOURCE-OF-TRUTH — MANDATORY RULE

この施工に関する情報をChat内だけに残してはならない。

作業開始時に対象RepositoryのGitHub正本を確認し、施工開始から販売READYまでの証拠をGitHubへ継続保存すること。

必須保存対象

以下を正本化する。

- 今回受領した設計施工仕様指示書
- 商品仕様
- SALES READY要件
- 実装仕様
- 修正指示
- AIへの施工指示
- 市場・競合調査結果
- Manus調査・施工結果
- Claudeレビュー・監査結果
- Gemini調査結果
- Codex施工結果
- QA仕様
- QA結果
- FAIL内容
- 修正履歴
- 再QA結果
- 販売監査全文
- GO / CONDITIONAL / NO GO判定
- Decision Log
- 本人承認待ち
- 販売者情報待ち
- 現在Stage
- 次の一手

推奨正本構造

既存Repository構造を最優先する。

適切な保存場所が存在しない場合のみ、以下を参考に整理する。

"docs/specs/"
設計・施工仕様書

"docs/audits/"
監査全文

"docs/research/"
市場・競合調査

"docs/qa/"
QA仕様・結果

"docs/decisions/"
Decision Log

"docs/sales/"
販売仕様・SALES READY資料

既存の "MASTER.md" / "AGENTS.md" / "ZERO_SPEC.md" 等がある場合は、そのRepositoryの既存正本規則を優先する。

MASTER更新

施工状態が変わるたびに、正本上で最低限以下を復元可能にする。

- Product
- Current Stage
- Repository
- Branch
- HEAD
- Latest QA
- Latest Audit
- Blockers
- Approval Required
- Next Action

指示書保存

今回受領した施工仕様書についても、単なるChat命令として消費せず、対象Repositoryへ保存する。

後日、新しいChat・別AI・別PCから作業を再開しても、

GitHubだけを読めば「何を作っているか・なぜそうしたか・現在どこまで終わったか・次に何をするか」が復元できる状態

を維持する。

AI結果

各AIの結果は要約だけでなく、重要な監査・調査については可能な限り全文または十分な証拠を保存する。

AI回答を事実として無条件採用しない。

実コード・実画面・一次情報・QAと照合した結果をDecision Logへ残す。

Git運用

安全にcommit可能な状態なら、正本更新を施工単位でcommitする。

既存未コミット作業を勝手に巻き込まない。

禁止：

- "git add ." による無関係変更混入
- 他施工の勝手なdiscard
- "reset --hard"
- force push
- unrelated変更のcommit

既存作業との安全な分離が不可能な場合は、正本ファイルを作成した上で "GIT_COMMIT_HOLD" とし、理由を報告する。

完了条件

販売READYだけでは完了としない。

以下すべてを満たして完了：

1. 商品施工完了
2. QA完了
3. 最終監査完了
4. GitHub正本更新
5. 施工仕様書保存
6. Decision Log更新
7. HEAD / branch / commit記録
8. 次工程記録

最終報告には必ず、

"Spec Saved:"
"GitHub Source-of-Truth:"
"Spec Path:"
"Audit Path:"
"QA Path:"
"Decision Log:"
"Branch:"
"Commit:"
"Push:"
"Next Action:"

を含めること。
追加です、さっきの設計施工仕様指示書通り続けて
```

## 正本運用の適用方針

本リポジトリには、受領時点で既存の `MASTER.md`、`AGENTS.md`、`ZERO_SPEC.md`、`README.md`、`LICENSE` が存在しなかった。そのため、本仕様書の推奨構造を採用し、トップレベルの `MASTER.md` を復元起点とする。既存の配布PWAコードおよびGitHub Pages設定は、販売施工中もその正本性を保持する。

**証拠基準**は次の通りとする。市場・OS・法令等の外部事実は一次情報を優先し、AI出力は証拠そのものとは扱わない。実装に関する記載は対象コミットのコードとQAで照合する。確認できない第三者AIの結果は「未実施」と明示し、作成しない。

## 更新履歴

| 日付 | 内容 | 担当 |
| --- | --- | --- |
| 2026-08-19 | 初回受領・原文正本化・運用方針確立 | Manus AI |
