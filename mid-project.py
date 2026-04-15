import yfinance as yf
import pandas as pd

def get_stock_fundamentals_v2(stock_id):
    """
    使用 Yahoo Finance 獲取台股基本面資料 (EPS, PEG, PE, ROE)
    """
    # 台股編號需加上 .TW (上市) 或 .TWO (上櫃)
    # 這裡我們用簡單的邏輯判斷，大多數為 .TW
    ticker_str = f"{stock_id}.TW"
    print(f"\n正在從 Yahoo Finance 抓取 {ticker_str} 的資料...")
    
    try:
        stock = yf.Ticker(ticker_str)
        info = stock.info
        
        # 提取作業要求的特定欄位
        data = {
            "股票代號": stock_id,
            "每股盈餘 (EPS)": info.get('trailingEps', '無資料'),
            "本益比 (PE)": info.get('trailingPE', '無資料'),
            "PEG 比例": info.get('pegRatio', '無資料'),
            "股東權益報酬率 (ROE)": info.get('returnOnEquity', '無資料'),
            "營收成長時間 (最近季度)": info.get('lastFiscalYearEnd', '無資料')
        }
        
        # 轉換成 DataFrame 方便閱讀
        df = pd.DataFrame([data])
        
        print(f"✅ 資料抓取成功！")
        print("-" * 40)
        print(df.to_string(index=False))
        print("-" * 40)
        return df

    except Exception as e:
        print(f"💥 抓取失敗，原因: {e}")
        print("提示: 請確認輸入的是正確的台股編號 (如 2330)。")

if __name__ == "__main__":
    code = input("請輸入台股編號 (例如 2330): ")
    get_stock_fundamentals_v2(code)
