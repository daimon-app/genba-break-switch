# 切り替えスイッチ — 調査メモ

調査日: 2026-08-19 JST

## 実装正本

- GitHub正本は `https://github.com/daimon-app/genba-break-switch`、既定ブランチは `main`。
- 最新コミットは `daaf6170220880c36da612935ba9c2dce11089ab`（2026-06-16 19:43:50 JST、`Add files via upload`）。
- 現行実装は単一HTMLのPWAで、休憩・マイクロリセット・瞑想タイマー・自然音・一時停止・画面復帰時の残時間再計算・画面消灯防止（対応端末のみ）・端末ローカルの記録を含む。
- Notification API、Push API、Push購読、Service Workerの `showNotification`、バックグラウンド同期、OSアラーム連携は実装されていない。

## 競合の確認結果

| 類型 | 代表例 | 確認した事実 | 切り替えスイッチへの示唆 |
| --- | --- | --- | --- |
| 大規模な瞑想・睡眠アプリ | Insight Timer | App Store日本ページでは、iPhone/iPad/Apple Watch対応、サイズ246.9MB、年間6,800円または月額1,150円のサブスクリプションが表示されている。 | 大量コンテンツ・ガイド瞑想・睡眠ライブラリで競争しない。現場で迷わせない「数秒で開始→次の一手へ戻る」に絞る。 |
| 一般的な作業・休憩タイマー | 断続集中タイマー | App Store日本ページでは、ポモドーロやタバタのような作業・休憩インターバルの繰り返しを訴求し、カテゴリはビジネス、無料。 | 一般タイマーは無料の強い代替。対象を事務・学習ではなく、現場の短い再始動行動とする。 |
| OS標準タイマー／アラーム | iOS・Android標準アプリ | 端末の標準タイマーはOSレベルの通知・アラームという役割を持つ。現行PWAはこの機能を代替しない。 | 終了を確実に知る必要がある休憩は、標準タイマー／アラーム併用を明示する。 |

## プラットフォーム確認結果

| 論点 | 公式仕様・現行実装 | 販売上の扱い |
| --- | --- | --- |
| PWAインストール | Chromeのインストール促進はHTTPS、manifest、192/512pxアイコン、対応display等を条件とし、利用者の一定の操作・閲覧時間も必要。現行manifestは主要な構成項目を持つが、配信HTTPSと実地確認は未了。 | 「アプリのようにホーム画面へ追加可能」とし、端末・ブラウザ・配信条件で表示が異なる旨を明記する。 |
| Android | 現行コードはWeb標準PWA。端末標準アラームやOS通知を使う実装はない。 | 「AndroidでOSアラームのように確実に鳴る」は不可。画面を表示したままの利用、または標準タイマー併用を案内する。 |
| iOS | AppleはiOS/iPadOS 16.4以降、ホーム画面WebアプリへのWeb Pushをサポートするが、許可・Push購読・サーバー・Service Workerによる通知処理が必要。現行実装にはない。 | 「iPhoneでプッシュ通知・終了通知が来る」と約束しない。iPhoneではSafariからホーム画面追加の手順を案内する。 |
| 画面消灯防止 | Wake LockはHTTPS上の表示中ドキュメントで使え、バッテリー節約設定、低電力、非表示化等で拒否または解放され得る。現行コードは対応時に要求し、復帰時に再要求する。 | 「画面を消さない」は不可。「対応端末では画面消灯を抑制するよう試みます。端末設定等で解除される場合があります」とする。 |
| 画面外の通知 | Notifications APIは権限が必要。モバイルではService Workerの `showNotification()` を使うべきだが、現行にはない。 | 「アプリ内の終了音」「表示中のカウント表示」のみ。OS通知、バックグラウンド終了通知、確実なアラームは約束しない。 |
| オフライン | Service Workerはアプリ本体・manifest・音源・アイコンをキャッシュするため、初回ロード／更新成功後の基本オフライン利用を意図している。 | 「初回読み込み後は基本機能をオフラインで使える設計」と限定表現にする。インストール・更新完了前、端末のストレージ削除時などは保証しない。 |

## 安全・表現

- 厚生労働省は2026年の職場熱中症対策で、暑さ指数の把握・活用と熱中症予防対策を促進している。休憩は安全管理の一部であり、本製品単独での熱中症予防、安全確保、労務コンプライアンスを保証してはならない。
- 「暑い日モード」の時間設定は固定の行動提案であり、WBGT、作業強度、服装、体調、責任者の指示を反映する安全判断機能ではない。販売ページ・アプリ内に免責と標準的な注意表示を設ける。

## 参照

1. Apple Developer, "Sending web push notifications in web apps and browsers" — https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers
2. MDN, "Screen Wake Lock API" — https://developer.mozilla.org/en-US/docs/Web/API/Screen_Wake_Lock_API
3. MDN, "Using the Notifications API" — https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API/Using_the_Notifications_API
4. web.dev, "What does it take to be installable?" — https://web.dev/articles/install-criteria
5. Apple, "Turn a website into an app in Safari on iPhone" — https://support.apple.com/guide/iphone/open-as-web-app-iphea86e5236/ios
6. App Store, "Insight Timer - 瞑想アプリ" — https://apps.apple.com/jp/app/insight-timer-%E7%9E%91%E6%83%B3%E3%82%A2%E3%83%97%E3%83%AA/id337472899
7. App Store, "断続集中タイマー" — https://apps.apple.com/jp/app/%E6%96%AD%E7%B6%9A%E9%9B%86%E4%B8%AD%E3%82%BF%E3%82%A4%E3%83%9E%E3%83%BC/id1344040001
8. 厚生労働省, "STOP！熱中症 クールワークキャンペーン" — https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000116133.html
9. 厚生労働省, "働く人の今すぐ使える熱中症ガイド" — https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000116133_00001.html
