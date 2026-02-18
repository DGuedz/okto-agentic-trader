def evaluate_confluence(market, regime):
    obi = float(market.get("obi", 0.0))
    rsi = float(market.get("rsi", 50.0))
    atr_pct = float(market.get("atr_pct", 0.0))
    spread_pct = float(market.get("spread_pct", 0.0))

    checks = []
    if regime == "BULL":
        checks.append(("OBI_BULL", obi > 0.10))
        checks.append(("RSI_BULL", rsi >= 50))
    elif regime == "BEAR":
        checks.append(("OBI_BEAR", obi < -0.10))
        checks.append(("RSI_BEAR", rsi <= 50))
    else:
        checks.append(("OBI_NEUTRAL", -0.10 <= obi <= 0.10))
        checks.append(("RSI_NEUTRAL", 40 <= rsi <= 60))

    checks.append(("ATR_OK", 0.08 <= atr_pct <= 1.20))
    checks.append(("SPREAD_OK", spread_pct <= 0.03))

    score = sum(1 for _, ok in checks if ok)
    return {
        "score": score,
        "total": len(checks),
        "checks": checks,
        "confirmed": score >= 3,
    }


class ConfluenceEngine:
    def evaluate(self, regime_data):
        regime = regime_data.get("regime", "RANGE")
        indicators = regime_data.get("indicators", {})
        result = evaluate_confluence(indicators, regime)
        score = result["score"]
        reasons = [name for name, ok in result["checks"] if ok]

        if score < 2:
            action = "HALT"
        elif regime == "BULL" and score >= 3:
            action = "LONG"
        elif regime == "BEAR" and score >= 3:
            action = "SHORT"
        else:
            action = "NEUTRAL"

        return {
            "action": action,
            "score": score,
            "reasons": reasons,
            "checks": result["checks"],
        }
