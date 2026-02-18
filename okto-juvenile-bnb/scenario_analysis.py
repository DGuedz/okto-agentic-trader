def analyze_scenarios(capital, target_profit_per_trade):
    print(f"\n🎯 ANÁLISE DE CENÁRIOS: Lucro Fixo de ${target_profit_per_trade:.2f} por Trade")
    print(f"💰 Capital Inicial: ${capital:.2f}")
    print("-" * 65)
    print(f"{'Leverage':<10} | {'Move % Nec.':<12} | {'Risco Liq.':<12} | {'Viabilidade':<15}")
    print("-" * 65)

    leverages = [5, 10, 20, 50, 75]
    
    for lev in leverages:
        # Cálculo: Para lucrar $0.50 com $11 de margem
        # Profit = Margin * Leverage * Move%
        # 0.50 = 11 * lev * Move%
        # Move% = 0.50 / (11 * lev)
        
        required_move_pct = (target_profit_per_trade / (capital * lev)) * 100
        liquidation_pct = 100 / lev # Aproximado
        
        # Avaliação de Viabilidade
        if required_move_pct > 1.0:
            status = "🔴 DIFÍCIL (Swing)"
        elif required_move_pct > 0.4:
            status = "🟡 MÉDIO (Intra)"
        elif required_move_pct > 0.1:
            status = "🟢 ÓTIMO (Scalp)"
        else:
            status = "⚡ AGRESSIVO (HFT)"
            
        print(f"{lev}x{'':<8} | {required_move_pct:.4f}%{'':<5} | -{liquidation_pct:.2f}%{'':<5} | {status}")

    print("-" * 65)
    print("\n📝 CONCLUSÃO TÉCNICA:")
    print("1. Para buscar $0.50 por trade com banca de $11:")
    print("   - 5x exige movimento de ~0.9% (muito longo para scalp rápido).")
    print("   - 20x exige movimento de ~0.22% (ideal para scalp, risco controlado).")
    print("   - 50x exige apenas ~0.09% (muito rápido, mas stop loss fica curto).")
    
    print("\n💡 RECOMENDAÇÃO: 20x Leverage")
    print("   - Meta: 0.22% de movimento (fácil de pegar em 1 candle de 5min).")
    print("   - Risco: Liquidação em -5% (dá espaço para respirar).")

analyze_scenarios(11.21, 0.50)
