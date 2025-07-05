DEFAULT_URL = "https://3geeggzw92.execute-api.ap-northeast-1.amazonaws.com/default/"
COLUMNS = ["UID", "APIキー", "処理年度", "メモ", "企業番号", "企業名", "所在地", "連絡先", "決算期", "詳細リクエスト", "判定結果", "不正会計確率", "入力単位", "現金及び預金", "受取手形", "売掛金", "有価証券", "商品及び製品", "短期貸付金", "前渡金", "未収入金", "前払費用", "仮払金", "貸倒引当金_流動資産", "流動資産小計", "その他流動資産", "流動資産", "建物及び構築物", "機械及び装置", "工具・器具及び備品", "リース資産", "土地", "建設仮勘定", "減価償却累計額_有形資産", "有形固定資産小計", "その他有形固定資産", "有形固定資産", "ソフトウエア", "のれん", "無形固定資産小計", "その他無形固定資産", "無形固定資産", "関係会社株式", "投資有価証券", "出資金", "長期貸付金", "長期前払費用", "繰延税金資産", "減価償却累計額_投資等資産", "貸倒引当金_投資等資産", "投資等資産小計", "その他投資等資産", "投資等資産", "固定資産", "創業費・開業費", "開発費", "繰延資産小計", "その他繰延資産", "繰延資産", "資産合計", "支払手形", "買掛金", "短期借入金", "未払金", "未払費用", "前受金", "未成工事受入金", "前受収益", "リース債務_流動負債", "未払法人税等", "賞与引当金", "流動負債小計", "その他流動負債", "流動負債", "社債", "長期借入金", "リース債務_固定負債", "退職給付引当金", "繰延税金負債", "固定負債小計", "その他固定負債", "固定負債", "特別法上の準備金", "負債合計", "資本金", "資本準備金", "その他資本剰余金", "資本剰余金", "利益準備金", "任意積立金", "繰越利益剰余金", "その他利益剰余金", "利益剰余金", "自己株式", "その他有価証券評価差額金", "為替換算調整勘定", "その他評価損益", "その他包括利益累計額", "新株予約権", "少数株主持分", "純資産合計", "負債及び純資産合計", "売上高", "期首材料棚卸高", "材料仕入高", "期末材料棚卸高", "材料費", "従業員給与_原価", "従業員賞与_原価", "従業員退職金_原価", "法定福利費_原価", "福利厚生費_原価", "労務費小計", "その他の労務費", "労務費", "外注加工費", "水道光熱費_原価", "消耗工具器具備品費_原価", "租税公課_原価", "減価償却費_原価", "修繕費_原価", "保険料_原価", "賃借料_原価", "研究開発費_原価", "経費小計", "その他の経費_原価", "経費", "売上原価小計", "期首仕掛品棚卸高", "期末仕掛品棚卸高", "他勘定振替高", "売上原価", "売上総利益", "販売手数料", "荷造運送費", "車両燃料費", "広告宣伝費", "保管費", "人件費", "役員報酬", "役員賞与", "役員退職金", "従業員給与_販管費", "従業員賞与_販管費", "従業員退職金_販管費", "法定福利費_販管費", "福利厚生費_販管費", "接待交際費", "旅費交通費", "通信費", "水道光熱費_販管費", "事務用消耗品費", "消耗工具器具備品_販管費", "租税公課_販管費", "図書費", "減価償却費_販管費", "修繕費_販管費", "保険料_販管費", "賃借料_販管費", "寄付金", "研究開発費_販管費", "販売費及び一般管理費小計", "その他の経費_販管費", "販売費及び一般管理費", "営業利益", "受取利息及び受取配当金", "その他の営業外収入", "営業外収益", "支払利息及び手形譲渡損", "その他の営業外費用", "営業外費用", "経常損益", "経常利益固定資産売却益", "投資有価証券売却益", "前期修正損益", "その他_特別利益", "特別利益", "固定資産売却損", "減損損失_PL", "災害による損失", "その他特別損失", "特別損失", "特別損益", "税引前当期純利益", "法人税等", "法人税等調整額", "その他の調整額", "税金等控除額", "当期純利益", "減価償却費", "減損損失_CF", "諸引当金増減額", "非資金の費用項目", "受取手形増減額", "売掛金増減額", "棚卸資産増減額", "その他資産増減額", "支払手形増減額", "買掛金増減額", "前受金増減額", "その他流動負債増減額", "その他固定負債増減額_営業CF", "役員賞与支払額", "回収及び支払サイト", "営業キャッシュフロー", "有価証券増減額", "土地増減額", "減価償却資産増減額", "無形固定資産増減額", "投資有価証券増減額", "長期貸付金増減額", "その他固定資産増減額_投資CF", "繰延資産増減額", "投資キャッシュフロー", "フリーキャッシュフロー（Ⅰ＋Ⅱ）", "短期借入金増減額", "長期借入金増減額", "資本金増減額", "配当金支払額", "財務キャッシュフロー", "キャッシュの増加・減少額（Ⅰ＋Ⅱ＋Ⅲ）", "キャッシュの期首残高", "キャッシュの期末残高"]
INDEX = ["メモ", "企業番号", "企業名", "所在地", "連絡先", "決算期", "入力単位", "処理年度"]
HIDDEN = ["UID", "APIキー"]
DROP = ["詳細リクエスト", "判定結果", "不正会計確率"] + ["役員報酬", "役員退職金", "従業員給与_販管費", "従業員賞与_販管費", "従業員退職金_販管費", "法定福利費_販管費"]
BS = ["現金及び預金", "受取手形", "売掛金", "有価証券", "商品及び製品", "短期貸付金", "前渡金", "未収入金", "前払費用", "仮払金", "貸倒引当金_流動資産", "流動資産小計", "その他流動資産", "流動資産", "建物及び構築物", "機械及び装置", "工具・器具及び備品", "リース資産", "土地", "建設仮勘定", "減価償却累計額_有形資産", "有形固定資産小計", "その他有形固定資産", "有形固定資産", "ソフトウエア", "のれん", "無形固定資産小計", "その他無形固定資産", "無形固定資産", "関係会社株式", "投資有価証券", "出資金", "長期貸付金", "長期前払費用", "繰延税金資産", "減価償却累計額_投資等資産", "貸倒引当金_投資等資産", "投資等資産小計", "その他投資等資産", "投資等資産", "固定資産", "創業費・開業費", "開発費", "繰延資産小計", "その他繰延資産", "繰延資産", "資産合計", "支払手形", "買掛金", "短期借入金", "未払金", "未払費用", "前受金", "未成工事受入金", "前受収益", "リース債務_流動負債", "未払法人税等", "賞与引当金", "流動負債小計", "その他流動負債", "流動負債", "社債", "長期借入金", "リース債務_固定負債", "退職給付引当金", "繰延税金負債", "固定負債小計", "その他固定負債", "固定負債", "特別法上の準備金", "負債合計", "資本金", "資本準備金", "その他資本剰余金", "資本剰余金", "利益準備金", "任意積立金", "繰越利益剰余金", "その他利益剰余金", "利益剰余金", "自己株式", "その他有価証券評価差額金", "為替換算調整勘定", "その他評価損益", "その他包括利益累計額", "新株予約権", "少数株主持分", "純資産合計", "負債及び純資産合計"]
ASSETS = ["現金及び預金", "受取手形", "売掛金", "有価証券", "商品及び製品", "短期貸付金", "前渡金", "未収入金", "前払費用", "仮払金", "貸倒引当金_流動資産", "流動資産小計", "その他流動資産", "流動資産", "建物及び構築物", "機械及び装置", "工具・器具及び備品", "リース資産", "土地", "建設仮勘定", "減価償却累計額_有形資産", "有形固定資産小計", "その他有形固定資産", "有形固定資産", "ソフトウエア", "のれん", "無形固定資産小計", "その他無形固定資産", "無形固定資産", "関係会社株式", "投資有価証券", "出資金", "長期貸付金", "長期前払費用", "繰延税金資産", "減価償却累計額_投資等資産", "貸倒引当金_投資等資産", "投資等資産小計", "その他投資等資産", "投資等資産", "固定資産", "創業費・開業費", "開発費", "繰延資産小計", "その他繰延資産", "繰延資産", "資産合計"]
LIABILITITES = ["支払手形", "買掛金", "短期借入金", "未払金", "未払費用", "前受金", "未成工事受入金", "前受収益", "リース債務_流動負債", "未払法人税等", "賞与引当金", "流動負債小計", "その他流動負債", "流動負債", "社債", "長期借入金", "リース債務_固定負債", "退職給付引当金", "繰延税金負債", "固定負債小計", "その他固定負債", "固定負債", "特別法上の準備金", "負債合計"]
NET_ASSETS = ["資本金", "資本準備金", "その他資本剰余金", "資本剰余金", "利益準備金", "任意積立金", "繰越利益剰余金", "その他利益剰余金", "利益剰余金", "自己株式", "その他有価証券評価差額金", "為替換算調整勘定", "その他評価損益", "その他包括利益累計額", "新株予約権", "少数株主持分", "純資産合計", "負債及び純資産合計"]
PL = ["売上高", "期首材料棚卸高", "材料仕入高", "期末材料棚卸高", "材料費", "従業員給与_原価", "従業員賞与_原価", "従業員退職金_原価", "法定福利費_原価", "福利厚生費_原価", "労務費小計", "その他の労務費", "労務費", "外注加工費", "水道光熱費_原価", "消耗工具器具備品費_原価", "租税公課_原価", "減価償却費_原価", "修繕費_原価", "保険料_原価", "賃借料_原価", "研究開発費_原価", "経費小計", "その他の経費_原価", "経費", "売上原価小計", "期首仕掛品棚卸高", "期末仕掛品棚卸高", "他勘定振替高", "売上原価", "売上総利益", "販売手数料", "荷造運送費", "車両燃料費", "広告宣伝費", "保管費", "人件費", "役員報酬", "役員賞与", "役員退職金", "従業員給与_販管費", "従業員賞与_販管費", "従業員退職金_販管費", "法定福利費_販管費", "福利厚生費_販管費", "接待交際費", "旅費交通費", "通信費", "水道光熱費_販管費", "事務用消耗品費", "消耗工具器具備品_販管費", "租税公課_販管費", "図書費", "減価償却費_販管費", "修繕費_販管費", "保険料_販管費", "賃借料_販管費", "寄付金", "研究開発費_販管費", "販売費及び一般管理費小計", "その他の経費_販管費", "販売費及び一般管理費", "営業利益", "受取利息及び受取配当金", "その他の営業外収入", "営業外収益", "支払利息及び手形譲渡損", "その他の営業外費用", "営業外費用", "経常損益", "経常利益固定資産売却益", "投資有価証券売却益", "前期修正損益", "その他_特別利益", "特別利益", "固定資産売却損", "減損損失_PL", "災害による損失", "その他特別損失", "特別損失", "特別損益", "税引前当期純利益", "法人税等", "法人税等調整額", "その他の調整額", "税金等控除額", "当期純利益"]
PL_ABST = ["売上高", "売上原価", "売上総利益", "販売費及び一般管理費", "営業利益", "受取利息及び受取配当金", "その他の営業外収入", "営業外収益", "支払利息及び手形譲渡損", "その他の営業外費用", "営業外費用", "経常損益", "経常利益固定資産売却益", "投資有価証券売却益", "前期修正損益", "その他_特別利益", "特別利益", "固定資産売却損", "減損損失_PL", "災害による損失", "その他特別損失", "特別損失", "特別損益", "税引前当期純利益", "法人税等", "法人税等調整額", "その他の調整額", "税金等控除額", "当期純利益"]
COST_DETAILS = ["期首材料棚卸高", "材料仕入高", "期末材料棚卸高", "材料費", "従業員給与_原価", "従業員賞与_原価", "従業員退職金_原価", "法定福利費_原価", "福利厚生費_原価", "労務費小計", "その他の労務費", "労務費", "外注加工費", "水道光熱費_原価", "消耗工具器具備品費_原価", "租税公課_原価", "減価償却費_原価", "修繕費_原価", "保険料_原価", "賃借料_原価", "研究開発費_原価", "経費小計", "その他の経費_原価", "経費", "売上原価小計", "期首仕掛品棚卸高", "期末仕掛品棚卸高", "他勘定振替高"]
SGA_DETAILS = ["販売手数料", "荷造運送費", "車両燃料費", "広告宣伝費", "保管費", "人件費", "役員報酬", "役員賞与", "役員退職金", "従業員給与_販管費", "従業員賞与_販管費", "従業員退職金_販管費", "法定福利費_販管費", "福利厚生費_販管費", "接待交際費", "旅費交通費", "通信費", "水道光熱費_販管費", "事務用消耗品費", "消耗工具器具備品_販管費", "租税公課_販管費", "図書費", "減価償却費_販管費", "修繕費_販管費", "保険料_販管費", "賃借料_販管費", "寄付金", "研究開発費_販管費", "販売費及び一般管理費小計", "その他の経費_販管費"]
SGA_DROP = ["役員報酬", "役員退職金", "従業員給与_販管費", "従業員賞与_販管費", "従業員退職金_販管費", "法定福利費_販管費"]
CF = ["減価償却費", "減損損失_CF", "諸引当金増減額", "非資金の費用項目", "受取手形増減額", "売掛金増減額", "棚卸資産増減額", "その他資産増減額", "支払手形増減額", "買掛金増減額", "前受金増減額", "その他流動負債増減額", "その他固定負債増減額_営業CF", "役員賞与支払額", "回収及び支払サイト", "営業キャッシュフロー", "有価証券増減額", "土地増減額", "減価償却資産増減額", "無形固定資産増減額", "投資有価証券増減額", "長期貸付金増減額", "その他固定資産増減額_投資CF", "繰延資産増減額", "投資キャッシュフロー", "フリーキャッシュフロー（Ⅰ＋Ⅱ）", "短期借入金増減額", "長期借入金増減額", "資本金増減額", "配当金支払額", "財務キャッシュフロー", "キャッシュの増加・減少額（Ⅰ＋Ⅱ＋Ⅲ）", "キャッシュの期首残高", "キャッシュの期末残高"]
ITEMS = {
    "versions": [
        {
            "items": [
                {
                    "en": "CashAndDeposits",
                    "ja": "現金及び預金"
                },
                {
                    "en": "NotesReceivableTrade",
                    "ja": "受取手形"
                },
                {
                    "en": "AccountsReceivableTrade",
                    "ja": "売掛金"
                },
                {
                    "en": "ShortTermInvestmentSecurities",
                    "ja": "有価証券"
                },
                {
                    "en": "MerchandiseAndFinishedGoods",
                    "ja": "商品及び製品"
                },
                {
                    "en": "ShortTermLoansReceivable",
                    "ja": "短期貸付金"
                },
                {
                    "en": "AdvancePaymentsTrade",
                    "ja": "前渡金"
                },
                {
                    "en": "AccountsReceivableOther",
                    "ja": "未収入金"
                },
                {
                    "en": "PrepaidExpenses",
                    "ja": "前払費用"
                },
                {
                    "en": "SuspensePayments",
                    "ja": "仮払金"
                },
                {
                    "en": "AllowanceForDoubtfulAccountsCA",
                    "ja": "貸倒引当金_流動資産"
                },
                {
                    "en": "CurrentAssetsSubTotal",
                    "ja": "流動資産小計"
                },
                {
                    "en": "OtherCA",
                    "ja": "その他流動資産"
                },
                {
                    "en": "CurrentAssets",
                    "ja": "流動資産"
                },
                {
                    "en": "BuildingsAndStructures",
                    "ja": "建物及び構築物"
                },
                {
                    "en": "MachineryAndEquipment",
                    "ja": "機械及び装置"
                },
                {
                    "en": "ToolsFurnitureAndFixtures",
                    "ja": "工具・器具及び備品"
                },
                {
                    "en": "LeaseAssetsPPE",
                    "ja": "リース資産"
                },
                {
                    "en": "Land",
                    "ja": "土地"
                },
                {
                    "en": "ConstructionInProgress",
                    "ja": "建設仮勘定"
                },
                {
                    "en": "AccumulatedDepreciationPPE",
                    "ja": "減価償却累計額_有形資産"
                },
                {
                    "en": "PropertyPlantAndEquipmentSubTotal",
                    "ja": "有形固定資産小計"
                },
                {
                    "en": "OtherPPE",
                    "ja": "その他有形固定資産"
                },
                {
                    "en": "PropertyPlantAndEquipment",
                    "ja": "有形固定資産"
                },
                {
                    "en": "Software",
                    "ja": "ソフトウエア"
                },
                {
                    "en": "Goodwill",
                    "ja": "のれん"
                },
                {
                    "en": "IntangibleAssetsSubTotal",
                    "ja": "無形固定資産小計"
                },
                {
                    "en": "OtherIA",
                    "ja": "その他無形固定資産"
                },
                {
                    "en": "IntangibleAssets",
                    "ja": "無形固定資産"
                },
                {
                    "en": "StocksOfSubsidiariesAndAffiliates",
                    "ja": "関係会社株式"
                },
                {
                    "en": "InvestmentSecurities",
                    "ja": "投資有価証券"
                },
                {
                    "en": "InvestmentsInCapital",
                    "ja": "出資金"
                },
                {
                    "en": "LongTermLoansReceivable",
                    "ja": "長期貸付金"
                },
                {
                    "en": "LongTermPrepaidExpenses",
                    "ja": "長期前払費用"
                },
                {
                    "en": "DeferredTaxAssets",
                    "ja": "繰延税金資産"
                },
                {
                    "en": "AccumulatedDepreciationIOA",
                    "ja": "減価償却累計額_投資等資産"
                },
                {
                    "en": "AllowanceForDoubtfulAccountsIOA",
                    "ja": "貸倒引当金_投資等資産"
                },
                {
                    "en": "InvestmentsAndOtherAssetsSubTotal",
                    "ja": "投資等資産小計"
                },
                {
                    "en": "OtherIOA",
                    "ja": "その他投資等資産"
                },
                {
                    "en": "InvestmentsAndOtherAssets",
                    "ja": "投資等資産"
                },
                {
                    "en": "NoncurrentAssets",
                    "ja": "固定資産"
                },
                {
                    "en": "DeferredOrganizationAndBusinessCommencementExpensesDA",
                    "ja": "創業費・開業費"
                },
                {
                    "en": "DevelopmentExpensesDA",
                    "ja": "開発費"
                },
                {
                    "en": "DeferredAssetsSubTotal",
                    "ja": "繰延資産小計"
                },
                {
                    "en": "OtherDA",
                    "ja": "その他繰延資産"
                },
                {
                    "en": "DeferredAssets",
                    "ja": "繰延資産"
                },
                {
                    "en": "Assets",
                    "ja": "資産合計"
                },
                {
                    "en": "NotesPayableTrade",
                    "ja": "支払手形"
                },
                {
                    "en": "AccountsPayableTrade",
                    "ja": "買掛金"
                },
                {
                    "en": "ShortTermLoansPayable",
                    "ja": "短期借入金"
                },
                {
                    "en": "AccountsPayableOther",
                    "ja": "未払金"
                },
                {
                    "en": "AccruedExpenses",
                    "ja": "未払費用"
                },
                {
                    "en": "AdvancesReceived",
                    "ja": "前受金"
                },
                {
                    "en": "AdvancesReceivedOnUncompletedContracts",
                    "ja": "未成工事受入金"
                },
                {
                    "en": "UnearnedRevenue",
                    "ja": "前受収益"
                },
                {
                    "en": "LeaseObligationsCL",
                    "ja": "リース債務_流動負債"
                },
                {
                    "en": "IncomeTaxesPayable",
                    "ja": "未払法人税等"
                },
                {
                    "en": "ProvisionForBonuses",
                    "ja": "賞与引当金"
                },
                {
                    "en": "CurrentLiabilitiesSubTotal",
                    "ja": "流動負債小計"
                },
                {
                    "en": "OtherCL",
                    "ja": "その他流動負債"
                },
                {
                    "en": "CurrentLiabilities",
                    "ja": "流動負債"
                },
                {
                    "en": "BondsPayable",
                    "ja": "社債"
                },
                {
                    "en": "LongTermLoansPayable",
                    "ja": "長期借入金"
                },
                {
                    "en": "LeaseObligationsNCL",
                    "ja": "リース債務_固定負債"
                },
                {
                    "en": "ProvisionForRetirementBenefits",
                    "ja": "退職給付引当金"
                },
                {
                    "en": "DeferredTaxLiabilities",
                    "ja": "繰延税金負債"
                },
                {
                    "en": "NoncurrentLiabilitiesSubTotal",
                    "ja": "固定負債小計"
                },
                {
                    "en": "OtherNCL",
                    "ja": "その他固定負債"
                },
                {
                    "en": "NoncurrentLiabilities",
                    "ja": "固定負債"
                },
                {
                    "en": "ReservesUnderTheSpecialLaws",
                    "ja": "特別法上の準備金"
                },
                {
                    "en": "Liabilities",
                    "ja": "負債合計"
                },
                {
                    "en": "CapitalStock",
                    "ja": "資本金"
                },
                {
                    "en": "LegalCapitalSurplus",
                    "ja": "資本準備金"
                },
                {
                    "en": "OtherCapitalSurplus",
                    "ja": "その他資本剰余金"
                },
                {
                    "en": "CapitalSurplus",
                    "ja": "資本剰余金"
                },
                {
                    "en": "LegalRetainedEarnings",
                    "ja": "利益準備金"
                },
                {
                    "en": "VoluntaryRetainedEarnings",
                    "ja": "任意積立金"
                },
                {
                    "en": "RetainedEarningsBroughtForward",
                    "ja": "繰越利益剰余金"
                },
                {
                    "en": "OtherRetainedEarnings",
                    "ja": "その他利益剰余金"
                },
                {
                    "en": "RetainedEarnings",
                    "ja": "利益剰余金"
                },
                {
                    "en": "TreasuryStock",
                    "ja": "自己株式"
                },
                {
                    "en": "OtherLossGainOnValuationOfSecurities",
                    "ja": "その他有価証券評価差額金"
                },
                {
                    "en": "ForeignCurrencyTranslationAdjustment",
                    "ja": "為替換算調整勘定"
                },
                {
                    "en": "OtherLossGainOnValuation",
                    "ja": "その他評価損益"
                },
                {
                    "en": "OtherAccumulatedComprehensiveIncome",
                    "ja": "その他包括利益累計額"
                },
                {
                    "en": "SubscriptionRightsToShares",
                    "ja": "新株予約権"
                },
                {
                    "en": "MinorityInterests",
                    "ja": "少数株主持分"
                },
                {
                    "en": "NetAssets",
                    "ja": "純資産合計"
                },
                {
                    "en": "LiabilitiesAndNetAssets",
                    "ja": "負債及び純資産合計"
                },
                {
                    "en": "NetSales",
                    "ja": "売上高"
                },
                {
                    "en": "OpeningMaterialsInventory",
                    "ja": "期首材料棚卸高"
                },
                {
                    "en": "MaterialPurchased",
                    "ja": "材料仕入高"
                },
                {
                    "en": "EndingMaterialsInventory",
                    "ja": "期末材料棚卸高"
                },
                {
                    "en": "MaterialCost",
                    "ja": "材料費"
                },
                {
                    "en": "SalariesCOS",
                    "ja": "従業員給与_原価"
                },
                {
                    "en": "BonusCOS",
                    "ja": "従業員賞与_原価"
                },
                {
                    "en": "RetirementPaymentsCOS",
                    "ja": "従業員退職金_原価"
                },
                {
                    "en": "LegalWelfareExpensesCOS",
                    "ja": "法定福利費_原価"
                },
                {
                    "en": "WelfareExpensesCOS",
                    "ja": "福利厚生費_原価"
                },
                {
                    "en": "LaborCostSubTotal",
                    "ja": "労務費小計"
                },
                {
                    "en": "OtherLaborCost",
                    "ja": "その他の労務費"
                },
                {
                    "en": "LaborLost",
                    "ja": "労務費"
                },
                {
                    "en": "OutsourcingProcessingExpense",
                    "ja": "外注加工費"
                },
                {
                    "en": "UtilitiesExpensesCOS",
                    "ja": "水道光熱費_原価"
                },
                {
                    "en": "ConsumableToolsEquipmentAndFixturesCOS",
                    "ja": "消耗工具器具備品費_原価"
                },
                {
                    "en": "TaxesAndDuesCOS",
                    "ja": "租税公課_原価"
                },
                {
                    "en": "DepreciationCOS",
                    "ja": "減価償却費_原価"
                },
                {
                    "en": "RepairExpensesCOS",
                    "ja": "修繕費_原価"
                },
                {
                    "en": "InsuranceExpensesCOS",
                    "ja": "保険料_原価"
                },
                {
                    "en": "RentExpensesCOS",
                    "ja": "賃借料_原価"
                },
                {
                    "en": "ResearchAndDevelopmentExpensesCOS",
                    "ja": "研究開発費_原価"
                },
                {
                    "en": "ExpensesSubTotalCOS",
                    "ja": "経費小計"
                },
                {
                    "en": "OtherExpensesCOS",
                    "ja": "その他の経費_原価"
                },
                {
                    "en": "ExpensesCOS",
                    "ja": "経費"
                },
                {
                    "en": "CostOfSalesSubTotal",
                    "ja": "売上原価小計"
                },
                {
                    "en": "OpeningWorkInProcessInventory",
                    "ja": "期首仕掛品棚卸高"
                },
                {
                    "en": "EndingWorkInProcessInventory",
                    "ja": "期末仕掛品棚卸高"
                },
                {
                    "en": "TransferToOtherAccountCOS",
                    "ja": "他勘定振替高"
                },
                {
                    "en": "CostOfSales",
                    "ja": "売上原価"
                },
                {
                    "en": "GrossProfit",
                    "ja": "売上総利益"
                },
                {
                    "en": "SalesCommissionSGA",
                    "ja": "販売手数料"
                },
                {
                    "en": "PackingAndTransportationExpensesSGA",
                    "ja": "荷造運送費"
                },
                {
                    "en": "VehicleAndFuelExpensesSGA",
                    "ja": "車両燃料費"
                },
                {
                    "en": "AdvertisingExpensesSGA",
                    "ja": "広告宣伝費"
                },
                {
                    "en": "WarehousingExpensesSGA",
                    "ja": "保管費"
                },
                {
                    "en": "PersonalExpensesSGA",
                    "ja": "人件費"
                },
                {
                    "en": "DirectorsBonusSGA",
                    "ja": "役員賞与"
                },
                {
                    "en": "WelfareExpensesSGA",
                    "ja": "福利厚生費_販管費"
                },
                {
                    "en": "EntertainmentExpensesSGA",
                    "ja": "接待交際費"
                },
                {
                    "en": "TravelAndTransportationExpensesSGA",
                    "ja": "旅費交通費"
                },
                {
                    "en": "CommunicationExpensesSGA",
                    "ja": "通信費"
                },
                {
                    "en": "UtilitiesExpensesSGA",
                    "ja": "水道光熱費_販管費"
                },
                {
                    "en": "OfficeSuppliesExpensesSGA",
                    "ja": "事務用消耗品費"
                },
                {
                    "en": "ConsumableToolsEquipmentAndFixturesSGA",
                    "ja": "消耗工具器具備品_販管費"
                },
                {
                    "en": "TaxesAndDuesSGA",
                    "ja": "租税公課_販管費"
                },
                {
                    "en": "BookExpensesSGA",
                    "ja": "図書費"
                },
                {
                    "en": "DepreciationSGA",
                    "ja": "減価償却費_販管費"
                },
                {
                    "en": "RepairExpensesSGA",
                    "ja": "修繕費_販管費"
                },
                {
                    "en": "InsuranceExpensesSGA",
                    "ja": "保険料_販管費"
                },
                {
                    "en": "RentExpensesSGA",
                    "ja": "賃借料_販管費"
                },
                {
                    "en": "ContributionSGA",
                    "ja": "寄付金"
                },
                {
                    "en": "ResearchAndDevelopmentExpensesSGA",
                    "ja": "研究開発費_販管費"
                },
                {
                    "en": "SellingGeneralAndAdministrativeExpensesSubTotal",
                    "ja": "販売費及び一般管理費小計"
                },
                {
                    "en": "OtherSGA",
                    "ja": "その他の経費_販管費"
                },
                {
                    "en": "SellingGeneralAndAdministrativeExpenses",
                    "ja": "販売費及び一般管理費"
                },
                {
                    "en": "OperatingIncome",
                    "ja": "営業利益"
                },
                {
                    "en": "InterestAndDividendsIncomeNOI",
                    "ja": "受取利息及び受取配当金"
                },
                {
                    "en": "OtherNOI",
                    "ja": "その他の営業外収入"
                },
                {
                    "en": "NonOperatingIncome",
                    "ja": "営業外収益"
                },
                {
                    "en": "InterestAndDividendsExpenseNOE",
                    "ja": "支払利息及び手形譲渡損"
                },
                {
                    "en": "OtherNOE",
                    "ja": "その他の営業外費用"
                },
                {
                    "en": "NonOperatingExpenses",
                    "ja": "営業外費用"
                },
                {
                    "en": "OrdinaryIncome",
                    "ja": "経常損益"
                },
                {
                    "en": "GainOnSalesOfNoncurrentAssetsEI",
                    "ja": "経常利益固定資産売却益"
                },
                {
                    "en": "GainOnSalesOfInvestmentSecuritiesEI",
                    "ja": "投資有価証券売却益"
                },
                {
                    "en": "Profit LossFromPriorPeriodAdjustmentsEI",
                    "ja": "前期修正損益"
                },
                {
                    "en": "OtherEI",
                    "ja": "その他_特別利益"
                },
                {
                    "en": "ExtraordinaryIncome",
                    "ja": "特別利益"
                },
                {
                    "en": "LossOnSalesOfNoncurrentAssetsEL",
                    "ja": "固定資産売却損"
                },
                {
                    "en": "ImpairmentLossEL",
                    "ja": "減損損失_PL"
                },
                {
                    "en": "LossOnDisasterEL",
                    "ja": "災害による損失"
                },
                {
                    "en": "OtherEL",
                    "ja": "その他特別損失"
                },
                {
                    "en": "ExtraordinaryLoss",
                    "ja": "特別損失"
                },
                {
                    "en": "ExtraordinaryProfitLoss",
                    "ja": "特別損益"
                },
                {
                    "en": "IncomeBeforeIncomeTaxes",
                    "ja": "税引前当期純利益"
                },
                {
                    "en": "IncomeTaxes",
                    "ja": "法人税等"
                },
                {
                    "en": "IncomeTaxesDeferred",
                    "ja": "法人税等調整額"
                },
                {
                    "en": "OtherAdjustment",
                    "ja": "その他の調整額"
                },
                {
                    "en": "TaxRelief",
                    "ja": "税金等控除額"
                },
                {
                    "en": "ProfitLoss",
                    "ja": "当期純利益"
                },
                {
                    "en": "DepreciationOpeCF",
                    "ja": "減価償却費"
                },
                {
                    "en": "ImpairmentLossOpeCF",
                    "ja": "減損損失_CF"
                },
                {
                    "en": "IncreaseDecreaseInProvisionOpeCF",
                    "ja": "諸引当金増減額"
                },
                {
                    "en": "NonFundExpenseOpeCF",
                    "ja": "非資金の費用項目"
                },
                {
                    "en": "IncreaseDecreaseInNotesReceivableTradeOpeCF",
                    "ja": "受取手形増減額"
                },
                {
                    "en": "IncreaseDecreaseInAccountsReceivableTradeOpeCF",
                    "ja": "売掛金増減額"
                },
                {
                    "en": "IncreaseDecreaseInInventoriesOpeCF",
                    "ja": "棚卸資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherAssetOpeCF",
                    "ja": "その他資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInNotesPayableTradeOpeCF",
                    "ja": "支払手形増減額"
                },
                {
                    "en": "IncreaseDecreaseInAccountsPayableTradeOpeCF",
                    "ja": "買掛金増減額"
                },
                {
                    "en": "IncreaseDecreaseInAdvancesReceivedOpeCF",
                    "ja": "前受金増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherCAOpeCF",
                    "ja": "その他流動負債増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherNCAOpeCF",
                    "ja": "その他固定負債増減額_営業CF"
                },
                {
                    "en": "DirectorsBonusOpeCF",
                    "ja": "役員賞与支払額"
                },
                {
                    "en": "CollectionAndPaymentsOpeCF",
                    "ja": "回収及び支払サイト"
                },
                {
                    "en": "NetCashProvidedByUsedInOperatingActivities",
                    "ja": "営業キャッシュフロー"
                },
                {
                    "en": "IncreaseDecreaseInShortTermInvestmentSecuritiesInvCF",
                    "ja": "有価証券増減額"
                },
                {
                    "en": "IncreaseDecreaseInLandInvCF",
                    "ja": "土地増減額"
                },
                {
                    "en": "IncreaseDecreaseInDepreciableAssetInvCF",
                    "ja": "減価償却資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInIntangibleAssetsInvCF",
                    "ja": "無形固定資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInLongTermInvestmentSecuritiesInvCF",
                    "ja": "投資有価証券増減額"
                },
                {
                    "en": "IncreaseDecreaseInLongTermLoansReceivableInvCF",
                    "ja": "長期貸付金増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherNCAInvCF",
                    "ja": "その他固定資産増減額_投資CF"
                },
                {
                    "en": "IncreaseDecreaseInDeferredAssetsInvCF",
                    "ja": "繰延資産増減額"
                },
                {
                    "en": "NetCashProvidedByUsedInInvestmentActivities",
                    "ja": "投資キャッシュフロー"
                },
                {
                    "en": "FreeCashFlow",
                    "ja": "フリーキャッシュフロー（Ⅰ＋Ⅱ）"
                },
                {
                    "en": "IncreaseDecreaseInShortTermLoansPayableFinCF",
                    "ja": "短期借入金増減額"
                },
                {
                    "en": "IncreaseDecreaseInLongTermLoansPayableFinCF",
                    "ja": "長期借入金増減額"
                },
                {
                    "en": "IncreaseDecreaseInCapitalStockFinCF",
                    "ja": "資本金増減額"
                },
                {
                    "en": "CashDividendsPaidFinCF",
                    "ja": "配当金支払額"
                },
                {
                    "en": "NetCashProvidedByUsedInFinancingActivities",
                    "ja": "財務キャッシュフロー"
                },
                {
                    "en": "IncreaseDecreaseInNetCash",
                    "ja": "キャッシュの増加・減少額（Ⅰ＋Ⅱ＋Ⅲ）"
                },
                {
                    "en": "OpeningCash",
                    "ja": "キャッシュの期首残高"
                },
                {
                    "en": "EndingCash",
                    "ja": "キャッシュの期末残高"
                }
            ],
            "name": "1.0a"
        },
        {
            "items": [
                {
                    "en": "CashAndDeposits",
                    "ja": "現金及び預金"
                },
                {
                    "en": "NotesReceivableTrade",
                    "ja": "受取手形"
                },
                {
                    "en": "AccountsReceivableTrade",
                    "ja": "売掛金"
                },
                {
                    "en": "ShortTermInvestmentSecurities",
                    "ja": "有価証券"
                },
                {
                    "en": "MerchandiseAndFinishedGoods",
                    "ja": "商品及び製品"
                },
                {
                    "en": "ShortTermLoansReceivable",
                    "ja": "短期貸付金"
                },
                {
                    "en": "AdvancePaymentsTrade",
                    "ja": "前渡金"
                },
                {
                    "en": "AccountsReceivableOther",
                    "ja": "未収入金"
                },
                {
                    "en": "PrepaidExpenses",
                    "ja": "前払費用"
                },
                {
                    "en": "SuspensePayments",
                    "ja": "仮払金"
                },
                {
                    "en": "AllowanceForDoubtfulAccountsCA",
                    "ja": "貸倒引当金_流動資産"
                },
                {
                    "en": "CurrentAssetsSubTotal",
                    "ja": "流動資産小計"
                },
                {
                    "en": "OtherCA",
                    "ja": "その他流動資産"
                },
                {
                    "en": "CurrentAssets",
                    "ja": "流動資産"
                },
                {
                    "en": "BuildingsAndStructures",
                    "ja": "建物及び構築物"
                },
                {
                    "en": "MachineryAndEquipment",
                    "ja": "機械及び装置"
                },
                {
                    "en": "ToolsFurnitureAndFixtures",
                    "ja": "工具・器具及び備品"
                },
                {
                    "en": "LeaseAssetsPPE",
                    "ja": "リース資産"
                },
                {
                    "en": "Land",
                    "ja": "土地"
                },
                {
                    "en": "ConstructionInProgress",
                    "ja": "建設仮勘定"
                },
                {
                    "en": "AccumulatedDepreciationPPE",
                    "ja": "減価償却累計額_有形資産"
                },
                {
                    "en": "PropertyPlantAndEquipmentSubTotal",
                    "ja": "有形固定資産小計"
                },
                {
                    "en": "OtherPPE",
                    "ja": "その他有形固定資産"
                },
                {
                    "en": "PropertyPlantAndEquipment",
                    "ja": "有形固定資産"
                },
                {
                    "en": "Software",
                    "ja": "ソフトウエア"
                },
                {
                    "en": "Goodwill",
                    "ja": "のれん"
                },
                {
                    "en": "IntangibleAssetsSubTotal",
                    "ja": "無形固定資産小計"
                },
                {
                    "en": "OtherIA",
                    "ja": "その他無形固定資産"
                },
                {
                    "en": "IntangibleAssets",
                    "ja": "無形固定資産"
                },
                {
                    "en": "StocksOfSubsidiariesAndAffiliates",
                    "ja": "関係会社株式"
                },
                {
                    "en": "InvestmentSecurities",
                    "ja": "投資有価証券"
                },
                {
                    "en": "InvestmentsInCapital",
                    "ja": "出資金"
                },
                {
                    "en": "LongTermLoansReceivable",
                    "ja": "長期貸付金"
                },
                {
                    "en": "LongTermPrepaidExpenses",
                    "ja": "長期前払費用"
                },
                {
                    "en": "DeferredTaxAssets",
                    "ja": "繰延税金資産"
                },
                {
                    "en": "AccumulatedDepreciationIOA",
                    "ja": "減価償却累計額_投資等資産"
                },
                {
                    "en": "AllowanceForDoubtfulAccountsIOA",
                    "ja": "貸倒引当金_投資等資産"
                },
                {
                    "en": "InvestmentsAndOtherAssetsSubTotal",
                    "ja": "投資等資産小計"
                },
                {
                    "en": "OtherIOA",
                    "ja": "その他投資等資産"
                },
                {
                    "en": "InvestmentsAndOtherAssets",
                    "ja": "投資等資産"
                },
                {
                    "en": "NoncurrentAssets",
                    "ja": "固定資産"
                },
                {
                    "en": "DeferredOrganizationAndBusinessCommencementExpensesDA",
                    "ja": "創業費・開業費"
                },
                {
                    "en": "DevelopmentExpensesDA",
                    "ja": "開発費"
                },
                {
                    "en": "DeferredAssetsSubTotal",
                    "ja": "繰延資産小計"
                },
                {
                    "en": "OtherDA",
                    "ja": "その他繰延資産"
                },
                {
                    "en": "DeferredAssets",
                    "ja": "繰延資産"
                },
                {
                    "en": "Assets",
                    "ja": "資産合計"
                },
                {
                    "en": "NotesPayableTrade",
                    "ja": "支払手形"
                },
                {
                    "en": "AccountsPayableTrade",
                    "ja": "買掛金"
                },
                {
                    "en": "ShortTermLoansPayable",
                    "ja": "短期借入金"
                },
                {
                    "en": "AccountsPayableOther",
                    "ja": "未払金"
                },
                {
                    "en": "AccruedExpenses",
                    "ja": "未払費用"
                },
                {
                    "en": "AdvancesReceived",
                    "ja": "前受金"
                },
                {
                    "en": "AdvancesReceivedOnUncompletedContracts",
                    "ja": "未成工事受入金"
                },
                {
                    "en": "UnearnedRevenue",
                    "ja": "前受収益"
                },
                {
                    "en": "LeaseObligationsCL",
                    "ja": "リース債務_流動負債"
                },
                {
                    "en": "IncomeTaxesPayable",
                    "ja": "未払法人税等"
                },
                {
                    "en": "ProvisionForBonuses",
                    "ja": "賞与引当金"
                },
                {
                    "en": "CurrentLiabilitiesSubTotal",
                    "ja": "流動負債小計"
                },
                {
                    "en": "OtherCL",
                    "ja": "その他流動負債"
                },
                {
                    "en": "CurrentLiabilities",
                    "ja": "流動負債"
                },
                {
                    "en": "BondsPayable",
                    "ja": "社債"
                },
                {
                    "en": "LongTermLoansPayable",
                    "ja": "長期借入金"
                },
                {
                    "en": "LeaseObligationsNCL",
                    "ja": "リース債務_固定負債"
                },
                {
                    "en": "ProvisionForRetirementBenefits",
                    "ja": "退職給付引当金"
                },
                {
                    "en": "DeferredTaxLiabilities",
                    "ja": "繰延税金負債"
                },
                {
                    "en": "NoncurrentLiabilitiesSubTotal",
                    "ja": "固定負債小計"
                },
                {
                    "en": "OtherNCL",
                    "ja": "その他固定負債"
                },
                {
                    "en": "NoncurrentLiabilities",
                    "ja": "固定負債"
                },
                {
                    "en": "ReservesUnderTheSpecialLaws",
                    "ja": "特別法上の準備金"
                },
                {
                    "en": "Liabilities",
                    "ja": "負債合計"
                },
                {
                    "en": "CapitalStock",
                    "ja": "資本金"
                },
                {
                    "en": "LegalCapitalSurplus",
                    "ja": "資本準備金"
                },
                {
                    "en": "OtherCapitalSurplus",
                    "ja": "その他資本剰余金"
                },
                {
                    "en": "CapitalSurplus",
                    "ja": "資本剰余金"
                },
                {
                    "en": "LegalRetainedEarnings",
                    "ja": "利益準備金"
                },
                {
                    "en": "VoluntaryRetainedEarnings",
                    "ja": "任意積立金"
                },
                {
                    "en": "RetainedEarningsBroughtForward",
                    "ja": "繰越利益剰余金"
                },
                {
                    "en": "OtherRetainedEarnings",
                    "ja": "その他利益剰余金"
                },
                {
                    "en": "RetainedEarnings",
                    "ja": "利益剰余金"
                },
                {
                    "en": "TreasuryStock",
                    "ja": "自己株式"
                },
                {
                    "en": "OtherLossGainOnValuationOfSecurities",
                    "ja": "その他有価証券評価差額金"
                },
                {
                    "en": "ForeignCurrencyTranslationAdjustment",
                    "ja": "為替換算調整勘定"
                },
                {
                    "en": "OtherLossGainOnValuation",
                    "ja": "その他評価損益"
                },
                {
                    "en": "OtherAccumulatedComprehensiveIncome",
                    "ja": "その他包括利益累計額"
                },
                {
                    "en": "SubscriptionRightsToShares",
                    "ja": "新株予約権"
                },
                {
                    "en": "MinorityInterests",
                    "ja": "少数株主持分"
                },
                {
                    "en": "NetAssets",
                    "ja": "純資産合計"
                },
                {
                    "en": "LiabilitiesAndNetAssets",
                    "ja": "負債及び純資産合計"
                },
                {
                    "en": "NetSales",
                    "ja": "売上高"
                },
                {
                    "en": "OpeningMaterialsInventory",
                    "ja": "期首材料棚卸高"
                },
                {
                    "en": "MaterialPurchased",
                    "ja": "材料仕入高"
                },
                {
                    "en": "EndingMaterialsInventory",
                    "ja": "期末材料棚卸高"
                },
                {
                    "en": "MaterialCost",
                    "ja": "材料費"
                },
                {
                    "en": "SalariesCOS",
                    "ja": "従業員給与_原価"
                },
                {
                    "en": "BonusCOS",
                    "ja": "従業員賞与_原価"
                },
                {
                    "en": "RetirementPaymentsCOS",
                    "ja": "従業員退職金_原価"
                },
                {
                    "en": "LegalWelfareExpensesCOS",
                    "ja": "法定福利費_原価"
                },
                {
                    "en": "WelfareExpensesCOS",
                    "ja": "福利厚生費_原価"
                },
                {
                    "en": "LaborCostSubTotal",
                    "ja": "労務費小計"
                },
                {
                    "en": "OtherLaborCost",
                    "ja": "その他の労務費"
                },
                {
                    "en": "LaborLost",
                    "ja": "労務費"
                },
                {
                    "en": "OutsourcingProcessingExpense",
                    "ja": "外注加工費"
                },
                {
                    "en": "UtilitiesExpensesCOS",
                    "ja": "水道光熱費_原価"
                },
                {
                    "en": "ConsumableToolsEquipmentAndFixturesCOS",
                    "ja": "消耗工具器具備品費_原価"
                },
                {
                    "en": "TaxesAndDuesCOS",
                    "ja": "租税公課_原価"
                },
                {
                    "en": "DepreciationCOS",
                    "ja": "減価償却費_原価"
                },
                {
                    "en": "RepairExpensesCOS",
                    "ja": "修繕費_原価"
                },
                {
                    "en": "InsuranceExpensesCOS",
                    "ja": "保険料_原価"
                },
                {
                    "en": "RentExpensesCOS",
                    "ja": "賃借料_原価"
                },
                {
                    "en": "ResearchAndDevelopmentExpensesCOS",
                    "ja": "研究開発費_原価"
                },
                {
                    "en": "ExpensesSubTotalCOS",
                    "ja": "経費小計"
                },
                {
                    "en": "OtherExpensesCOS",
                    "ja": "その他の経費_原価"
                },
                {
                    "en": "ExpensesCOS",
                    "ja": "経費"
                },
                {
                    "en": "CostOfSalesSubTotal",
                    "ja": "売上原価小計"
                },
                {
                    "en": "OpeningWorkInProcessInventory",
                    "ja": "期首仕掛品棚卸高"
                },
                {
                    "en": "EndingWorkInProcessInventory",
                    "ja": "期末仕掛品棚卸高"
                },
                {
                    "en": "TransferToOtherAccountCOS",
                    "ja": "他勘定振替高"
                },
                {
                    "en": "CostOfSales",
                    "ja": "売上原価"
                },
                {
                    "en": "GrossProfit",
                    "ja": "売上総利益"
                },
                {
                    "en": "SalesCommissionSGA",
                    "ja": "販売手数料"
                },
                {
                    "en": "PackingAndTransportationExpensesSGA",
                    "ja": "荷造運送費"
                },
                {
                    "en": "VehicleAndFuelExpensesSGA",
                    "ja": "車両燃料費"
                },
                {
                    "en": "AdvertisingExpensesSGA",
                    "ja": "広告宣伝費"
                },
                {
                    "en": "WarehousingExpensesSGA",
                    "ja": "保管費"
                },
                {
                    "en": "DirectorsCompensationsSGA",
                    "ja": "役員報酬"
                },
                {
                    "en": "DirectorsBonusSGA",
                    "ja": "役員賞与"
                },
                {
                    "en": "DirectorsRetirementPaymentsSGA",
                    "ja": "役員退職金"
                },
                {
                    "en": "SalariesSGA",
                    "ja": "従業員給与_販管費"
                },
                {
                    "en": "BonusSGA",
                    "ja": "従業員賞与_販管費"
                },
                {
                    "en": "RetirementPaymentsSGA",
                    "ja": "従業員退職金_販管費"
                },
                {
                    "en": "LegalWelfareExpensesSGA",
                    "ja": "法定福利費_販管費"
                },
                {
                    "en": "WelfareExpensesSGA",
                    "ja": "福利厚生費_販管費"
                },
                {
                    "en": "EntertainmentExpensesSGA",
                    "ja": "接待交際費"
                },
                {
                    "en": "TravelAndTransportationExpensesSGA",
                    "ja": "旅費交通費"
                },
                {
                    "en": "CommunicationExpensesSGA",
                    "ja": "通信費"
                },
                {
                    "en": "UtilitiesExpensesSGA",
                    "ja": "水道光熱費_販管費"
                },
                {
                    "en": "OfficeSuppliesExpensesSGA",
                    "ja": "事務用消耗品費"
                },
                {
                    "en": "ConsumableToolsEquipmentAndFixturesSGA",
                    "ja": "消耗工具器具備品_販管費"
                },
                {
                    "en": "TaxesAndDuesSGA",
                    "ja": "租税公課_販管費"
                },
                {
                    "en": "BookExpensesSGA",
                    "ja": "図書費"
                },
                {
                    "en": "DepreciationSGA",
                    "ja": "減価償却費_販管費"
                },
                {
                    "en": "RepairExpensesSGA",
                    "ja": "修繕費_販管費"
                },
                {
                    "en": "InsuranceExpensesSGA",
                    "ja": "保険料_販管費"
                },
                {
                    "en": "RentExpensesSGA",
                    "ja": "賃借料_販管費"
                },
                {
                    "en": "ContributionSGA",
                    "ja": "寄付金"
                },
                {
                    "en": "ResearchAndDevelopmentExpensesSGA",
                    "ja": "研究開発費_販管費"
                },
                {
                    "en": "SellingGeneralAndAdministrativeExpensesSubTotal",
                    "ja": "販売費及び一般管理費小計"
                },
                {
                    "en": "OtherSGA",
                    "ja": "その他の経費_販管費"
                },
                {
                    "en": "SellingGeneralAndAdministrativeExpenses",
                    "ja": "販売費及び一般管理費"
                },
                {
                    "en": "OperatingIncome",
                    "ja": "営業利益"
                },
                {
                    "en": "InterestAndDividendsIncomeNOI",
                    "ja": "受取利息及び受取配当金"
                },
                {
                    "en": "OtherNOI",
                    "ja": "その他の営業外収入"
                },
                {
                    "en": "NonOperatingIncome",
                    "ja": "営業外収益"
                },
                {
                    "en": "InterestAndDividendsExpenseNOE",
                    "ja": "支払利息及び手形譲渡損"
                },
                {
                    "en": "OtherNOE",
                    "ja": "その他の営業外費用"
                },
                {
                    "en": "NonOperatingExpenses",
                    "ja": "営業外費用"
                },
                {
                    "en": "OrdinaryIncome",
                    "ja": "経常損益"
                },
                {
                    "en": "GainOnSalesOfNoncurrentAssetsEI",
                    "ja": "経常利益固定資産売却益"
                },
                {
                    "en": "GainOnSalesOfInvestmentSecuritiesEI",
                    "ja": "投資有価証券売却益"
                },
                {
                    "en": "Profit LossFromPriorPeriodAdjustmentsEI",
                    "ja": "前期修正損益"
                },
                {
                    "en": "OtherEI",
                    "ja": "その他_特別利益"
                },
                {
                    "en": "ExtraordinaryIncome",
                    "ja": "特別利益"
                },
                {
                    "en": "LossOnSalesOfNoncurrentAssetsEL",
                    "ja": "固定資産売却損"
                },
                {
                    "en": "ImpairmentLossEL",
                    "ja": "減損損失_PL"
                },
                {
                    "en": "LossOnDisasterEL",
                    "ja": "災害による損失"
                },
                {
                    "en": "OtherEL",
                    "ja": "その他特別損失"
                },
                {
                    "en": "ExtraordinaryLoss",
                    "ja": "特別損失"
                },
                {
                    "en": "ExtraordinaryProfitLoss",
                    "ja": "特別損益"
                },
                {
                    "en": "IncomeBeforeIncomeTaxes",
                    "ja": "税引前当期純利益"
                },
                {
                    "en": "IncomeTaxes",
                    "ja": "法人税等"
                },
                {
                    "en": "IncomeTaxesDeferred",
                    "ja": "法人税等調整額"
                },
                {
                    "en": "OtherAdjustment",
                    "ja": "その他の調整額"
                },
                {
                    "en": "TaxRelief",
                    "ja": "税金等控除額"
                },
                {
                    "en": "ProfitLoss",
                    "ja": "当期純利益"
                },
                {
                    "en": "DepreciationOpeCF",
                    "ja": "減価償却費"
                },
                {
                    "en": "ImpairmentLossOpeCF",
                    "ja": "減損損失_CF"
                },
                {
                    "en": "IncreaseDecreaseInProvisionOpeCF",
                    "ja": "諸引当金増減額"
                },
                {
                    "en": "NonFundExpenseOpeCF",
                    "ja": "非資金の費用項目"
                },
                {
                    "en": "IncreaseDecreaseInNotesReceivableTradeOpeCF",
                    "ja": "受取手形増減額"
                },
                {
                    "en": "IncreaseDecreaseInAccountsReceivableTradeOpeCF",
                    "ja": "売掛金増減額"
                },
                {
                    "en": "IncreaseDecreaseInInventoriesOpeCF",
                    "ja": "棚卸資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherAssetOpeCF",
                    "ja": "その他資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInNotesPayableTradeOpeCF",
                    "ja": "支払手形増減額"
                },
                {
                    "en": "IncreaseDecreaseInAccountsPayableTradeOpeCF",
                    "ja": "買掛金増減額"
                },
                {
                    "en": "IncreaseDecreaseInAdvancesReceivedOpeCF",
                    "ja": "前受金増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherCAOpeCF",
                    "ja": "その他流動負債増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherNCAOpeCF",
                    "ja": "その他固定負債増減額_営業CF"
                },
                {
                    "en": "DirectorsBonusOpeCF",
                    "ja": "役員賞与支払額"
                },
                {
                    "en": "CollectionAndPaymentsOpeCF",
                    "ja": "回収及び支払サイト"
                },
                {
                    "en": "NetCashProvidedByUsedInOperatingActivities",
                    "ja": "営業キャッシュフロー"
                },
                {
                    "en": "IncreaseDecreaseInShortTermInvestmentSecuritiesInvCF",
                    "ja": "有価証券増減額"
                },
                {
                    "en": "IncreaseDecreaseInLandInvCF",
                    "ja": "土地増減額"
                },
                {
                    "en": "IncreaseDecreaseInDepreciableAssetInvCF",
                    "ja": "減価償却資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInIntangibleAssetsInvCF",
                    "ja": "無形固定資産増減額"
                },
                {
                    "en": "IncreaseDecreaseInLongTermInvestmentSecuritiesInvCF",
                    "ja": "投資有価証券増減額"
                },
                {
                    "en": "IncreaseDecreaseInLongTermLoansReceivableInvCF",
                    "ja": "長期貸付金増減額"
                },
                {
                    "en": "IncreaseDecreaseInOtherNCAInvCF",
                    "ja": "その他固定資産増減額_投資CF"
                },
                {
                    "en": "IncreaseDecreaseInDeferredAssetsInvCF",
                    "ja": "繰延資産増減額"
                },
                {
                    "en": "NetCashProvidedByUsedInInvestmentActivities",
                    "ja": "投資キャッシュフロー"
                },
                {
                    "en": "FreeCashFlow",
                    "ja": "フリーキャッシュフロー（Ⅰ＋Ⅱ）"
                },
                {
                    "en": "IncreaseDecreaseInShortTermLoansPayableFinCF",
                    "ja": "短期借入金増減額"
                },
                {
                    "en": "IncreaseDecreaseInLongTermLoansPayableFinCF",
                    "ja": "長期借入金増減額"
                },
                {
                    "en": "IncreaseDecreaseInCapitalStockFinCF",
                    "ja": "資本金増減額"
                },
                {
                    "en": "CashDividendsPaidFinCF",
                    "ja": "配当金支払額"
                },
                {
                    "en": "NetCashProvidedByUsedInFinancingActivities",
                    "ja": "財務キャッシュフロー"
                },
                {
                    "en": "IncreaseDecreaseInNetCash",
                    "ja": "キャッシュの増加・減少額（Ⅰ＋Ⅱ＋Ⅲ）"
                },
                {
                    "en": "OpeningCash",
                    "ja": "キャッシュの期首残高"
                },
                {
                    "en": "EndingCash",
                    "ja": "キャッシュの期末残高"
                }
            ],
            "name": "1.0b"
        }
    ]
}
EXAMPLE = {
    "n_items": 204,
    "version": "1.0a",
    "items": [
        {
            "name": "CashAndDeposits",
            "value": 4387591
        },
        {
            "name": "NotesReceivableTrade",
            "value": 1
        },
        {
            "name": "AccountsReceivableTrade",
            "value": 91
        },
        {
            "name": "ShortTermInvestmentSecurities",
            "value": 161809456
        },
        {
            "name": "MerchandiseAndFinishedGoods",
            "value": 32257201
        },
        {
            "name": "ShortTermLoansReceivable",
            "value": 35
        },
        {
            "name": "AdvancePaymentsTrade",
            "value": 2000
        },
        {
            "name": "AccountsReceivableOther",
            "value": 37
        },
        {
            "name": "PrepaidExpenses",
            "value": 909
        },
        {
            "name": "SuspensePayments",
            "value": 5
        },
        {
            "name": "AllowanceForDoubtfulAccountsCA",
            "value": 5686981
        },
        {
            "name": "CurrentAssetsSubTotal",
            "value": 1027250
        },
        {
            "name": "OtherCA",
            "value": 50936189
        },
        {
            "name": "CurrentAssets",
            "value": 2069987
        },
        {
            "name": "BuildingsAndStructures",
            "value": 7
        },
        {
            "name": "MachineryAndEquipment",
            "value": 192328
        },
        {
            "name": "ToolsFurnitureAndFixtures",
            "value": 6227150
        },
        {
            "name": "LeaseAssetsPPE",
            "value": 90849529
        },
        {
            "name": "Land",
            "value": 113
        },
        {
            "name": "ConstructionInProgress",
            "value": 1
        },
        {
            "name": "AccumulatedDepreciationPPE",
            "value": 132114
        },
        {
            "name": "PropertyPlantAndEquipmentSubTotal",
            "value": 85259973
        },
        {
            "name": "OtherPPE",
            "value": 19
        },
        {
            "name": "PropertyPlantAndEquipment",
            "value": 438
        },
        {
            "name": "Software",
            "value": 5842
        },
        {
            "name": "Goodwill",
            "value": 312020
        },
        {
            "name": "IntangibleAssetsSubTotal",
            "value": 892842457
        },
        {
            "name": "OtherIA",
            "value": 1476
        },
        {
            "name": "IntangibleAssets",
            "value": 1
        },
        {
            "name": "StocksOfSubsidiariesAndAffiliates",
            "value": 12834
        },
        {
            "name": "InvestmentSecurities",
            "value": 128
        },
        {
            "name": "InvestmentsInCapital",
            "value": 86033751
        },
        {
            "name": "LongTermLoansReceivable",
            "value": 198
        },
        {
            "name": "LongTermPrepaidExpenses",
            "value": 14
        },
        {
            "name": "DeferredTaxAssets",
            "value": 2463678
        },
        {
            "name": "AccumulatedDepreciationIOA",
            "value": 72367992
        },
        {
            "name": "AllowanceForDoubtfulAccountsIOA",
            "value": 1829046
        },
        {
            "name": "InvestmentsAndOtherAssetsSubTotal",
            "value": 102112864
        },
        {
            "name": "OtherIOA",
            "value": 325
        },
        {
            "name": "InvestmentsAndOtherAssets",
            "value": 1425277
        },
        {
            "name": "NoncurrentAssets",
            "value": 839803
        },
        {
            "name": "DeferredOrganizationAndBusinessCommencementExpensesDA",
            "value": 529053140
        },
        {
            "name": "DevelopmentExpensesDA",
            "value": 623
        },
        {
            "name": "DeferredAssetsSubTotal",
            "value": 2
        },
        {
            "name": "OtherDA",
            "value": 1896
        },
        {
            "name": "DeferredAssets",
            "value": 204
        },
        {
            "name": "Assets",
            "value": 8
        },
        {
            "name": "NotesPayableTrade",
            "value": 660365
        },
        {
            "name": "AccountsPayableTrade",
            "value": 924561721
        },
        {
            "name": "ShortTermLoansPayable",
            "value": 491205
        },
        {
            "name": "AccountsPayableOther",
            "value": 22622
        },
        {
            "name": "AccruedExpenses",
            "value": 189
        },
        {
            "name": "AdvancesReceived",
            "value": 133821
        },
        {
            "name": "AdvancesReceivedOnUncompletedContracts",
            "value": 8
        },
        {
            "name": "UnearnedRevenue",
            "value": 17
        },
        {
            "name": "LeaseObligationsCL",
            "value": 66
        },
        {
            "name": "IncomeTaxesPayable",
            "value": 16342
        },
        {
            "name": "ProvisionForBonuses",
            "value": 132207474
        },
        {
            "name": "CurrentLiabilitiesSubTotal",
            "value": 17106
        },
        {
            "name": "OtherCL",
            "value": 280170919
        },
        {
            "name": "CurrentLiabilities",
            "value": 613519
        },
        {
            "name": "BondsPayable",
            "value": 98672
        },
        {
            "name": "LongTermLoansPayable",
            "value": 18
        },
        {
            "name": "LeaseObligationsNCL",
            "value": 69854
        },
        {
            "name": "ProvisionForRetirementBenefits",
            "value": 772329926
        },
        {
            "name": "DeferredTaxLiabilities",
            "value": 1
        },
        {
            "name": "NoncurrentLiabilitiesSubTotal",
            "value": 1142721
        },
        {
            "name": "OtherNCL",
            "value": 171
        },
        {
            "name": "NoncurrentLiabilities",
            "value": 9489328
        },
        {
            "name": "ReservesUnderTheSpecialLaws",
            "value": 783
        },
        {
            "name": "Liabilities",
            "value": 34090887
        },
        {
            "name": "CapitalStock",
            "value": 1160422
        },
        {
            "name": "LegalCapitalSurplus",
            "value": 16746
        },
        {
            "name": "OtherCapitalSurplus",
            "value": 162
        },
        {
            "name": "CapitalSurplus",
            "value": 245226101
        },
        {
            "name": "LegalRetainedEarnings",
            "value": 16
        },
        {
            "name": "VoluntaryRetainedEarnings",
            "value": 28988
        },
        {
            "name": "RetainedEarningsBroughtForward",
            "value": 1468924
        },
        {
            "name": "OtherRetainedEarnings",
            "value": 572769
        },
        {
            "name": "RetainedEarnings",
            "value": 9
        },
        {
            "name": "TreasuryStock",
            "value": 703671452
        },
        {
            "name": "OtherLossGainOnValuationOfSecurities",
            "value": 62581782
        },
        {
            "name": "ForeignCurrencyTranslationAdjustment",
            "value": 44490719
        },
        {
            "name": "OtherLossGainOnValuation",
            "value": 24
        },
        {
            "name": "OtherAccumulatedComprehensiveIncome",
            "value": 850
        },
        {
            "name": "SubscriptionRightsToShares",
            "value": 82
        },
        {
            "name": "MinorityInterests",
            "value": 232235
        },
        {
            "name": "NetAssets",
            "value": 1
        },
        {
            "name": "LiabilitiesAndNetAssets",
            "value": 503609364
        },
        {
            "name": "NetSales",
            "value": 284756289
        },
        {
            "name": "OpeningMaterialsInventory",
            "value": 3
        },
        {
            "name": "MaterialPurchased",
            "value": 1
        },
        {
            "name": "EndingMaterialsInventory",
            "value": 80
        },
        {
            "name": "MaterialCost",
            "value": 2162
        },
        {
            "name": "SalariesCOS",
            "value": 8296103
        },
        {
            "name": "BonusCOS",
            "value": 5237
        },
        {
            "name": "RetirementPaymentsCOS",
            "value": 7748
        },
        {
            "name": "LegalWelfareExpensesCOS",
            "value": 1658
        },
        {
            "name": "WelfareExpensesCOS",
            "value": 497680685
        },
        {
            "name": "LaborCostSubTotal",
            "value": 250697
        },
        {
            "name": "OtherLaborCost",
            "value": 2318325
        },
        {
            "name": "LaborLost",
            "value": 37453068
        },
        {
            "name": "OutsourcingProcessingExpense",
            "value": 73680
        },
        {
            "name": "UtilitiesExpensesCOS",
            "value": 12437316
        },
        {
            "name": "ConsumableToolsEquipmentAndFixturesCOS",
            "value": 10
        },
        {
            "name": "TaxesAndDuesCOS",
            "value": 55014
        },
        {
            "name": "DepreciationCOS",
            "value": 8979
        },
        {
            "name": "RepairExpensesCOS",
            "value": 35448918
        },
        {
            "name": "InsuranceExpensesCOS",
            "value": 786906
        },
        {
            "name": "RentExpensesCOS",
            "value": 457352
        },
        {
            "name": "ResearchAndDevelopmentExpensesCOS",
            "value": 194111801
        },
        {
            "name": "ExpensesSubTotalCOS",
            "value": 468306610
        },
        {
            "name": "OtherExpensesCOS",
            "value": 1971715
        },
        {
            "name": "ExpensesCOS",
            "value": 15
        },
        {
            "name": "CostOfSalesSubTotal",
            "value": 10378840
        },
        {
            "name": "OpeningWorkInProcessInventory",
            "value": 19421
        },
        {
            "name": "EndingWorkInProcessInventory",
            "value": 1939619
        },
        {
            "name": "TransferToOtherAccountCOS",
            "value": 104
        },
        {
            "name": "CostOfSales",
            "value": 296061
        },
        {
            "name": "GrossProfit",
            "value": 149119773
        },
        {
            "name": "SalesCommissionSGA",
            "value": 14
        },
        {
            "name": "PackingAndTransportationExpensesSGA",
            "value": 1265202
        },
        {
            "name": "VehicleAndFuelExpensesSGA",
            "value": 22045
        },
        {
            "name": "AdvertisingExpensesSGA",
            "value": 232928004
        },
        {
            "name": "WarehousingExpensesSGA",
            "value": 167451
        },
        {
            "name": "PersonalExpensesSGA",
            "value": 281
        },
        {
            "name": "DirectorsBonusSGA",
            "value": 1
        },
        {
            "name": "WelfareExpensesSGA",
            "value": 22742750
        },
        {
            "name": "EntertainmentExpensesSGA",
            "value": 66
        },
        {
            "name": "TravelAndTransportationExpensesSGA",
            "value": 14188346
        },
        {
            "name": "CommunicationExpensesSGA",
            "value": 89
        },
        {
            "name": "UtilitiesExpensesSGA",
            "value": 10434
        },
        {
            "name": "OfficeSuppliesExpensesSGA",
            "value": 273544530
        },
        {
            "name": "ConsumableToolsEquipmentAndFixturesSGA",
            "value": 18846473
        },
        {
            "name": "TaxesAndDuesSGA",
            "value": 5
        },
        {
            "name": "BookExpensesSGA",
            "value": 13264
        },
        {
            "name": "DepreciationSGA",
            "value": 15378
        },
        {
            "name": "RepairExpensesSGA",
            "value": 137283
        },
        {
            "name": "InsuranceExpensesSGA",
            "value": 839873807
        },
        {
            "name": "RentExpensesSGA",
            "value": 11871603
        },
        {
            "name": "ContributionSGA",
            "value": 116047047
        },
        {
            "name": "ResearchAndDevelopmentExpensesSGA",
            "value": 183
        },
        {
            "name": "SellingGeneralAndAdministrativeExpensesSubTotal",
            "value": 945645021
        },
        {
            "name": "OtherSGA",
            "value": 863510065
        },
        {
            "name": "SellingGeneralAndAdministrativeExpenses",
            "value": 1302958
        },
        {
            "name": "OperatingIncome",
            "value": 3
        },
        {
            "name": "InterestAndDividendsIncomeNOI",
            "value": 1983650
        },
        {
            "name": "OtherNOI",
            "value": 225992
        },
        {
            "name": "NonOperatingIncome",
            "value": 9
        },
        {
            "name": "InterestAndDividendsExpenseNOE",
            "value": 1
        },
        {
            "name": "OtherNOE",
            "value": 2
        },
        {
            "name": "NonOperatingExpenses",
            "value": 8100
        },
        {
            "name": "OrdinaryIncome",
            "value": 1
        },
        {
            "name": "GainOnSalesOfNoncurrentAssetsEI",
            "value": 6784
        },
        {
            "name": "GainOnSalesOfInvestmentSecuritiesEI",
            "value": 4
        },
        {
            "name": "Profit LossFromPriorPeriodAdjustmentsEI",
            "value": 20066749
        },
        {
            "name": "OtherEI",
            "value": 726
        },
        {
            "name": "ExtraordinaryIncome",
            "value": 13
        },
        {
            "name": "LossOnSalesOfNoncurrentAssetsEL",
            "value": 29706
        },
        {
            "name": "ImpairmentLossEL",
            "value": 6564268
        },
        {
            "name": "LossOnDisasterEL",
            "value": 2457480
        },
        {
            "name": "OtherEL",
            "value": 21474
        },
        {
            "name": "ExtraordinaryLoss",
            "value": 3559
        },
        {
            "name": "ExtraordinaryProfitLoss",
            "value": 368975586
        },
        {
            "name": "IncomeBeforeIncomeTaxes",
            "value": 13220
        },
        {
            "name": "IncomeTaxes",
            "value": 370285
        },
        {
            "name": "IncomeTaxesDeferred",
            "value": 11
        },
        {
            "name": "OtherAdjustment",
            "value": 219972
        },
        {
            "name": "TaxRelief",
            "value": 35688374
        },
        {
            "name": "ProfitLoss",
            "value": 76820023
        },
        {
            "name": "DepreciationOpeCF",
            "value": 48190
        },
        {
            "name": "ImpairmentLossOpeCF",
            "value": 1376184
        },
        {
            "name": "IncreaseDecreaseInProvisionOpeCF",
            "value": 1136043
        },
        {
            "name": "NonFundExpenseOpeCF",
            "value": 1
        },
        {
            "name": "IncreaseDecreaseInNotesReceivableTradeOpeCF",
            "value": 15166810
        },
        {
            "name": "IncreaseDecreaseInAccountsReceivableTradeOpeCF",
            "value": 258
        },
        {
            "name": "IncreaseDecreaseInInventoriesOpeCF",
            "value": 354248957
        },
        {
            "name": "IncreaseDecreaseInOtherAssetOpeCF",
            "value": 20427
        },
        {
            "name": "IncreaseDecreaseInNotesPayableTradeOpeCF",
            "value": 743
        },
        {
            "name": "IncreaseDecreaseInAccountsPayableTradeOpeCF",
            "value": 13698
        },
        {
            "name": "IncreaseDecreaseInAdvancesReceivedOpeCF",
            "value": 9511181
        },
        {
            "name": "IncreaseDecreaseInOtherCAOpeCF",
            "value": 850477257
        },
        {
            "name": "IncreaseDecreaseInOtherNCAOpeCF",
            "value": 2511795
        },
        {
            "name": "DirectorsBonusOpeCF",
            "value": 699074252
        },
        {
            "name": "CollectionAndPaymentsOpeCF",
            "value": 386154
        },
        {
            "name": "NetCashProvidedByUsedInOperatingActivities",
            "value": 584
        },
        {
            "name": "IncreaseDecreaseInShortTermInvestmentSecuritiesInvCF",
            "value": 343594821
        },
        {
            "name": "IncreaseDecreaseInLandInvCF",
            "value": 760950
        },
        {
            "name": "IncreaseDecreaseInDepreciableAssetInvCF",
            "value": 34
        },
        {
            "name": "IncreaseDecreaseInIntangibleAssetsInvCF",
            "value": 3592
        },
        {
            "name": "IncreaseDecreaseInLongTermInvestmentSecuritiesInvCF",
            "value": 20
        },
        {
            "name": "IncreaseDecreaseInLongTermLoansReceivableInvCF",
            "value": 11713
        },
        {
            "name": "IncreaseDecreaseInOtherNCAInvCF",
            "value": 1762
        },
        {
            "name": "IncreaseDecreaseInDeferredAssetsInvCF",
            "value": 12208617
        },
        {
            "name": "NetCashProvidedByUsedInInvestmentActivities",
            "value": 2399
        },
        {
            "name": "FreeCashFlow",
            "value": 127730
        },
        {
            "name": "IncreaseDecreaseInShortTermLoansPayableFinCF",
            "value": 605
        },
        {
            "name": "IncreaseDecreaseInLongTermLoansPayableFinCF",
            "value": 64291
        },
        {
            "name": "IncreaseDecreaseInCapitalStockFinCF",
            "value": 217107129
        },
        {
            "name": "CashDividendsPaidFinCF",
            "value": 394291
        },
        {
            "name": "NetCashProvidedByUsedInFinancingActivities",
            "value": 53180
        },
        {
            "name": "IncreaseDecreaseInNetCash",
            "value": 3617
        },
        {
            "name": "OpeningCash",
            "value": 3
        },
        {
            "name": "EndingCash",
            "value": 473457
        }
    ]
}