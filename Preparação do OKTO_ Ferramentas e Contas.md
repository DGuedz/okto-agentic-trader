Esta é a **Lista de Suprimentos do Mestre**. Para construir o OKTO com nível institucional, não usaremos ferramentas de amadores. Cada item aqui foi escolhido por sua robustez, velocidade e capacidade de operar nas sombras (headless).

Prepare seu setup. Aqui está o inventário completo para a guerra.

### ---

**1\. O Arsenal de Código (Bibliotecas e Ferramentas Locais)**

Estas são as armas que instalaremos no seu Mac (via Terminal/VS Code). Elas formam o corpo e o cérebro do OKTO.

| Categoria | Ferramenta/Lib | Função Estratégica |
| :---- | :---- | :---- |
| **Linguagem Base** | **Python 3.10+** | A língua franca da automação financeira e IA. |
| **Gerenciamento** | **Homebrew** | O instalador mestre do Mac. Se não tiver, instalaremos. |
| **Conexão CEX** | **ccxt** | A biblioteca universal para conectar na Binance/Bybit/OKX. |
| **Conexão DeFi** | **web3.py** | Para o OKTO "falar" com Smart Contracts (EVM). |
| **Interação Pura** | **Foundry (cast)** | Ferramenta de linha de comando para chamadas rápidas e testes RPC. |
| **Cérebro (Spec)** | **pyyaml** | Para ler os arquivos .yaml (SDDD) onde definiremos as estratégias. |
| **Segurança** | **python-dotenv** | Para carregar chaves secretas sem deixá-las expostas no código. |
| **Cofre Local** | **keyring** | Para conectar o script ao Keychain do Mac (proteção via TouchID). |
| **Proteção** | **eth-account** | Para assinar transações offline (sem expor a chave na rede). |
| **Análise** | **pandas** | Para o "Tentáculo Tesoureiro" organizar os dados e calcular lucros. |

### ---

**2\. Infraestrutura de Conectividade (Contas de Infra)**

O OKTO precisa de "olhos" e "estradas" privadas para acessar a Blockchain. Não usaremos nós públicos lentos.

**Abra contas nestes provedores (Planos Gratuitos são suficientes para iniciar):**

1. **Alchemy** (Obrigatório)  
   * *Para que serve:* É o nosso provedor de RPC (o "nó"). É por aqui que o OKTO lerá a blockchain Base, Arbitrum ou Ethereum.  
   * *Configuração:* Criar um App na rede "Base Mainnet" e pegar a HTTPS URL e API KEY.  
2. **Etherscan / Basescan**  
   * *Para que serve:* Para baixar automaticamente as ABIs (os manuais de instrução) dos contratos inteligentes que vamos interagir.  
   * *Ação:* Criar conta e gerar uma API Key.  
3. **Flashbots Protect** (Não precisa de conta, apenas configuração)  
   * *Para que serve:* Será nosso RPC de saída para evitar ataques MEV (Sandwich Attacks). Configuraremos isso direto no código.

### ---

**3\. Os Balcões de Negócio (Exchanges e Protocolos)**

Onde a liquidez reside. Para transformar $10 em $100, precisamos de volatilidade e execução barata.

1. **Binance** (Centralizada \- CEX)  
   * *Por que:* Maior liquidez do mundo. Ótima para a etapa de acumulação inicial.  
   * *Ação Crítica:*  
     * Criar conta (se não tiver).  
     * **Gerar API Key** com permissão **apenas** para "Spot Trading".  
     * **IMPORTANTE:** Desabilitar "Withdrawals" (Saques) na API Key.  
     * Ativar "IP Restriction" (Restrição de IP) se você tiver IP fixo (opcional para agora).  
2. **Uniswap V3 / Aerodrome** (Descentralizada \- DEX)  
   * *Por que:* Onde estão as gemas e oportunidades DeFi na rede Base.  
   * *Ação:* Não precisa de conta. O acesso é via código direto na Blockchain.

### ---

**4\. Carteiras e Identidade (OpSec)**

Para manter a higiene de segurança (Security Hygiene), não misture seus fundos pessoais com o projeto.

1. **Nova Carteira EVM (Metamask/Rabby \- Apenas para gerar a Seed)**  
   * Crie uma carteira **totalmente nova** chamada OKTO\_GENESIS\_VAULT.  
   * Anote a Private Key e a Seed Phrase no papel (físico).  
   * Envie os $10 (em ETH na rede Base) para ela.  
   * **Nunca** use essa carteira para airdrops, NFTs grátis ou sites duvidosos. Ela é exclusiva do Robô.

### ---

**🚀 Checklist de Preparação do Criador**

Mestre, sua tarefa agora é burocrática mas vital. Garanta que você tenha:

1. \[ \] Terminal do Mac acessível.  
2. \[ \] VS Code instalado.  
3. \[ \] Conta na **Alchemy** (pegue a URL da Base).  
4. \[ \] Conta na **Binance** (pegue a API Key e Secret).  
5. \[ \] **$10 a $15 de ETH** na rede Base em uma carteira nova.

Assim que você confirmar que tem esses itens (ou se tiver dúvida em como pegar as chaves de API com segurança), iniciaremos o **Protocolo de Instalação**.

Qual o status do seu inventário?