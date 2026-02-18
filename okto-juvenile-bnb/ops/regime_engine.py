from dataclasses import dataclass


@dataclass
class RegimeDecision:
    regime: str
    seed_side: str
    leverage: int
    lower: float
    upper: float
    grids: int
    allow_open_shorts: bool
    reason: str


def detect_regime(market):
    obi = float(market.get("obi", 0.0))
    rsi = float(market.get("rsi", 50.0))
    atr_pct = float(market.get("atr_pct", 0.0))

    if atr_pct >= 0.70:
        return "HIGH_VOL_BREAKOUT"
    if obi >= 0.12 and rsi >= 50:
        return "BULL"
    if obi <= -0.12 and rsi <= 50:
        return "BEAR"
    return "RANGE"


def recommend_grid(market, base_leverage=2, hard_max_leverage=10):
    price = float(market["price"])
    atr = float(market["atr"])
    atr_pct = float(market.get("atr_pct", 0.0))
    obi = float(market.get("obi", 0.0))
    regime = detect_regime(market)

    # Conservative defaults for small balance.
    leverage = max(1, min(int(base_leverage), hard_max_leverage))
    seed_side = "buy"
    allow_open_shorts = False

    if regime == "BULL":
        leverage = min(max(leverage, 2), 3, hard_max_leverage)
        seed_side = "buy"
        lower = price - (1.4 * atr)
        upper = price + (1.0 * atr)
        reason = "Bullish confluence: positive OBI + RSI >= 50."
    elif regime == "BEAR":
        leverage = min(max(leverage, 2), 3, hard_max_leverage)
        seed_side = "sell"
        lower = price - (1.0 * atr)
        upper = price + (1.4 * atr)
        reason = "Bearish confluence: negative OBI + RSI <= 50."
    elif regime == "HIGH_VOL_BREAKOUT":
        leverage = min(2, hard_max_leverage)
        seed_side = "buy" if obi >= 0 else "sell"
        lower = price - (2.2 * atr)
        upper = price + (2.2 * atr)
        reason = "High volatility breakout mode. Wider range, lower leverage."
    else:
        leverage = min(2, hard_max_leverage)
        seed_side = "both"
        lower = price - (1.2 * atr)
        upper = price + (1.2 * atr)
        reason = "Range mode: balanced grid and reduced directional bias."

    # Grid density: adapt by volatility, then clamp to practical bounds.
    # Low ATR% -> more levels; high ATR% -> fewer levels.
    if atr_pct <= 0.20:
        grids = 6
    elif atr_pct <= 0.45:
        grids = 4
    else:
        grids = 3

    lower = round(max(0.01, lower), 2)
    upper = round(max(lower + 0.2, upper), 2)

    return RegimeDecision(
        regime=regime,
        seed_side=seed_side,
        leverage=leverage,
        lower=lower,
        upper=upper,
        grids=grids,
        allow_open_shorts=allow_open_shorts,
        reason=reason,
    )


class RegimeEngine:
    def __init__(self, symbol):
        self.symbol = symbol

    def detect_regime(self, market):
        return detect_regime(market)

    def recommend(self, market, base_leverage=2, hard_max_leverage=10):
        return recommend_grid(market, base_leverage, hard_max_leverage)
