# Services data: Blockchain & Web3 (SYV-01) + Full Stack Engineering (SYV-02). No em dashes.

SERVICES_A = {

# ---------------------------------------------------------------- BLOCKCHAIN
"smart-contract-development": dict(
  practice="blockchain-web3", name="Smart Contract Development",
  short="Solidity, Rust, and Move systems designed, tested, and hardened before mainnet.",
  meta="Smart contract development in Solidity, Rust, and Move. Senior engineers, adversarial testing, audit-ready code shipped to mainnet.",
  hero="Contracts written to survive mainnet, not just compile.",
  body=[
    "Smart contracts are the one part of your stack you cannot hotfix. Syvora writes them the way infrastructure should be written: specified before coded, tested adversarially, and reviewed by engineers who have shipped protocols that hold real value.",
    "We work in Solidity, Rust, and Move across EVM chains, Solana, and Move-based networks. Every engagement produces a contract system plus the test suite, deployment scripts, and documentation your auditors and future engineers will actually use."
  ],
  scope=[
    ("Architecture & specification.", "Threat modeling, state machine design, and a written spec before the first line of code."),
    ("Implementation.", "Solidity, Rust, or Move with gas-aware patterns and upgradeability decided deliberately, not by default."),
    ("Testing.", "Unit, fork, fuzz, and invariant testing in Foundry or the native toolchain, wired into CI."),
    ("Deployment & operations.", "Deterministic deploy scripts, multisig and timelock setup, and verified source on explorers."),
    ("Audit management.", "Preparation, auditor liaison, and remediation so findings close fast."),
    ("Handover.", "NatSpec documentation and a walkthrough your team can maintain from."),
  ],
  deliverables=["Written technical spec", "Contract system with full test suite", "Deployment and verification scripts", "Audit readiness pack", "Post-deploy monitoring plan"],
  faqs=[
    ("Which chains and languages do you cover?", "EVM chains in Solidity, Solana in Rust, and Move networks such as Aptos and Sui. The same specification and testing discipline applies across all of them."),
    ("Do you work with external auditors?", "Yes. We prepare the codebase, manage the audit relationship, and remediate findings. Several engagements have gone through top-tier firms with clean re-reviews."),
    ("Can you take over an existing codebase?", "Yes. We start with a review and test-coverage pass, then stabilize before adding features. You get a written assessment in the first two weeks."),
  ],
  tech=["ethereum", "solana", "solidity", "rust"], related=["smart-contract-audit-readiness", "protocol-token-design", "defi-development"],
),

"protocol-token-design": dict(
  practice="blockchain-web3", name="Protocol & Token Design",
  short="Tokenomics, value flow mapping, and incentive modeling before a single contract is written.",
  meta="Protocol and token design services: tokenomics, incentive modeling, emissions, and governance design grounded in engineering reality.",
  hero="Token models designed on spreadsheets before they cost you on mainnet.",
  body=[
    "Most token problems are design problems that were shipped. Syvora treats protocol design as an engineering discipline: value flows mapped end to end, incentives simulated against adversarial behavior, and emissions modeled against realistic demand instead of hope.",
    "The output is a design your engineers can implement directly and your investors can interrogate: supply schedules, sinks and sources, governance mechanics, and the contract architecture that enforces all of it."
  ],
  scope=[
    ("Value flow mapping.", "Who pays, who earns, and where value accrues, drawn as a system, not a slide."),
    ("Token mechanics.", "Supply, emissions, vesting, staking, and burn mechanics modeled with scenarios."),
    ("Incentive simulation.", "Stress tests against mercenary capital, sybil behavior, and low-liquidity conditions."),
    ("Governance design.", "Voting, delegation, and treasury mechanics matched to how your community actually behaves."),
    ("Launch economics.", "Initial distribution, liquidity strategy, and unlock cliffs planned against market reality."),
    ("Implementation spec.", "A contract-level specification that goes straight to our smart contract team or yours."),
  ],
  deliverables=["Token design document", "Emissions and supply model", "Incentive simulation report", "Governance specification", "Contract implementation spec"],
  faqs=[
    ("Do we need a token at all?", "Sometimes no, and we will say so. The first workshop tests whether a token creates value or just creates sell pressure."),
    ("Can you review an existing token model?", "Yes. A design review takes one to two weeks and produces a written assessment with concrete fixes, ranked by impact."),
    ("Do you implement the design too?", "Yes. The design hands off directly to our smart contract development practice, so nothing is lost in translation."),
  ],
  tech=["ethereum", "solana", "solidity"], related=["smart-contract-development", "defi-development", "tokenization-rwa"],
),

"defi-development": dict(
  practice="blockchain-web3", name="DeFi Development",
  short="AMMs, lending markets, staking, vaults, and derivatives infrastructure built to hold value.",
  meta="DeFi development services: AMMs, lending protocols, staking systems, vaults, and derivatives built by engineers behind production protocols.",
  hero="DeFi systems built by people who have watched TVL arrive.",
  body=[
    "DeFi is where contract engineering meets market microstructure. Syvora builds AMMs, lending markets, staking systems, vaults, and structured products with the paranoia they deserve: oracle assumptions documented, liquidation paths tested, and economic attacks simulated before launch.",
    "We build from first principles or fork responsibly. Either way you get a protocol with clean accounting, defensible parameters, and the monitoring to see trouble before your users tweet it."
  ],
  scope=[
    ("Exchange infrastructure.", "AMM design and implementation, from constant product to concentrated liquidity."),
    ("Lending & credit.", "Money markets with interest rate models, liquidation engines, and risk parameters that hold."),
    ("Staking & vaults.", "Reward distribution, auto-compounding strategies, and ERC-4626 vault systems."),
    ("Derivatives.", "Perps, options, and structured product rails with margin and settlement logic."),
    ("Oracle strategy.", "Price feed architecture, manipulation resistance, and fallback design."),
    ("Economic security.", "Attack simulation, parameter tuning, and invariant monitoring in production."),
  ],
  deliverables=["Protocol architecture document", "Audited-ready contract system", "Risk parameter framework", "Liquidation and oracle test reports", "Live monitoring dashboards"],
  faqs=[
    ("Do you fork or build from scratch?", "Whichever serves the goal. Forking proven code reduces risk when the mechanism matches; novel mechanisms get novel code with heavier testing."),
    ("How do you handle oracle risk?", "Oracle assumptions are documented explicitly, manipulation costs are estimated, and every feed has a fallback and circuit breaker path."),
    ("Can you help post-launch?", "Yes. Managed services cover parameter reviews, upgrade execution, and incident response with defined SLAs."),
  ],
  tech=["ethereum", "arbitrum", "solidity", "rust"], related=["smart-contract-development", "protocol-token-design", "blockchain-indexing-data"],
),

"tokenization-rwa": dict(
  practice="blockchain-web3", name="Tokenization & RWA",
  short="Asset tokenization rails with compliance-aware architecture from day one.",
  meta="Real world asset tokenization development: compliant token rails, transfer restrictions, registry design, and issuance infrastructure.",
  hero="Real assets on-chain without the compliance afterthought.",
  body=[
    "Tokenizing real world assets is ten percent token contract and ninety percent everything around it: identity, transfer restrictions, registries, redemption, and reporting. Syvora builds the whole rail, designed with your legal counsel rather than around them.",
    "We have built issuance and lifecycle infrastructure for asset-backed tokens where every transfer rule is enforced on-chain and every action is auditable off-chain."
  ],
  scope=[
    ("Token standard selection.", "ERC-20 with restrictions, ERC-1400 family, or custom, chosen against your regulatory posture."),
    ("Compliance architecture.", "Allowlists, identity attestation, jurisdiction gating, and transfer restriction engines."),
    ("Issuance & lifecycle.", "Minting, distribution, corporate actions, redemption, and burn workflows."),
    ("Registry & reporting.", "Cap table synchronization and audit-grade event logs for administrators."),
    ("Custody integration.", "Flows that work with qualified custodians and institutional wallets."),
    ("Investor experience.", "Onboarding, KYC handoff, and dashboards that non-crypto investors can use."),
  ],
  deliverables=["Compliance-aware architecture spec", "Token and registry contracts", "Issuance admin console", "Integration layer for custody and KYC", "Operations runbook"],
  faqs=[
    ("Do you provide legal advice?", "No. We implement the rules your counsel defines, and we are fluent enough in the landscape to make that collaboration fast."),
    ("Which asset classes have you worked with?", "Funds, credit instruments, and revenue-share structures. The rail pattern transfers across asset classes with different restriction logic."),
    ("Public chain or permissioned?", "Both. We help you decide based on distribution goals, then build for that environment."),
  ],
  tech=["ethereum", "base", "solidity", "typescript"], related=["smart-contract-development", "wallet-account-abstraction", "smart-contract-audit-readiness"],
),

"cross-chain-interoperability": dict(
  practice="blockchain-web3", name="Cross-Chain & Interoperability",
  short="Bridges, messaging layers, and coordinated multichain deployments.",
  meta="Cross-chain development services: bridge integration, cross-chain messaging, and multichain deployment architecture done safely.",
  hero="Multichain without multiplying your attack surface.",
  body=[
    "Cross-chain is where most of crypto's worst losses happened, which is exactly why it deserves engineering rather than optimism. Syvora designs multichain architectures that minimize trust assumptions: canonical messaging where possible, audited bridge integrations where necessary, and deployment coordination that keeps every chain in sync.",
    "Whether you are expanding an existing protocol to new chains or building natively multichain, we make the trust model explicit and the operations boring."
  ],
  scope=[
    ("Interop architecture.", "Trust model analysis across LayerZero, CCIP, Hyperlane, and native bridges."),
    ("Cross-chain messaging.", "Application-level messaging with replay protection, ordering, and failure handling."),
    ("Asset bridging.", "Lock-and-mint, burn-and-mint, and liquidity network patterns implemented safely."),
    ("Multichain deployment.", "Deterministic addresses, coordinated upgrades, and per-chain configuration management."),
    ("Chain expansion.", "Taking an existing protocol to new EVM chains or Solana with parity testing."),
    ("Monitoring.", "Cross-chain state reconciliation and alerting when chains disagree."),
  ],
  deliverables=["Interoperability architecture doc", "Messaging and bridge integration code", "Multichain deployment tooling", "Reconciliation monitors", "Trust model documentation"],
  faqs=[
    ("Which messaging layers do you recommend?", "It depends on the chains, value at risk, and latency needs. We present the trust trade-offs in writing and recommend one, with reasons."),
    ("Can you audit our current bridge setup?", "Yes. A cross-chain review maps every trust assumption and failure mode, typically in two to three weeks."),
    ("Do you support non-EVM chains?", "Yes, including Solana. Parity across VM environments is handled with shared specs and cross-environment test vectors."),
  ],
  tech=["ethereum", "arbitrum", "base", "solana"], related=["defi-development", "smart-contract-development", "blockchain-indexing-data"],
),

"wallet-account-abstraction": dict(
  practice="blockchain-web3", name="Wallets & Account Abstraction",
  short="Embedded wallets, gasless flows, session keys, and onboarding UX that converts.",
  meta="Wallet and account abstraction development: ERC-4337 smart accounts, embedded wallets, gasless transactions, and session keys.",
  hero="Onboarding where the wallet disappears and the user stays.",
  body=[
    "The wallet is where most Web3 products lose their users. Syvora builds account experiences that feel like normal software: email or passkey sign-in, sponsored gas, session keys for repeat actions, and recovery that does not involve a seed phrase lecture.",
    "We work across ERC-4337 smart accounts, embedded wallet providers, and custom signer infrastructure, and we integrate it into your product so conversion is measured, not assumed."
  ],
  scope=[
    ("Smart accounts.", "ERC-4337 account deployment, paymasters, and bundler strategy."),
    ("Embedded wallets.", "Privy, Dynamic, Turnkey, or custom MPC flows integrated into your app."),
    ("Gas abstraction.", "Sponsored transactions, ERC-20 gas payment, and spend policy controls."),
    ("Session keys.", "Scoped permissions so users approve once and act many times safely."),
    ("Recovery & security.", "Passkeys, social recovery, and progressive security as balances grow."),
    ("Onboarding UX.", "Funnel instrumentation and iteration on the flows that create activated users."),
  ],
  deliverables=["Account architecture decision doc", "Integrated wallet infrastructure", "Paymaster and policy configuration", "Session key permission system", "Onboarding funnel dashboard"],
  faqs=[
    ("Build custom or use a provider?", "Providers win for speed in most consumer cases; custom wins for control and unit economics at scale. We model both costs before recommending."),
    ("Does account abstraction work on L2s?", "Yes, and that is where it shines: sponsored gas on L2s costs cents and removes the largest onboarding objection."),
    ("Can you retrofit an existing dapp?", "Yes. Smart accounts can sit alongside EOA support, so existing users keep working while new users get the improved flow."),
  ],
  tech=["ethereum", "base", "typescript", "react"], related=["web-application-development", "smart-contract-development", "tokenization-rwa"],
),

"smart-contract-audit-readiness": dict(
  practice="blockchain-web3", name="Security & Audit Readiness",
  short="Internal reviews, fuzzing, invariant testing, and external audit management.",
  meta="Smart contract security services: internal review, fuzzing, invariant testing, and audit preparation that cuts audit time and findings.",
  hero="Walk into your audit with the findings already fixed.",
  body=[
    "Audits are expensive when they find what you should have caught. Syvora runs the security pass before the auditors do: manual review by protocol engineers, fuzz and invariant campaigns, and documentation that lets external auditors spend their hours on deep issues instead of orientation.",
    "Teams come to us two ways: before a first audit to compress cost and calendar, or after an incident to rebuild confidence. Both end with a codebase you can defend."
  ],
  scope=[
    ("Internal security review.", "Line-by-line review focused on value flows, access control, and upgrade paths."),
    ("Fuzzing & invariants.", "Foundry invariant suites and differential fuzzing against reference models."),
    ("Static & dynamic analysis.", "Slither, Semgrep rulesets, and fork-based exploit reproduction."),
    ("Audit preparation.", "Spec documents, known-issues log, and scoped repos that auditors thank you for."),
    ("Audit management.", "Firm selection, scheduling, finding triage, and verified remediation."),
    ("Incident response.", "War-room support, exploit analysis, and post-mortems with fixes shipped."),
  ],
  deliverables=["Internal review report", "Invariant and fuzz test suite", "Audit readiness pack", "Remediation log with diffs", "Security operations runbook"],
  faqs=[
    ("Are you replacing an external audit?", "No. We make external audits faster and cheaper by removing the shallow findings first. High-value systems should still get independent review."),
    ("How long does readiness take?", "Two to five weeks depending on codebase size. The invariant suite stays with you and keeps paying off after launch."),
    ("Can you help choose an audit firm?", "Yes. We match scope and mechanism complexity to firms we have worked with, and we manage the engagement end to end."),
  ],
  tech=["solidity", "rust", "ethereum"], related=["smart-contract-development", "defi-development", "cross-chain-interoperability"],
),

"blockchain-indexing-data": dict(
  practice="blockchain-web3", name="On-Chain Data & Indexing",
  short="Subgraphs, custom indexers, analytics pipelines, and explorers.",
  meta="Blockchain indexing and data services: subgraphs, custom indexers, real-time pipelines, and analytics your product can query fast.",
  hero="On-chain data your product can query in milliseconds.",
  body=[
    "Chains are terrible databases. Every serious Web3 product needs an indexing layer that turns raw logs into queryable state, and that layer is usually built twice: once badly, then properly. Syvora builds it properly the first time.",
    "We ship subgraphs where they fit and custom indexers where they do not: reorg-safe ingestion, backfill tooling, and APIs shaped around your product's actual queries."
  ],
  scope=[
    ("Subgraph development.", "The Graph subgraphs with schema design, migrations, and hosted or decentralized deployment."),
    ("Custom indexers.", "Purpose-built pipelines in TypeScript or Rust with reorg handling and exactly-once semantics."),
    ("Real-time streams.", "Websocket and webhook delivery for balances, positions, and protocol events."),
    ("Analytics pipelines.", "Warehouse loading for dashboards, token holder analysis, and growth metrics."),
    ("API layer.", "GraphQL or REST endpoints with caching designed for your query patterns."),
    ("Explorers & dashboards.", "Internal explorers and public dashboards that make your protocol legible."),
  ],
  deliverables=["Indexing architecture doc", "Deployed subgraph or indexer", "Backfill and reorg tooling", "Query API with docs", "Analytics dashboard"],
  faqs=[
    ("Subgraph or custom indexer?", "Subgraphs win for standard event indexing; custom wins for cross-contract joins, heavy aggregation, or strict latency. We prototype the deciding query first."),
    ("How do you handle reorgs?", "Ingestion tracks block hashes with configurable confirmation depth, and every table supports rollback. Reorg handling is tested, not assumed."),
    ("Multi-chain indexing?", "Yes. One schema across chains with chain-id partitioning, so your product queries one API regardless of deployment count."),
  ],
  tech=["typescript", "rust", "postgresql", "ethereum"], related=["defi-development", "api-backend-development", "data-engineering-analytics"],
),

# ---------------------------------------------------------------- FULL STACK
"web-application-development": dict(
  practice="full-stack-engineering", name="Web Application Development",
  short="React, Next.js, and TypeScript products taken from MVP to scale.",
  meta="Web application development services: React, Next.js, and TypeScript products built by senior engineers from MVP through scale.",
  hero="Web apps that ship in weeks and survive success.",
  body=[
    "Syvora builds web applications the way products deserve: TypeScript end to end, a design system from day one, and architecture decisions written down so the codebase still makes sense at ten times the traffic.",
    "We take products from first commit to production, or step into existing codebases to accelerate teams. Either way you get senior engineers, weekly demos, and software your users can feel."
  ],
  scope=[
    ("Product engineering.", "Next.js and React applications with server components, edge rendering, and clean data flow."),
    ("Design system implementation.", "Component libraries with accessibility and theming built in, not bolted on."),
    ("State & data.", "Query caching, optimistic updates, and realtime sync patterns matched to the product."),
    ("Auth & billing.", "Session management, RBAC, and subscription billing integrated properly."),
    ("Performance.", "Core Web Vitals budgets enforced in CI, not discovered in analytics."),
    ("Team acceleration.", "Embedding with your engineers, raising velocity and standards together."),
  ],
  deliverables=["Production web application", "Component library and design tokens", "CI/CD with preview environments", "Performance budget reports", "Architecture decision records"],
  faqs=[
    ("What is a typical timeline?", "A focused MVP ships in six to ten weeks. The first working demo is on screen by week three regardless of scope."),
    ("Do you work in our repo and process?", "Yes. Your repo, your PR process, your standups if you want us there. We adapt to teams; we do not make teams adapt to us."),
    ("Who owns the code?", "You do, fully, from the first commit. No lock-in and no proprietary scaffolding."),
  ],
  tech=["typescript", "react", "nextjs", "cloudflare"], related=["api-backend-development", "product-design-ui-engineering", "performance-reliability-engineering"],
),

"api-backend-development": dict(
  practice="full-stack-engineering", name="API & Backend Development",
  short="Node.js, Python, and Go services with REST, GraphQL, and event-driven architecture.",
  meta="Backend and API development services: Node.js, Python, and Go systems with REST, GraphQL, and event-driven architecture.",
  hero="Backends that stay boring at 100x the load.",
  body=[
    "The best backend is one nobody talks about. Syvora designs services that are observable, testable, and honest about failure: idempotent endpoints, explicit contracts, and queues where queues belong.",
    "We build in Node.js, Python, and Go, choosing per workload rather than per fashion, and every service ships with the dashboards and alerts that let a small team run it calmly."
  ],
  scope=[
    ("API design.", "REST and GraphQL contracts with versioning, pagination, and error semantics defined up front."),
    ("Service architecture.", "Modular monoliths by default, services where boundaries earn it."),
    ("Event-driven systems.", "Queues, outbox patterns, and exactly-once processing where it matters."),
    ("Data modeling.", "PostgreSQL schemas designed for the queries you will actually run."),
    ("Integrations.", "Third-party APIs wrapped with retries, circuit breakers, and sane timeouts."),
    ("Observability.", "Structured logs, traces, and SLO dashboards from the first deploy."),
  ],
  deliverables=["API specification and docs", "Production services with tests", "Queue and worker infrastructure", "Observability stack", "Runbooks for on-call"],
  faqs=[
    ("Monolith or microservices?", "Modular monolith until the pain is real, then extraction along proven seams. We optimize for your team size, not conference talks."),
    ("Which language will you pick?", "TypeScript for product velocity, Go for throughput-critical services, Python for data-heavy work. The decision is written down with reasons."),
    ("Can you scale an existing backend?", "Yes. We start with profiling and a bottleneck map, then fix in order of impact. Most systems have two or three real problems, not twenty."),
  ],
  tech=["nodejs", "go", "python", "postgresql"], related=["web-application-development", "cloud-infrastructure", "database-architecture"],
),

"cloud-infrastructure": dict(
  practice="full-stack-engineering", name="Cloud & Infrastructure",
  short="AWS, GCP, and Cloudflare with IaC, CI/CD, and observability built in.",
  meta="Cloud infrastructure services: AWS, GCP, and Cloudflare architecture with Terraform, CI/CD pipelines, and observability built in.",
  hero="Infrastructure as code, bills as expected.",
  body=[
    "Cloud goes wrong in two directions: fragile or expensive, and often both. Syvora builds infrastructure that is reproducible from a repo, observable from one screen, and priced like someone read the invoice.",
    "We work across AWS, GCP, and Cloudflare, and we are unusually good at knowing when a workload belongs on a hyperscaler versus the edge."
  ],
  scope=[
    ("Architecture.", "Environment design, network topology, and service selection matched to workload and budget."),
    ("Infrastructure as code.", "Terraform modules with state discipline and review-gated changes."),
    ("CI/CD.", "Pipelines with preview environments, progressive rollout, and one-command rollback."),
    ("Edge & serverless.", "Cloudflare Workers, Pages, and D1 where latency and cost favor the edge."),
    ("Observability.", "Metrics, logs, traces, and alerting tuned to signal, not noise."),
    ("Cost engineering.", "Rightsizing, commitment planning, and monthly reviews that keep spend flat as usage grows."),
  ],
  deliverables=["Infrastructure repository", "CI/CD pipelines", "Environment parity across dev, staging, prod", "Observability dashboards", "Cost baseline and savings report"],
  faqs=[
    ("Can you migrate us between clouds?", "Yes. Migrations run as parallel environments with staged cutover and rollback rehearsed before the real day."),
    ("Do you do Kubernetes?", "When it earns its complexity. Plenty of products run better on managed containers or the edge; we recommend against ceremony."),
    ("How much can we save?", "Typical first-pass reviews find fifteen to forty percent, mostly from idle capacity, over-provisioned databases, and egress mistakes."),
  ],
  tech=["aws", "gcp", "cloudflare", "kubernetes"], related=["devops-platform-engineering", "api-backend-development", "performance-reliability-engineering"],
),

"database-architecture": dict(
  practice="full-stack-engineering", name="Database & Data Layer",
  short="PostgreSQL, MongoDB, Redis, and warehouse pipelines designed for growth.",
  meta="Database architecture services: PostgreSQL design, query optimization, caching strategy, and pipelines that scale with your product.",
  hero="Schemas designed for year three, shipped in week one.",
  body=[
    "Your data layer is the part of the stack that gets harder to change every day you wait. Syvora designs schemas around the queries your product will actually run, adds caching where measurements justify it, and leaves you with migrations that run in seconds, not maintenance windows.",
    "From transactional PostgreSQL to Redis caching to warehouse feeds, we make the data layer a competitive advantage instead of a recurring incident."
  ],
  scope=[
    ("Schema design.", "Normalized where it protects you, denormalized where it pays, documented either way."),
    ("Query optimization.", "Index strategy, plan analysis, and the removal of N+1 patterns at the source."),
    ("Caching.", "Redis layers with explicit invalidation rules instead of hopeful TTLs."),
    ("Migrations.", "Zero-downtime migration patterns with rehearsed rollbacks."),
    ("Scaling.", "Read replicas, partitioning, and connection pooling introduced when metrics demand."),
    ("Warehouse feeds.", "CDC or batch pipelines into your analytics stack without hurting production."),
  ],
  deliverables=["Data model documentation", "Migration framework", "Query performance report", "Caching layer with invalidation map", "Backup and recovery runbook"],
  faqs=[
    ("Postgres or Mongo?", "PostgreSQL by default; it handles document workloads better than most teams expect. Mongo when the access pattern genuinely fits."),
    ("Our queries got slow. Where do you start?", "pg_stat_statements and a day of profiling. Most slowdowns trace to a handful of queries and one missing index strategy."),
    ("Can you fix our data layer without downtime?", "Yes. Expand-and-contract migrations plus dual writes let us restructure under live traffic."),
  ],
  tech=["postgresql", "nodejs", "python"], related=["api-backend-development", "data-engineering-analytics", "performance-reliability-engineering"],
),

"product-design-ui-engineering": dict(
  practice="full-stack-engineering", name="Product Design & UI Engineering",
  short="Design systems, component libraries, accessibility, and motion.",
  meta="Product design and UI engineering: design systems, component libraries, accessibility, and interface motion built to production quality.",
  hero="Interfaces where design and code are the same conversation.",
  body=[
    "The gap between design files and shipped UI is where products lose their polish. Syvora closes it by pairing designers and UI engineers in the same pod: tokens defined once, components built to spec, and motion that serves comprehension instead of decoration.",
    "The result is a design system your whole team ships from, and an interface your users describe as fast before they describe it as pretty."
  ],
  scope=[
    ("Design systems.", "Tokens, primitives, and composition patterns documented as living code."),
    ("Component engineering.", "Accessible, themeable React components with real keyboard support."),
    ("Interface motion.", "Transitions and micro-interactions with purpose, tuned for perceived speed."),
    ("Accessibility.", "WCAG-aligned builds verified with tooling and manual passes."),
    ("Design-to-code workflow.", "Figma structures that map one to one with the component library."),
    ("UI performance.", "Render profiling and interaction latency treated as design requirements."),
  ],
  deliverables=["Design token system", "Documented component library", "Accessibility audit and fixes", "Motion specification", "Figma to code workflow guide"],
  faqs=[
    ("Do you replace our designers?", "No. We pair with them. When you have no design team, our designers embed in the pod and hand off a system yours can grow later."),
    ("Which stack do components target?", "React with TypeScript by default, styled with your existing approach or a token-driven system we set up together."),
    ("Can you retrofit accessibility?", "Yes. We audit, fix in priority order, and wire checks into CI so regressions get caught at review time."),
  ],
  tech=["react", "typescript", "nextjs"], related=["web-application-development", "shopify-commerce-engineering", "mobile-app-development"],
),

"shopify-commerce-engineering": dict(
  practice="full-stack-engineering", name="Shopify & Commerce Engineering",
  short="Shopify apps, storefronts, and checkout extensions running in production.",
  meta="Shopify development services: public and private apps, headless storefronts, checkout extensions, and commerce integrations.",
  hero="Commerce engineering from a team that ships on Shopify weekly.",
  body=[
    "Shopify rewards teams who respect the platform: its APIs, its review process, and its performance rules. Syvora builds public and private apps, theme extensions, headless storefronts, and the integrations that connect commerce to the rest of your stack.",
    "We keep embeds light, webhooks compliant, and merchant experience first, because app store ratings are earned in the details."
  ],
  scope=[
    ("App development.", "Public and custom apps on Remix with Polaris UI and the GraphQL Admin API."),
    ("Theme & checkout extensions.", "App embeds under strict size budgets and checkout UI extensions that convert."),
    ("Headless storefronts.", "Hydrogen or Next.js storefronts with sub-second navigation."),
    ("Integrations.", "ERP, fulfillment, subscription, and marketing stacks synced reliably."),
    ("Data & webhooks.", "GDPR webhooks, bulk operations, and reconciliation jobs that never drift."),
    ("Performance.", "Lighthouse budgets on storefronts and near-zero impact from embedded scripts."),
  ],
  deliverables=["Production Shopify app or storefront", "App review submission pack", "Webhook and sync infrastructure", "Merchant onboarding flow", "Performance budget report"],
  faqs=[
    ("Public app or custom app?", "Public for distribution, custom for one merchant's control. We have shipped both and will model the revenue and review trade-offs with you."),
    ("Can you get us through app review?", "Yes. Our apps pass review because compliance is designed in from the start, including GDPR webhooks and billing rules."),
    ("Headless or Liquid?", "Liquid until the business case for headless is concrete. Headless done well is powerful; done casually it is an expensive slowdown."),
  ],
  tech=["shopify", "typescript", "react", "cloudflare"], related=["web-application-development", "api-backend-development", "technical-seo-growth"],
),

"performance-reliability-engineering": dict(
  practice="full-stack-engineering", name="Performance & Reliability",
  short="Profiling, load testing, and SLO-driven operations.",
  meta="Performance and reliability engineering: profiling, load testing, SLOs, and incident response that keep products fast and up.",
  hero="Fast is a feature. Up is a promise.",
  body=[
    "Performance work fails when it is vibes-based. Syvora runs it as engineering: measure, find the bottleneck, fix it, prove the fix, and put a budget in CI so it stays fixed.",
    "Reliability gets the same treatment: SLOs that reflect user experience, alerts that mean something, and incident practice before incidents happen."
  ],
  scope=[
    ("Profiling.", "Backend, frontend, and database profiling that names the actual bottleneck."),
    ("Load testing.", "Realistic traffic models with k6, run before launches instead of after outages."),
    ("Web performance.", "Core Web Vitals improvements that show up in conversion, not just scores."),
    ("SLOs & alerting.", "Service level objectives with burn-rate alerts replacing pager noise."),
    ("Resilience.", "Timeouts, retries, backpressure, and graceful degradation by design."),
    ("Incident practice.", "Runbooks, game days, and post-mortems that actually change the system."),
  ],
  deliverables=["Performance audit with ranked fixes", "Load test suite and reports", "SLO definitions and dashboards", "CI performance budgets", "Incident response runbooks"],
  faqs=[
    ("How fast can you find our bottleneck?", "Usually within the first week. Systems rarely have mysterious slowness; they have unmeasured slowness."),
    ("What results are typical?", "Recent engagements: p95 API latency down 60 to 80 percent, page loads under two seconds, and infra bills lower as a side effect."),
    ("Do you stay for operations?", "Optionally, yes. Managed reliability keeps the SLOs owned after the project ends."),
  ],
  tech=["go", "nodejs", "postgresql", "cloudflare"], related=["cloud-infrastructure", "api-backend-development", "qa-test-automation"],
),

"legacy-modernization": dict(
  practice="full-stack-engineering", name="Legacy Modernization",
  short="Refactors and replatforms delivered without stopping the business.",
  meta="Legacy modernization services: strangler-pattern replatforms, framework migrations, and refactors shipped without business downtime.",
  hero="Modernize the plane while it keeps flying.",
  body=[
    "Rewrites fail when they pause the business and bet everything on a big-bang cutover. Syvora modernizes incrementally: strangler patterns, parallel runs, and migration slices that ship value every few weeks while risk stays contained.",
    "We have moved products off aging frameworks, split monoliths that had stopped scaling, and untangled data models nobody wanted to touch, all with the old system serving customers until the moment it did not need to."
  ],
  scope=[
    ("Assessment.", "Codebase archaeology, dependency risk map, and a sequenced modernization plan."),
    ("Strangler migration.", "New capabilities built beside the legacy system with traffic shifted gradually."),
    ("Framework upgrades.", "Major version and framework migrations with automated codemods where possible."),
    ("Monolith decomposition.", "Service extraction along seams proven by real coupling data."),
    ("Data migration.", "Dual-write and backfill strategies with reconciliation reports."),
    ("Team enablement.", "Pairing and documentation so your engineers own the new world."),
  ],
  deliverables=["Modernization roadmap", "Migrated system slices in production", "Parity and reconciliation reports", "Updated CI/CD and environments", "Architecture decision records"],
  faqs=[
    ("Rewrite or refactor?", "Almost always incremental. Full rewrites are justified rarely, and when they are, we still ship them in slices."),
    ("How do you avoid breaking things?", "Characterization tests around legacy behavior, parallel runs with diffing, and cutovers that are rehearsed and reversible."),
    ("Our original developers are gone. Problem?", "Common, and fine. The codebase tells the truth; we read it, document it, and reduce the bus factor as we go."),
  ],
  tech=["typescript", "python", "postgresql", "aws"], related=["cloud-infrastructure", "database-architecture", "api-backend-development"],
),
}
