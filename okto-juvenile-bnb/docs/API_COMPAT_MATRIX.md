# API Compatibility Matrix (Binance Futures)

Last reviewed: 2026-02-18  
Scope: endpoints and streams that directly impact OKTO execution and monitoring.

## Core Order Flow (USDⓈ-M)

| Capability | Preferred API | Status | Notes for OKTO |
|---|---|---|---|
| Place vanilla order | `POST /fapi/v1/order` | Active | Keep as default for LIMIT/MARKET. |
| Place batch vanilla orders | `POST /fapi/v1/batchOrders` | Active | Use for grid placement when API limits allow. |
| Conditional orders (new path) | `POST /fapi/v1/algoOrder` | Active (required for migrated types) | Required for `STOP*`, `TAKE_PROFIT*`, `TRAILING_STOP_MARKET` after migration. |
| Cancel conditional orders | `DELETE /fapi/v1/algoOrder` | Active | Use when replacing risk controls. |
| Query open conditional orders | `GET /fapi/v1/openAlgoOrders` | Active | Add to monitoring for full open-order visibility. |

## Conditional Order Migration

| Change | Effective date | Risk | Action |
|---|---|---|---|
| Conditional types migrated to Algo Service | 2025-12-09 | High | Route all conditional order logic to `algoOrder` endpoints. |
| `POST /fapi/v1/order` for migrated conditional types returns `-4120 STOP_ORDER_SWITCH_ALGO` | 2025-12-09+ | High | Treat as expected compatibility error and auto-fallback to algo endpoints. |
| `CONDITIONAL_ORDER_TRIGGER_REJECT` deprecated | 2025-12-15 | Medium | Monitor `ALGO_UPDATE` instead of legacy reject event. |

## User Stream / Execution Events

| Event/Field | Channel | Status | Notes for OKTO |
|---|---|---|---|
| `ORDER_TRADE_UPDATE` | User Data Stream | Active | Still primary source for order lifecycle. |
| `ALGO_UPDATE` | User Data Stream | Active | Required for conditional/algo lifecycle and errors. |
| `er` (expire reason) | `ORDER_TRADE_UPDATE` | Added | Parse and store for post-mortem. |
| `nq` in `<symbol>@aggTrade` | Market Stream | Added | Only normal trades aggregated; do not assume RPI-inclusive flow. |

## Exchange Metadata / Limits

| Item | Change | Impact | Action |
|---|---|---|---|
| `MAX_NUM_ALGO_ORDERS` removed from `GET /fapi/v1/exchangeInfo` | 2025-12-29 | Medium | Do not depend on this filter. Use fixed conditional cap policy (200) in risk checks. |
| Single WS connection max streams increased to 1024 | 2025-07-02 | Low | Optional scaling headroom for market fan-out. |

## RPI / Order Book Behavior

| Item | Date | Impact | Action |
|---|---|---|---|
| RPI order introduced | 2025-11-18 | Medium | RPI trades may not appear in standard depth/bookTicker views. |
| `GET /fapi/v1/rpiDepth` and `<symbol>@rpiDepth@500ms` | 2025-11-25 | Medium | Use only if strategy explicitly models RPI liquidity. |

## Account / Activation / Safety

| Case | Signal | Action |
|---|---|---|
| Inactive account | `-4109` | Transfer small amount to USD-M Futures account, retry. |
| Throttled/system protection | `-1008` variants | Backoff with jitter; keep reduce-only/close-position path available. |
| Timestamp recvWindow mismatch | `-5028` family | Re-sync clock, retry with sane `recvWindow` and strict timestamp handling. |

## Implementation Guidance for OKTO

1. Keep vanilla grid orders on `fapi/v1/order`.
2. Route all conditional controls (stop/tp/trailing) through `fapi/v1/algoOrder`.
3. In monitoring, parse both `ORDER_TRADE_UPDATE` and `ALGO_UPDATE`.
4. Treat `-4120` as non-fatal compatibility signal and auto-switch endpoint.
5. Maintain a compatibility shim layer (endpoint adapter) to isolate future API shifts.

## Minimal Fallback Policy

- If algo endpoint fails with transient errors: retry with bounded exponential backoff.
- If fallback exhausted: cancel open risk-bearing orders and switch bot to HOLD mode.
- Emit structured error logs with endpoint, code, message, symbol, and run_id.
