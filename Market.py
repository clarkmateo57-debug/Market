import streamlit as st

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

st.title("Live CTA Strategy")
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

import streamlit as st

# ---- HEADER ----
st.markdown("""
<div class="header">
    <h1>⚡ Live CTA Trading System</h1>
    <p>Real-time futures trading with predictive analytics</p>
</div>
""", unsafe_allow_html=True)

# ---- STATUS BAR ----
status_left, status_right = st.columns([3, 1])

with status_left:
    st.markdown("""
    <div class="status-indicator">
        <div class="live-dot"></div>
        <span><strong>LIVE MARKET DATA</strong> - Real-time streaming</span>
    </div>
    """, unsafe_allow_html=True)

with status_right:
    timestamp_placeholder = st.empty()   # replaces <div id="timestamp"></div>

# ---- GRID 1 ----
col_markets, col_orders = st.columns([2, 1])

with col_markets:
    st.markdown("<h3>📊 Active Markets</h3>", unsafe_allow_html=True)
    markets_container = st.container()   # replaces <div id="markets"></div>

with col_orders:
    st.markdown("<h3>📈 Order Flow</h3>", unsafe_allow_html=True)
    order_feed = st.container()          # replaces <div id="orderFeed"></div>

# ---- GRID 2 ----
col_stats, col_equity = st.columns([2, 1])

with col_stats:
    st.markdown("<h3>💼 Portfolio Statistics</h3>", unsafe_allow_html=True)

    s1, s2 = st.columns(2)
    s3, s4 = st.columns(2)

    total_orders = s1.metric("Total Orders", 0)
    long_positions = s2.metric("Long Positions", 0)
    short_positions = s3.metric("Short Positions", 0)
    total_contracts = s4.metric("Total Contracts", 0)

with col_equity:
    st.markdown("<h3>📉 Portfolio Equity</h3>", unsafe_allow_html=True)
    equity_chart_placeholder = st.empty()   # replaces <canvas id="equityChart"></canvas>
    <script>
       markets = [
    { "name": "Crude Oil (CL)", "symbol": "CL", "price": 72.50, "volatility": 0.025, "trend": 0.001 },
    { "name": "Gold (GC)", "symbol": "GC", "price": 2050.00, "volatility": 0.015, "trend": 0.0005 },
    { "name": "S&P 500 (ES)", "symbol": "ES", "price": 4780.00, "volatility": 0.018, "trend": 0.0008 },
    { "name": "EUR/USD (EC)", "symbol": "EC", "price": 1.0950, "volatility": 0.012, "trend": -0.0003 },
    { "name": "Treasury (ZN)", "symbol": "ZN", "price": 110.50, "volatility": 0.01, "trend": -0.0002 },
    { "name": "Natural Gas (NG)", "symbol": "NG", "price": 2.85, "volatility": 0.035, "trend": 0.002 }
]
        
        var params = {
            fastMA: 10,
            slowMA: 30,
            riskPerTrade: 2,
            atrPeriod: 14
        };
        
        var priceHistory = {};
        var orders = [];
        var positions = {};
        var equity = [100000];
        var totalOrders = 0;
        var equityChart;
        
        for (var i = 0; i < markets.length; i++) {
            var m = markets[i];
            priceHistory[m.symbol] = [];
            for (var j = 0; j < 100; j++) {
                priceHistory[m.symbol].push(m.price * (1 + (Math.random() - 0.5) * m.volatility * 0.5));
            }
            positions[m.symbol] = { contracts: 0, side: null, entry: 0 };
        }
        
        function calculateMA(prices, period) {
            if (prices.length < period) return null;
            var slice = prices.slice(-period);
            var sum = 0;
            for (var i = 0; i < slice.length; i++) {
                sum += slice[i];
            }
            return sum / period;
        }
        
        function calculateATR(prices, period) {
            if (prices.length < period + 1) return null;
            var ranges = [];
            for (var i = prices.length - period; i < prices.length; i++) {
                ranges.push(Math.abs(prices[i] - prices[i - 1]));
            }
            var sum = 0;
            for (var i = 0; i < ranges.length; i++) {
                sum += ranges[i];
            }
            return sum / ranges.length;
        }
        
        function predictNextPrice(prices) {
            var n = prices.length;
            if (n < 3) return prices[n - 1];
            
            var velocity = prices[n - 1] - prices[n - 2];
            var acceleration = prices[n - 1] - 2 * prices[n - 2] + prices[n - 3];
            var prediction = prices[n - 1] + velocity + 0.5 * acceleration;
            
            return prediction;
        }
        
        function calculateMomentum(prices) {
            var n = prices.length;
            if (n < 10) return 0;
            return (prices[n - 1] - prices[n - 10]) / prices[n - 10];
        }
        
        function executeOrder(market, side, contracts, reason) {
            var timestamp = new Date().toLocaleTimeString();
            var order = {
                timestamp: timestamp,
                market: market.name,
                symbol: market.symbol,
                side: side,
                contracts: contracts,
                price: market.price,
                reason: reason
            };
            
            orders.unshift(order);
            if (orders.length > 50) orders.pop();
            
            totalOrders++;
            
            if (side === 'CLOSE') {
                positions[market.symbol] = { contracts: 0, side: null, entry: 0 };
            } else {
                positions[market.symbol] = {
                    contracts: contracts,
                    side: side,
                    entry: market.price
                };
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
