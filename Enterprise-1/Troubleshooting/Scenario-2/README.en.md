# Scenario 02 | Primary WAN failure

**Languages:** [Português](README.MD) | [English](README.en.md)

**Status:** procedure not executed.

**Objective:** simulate the loss of the Gold-to-DC primary path and measure recovery via an alternative Internet/IPsec path, **if configured**.

## Procedure

1. Record topology, route state, IPsec state, loss and latency before failure.
2. Start continuous pings and a test TCP flow between Gold and DC endpoints.
3. Interrupt **only the intended lab link** and record the timestamp.
4. Inspect health checks, routing changes, tunnel state, packet loss and recovery time.
5. Restore the primary link and document failback behavior, loops and asymmetric routing.

## Acceptance

- Forward and return routes converge to valid paths.
- Loss and recovery time are **measured**, not assumed.
- Existing-session survival or reset is explicitly recorded.
- Security policy still applies over the backup path.

**Note:** the academic plan mentions a 10-second tolerance as an objective, **not as an achieved result**. [Evidence guide](../../evidence/README.en.md).
