# Binance Data Schema Reference

## SPOT 现货数据

### Klines (K线)

来源 API: `/api/v3/klines`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | open_time | int | 开盘时间 (毫秒/微秒*) |
| 1 | open | string | 开盘价 |
| 2 | high | string | 最高价 |
| 3 | low | string | 最低价 |
| 4 | close | string | 收盘价 |
| 5 | volume | string | 成交量 (base asset) |
| 6 | close_time | int | 收盘时间 |
| 7 | quote_asset_volume | string | 成交额 (quote asset) |
| 8 | number_of_trades | int | 成交笔数 |
| 9 | taker_buy_base_volume | string | 主动买入成交量 |
| 10 | taker_buy_quote_volume | string | 主动买入成交额 |
| 11 | ignore | string | 忽略字段 |

*注: 2025年1月1日起时间戳为微秒级

### Trades (逐笔成交)

来源 API: `/api/v3/historicalTrades`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | trade_id | int | 成交ID |
| 1 | price | string | 成交价格 |
| 2 | qty | string | 成交数量 |
| 3 | quote_qty | string | 成交金额 |
| 4 | time | int | 成交时间 |
| 5 | is_buyer_maker | bool | 买方是否为maker |
| 6 | is_best_match | bool | 是否最优匹配 |

### AggTrades (聚合成交)

来源 API: `/api/v3/aggTrades`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | agg_trade_id | int | 聚合成交ID |
| 1 | price | string | 成交价格 |
| 2 | quantity | string | 成交数量 |
| 3 | first_trade_id | int | 首笔成交ID |
| 4 | last_trade_id | int | 末笔成交ID |
| 5 | timestamp | int | 成交时间 |
| 6 | is_buyer_maker | bool | 买方是否为maker |
| 7 | is_best_match | bool | 是否最优匹配 |

---

## USD-M Futures (U本位合约)

### Klines

来源 API: `/fapi/v1/klines`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | open_time | int | 开盘时间 |
| 1 | open | string | 开盘价 |
| 2 | high | string | 最高价 |
| 3 | low | string | 最低价 |
| 4 | close | string | 收盘价 |
| 5 | volume | string | 成交量 |
| 6 | close_time | int | 收盘时间 |
| 7 | quote_asset_volume | string | 成交额 |
| 8 | number_of_trades | int | 成交笔数 |
| 9 | taker_buy_base_volume | string | 主动买入成交量 |
| 10 | taker_buy_quote_volume | string | 主动买入成交额 |
| 11 | ignore | string | 忽略字段 |

### Trades

来源 API: `/fapi/v1/trades`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | trade_id | int | 成交ID |
| 1 | price | string | 成交价格 |
| 2 | qty | string | 成交数量 |
| 3 | quote_qty | string | 成交金额 |
| 4 | time | int | 成交时间 |
| 5 | is_buyer_maker | bool | 买方是否为maker |

### AggTrades

来源 API: `/fapi/v1/aggTrades`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | agg_trade_id | int | 聚合成交ID |
| 1 | price | string | 成交价格 |
| 2 | quantity | string | 成交数量 |
| 3 | first_trade_id | int | 首笔成交ID |
| 4 | last_trade_id | int | 末笔成交ID |
| 5 | timestamp | int | 成交时间 |
| 6 | is_buyer_maker | bool | 买方是否为maker |

---

## COIN-M Futures (币本位合约)

### Klines

来源 API: `/dapi/v1/klines`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | open_time | int | 开盘时间 |
| 1 | open | string | 开盘价 |
| 2 | high | string | 最高价 |
| 3 | low | string | 最低价 |
| 4 | close | string | 收盘价 |
| 5 | volume | string | 成交量 (合约张数) |
| 6 | close_time | int | 收盘时间 |
| 7 | base_asset_volume | string | 成交量 (base asset) |
| 8 | number_of_trades | int | 成交笔数 |
| 9 | taker_buy_volume | string | 主动买入成交量 (张) |
| 10 | taker_buy_base_volume | string | 主动买入成交量 (base) |
| 11 | ignore | string | 忽略字段 |

### Trades

来源 API: `/dapi/v1/trades`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | trade_id | int | 成交ID |
| 1 | price | string | 成交价格 |
| 2 | qty | string | 成交数量 (张) |
| 3 | base_qty | string | 成交数量 (base asset) |
| 4 | time | int | 成交时间 |
| 5 | is_buyer_maker | bool | 买方是否为maker |

### AggTrades

来源 API: `/dapi/v1/aggTrades`

与 USD-M AggTrades 结构相同。

---

## 期货专用数据

### Index Price Klines (指数价格K线)

与普通 Klines 结构相同，但价格为指数价格。

### Mark Price Klines (标记价格K线)

与普通 Klines 结构相同，但价格为标记价格。

### Premium Index Klines (溢价指数K线)

与普通 Klines 结构相同，反映期货与现货的价差。

### Funding Rate (资金费率)

**仅提供月度数据**

来源 API: `/fapi/v1/fundingRate` 或 `/dapi/v1/fundingRate`

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | symbol | string | 交易对 |
| 1 | fundingTime | int | 资金费率时间 (毫秒) |
| 2 | fundingRate | string | 资金费率 |

资金费率每 8 小时结算一次（00:00, 08:00, 16:00 UTC）。

### Metrics (市场指标)

**仅提供日度数据**

| 列索引 | 字段名 | 类型 | 说明 |
|-------|--------|------|------|
| 0 | create_time | int | 创建时间 |
| 1 | symbol | string | 交易对 |
| 2 | sum_open_interest | string | 未平仓合约总量 |
| 3 | sum_open_interest_value | string | 未平仓合约总价值 |
| 4 | count_toptrader_long_short_ratio | string | 大户多空人数比 |
| 5 | sum_toptrader_long_short_ratio | string | 大户多空持仓比 |
| 6 | count_long_short_ratio | string | 多空人数比 |
| 7 | sum_taker_long_short_vol_ratio | string | 主动买卖量比 |

---

## 数据读取示例

```python
import pandas as pd
import zipfile

# 读取 klines
with zipfile.ZipFile('BTCUSDT-1h-2024-01.zip') as z:
    with z.open(z.namelist()[0]) as f:
        df = pd.read_csv(f, header=None)
        df.columns = [
            'open_time', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_volume', 'trades', 'taker_buy_base',
            'taker_buy_quote', 'ignore'
        ]

# 转换时间戳
df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')

# 转换价格为数值
for col in ['open', 'high', 'low', 'close', 'volume']:
    df[col] = df[col].astype(float)
```
