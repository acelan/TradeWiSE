#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# TradeWiSE Project
#
# This file is part of the TradeWiSE project, an automated trading and financial analysis platform.
# It is licensed under the Mozilla Public License 2.0 (MPL 2.0), which allows for wide use and modification
# while ensuring that enhancements and modifications remain available to the community.
#
# You can find the MPL 2.0 license in the root directory of the project or at https://www.mozilla.org/MPL/2.0/.
#
# Copyright (c) 2023 by wildfootw <wildfootw@wildfoo.tw>
#

import requests

def test_create_balance_sheet():
    # Endpoint URL
    url = 'http://database-api/balance_sheet/'

    # Test data for posting a balance sheet
    post_data = {
        "version": "v1",
        "ticker_symbol": "TEST",
        "reporting_year": 111,
        "reporting_season": 4,
        '流動資產': '', '現金及約當現金': 1342814083.0, '透過損益按公允價值衡量之金融資產－流動': 1070398.0, '透過其他綜合損益按公允價值衡量之金融資產－流動': 122998543.0, '按攤銷後成本衡量之金融資產－流動': 94600219.0, '避險之金融資產－流動': 2329.0, '應收帳款淨額': 229755887.0, '應收帳款－關係人淨額': 1583958.0, '其他應收款－關係人淨額': 68975.0, '存貨': 221149148.0, '其他流動資產': 38853204.0, '流動資產合計': 2052896744.0, '非流動資產': '', '透過其他綜合損益按公允價值衡量之金融資產－非流動': 6159200.0, '按攤銷後成本衡量之金融資產－非流動': 35127215.0, '採用權益法之投資': 27641505.0, '不動產、廠房及設備': 2693836970.0, '使用權資產': 41914136.0, '無形資產': 25999155.0, '遞延所得稅資產': 69185842.0, '其他非流動資產': 12018111.0, '非流動資產合計': 2911882134.0, '資產總額': 4964778878.0, '流動負債': '', '短期借款': 0.0, '透過損益按公允價值衡量之金融負債－流動': 116215.0, '避險之金融負債－流動': 813.0, '應付帳款': 54879708.0, '應付帳款－關係人': 1642637.0, '其他應付款': 454300789.0, '本期所得稅負債': 120801814.0, '其他流動負債': 312484841.0, '流動負債合計': 944226817.0, '非流動負債': '', '應付公司債': 834336439.0, '長期借款': 4760047.0, '遞延所得稅負債': 1031383.0, '租賃負債－非流動': 29764097.0, '其他非流動負債': 190171228.0, '非流動負債合計': 1060063194.0, '負債總額': 2004290011.0, '歸屬於母公司業主之權益': '', '股本': '', '普通股股本': 259303805.0, '股本合計': 259303805.0, '資本公積': '', '資本公積－發行溢價': 33076016.0, '資本公積－實際取得或處分子公司股權價格與帳面價值差額': 8406282.0, '資本公積-認列對子公司所有權權益變動數': 4229892.0, '資本公積－受贈資產': 64955.0, '資本公積－採用權益法認列關聯企業及合資股權淨值之變動數': 311863.0, '資本公積－合併溢額': 22803291.0, '資本公積－限制員工權利股票': 438029.0, '資本公積合計': 69330328.0, '保留盈餘': '', '法定盈餘公積': 311146899.0, '特別盈餘公積': 3154310.0, '未分配盈餘（或待彌補虧損）': 2323223479.0, '保留盈餘合計': 2637524688.0, '其他權益': '', '其他權益合計': -20505626.0, '庫藏股票': 0.0, '歸屬於母公司業主之權益合計': 2945653195.0, '非控制權益': 14835672.0, '權益總額': 2960488867.0, '負債及權益總計': 4964778878.0, '預收股款（權益項下）之約當發行股數（單位：股）': 0.0, '母公司暨子公司所持有之母公司庫藏股股數（單位：股）': 0.0
    }
    response = requests.post(url, json=post_data)
    assert response.status_code == 200
