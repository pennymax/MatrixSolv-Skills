---
name: binance-data
description: Binance 公开历史数据查询与下载助手。帮助用户了解 Binance 提供的历史市场数据类型、数据 schema、URL 结构，并协助下载数据。使用场景：(1) 查询 Binance 有哪些历史数据可用，(2) 了解数据字段含义和 schema，(3) 构建数据下载 URL，(4) 下载 klines/trades/aggTrades/fundingRate/metrics 等历史数据，(5) 获取交易对列表。触发词：Binance 数据、历史行情、K线下载、交易数据、aggTrades、资金费率、fundingRate、币安数据。
---

# Binance Public Data

帮助用户查询和下载 Binance 公开历史市场数据。

## 数据源

- 官方网站: https://data.binance.vision/
- 数据基础 URL: `https://data.binance.vision/`
- 数据从 2020-01-01 开始提供

## 可用数据类型

### 1. SPOT 现货数据

**注意**: 2025年1月1日起，SPOT 数据时间戳改为微秒级。

| 数据类型 | 说明 |
|---------|------|
| klines | K线数据 |
| trades | 逐笔成交 |
| aggTrades | 聚合成交 |

### 2. Futures 期货数据

| 市场类型 | 代码 | API 端点 |
|---------|------|----------|
| USD-M Futures | um | fapi.binance.com |
| COIN-M Futures | cm | dapi.binance.com |

期货额外数据类型：
- indexPriceKlines - 指数价格K线
- markPriceKlines - 标记价格K线
- premiumIndexKlines - 溢价指数K线
- **fundingRate** - 资金费率（仅月度数据）
- **metrics** - 市场指标数据（仅日度数据）

## 数据 Schema

详细字段定义见 [references/schema.md](references/schema.md)。

## URL 结构

```
https://data.binance.vision/data/{market}/{period}/{data_type}/{symbol}/{interval}/{filename}
```

参数说明：
- `market`: spot | futures/um | futures/cm
- `period`: daily | monthly
- `data_type`: klines | trades | aggTrades | fundingRate | metrics
- `symbol`: 交易对，如 BTCUSDT
- `interval`: K线周期（仅 klines 需要）
- `filename`: {SYMBOL}-{data_type}-{date}.zip

### K线周期

`1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1mo`

### URL 示例

```bash
# 现货月度 K线
https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1h/BTCUSDT-1h-2024-01.zip

# 现货日度 K线
https://data.binance.vision/data/spot/daily/klines/BTCUSDT/1m/BTCUSDT-1m-2024-01-15.zip

# USD-M 期货 aggTrades
https://data.binance.vision/data/futures/um/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-2024-01-15.zip

# USD-M 期货资金费率（月度）
https://data.binance.vision/data/futures/um/monthly/fundingRate/BTCUSDT/BTCUSDT-fundingRate-2024-01.zip

# USD-M 期货 metrics（日度）
https://data.binance.vision/data/futures/um/daily/metrics/BTCUSDT/BTCUSDT-metrics-2024-01-15.zip
```

## 下载数据

### 方式一：直接下载

```bash
# 使用 curl
curl -O "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1h/BTCUSDT-1h-2024-01.zip"

# 使用 wget
wget "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1h/BTCUSDT-1h-2024-01.zip"
```

### 方式二：使用下载脚本

使用 [scripts/download_binance_data.py](scripts/download_binance_data.py)：

```bash
# 下载现货 K线
python download_binance_data.py -t spot -s BTCUSDT -i 1h --start-date 2024-01-01 --end-date 2024-01-31

# 下载期货 aggTrades
python download_binance_data.py -t um -s BTCUSDT --data-type aggTrades --start-date 2024-01-01

# 下载期货资金费率（月度）
python download_binance_data.py -t um -s BTCUSDT --data-type fundingRate --period monthly --start-date 2024-01-01

# 下载期货 metrics（日度）
python download_binance_data.py -t um -s BTCUSDT --data-type metrics --start-date 2024-01-01
```

## 获取交易对列表

```python
import urllib.request
import json

# 现货
resp = urllib.request.urlopen("https://api.binance.com/api/v3/exchangeInfo")
symbols = [s['symbol'] for s in json.loads(resp.read())['symbols']]

# USD-M 期货
resp = urllib.request.urlopen("https://fapi.binance.com/fapi/v1/exchangeInfo")
symbols = [s['symbol'] for s in json.loads(resp.read())['symbols']]

# COIN-M 期货
resp = urllib.request.urlopen("https://dapi.binance.com/dapi/v1/exchangeInfo")
symbols = [s['symbol'] for s in json.loads(resp.read())['symbols']]
```

## 数据校验

每个 zip 文件都有对应的 `.CHECKSUM` 文件：

```bash
# Linux
sha256sum -c BTCUSDT-1h-2024-01.zip.CHECKSUM

# macOS
shasum -a 256 -c BTCUSDT-1h-2024-01.zip.CHECKSUM
```

## 常见任务

### 查询可用数据
1. 确定市场类型 (spot/um/cm)
2. 确定数据类型 (klines/trades/aggTrades/fundingRate/metrics)
3. 确定时间范围和周期
4. 注意：fundingRate 仅有月度数据，metrics 仅有日度数据

### 批量下载
使用脚本批量下载，支持：
- 多交易对
- 日期范围
- 自动跳过已存在文件
- 校验文件下载
