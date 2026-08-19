# 切り替えスイッチ — GitHub Pages公開・販売制約調査

> **調査日:** 2026-08-19 JST
>
> **対象公開先:** `https://daimon-app.github.io/genba-break-switch/`

## 結論

現行のGitHub Pagesは、**無償PWAの公開、情報ページ、オープンなフィードバック導線**には使用できる。一方で、GitHub公式ドキュメントはGitHub Pagesを、オンラインビジネス、EC、商取引の促進を主目的とするサイト、商用SaaSを運営する無料ホスティングとして使うことを意図・許可していないと明記している。[1]

したがって、現行のGitHub Pagesで**有償購入受付、決済フォーム、クレジットカード情報の取扱い、商取引を主目的とするLP**を開始してはならない。将来の有償販売は、適切な決済・事業者表示・プライバシー対応を提供する独自ドメインまたは承認済みのコマース基盤に移す必要がある。GitHub Pagesは価格・購入誘導のない無料公開ベータの案内とPWA本体に限定する。

## 確認した公式事項

| 論点 | 公式資料 | 本施工への判断 |
| --- | --- | --- |
| 静的公開 | GitHub Pagesはリポジトリ内のHTML/CSS/JavaScriptから静的サイトを公開できる。[2] | 現行の単一HTML PWAおよび無料ベータ案内の公開に適合する。 |
| 商取引の制限 | GitHub Pagesは、EC、商取引の促進を主目的とするサイト、商用SaaSを運営する無料ホスティングとしての利用を意図・許可していない。[1] | 販売LPと決済を現行Pagesに設置しない。 |
| 機微情報 | GitHub Pagesはパスワードやクレジットカード番号送信等の機微取引に使うべきではない。[1] | 問い合わせフォームや決済フォームを直接設置しない。 |
| アクセスログ | Pagesの訪問時、GitHubはセキュリティ目的で訪問者のIPアドレスを記録・保存する。[2] | プライバシーポリシーにGitHub Pages利用とIPログの可能性を明記する。 |

## SALES READYへの影響

| 販売状態 | 現行GitHub Pagesで可能か | 条件 |
| --- | --- | --- |
| 無料公開ベータ | 可 | 価格・決済・商取引誘導を置かず、制約・プライバシー・問い合わせ注意を表示する。 |
| 有償デジタル商品の販売 | 不可 | 商取引可能なホスティング／コマース基盤、販売者情報、特商法表記、決済、返金条件、最終確認画面を整備後に移行する。 |
| クレジットカード／パスワード入力フォーム | 不可 | GitHub Pagesに入力フォームを置かない。 |
| 公開フィードバック | 条件付き可 | GitHub Issues等の外部公開窓口を案内し、個人情報・機密情報を書き込まないよう注意する。 |

## 参照

[1] [GitHub Docs「GitHub Pages limits」](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)

[2] [GitHub Docs「What is GitHub Pages?」](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

[3] [GitHub General Privacy Statement（2026-04-27発効）](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
