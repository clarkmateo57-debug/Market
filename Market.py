import streamlit as st

# ---------------- CSS BLOCK 1 ----------------
st.markdown("""
<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #fff;
    min-height: 100vh;
}

.container {
    padding: 20px;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: 12px;
    max-width: 1600px;
    margin: 0 auto;
}

.header {
    text-align: center;
    margin-bottom: 30px;
}

.header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    color: #60a5fa;
}

.status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(30, 41, 59, 0.8);
    padding: 15px 25px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(96, 165, 250, 0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("Live CTA Strategy")

# ---------------- CSS BLOCK 2 ----------------
st.markdown("""
<style>

.status-indicator {
    display: flex;
    align-items: center;
    gap: 10px;
}

.live-dot {
    width: 12px;
    height: 12px;
    background: #10b981;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

.grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.card {
    background: rgba(30, 41, 59, 0.8);
    border-radius: 12px;
    padding: 20px;
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.card h3 {
    font-size: 1.2em;
    margin-bottom: 15px;
    color: #60a5fa;
}

.market-item {
    background: rgba(15, 23, 42, 0.6);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
    border-left: 4px solid #60a5fa;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.market-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.market-name {
    font-weight: bold;
    font-size: 1.1em;
}

.market-price {
    font-size: 1.3em;
    font-weight: bold;
}

.price-up {
    color: #10b981;
}

.price-down {
    color: #ef4444;
}

.market-details {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 10px;
    font-size: 0.9em;
}

.detail-item {
    display: flex;
    justify-content: space-between;
}

.label {
    color: #94a3b8;
}

.order-feed {
    height: 400px;
    overflow-y: auto;
    background: rgba(15, 23, 42, 0.6);
    padding: 15px;
    border-radius: 8px;
}

.order-item {
    padding: 10px;
    margin-bottom: 8px;
    border-radius: 6px;
    border-left: 3px solid;
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-10px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.order-long {
    background: rgba(16, 185, 129, 0.1);
    border-color: #10b981;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.order-short {
    background: rgba(239, 68, 68, 0.1);
    border-color: #ef4444;
}

.order-close {
    background: rgba(96, 165, 250, 0.1);
    border-color: #60a5fa;
}

.order-header {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    margin-bottom: 5px;
}

.order-details {
    font-size: 0.85em;
    color: #94a3b8;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
}

.stat-box {
    background: rgba(15, 23, 42, 0.6);
    padding: 15px;
    border-radius: 8px;
    text-align: center;
}

.stat-label {
    color: #94a3b8;
    font-size: 0.9em;
    margin-bottom: 5px;
}

.stat-value {
    font-size: 1.8em;
    font-weight: bold;
}

.prediction-box {
    background: rgba(139, 92, 246, 0.1);
    border: 1px solid rgba(139, 92, 246, 0.3);
    padding: 15px;
    border-radius: 8px;
    margin-top: 10px;
}

.prediction-label {
    color: #a78bfa;
    font-size: 0.9em;
    margin-bottom: 5px;
}

</style>
""", unsafe_allow_html=True)

import streamlit as st

# ---------------- CSS BLOCK ----------------
st.markdown("""
<style>

.prediction-value {
    font-size: 1.3em;
    font-weight: bold;
    color: #c4b5fd;
}

canvas {
    max-height: 300px;
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.4);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: rgba(96, 165, 250, 0.3);
    border-radius: 4px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>⚡ Live CTA Trading System</h1>
    <p>Real-time futures trading with predictive analytics</p>
</div>
""", unsafe_allow_html=True)

# ---------------- STATUS BAR ----------------
status_left, status_right = st.columns([3, 1])

with status_left:
    st.markdown("""
    <div class="status-indicator">
        <div class="live-dot"></div>
        <span><strong>LIVE MARKET DATA</strong> - Real-time streaming</span>
    </div>
    """, unsafe_allow_html=True)

with status_right:
    timestamp_placeholder = st.empty()

# ---------------- GRID 1 ----------------
col_markets, col_orders = st.columns([2, 1])

with col_markets:
    st.markdown("<h3>📊 Active Markets</h3>", unsafe_allow_html=True)
    markets_container = st.container()

with col_orders:
    st.markdown("<h3>📈 Order Flow</h3>", unsafe_allow_html=True)
    order_feed = st.container()

# ---------------- GRID 2 ----------------
col_stats, col_equity = st.columns([2, 1])

with col_stats:
    st.markdown("<h3>💼 Portfolio Statistics</h3>", unsafe_allow_html=True)

    s1, s2 = st.columns(2)
    s3, s4 = st.columns(2)

    import streamlit as st
import random
from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

# =========================
# CSS (merged into one block)
# =========================
st.markdown("""
<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #fff;
    min-height: 100vh;
}

.container {
    padding: 20px;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border-radius: 12px;
    max-width: 1600px;
    margin: 0 auto;
}

.header {
    text-align: center;
    margin-bottom: 30px;
}

.header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
    color: #60a5fa;
}

.status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(30, 41, 59, 0.8);
    padding: 15px 25px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.status-indicator {
    display: flex;
    align-items: center;
    gap: 10px;
}

.live-dot {
    width: 12px;
    height: 12px;
    background: #10b981;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

.grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
}

.card {
    background: rgba(30, 41, 59, 0.8);
    border-radius: 12px;
    padding: 20px;
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.card h3 {
    font-size: 1.2em;
    margin-bottom: 15px;
    color: #60a5fa;
}

.market-item {
    background: rgba(15, 23, 42, 0.6);
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
    border-left: 4px solid #60a5fa;
}

.market-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.market-name {
    font-weight: bold;
    font-size: 1.1em;
}

.market-price {
    font-size: 1.3em;
    font-weight: bold;
}

.price-up {
    color: #10b981;
}

.price-down {
    color: #ef4444;
}

.market-details {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 10px;
    font-size: 0.9em;
}

.detail-item {
    display: flex;
    justify-content: space-between;
}

.label {
    color: #94a3b8;
}

.order-feed {
    height: 400px;
    overflow-y: auto;
    background: rgba(15, 23, 42, 0.6);
    padding: 15px;
    border-radius: 8px;
}

.order-item {
    padding: 10px;
    margin-bottom: 8px;
    border-radius: 6px;
    border-left: 3px solid;
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-10px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.order-long {
    background: rgba(16, 185, 129, 0.1);
    border-color: #10b981;
}

.order-short {
    background: rgba(239, 68, 68, 0.1);
    border-color: #ef4444;
}

.order-close {
    background: rgba(96, 165, 250, 0.1);
    border-color: #60a5fa;
}

.order-header {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    margin-bottom: 5px;
}

.order-details {
    font-size: 0.85em;
    color: #94a3b8;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
}

.stat-box {
    background: rgba(15, 23, 42, 0.6);
    padding: 15px;
    border-radius: 8px;
    text-align: center;
}

.stat-label {
    color: #94a3b8;
    font-size: 0.9em;
    margin-bottom: 5px;
}

.stat-value {
    font-size: 1.8em;
    font-weight: bold;
}

.prediction-box {
    background: rgba(139, 92, 246, 0.1);
    border: 1px solid rgba(139, 92, 246, 0.3);
    padding: 15px;
    border-radius: 8px;
    margin-top: 10px;
}

.prediction-label {
    color: #a78bfa;
    font-size: 0.9em;
    margin-bottom: 5px;
}

.prediction-value {
    font-size: 1.3em;
    font-weight: bold;
    color: #c4b5fd;
}

canvas {
    max-height: 300px;
}

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.4);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: rgba(96, 165, 250, 0.3);
    border-radius: 4px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ENGINE: data structures
# =========================

@dataclass
class Market:
    name: str
    symbol: str
    price: float
    volatility: float
    trend: float

@dataclass
class Position:
    contracts: int = 0
    side: Optional[str] = None  # "LONG", "SHORT", or None
    entry: float = 0.0

@dataclass
class Order:
    timestamp: str
    market: str
    symbol: str
    side: str
    contracts: int
    price: float
    reason: str

# Engine parameters (from your JS)
PARAMS = {
    "fastMA": 10,
    "slowMA": 30,
    "riskPerTrade": 2,  # percent of equity
    "atrPeriod": 14
}

INITIAL_MARKETS: List[Market] = [
    Market("Crude Oil (CL)", "CL", 72.50, 0.025, 0.001),
    Market("Gold (GC)", "GC", 2050.00, 0.015, 0.0005),
    Market("S&P 500 (ES)", "ES", 4780.00, 0.018, 0.0008),
    Market("EUR/USD (EC)", "EC", 1.0950, 0.012, -0.0003),
    Market("Treasury (ZN)", "ZN", 110.50, 0.01, -0.0002),
    Market("Natural Gas (NG)", "NG", 2.85, 0.035, 0.002),
]

# =========================
# ENGINE: initialization
# =========================

def init_engine_state(state):
    if "markets" not in state:
        state.markets = [Market(m.name, m.symbol, m.price, m.volatility, m.trend) for m in INITIAL_MARKETS]

    if "price_history" not in state:
        state.price_history: Dict[str, List[float]] = {}
        for m in state.markets:
            prices = []
            for _ in range(100):
                shock = (random.random() - 0.5) * m.volatility * 0.5
                prices.append(m.price * (1 + shock))
            state.price_history[m.symbol] = prices

    if "positions" not in state:
        state.positions: Dict[str, Position] = {m.symbol: Position() for m in state.markets}

    if "orders" not in state:
        state.orders: List[Order] = []

    if "equity" not in state:
        state.equity: List[float] = [100_000.0]

    if "total_orders" not in state:
        state.total_orders: int = 0

# =========================
# ENGINE: indicators
# =========================

def calculate_ma(prices: List[float], period: int) -> Optional[float]:
    if len(prices) < period:
        return None
    slice_ = prices[-period:]
    return sum(slice_) / len(slice_)

def calculate_atr(prices: List[float], period: int) -> Optional[float]:
    if len(prices) < period + 1:
        return None
    ranges = []
    for i in range(len(prices) - period, len(prices)):
        ranges.append(abs(prices[i] - prices[i - 1]))
    return sum(ranges) / len(ranges)

def predict_next_price(prices: List[float]) -> float:
    n = len(prices)
    if n < 3:
        return prices[-1]
    velocity = prices[n - 1] - prices[n - 2]
    acceleration = prices[n - 1] - 2 * prices[n - 2] + prices[n - 3]
    return prices[n - 1] + velocity + 0.5 * acceleration

def calculate_momentum(prices: List[float]) -> float:
    n = len(prices)
    if n < 10:
        return 0.0
    return (prices[n - 1] - prices[n - 10]) / prices[n - 10]

# =========================
# ENGINE: orders & equity
# =========================

def execute_order(state, market: Market, side: str, contracts: int, reason: str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    order = Order(
        timestamp=timestamp,
        market=market.name,
        symbol=market.symbol,
        side=side,
        contracts=contracts,
        price=market.price,
        reason=reason
    )

    state.orders.insert(0, order)
    state.orders = state.orders[:50]  # keep last 50
    state.total_orders += 1

    if side == "CLOSE":
        state.positions[market.symbol] = Position()
    else:
        state.positions[market.symbol] = Position(
            contracts=contracts,
            side=side,
            entry=market.price
        )

def update_equity_from_positions(state):
    last_equity = state.equity[-1]
    pnl = 0.0
    for m in state.markets:
        pos = state.positions[m.symbol]
        if pos.contracts == 0 or pos.side is None:
            continue
        direction = 1 if pos.side == "LONG" else -1
        pnl += direction * pos.contracts * (m.price - pos.entry)
    state.equity.append(last_equity + pnl)

# =========================
# ENGINE: one simulation step
# =========================

def simulate_step(state):
    # update prices
    for i, m in enumerate(state.markets):
        prices = state.price_history[m.symbol]
        last_price = prices[-1]
        shock = (random.random() - 0.5) * m.volatility
        new_price = last_price * (1 + shock + m.trend)
        state.markets[i].price = new_price
        state.price_history[m.symbol].append(new_price)

    # trading logic
    for m in state.markets:
        prices = state.price_history[m.symbol]
        fast = calculate_ma(prices, PARAMS["fastMA"])
        slow = calculate_ma(prices, PARAMS["slowMA"])
        atr = calculate_atr(prices, PARAMS["atrPeriod"])
        prediction = predict_next_price(prices)
        momentum = calculate_momentum(prices)

        if fast is None or slow is None or atr is None:
            continue

        pos = state.positions[m.symbol]
        equity_now = state.equity[-1]
        risk_amount = equity_now * (PARAMS["riskPerTrade"] / 100.0)
        contracts = max(1, int(risk_amount / max(atr, 1e-6)))

        reason = None
        side = None

        if fast > slow and momentum > 0 and prediction > prices[-1]:
            if pos.side != "LONG":
                side = "LONG"
                reason = "Trend-following long entry"
        elif fast < slow and momentum < 0 and prediction < prices[-1]:
            if pos.side != "SHORT":
                side = "SHORT"
                reason = "Trend-following short entry"
        elif pos.side is not None:
            side = "CLOSE"
            reason = "Exit on signal reversal"

        if side is not None:
            execute_order(state, m, side, contracts, reason)

    update_equity_from_positions(state)

# =========================
# STREAMLIT UI
# =========================

init_engine_state(st.session_state)

st.markdown('<div class="container">', unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1>⚡ Live CTA Trading System</h1>
    <p>Real-time futures trading with predictive analytics</p>
</div>
""", unsafe_allow_html=True)

# Status bar
status_left, status_right = st.columns([3, 1])
with status_left:
    st.markdown("""
    <div class="status-bar">
        <div class="status-indicator">
            <div class="live-dot"></div>
            <span><strong>LIVE MARKET DATA</strong> - Real-time streaming</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
with status_right:
    st.markdown(
        f"<div id='timestamp'>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>",
        unsafe_allow_html=True
    )

# Controls
st.write("")
c1, c2 = st.columns(2)
with c1:
    if st.button("Run 1 step"):
        simulate_step(st.session_state)
with c2:
    if st.button("Run 10 steps"):
        for _ in range(10):
            simulate_step(st.session_state)

# Grid 1: Active markets & Order flow
left1, right1 = st.columns([2, 1])

with left1:
    st.markdown('<div class="card"><h3>📊 Active Markets</h3>', unsafe_allow_html=True)
    for m in st.session_state.markets:
        prices = st.session_state.price_history[m.symbol]
        last = prices[-1]
        prev = prices[-2] if len(prices) > 1 else last
        change = last - prev
        direction_class = "price-up" if change >= 0 else "price-down"
        st.markdown(f"""
        <div class="market-item">
            <div class="market-header">
                <div class="market-name">{m.name}</div>
                <div class="market-price {direction_class}">{last:.2f}</div>
            </div>
            <div class="market-details">
                <div class="detail-item">
                    <span class="label">Symbol</span><span>{m.symbol}</span>
                </div>
                <div class="detail-item">
                    <span class="label">Volatility</span><span>{m.volatility:.3f}</span>
                </div>
                <div class="detail-item">
                    <span class="label">Trend</span><span>{m.trend:.4f}</span>
                </div>
                <div class="detail-item">
                    <span class="label">Δ Price</span><span class="{direction_class}">{change:+.2f}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right1:
    st.markdown('<div class="card"><h3>📈 Order Flow</h3><div class="order-feed">', unsafe_allow_html=True)
    for order in st.session_state.orders:
        if order.side == "LONG":
            cls = "order-item order-long"
        elif order.side == "SHORT":
            cls = "order-item order-short"
        else:
            cls = "order-item order-close"
        st.markdown(f"""
        <div class="{cls}">
            <div class="order-header">
                <span>{order.timestamp} — {order.symbol} ({order.market})</span>
                <span>{order.side} {order.contracts} @ {order.price:.2f}</span>
            </div>
            <div class="order-details">
                {order.reason}
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

# Grid 2: Stats & Equity
left2, right2 = st.columns([2, 1])

with left2:
    st.markdown('<div class="card"><h3>💼 Portfolio Statistics</h3>', unsafe_allow_html=True)

    positions: Dict[str, Position] = st.session_state.positions
    total_orders = st.session_state.total_orders
    long_positions = sum(1 for p in positions.values() if p.side == "LONG")
    short_positions = sum(1 for p in positions.values() if p.side == "SHORT")
    total_contracts = sum(p.contracts for p in positions.values())

    st.markdown('<div class="stats-grid">', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-label">Total Orders</div>
        <div class="stat-value" id="totalOrders">{total_orders}</div>
    </div>
    <div class="stat-box">
        <div class="stat-label">Long Positions</div>
        <div class="stat-value price-up" id="longPositions">{long_positions}</div>
    </div>
    <div class="stat-box">
        <div class="stat-label">Short Positions</div>
        <div class="stat-value price-down" id="shortPositions">{short_positions}</div>
    </div>
    <div class="stat-box">
        <div class="stat-label">Total Contracts</div>
        <div class="stat-value" id="totalContracts">{total_contracts}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with right2:
    st.markdown('<div class="card"><h3>📉 Portfolio Equity</h3>', unsafe_allow_html=True)
    st.line_chart(st.session_state.equity)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
            }
            
            updateOrderFeed();
            updateStats();
        }
        
        function runStrategy() {
            for (var i = 0; i < markets.length; i++) {
                var market = markets[i];
                var prices = priceHistory[market.symbol];
                var fastMA = calculateMA(prices, params.fastMA);
                var slowMA = calculateMA(prices, params.slowMA);
                var atr = calculateATR(prices, params.atrPeriod);
                var prediction = predictNextPrice(prices);
                var momentum = calculateMomentum(prices);
                
                if (!fastMA || !slowMA || !atr) continue;
                
                var currentPrice = prices[prices.length - 1];
                var position = positions[market.symbol];
                
                var dollarRisk = equity[equity.length - 1] * (params.riskPerTrade / 100);
                var contracts = Math.max(1, Math.floor(dollarRisk / (atr * 100)));
                
                var trendSignal = fastMA > slowMA ? 1 : -1;
                var predictionSignal = prediction > currentPrice ? 1 : -1;
                var momentumSignal = momentum > 0.001 ? 1 : momentum < -0.001 ? -1 : 0;
                var combinedSignal = trendSignal + predictionSignal + momentumSignal;
                
                if (position.contracts === 0) {
                    if (combinedSignal >= 2) {
                        executeOrder(market, 'LONG', contracts, 'MA Cross + Prediction (' + prediction.toFixed(2) + ') + Momentum');
                    } else if (combinedSignal <= -2) {
                        executeOrder(market, 'SHORT', contracts, 'MA Cross + Prediction (' + prediction.toFixed(2) + ') + Momentum');
                    }
                } else {
                    if (position.side === 'LONG' && combinedSignal <= -1) {
                        executeOrder(market, 'CLOSE', position.contracts, 'Exit Long - Signal Reversal');
                    } else if (position.side === 'SHORT' && combinedSignal >= 1) {
                        executeOrder(market, 'CLOSE', position.contracts, 'Exit Short - Signal Reversal');
                    }
                }
                
                market.prediction = prediction;
                market.momentum = momentum;
            }
        }
        
        function updateMarkets() {
            for (var i = 0; i < markets.length; i++) {
                var market = markets[i];
                var random = (Math.random() - 0.5) * market.volatility;
                var trendComponent = market.trend;
                var noise = Math.sin(Date.now() / 10000) * market.volatility * 0.3;
                
                market.price = market.price * (1 + random + trendComponent + noise);
                
                priceHistory[market.symbol].push(market.price);
                if (priceHistory[market.symbol].length > 100) {
                    priceHistory[market.symbol].shift();
                }
            }
            
            var totalPnL = 0;
            for (var i = 0; i < markets.length; i++) {
                var market = markets[i];
                var pos = positions[market.symbol];
                if (pos.contracts > 0 && pos.entry > 0) {
                    var priceDiff = market.price - pos.entry;
                    var multiplier = pos.side === 'LONG' ? 1 : -1;
                    totalPnL += priceDiff * multiplier * pos.contracts * 100;
                }
            }
            
            equity.push(equity[0] + totalPnL);
            if (equity.length > 100) equity.shift();
            
            updateMarketsDisplay();
            updateEquityChart();
        }
        
        function updateMarketsDisplay() {
            var container = document.getElementById('markets');
            var html = '';
            
            for (var i = 0; i < markets.length; i++) {
                var market = markets[i];
                var prices = priceHistory[market.symbol];
                var change = prices[prices.length - 1] - prices[prices.length - 2];
                var changePercent = (change / prices[prices.length - 2]) * 100;
                var pos = positions[market.symbol];
                var fastMA = calculateMA(prices, params.fastMA);
                var slowMA = calculateMA(prices, params.slowMA);
                
                var posColor = pos.side === 'LONG' ? '#10b981' : pos.side === 'SHORT' ? '#ef4444' : '#94a3b8';
                var posText = pos.contracts > 0 ? pos.side + ' ' + pos.contracts : 'FLAT';
                
                html += '<div class="market-item">';
                html += '<div class="market-header">';
                html += '<span class="market-name">' + market.name + '</span>';
                html += '<span class="market-price ' + (change >= 0 ? 'price-up' : 'price-down') + '">';
                html += '$' + market.price.toFixed(2) + ' ' + (change >= 0 ? '▲' : '▼') + ' ' + Math.abs(changePercent).toFixed(2) + '%';
                html += '</span></div>';
                html += '<div class="market-details">';
                html += '<div class="detail-item"><span class="label">Fast MA:</span><span>' + (fastMA ? fastMA.toFixed(2) : '-') + '</span></div>';
                html += '<div class="detail-item"><span class="label">Slow MA:</span><span>' + (slowMA ? slowMA.toFixed(2) : '-') + '</span></div>';
                html += '<div class="detail-item"><span class="label">Position:</span><span style="color: ' + posColor + '">' + posText + '</span></div>';
                html += '<div class="detail-item"><span class="label">Momentum:</span><span>' + (market.momentum ? (market.momentum * 100).toFixed(2) + '%' : '-') + '</span></div>';
                html += '</div>';
                
                if (market.prediction) {
                    var predChange = ((market.prediction - market.price) / market.price * 100).toFixed(2);
                    html += '<div class="prediction-box">';
                    html += '<div class="prediction-label">🔮 Predicted Next Price (Calculus)</div>';
                    html += '<div class="prediction-value">$' + market.prediction.toFixed(2) + ' ';
                    html += (market.prediction > market.price ? '↗' : '↘') + ' ' + predChange + '%</div>';
                    html += '</div>';
                }
                
                html += '</div>';
            }
            
            container.innerHTML = html;
        }
        
        function updateOrderFeed() {
            var container = document.getElementById('orderFeed');
            var html = '';
            
            for (var i = 0; i < orders.length; i++) {
                var order = orders[i];
                var icon = order.side === 'LONG' ? '📈' : order.side === 'SHORT' ? '📉' : '✖';
                html += '<div class="order-item order-' + order.side.toLowerCase() + '">';
                html += '<div class="order-header">';
                html += '<span>' + icon + ' ' + order.side + '</span>';
                html += '<span>' + order.contracts + ' contracts</span>';
                html += '</div>';
                html += '<div class="order-details">';
                html += order.market + ' @ $' + order.price.toFixed(2) + '<br>';
                html += order.reason + '<br>';
                html += '<span style="color: #64748b">' + order.timestamp + '</span>';
                html += '</div></div>';
            }
            
            container.innerHTML = html;
        }
        
        function updateStats() {
            document.getElementById('totalOrders').textContent = totalOrders;
            
            var longCount = 0;
            var shortCount = 0;
            var totalContracts = 0;
            
            for (var key in positions) {
                var p = positions[key];
                if (p.side === 'LONG') longCount++;
                if (p.side === 'SHORT') shortCount++;
                totalContracts += p.contracts;
            }
            
            document.getElementById('longPositions').textContent = longCount;
            document.getElementById('shortPositions').textContent = shortCount;
            document.getElementById('totalContracts').textContent = totalContracts;
        }
        
        function updateEquityChart() {
            var data = [];
            for (var i = 0; i < equity.length; i++) {
                data.push({ x: i, y: equity[i] });
            }
            equityChart.data.datasets[0].data = data;
            equityChart.update('none');
        }
        
        function updateTimestamp() {
            document.getElementById('timestamp').textContent = new Date().toLocaleString();
        }
        
        function initChart() {
            var ctx = document.getElementById('equityChart').getContext('2d');
            equityChart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [{
                        label: 'Portfolio Value',
                        data: [],
                        borderColor: '#60a5fa',
                        backgroundColor: 'rgba(96, 165, 250, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: false }
                    },
                    scales: {
                        x: { display: false },
                        y: {
                            ticks: { color: '#94a3b8' },
                            grid: { color: 'rgba(148, 163, 184, 0.1)' }
                        }
                    },
                    animation: false
                }
            });
        }
        
        function mainLoop() {
            updateMarkets();
            runStrategy();
            updateTimestamp();
        }
        
        initChart();
        updateStats();
        setInterval(mainLoop, 500);
    </script>
</body>
</html>
