import React from 'react';
import { ArrowUp, ArrowDown } from 'lucide-react';

interface Order {
  price: number;
  size: number;
  total: number;
  type: 'bid' | 'ask';
}

const OrderRow = ({ order, maxTotal }: { order: Order; maxTotal: number }) => {
  const percent = (order.total / maxTotal) * 100;
  const isBid = order.type === 'bid';
  
  return (
    <div className="relative flex justify-between text-xs py-1 px-2 hover:bg-white/5 font-mono">
      <div 
        className={`absolute top-0 ${isBid ? 'right-0 bg-green-500/10' : 'left-0 bg-red-500/10'} h-full transition-all duration-300`}
        style={{ width: `${percent}%` }}
      />
      <span className={isBid ? 'text-green-400' : 'text-red-400'}>{order.price.toFixed(2)}</span>
      <span className="text-text-secondary z-10">{order.size.toFixed(4)}</span>
      <span className="text-text-muted z-10">{order.total.toFixed(2)}</span>
    </div>
  );
};

export default function OrderBook() {
  // Mock Data conforming to BNB Chain ecosystem style
  const asks: Order[] = Array.from({ length: 8 }, (_, i) => ({
    price: 642.50 + (i * 0.5),
    size: Math.random() * 2,
    total: Math.random() * 10,
    type: 'ask'
  })).reverse();

  const bids: Order[] = Array.from({ length: 8 }, (_, i) => ({
    price: 642.40 - (i * 0.5),
    size: Math.random() * 2,
    total: Math.random() * 10,
    type: 'bid'
  }));

  const maxTotal = Math.max(...[...asks, ...bids].map(o => o.total));

  return (
    <div className="w-full bg-surface-card border border-border-subtle rounded-lg overflow-hidden flex flex-col h-[400px]">
      <div className="p-3 border-b border-border-subtle flex justify-between items-center bg-surface-panel">
        <h3 className="text-sm font-bold text-text-primary flex items-center gap-2">
          <span className="w-2 h-2 bg-accent-amber-400 rounded-full animate-pulse"/>
          BNB/USDT
        </h3>
        <span className="text-xs text-text-muted">Order Book</span>
      </div>
      
      {/* Header */}
      <div className="flex justify-between px-2 py-1 text-[10px] text-text-muted uppercase bg-bg-1">
        <span>Price</span>
        <span>Size</span>
        <span>Total</span>
      </div>

      {/* Asks */}
      <div className="flex-1 overflow-y-auto custom-scrollbar flex flex-col justify-end">
        {asks.map((order, i) => <OrderRow key={`ask-${i}`} order={order} maxTotal={maxTotal} />)}
      </div>

      {/* Spread */}
      <div className="py-2 border-y border-border-subtle bg-bg-0 text-center font-mono text-sm flex justify-center items-center gap-2">
        <span className="text-accent-amber-400 font-bold">642.45</span>
        <span className="text-xs text-text-muted">≈ $642.45</span>
      </div>

      {/* Bids */}
      <div className="flex-1 overflow-y-auto custom-scrollbar">
        {bids.map((order, i) => <OrderRow key={`bid-${i}`} order={order} maxTotal={maxTotal} />)}
      </div>
    </div>
  );
}
