# Cenário 02 | Falha de WAN principal

**Estado:** roteiro ainda não executado.

**Objetivo:** simular perda do caminho principal Gold -> DC e medir recuperação via caminho alternativo (VPN sobre Internet, se configurada).

## Procedimento

1. Registrar topologia, estado de roteamento, IPsec, perda e latencia antes da falha.
2. Iniciar pings continuos e transacao TCP simulada entre host Gold e servico no DC.
3. Interromper **somente o enlace de laboratório** previsto e registrar timestamp.
4. Verificar health-check, mudanca de rota, estado VPN, perda e tempo de recuperação.
5. Restaurar link primario e verificar política de failback sem loop/assimetria.

## Criterios de aceite

- Rota de ida e retorno convergem para caminho valido.
- Falhas e tempo de recuperação **medidos**, sem inventar SLA.
- Queda ou manutenção de sessões existentes explicitamente registrada.
- Política de segurança permanece aplicavel durante failover.

**Observação:** o PIF cita tolerancia de 10 segundos como objetivo de teste; **não e resultado alcançado**. [Modelo de evidência](../../evidence/README.md).
