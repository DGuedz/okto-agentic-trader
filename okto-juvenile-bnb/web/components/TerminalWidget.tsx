"use client";

import { useState, useRef, useEffect } from 'react';

export default function TerminalWidget() {
  const [logs, setLogs] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [showDemoLogs, setShowDemoLogs] = useState(true);
  const logsEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    logsEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [logs]);

  const runSimulation = async () => {
    setIsLoading(true);
    setShowDemoLogs(false);
    setLogs(["[SYSTEM] Initializing simulation environment...", "[SYSTEM] Connecting to Okto Core...", "[SYSTEM] Loading market data..."]);
    
    try {
      const response = await fetch('/api/simulate', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
      });
      const data = await response.json();
      
      if (data.success) {
        // Process logs to remove ANSI codes for clean display
        // Regex to strip ANSI escape codes
        const stripAnsi = (str: string) => str.replace(/\x1b\[[0-9;]*m/g, '');
        
        let newLogs = [];
        if (Array.isArray(data.logs)) {
             newLogs = data.logs.map(stripAnsi);
        } else if (typeof data.output === 'string') {
             newLogs = data.output.split('\n').map(stripAnsi).filter((l: string) => l.trim() !== '');
        }
        
        setLogs(newLogs);
      } else {
        setLogs(prev => [...prev, `[ERROR] Simulation failed: ${data.output || "Unknown error"}`]);
      }
    } catch (error: any) {
      setLogs(prev => [...prev, `[CRITICAL] Network error: ${error.message}`]);
    } finally {
      setIsLoading(false);
    }
  };

  const DemoLogs = () => (
    <>
        <div className="flex gap-2">
            <span className="text-text-muted">10:42:01</span>
            <span className="text-state-info">[INFO]</span>
            <span className="text-text-secondary">Market scan complete. 12 pairs analyzed.</span>
        </div>
        <div className="flex gap-2">
            <span className="text-text-muted">10:42:05</span>
            <span className="text-state-warning">[WARN]</span>
            <span className="text-text-secondary">High slippage detected on POOL (1.2%). Vetoing trade.</span>
        </div>
        <div className="flex gap-2">
            <span className="text-text-muted">10:42:12</span>
            <span className="text-state-info">[INFO]</span>
            <span className="text-text-secondary">Capital Rotation: Checking High Water Mark...</span>
        </div>
        <div className="flex gap-2">
            <span className="text-text-muted">10:42:15</span>
            <span className="text-accent-neon-400">[EXEC]</span>
            <span className="text-text-primary">Scalp Entry Long BNB @ 620.50</span>
        </div>
            <div className="flex gap-2 opacity-50">
            <span className="text-text-muted">10:42:18</span>
            <span className="text-state-info">[INFO]</span>
            <span className="text-text-secondary">Monitoring position...</span>
        </div>
    </>
  );

  return (
    <div className="grid md:grid-cols-2 bg-surface-panel min-h-[400px]">
      {/* Spec Preview */}
      <div className="border-r border-border-subtle p-6 font-mono text-sm">
        <div className="text-text-muted mb-4 uppercase tracking-widest text-xs">/config/okto.yaml</div>
        <pre className="text-text-secondary overflow-x-auto">
          <code>
            <span className="text-accent-amber-400">strategy:</span><br/>
            &nbsp;&nbsp;name: &quot;bnb_scalp_v1&quot;<br/>
            &nbsp;&nbsp;assets: [&quot;BNB/USDT&quot;]<br/>
            &nbsp;&nbsp;interval: &quot;1m&quot;<br/>
            <br/>
            <span className="text-accent-amber-400">risk_manager:</span><br/>
            &nbsp;&nbsp;max_drawdown: 5.0%<br/>
            &nbsp;&nbsp;stop_loss: 1.5%<br/>
            &nbsp;&nbsp;take_profit: 3.0%<br/>
            &nbsp;&nbsp;leverage: 5x<br/>
            <br/>
            <span className="text-accent-amber-400">modules:</span><br/>
            &nbsp;&nbsp;- &quot;anti_mev&quot;<br/>
            &nbsp;&nbsp;- &quot;capital_rotation&quot;<br/>
            &nbsp;&nbsp;- &quot;regime_detection&quot;<br/>
          </code>
        </pre>
      </div>

      {/* Live Telemetry */}
      <div className="p-6 font-mono text-sm bg-bg-0 relative overflow-hidden flex flex-col h-[400px]">
        <div className="text-text-muted mb-4 uppercase tracking-widest text-xs flex justify-between shrink-0">
            <span>Terminal Telemetry</span>
            <span className={`text-accent-neon-400 flex items-center gap-2 ${isLoading ? 'animate-pulse' : ''}`}>
                {isLoading ? '● RUNNING' : '● IDLE'}
            </span>
        </div>
        
        <div className="space-y-3 overflow-y-auto flex-grow pb-16 custom-scrollbar">
            {showDemoLogs ? <DemoLogs /> : (
                logs.map((log, index) => {
                    let typeClass = "text-text-secondary";
                    let prefix = "[INFO]";
                    let prefixClass = "text-state-info";

                    if (log.includes("[WARN]")) {
                        prefix = "[WARN]";
                        prefixClass = "text-state-warning";
                    } else if (log.includes("[ERROR]") || log.includes("[CRITICAL]")) {
                        prefix = "[ERR]";
                        prefixClass = "text-state-error";
                    } else if (log.includes("[EXEC]") || log.includes("[SUCCESS]") || log.includes("[DONE]")) {
                        prefix = "[EXEC]";
                        prefixClass = "text-accent-neon-400";
                    } else if (log.includes("[REGIME]")) {
                        prefix = "[MODE]";
                        prefixClass = "text-accent-violet-400";
                    }

                    // Simple clean up of log line to remove duplicate prefixes if present in source
                    const cleanLog = log.replace(/\[.*?\]\s*/, ''); 

                    return (
                        <div key={index} className="flex gap-2 font-mono text-xs md:text-sm">
                            <span className="text-text-muted shrink-0">{new Date().toLocaleTimeString([], {hour12: false})}</span>
                            <span className={`${prefixClass} shrink-0`}>{prefix}</span>
                            <span className={`${typeClass} break-all`}>{cleanLog || log}</span>
                        </div>
                    );
                })
            )}
            <div ref={logsEndRef} />
        </div>

        <div className="absolute bottom-6 right-6 z-10">
            <button 
                onClick={runSimulation}
                disabled={isLoading}
                className={`px-4 py-2 bg-accent-amber-400 text-text-inverse font-bold text-xs rounded transition-all shadow-glowAmber ${isLoading ? 'opacity-50 cursor-not-allowed grayscale' : 'hover:brightness-110'}`}
            >
                {isLoading ? 'SIMULATING...' : 'RUN SIMULATION'}
            </button>
        </div>
      </div>
    </div>
  );
}
