# Services data: ServiceNow (SYV-03) + Extended Capabilities (SYV-04). No em dashes.

SERVICES_B = {

# ---------------------------------------------------------------- SERVICENOW
"servicenow-itsm-implementation": dict(
  practice="servicenow", name="ServiceNow ITSM Implementation",
  short="Incident, Problem, Change, Request, and Knowledge with ITIL-aligned process design.",
  meta="ServiceNow ITSM implementation services: Incident, Problem, Change, Request, and Knowledge delivered by certified consultants.",
  hero="ITSM that your agents adopt, not just log into.",
  body=[
    "An ITSM rollout succeeds or fails on process design, not module activation. Syvora implements Incident, Problem, Change, Request, and Knowledge with workflows shaped around how your teams actually operate, then measures adoption after go-live instead of declaring victory at it.",
    "Every engagement is run by certified consultants using documented decisions and tested releases, the same delivery discipline we apply to product engineering."
  ],
  scope=[
    ("Process design.", "ITIL-aligned workflows workshopped with the people who will live in them."),
    ("Core module configuration.", "Incident, Problem, Change, Request, and Knowledge configured, not customized by reflex."),
    ("Service catalog.", "Catalog items and record producers with fulfillment automation behind them."),
    ("SLAs & routing.", "Assignment rules, SLA definitions, and escalations that reflect reality."),
    ("Data migration.", "Clean import of users, groups, CIs, and open tickets from legacy tooling."),
    ("Adoption.", "Agent training, dashboards, and a thirty-day post-go-live tuning window."),
  ],
  deliverables=["Process design documents", "Configured ITSM modules", "Service catalog with fulfillment flows", "Migration and cutover plan", "Adoption dashboard and tuning report"],
  faqs=[
    ("How long does an ITSM implementation take?", "A focused core rollout lands in eight to twelve weeks. Scope discipline is the schedule; we protect it in writing."),
    ("Configuration or customization?", "Configuration first, always. Customization is reserved for genuine differentiators and documented so upgrades stay safe."),
    ("Can you rescue a stalled implementation?", "Yes. A two-week assessment produces a stabilization plan, and we take delivery from there."),
  ],
  tech=["servicenow-itsm"], related=["servicenow-itom-cmdb", "servicenow-service-portal", "servicenow-managed-services"],
),

"servicenow-itom-cmdb": dict(
  practice="servicenow", name="ServiceNow ITOM & CMDB",
  short="Discovery, Service Mapping, Event Management, and CMDB health governance.",
  meta="ServiceNow ITOM and CMDB services: Discovery, Service Mapping, Event Management, and CMDB governance that stays accurate.",
  hero="A CMDB your teams trust enough to query first.",
  body=[
    "Most CMDBs decay because they were populated once and governed never. Syvora implements ITOM so the data maintains itself: Discovery tuned to your network, Service Mapping tied to business services, and health governance that catches drift before it spreads.",
    "The outcome is operational: faster incident triage, honest change risk, and event noise reduced to signals someone should actually act on."
  ],
  scope=[
    ("Discovery.", "MID Server architecture, credential strategy, and scheduled discovery tuned for coverage."),
    ("Service mapping.", "Top-down maps of business services that make impact analysis real."),
    ("CMDB design.", "CSDM-aligned class model, identification and reconciliation rules."),
    ("Event management.", "Monitoring integrations with correlation and alert-to-incident automation."),
    ("Health governance.", "Completeness, correctness, and compliance dashboards with remediation workflows."),
    ("Integration.", "Cloud provider ingestion so ephemeral infrastructure stays represented."),
  ],
  deliverables=["Discovery architecture and schedules", "Populated CSDM-aligned CMDB", "Service maps for priority services", "Event correlation rules", "CMDB health scorecard"],
  faqs=[
    ("Our CMDB is a mess. Start over?", "Rarely. Reconciliation rules plus targeted re-discovery usually recover it faster than a rebuild, and we prove it on one class first."),
    ("Do you integrate cloud environments?", "Yes. AWS, Azure, and GCP ingestion with tagging discipline so cloud resources map to services automatically."),
    ("What does success look like?", "Change assessments referencing real dependencies, incident triage that starts from the map, and health scores trending up month over month."),
  ],
  tech=["servicenow-itom"], related=["servicenow-itsm-implementation", "servicenow-integrations", "servicenow-managed-services"],
),

"servicenow-hrsd-csm": dict(
  practice="servicenow", name="ServiceNow HRSD & CSM",
  short="Employee and customer workflows delivered through portal-first experiences.",
  meta="ServiceNow HRSD and CSM implementation: HR service delivery and customer service management with portal-first employee and customer experiences.",
  hero="HR and customer service that feels like a product.",
  body=[
    "HRSD and CSM succeed when the experience layer is treated as the product. Syvora designs the portal journey first, then wires HR case management, lifecycle events, and customer service operations behind it, so employees and customers get answers without learning your org chart.",
    "Deflection is engineered deliberately: knowledge, virtual agent, and catalog design working together, with the metrics to prove it."
  ],
  scope=[
    ("HR case & knowledge.", "COE-based case management with tiered fulfillment and knowledge at the point of need."),
    ("Lifecycle events.", "Onboarding, transfers, and offboarding orchestrated across HR, IT, and Facilities."),
    ("Employee Center.", "A unified portal with targeted content and to-dos per employee segment."),
    ("Customer service.", "Case routing, entitlements, SLAs, and account hierarchies for B2B or B2C."),
    ("Self-service & deflection.", "Catalog, knowledge, and virtual agent tuned against real contact drivers."),
    ("Confidentiality.", "HR data separation and security model designed for sensitive cases."),
  ],
  deliverables=["Journey and service design", "Configured HRSD or CSM workspaces", "Employee Center or customer portal", "Lifecycle event orchestrations", "Deflection and CSAT dashboards"],
  faqs=[
    ("Can HRSD and ITSM share one instance?", "Yes, with a security model that keeps HR cases confidential. That separation is designed first, not patched later."),
    ("How do you drive deflection?", "By mining actual contact drivers, then targeting the top ten with knowledge and automation. Deflection is a metric we report weekly."),
    ("B2B customer service with account hierarchies?", "Fully supported: accounts, contacts, entitlements, and partner access modeled to your commercial structure."),
  ],
  tech=["servicenow-hrsd"], related=["servicenow-service-portal", "servicenow-virtual-agent-ai", "servicenow-itsm-implementation"],
),

"servicenow-custom-app-development": dict(
  practice="servicenow", name="ServiceNow Custom App Development",
  short="Scoped applications on App Engine with Flow Designer and UI Builder.",
  meta="ServiceNow custom application development on App Engine: scoped apps, Flow Designer automation, and UI Builder workspaces.",
  hero="The workflows spreadsheets were never meant to run.",
  body=[
    "Every enterprise runs critical processes in spreadsheets and email because no system fits. App Engine fixes that when it is used with product discipline. Syvora builds scoped applications with proper data models, Flow Designer automation, and UI Builder experiences that feel intentional.",
    "We ship the way software teams ship: versioned in source control, tested with ATF, and released through update sets your platform team can trust."
  ],
  scope=[
    ("Product definition.", "Process mapping and an MVP scope that earns adoption before expansion."),
    ("Data model.", "Scoped tables with access controls designed against the platform, not around it."),
    ("Automation.", "Flow Designer and IntegrationHub flows replacing manual handoffs."),
    ("Experience.", "UI Builder workspaces and portal pages matched to each role."),
    ("Quality.", "ATF test coverage and instance-safe release management."),
    ("Governance.", "Documentation and technical debt boundaries so the app upgrades cleanly."),
  ],
  deliverables=["Scoped application in production", "Data model and security documentation", "Automated flows with error handling", "ATF test suite", "Release and upgrade playbook"],
  faqs=[
    ("Custom app or configure an existing module?", "We always check product-line fit first. Building what ServiceNow already sells is a maintenance tax with no upside."),
    ("How fast can an app ship?", "A well-scoped MVP lands in four to eight weeks, with the first working screens demoed by week three."),
    ("Will custom apps survive upgrades?", "Scoped apps built to platform standards upgrade smoothly. That is why we insist on scope, ATF, and documented boundaries."),
  ],
  tech=["servicenow-app-engine"], related=["servicenow-integrations", "servicenow-service-portal", "servicenow-itsm-implementation"],
),

"servicenow-integrations": dict(
  practice="servicenow", name="ServiceNow Integrations",
  short="Integration Hub, REST and SOAP, MID Server, and bidirectional sync with enterprise systems.",
  meta="ServiceNow integration services: IntegrationHub, REST and SOAP APIs, MID Server, and reliable bidirectional sync with ERP, CRM, and identity.",
  hero="ServiceNow talking to everything, reliably.",
  body=[
    "An isolated ServiceNow instance becomes another swivel-chair system. Syvora builds the integration architecture that connects it to identity, ERP, CRM, monitoring, and collaboration tools, with the error handling and reconciliation that separate integrations from incidents.",
    "IntegrationHub where spokes exist, custom REST where they do not, MID Server where the network requires it, and every interface documented like the contract it is."
  ],
  scope=[
    ("Integration architecture.", "Interface inventory, patterns, and an error-handling standard applied everywhere."),
    ("IntegrationHub.", "Spoke configuration and custom actions with credential hygiene."),
    ("API development.", "Scripted REST APIs and hardened outbound clients with retry and backoff."),
    ("Identity & HR feeds.", "Azure AD, Okta, and HRIS synchronization with reconciliation reports."),
    ("Eventing.", "Webhook and mid-server patterns for near-real-time flows behind the firewall."),
    ("Monitoring.", "Integration dashboards that surface failures before users file tickets."),
  ],
  deliverables=["Integration architecture document", "Production interfaces with runbooks", "Reconciliation jobs and reports", "Credential and security review", "Integration health dashboard"],
  faqs=[
    ("IntegrationHub or custom code?", "Spokes first for speed and supportability; custom REST when behavior or volume demands it. The decision is recorded per interface."),
    ("How do you prevent silent failures?", "Every interface gets structured error capture, alerting thresholds, and a reconciliation job that proves the two systems still agree."),
    ("Can you fix our flaky legacy integrations?", "Yes. We stabilize the worst offenders first with retries and idempotency, then re-platform them properly in priority order."),
  ],
  tech=["servicenow-integrationhub"], related=["servicenow-itom-cmdb", "servicenow-custom-app-development", "api-backend-development"],
),

"servicenow-service-portal": dict(
  practice="servicenow", name="Service Portal & Employee Center",
  short="Adoption-focused experiences on top of the platform.",
  meta="ServiceNow Service Portal and Employee Center development: branded, fast, adoption-focused portals that reduce ticket volume.",
  hero="Portals people use before they email you.",
  body=[
    "The portal is where your entire ServiceNow investment becomes visible. Syvora designs and builds Service Portal and Employee Center experiences that load fast, respect your brand, and route people to answers before agents get involved.",
    "We treat the portal like a product: analytics on every journey, search tuned against real queries, and iteration after launch instead of a screenshot in a deck."
  ],
  scope=[
    ("Experience design.", "Journey mapping and information architecture from real contact drivers."),
    ("Branded build.", "Custom widgets and themes on Service Portal or Employee Center, performance-budgeted."),
    ("Search & knowledge.", "Search tuning, curated results, and knowledge presentation that deflects."),
    ("Catalog UX.", "Request flows redesigned so completion rates climb."),
    ("Targeted content.", "Audience-based content and to-dos per department, location, or persona."),
    ("Analytics.", "Adoption dashboards: traffic, deflection, completion, and satisfaction."),
  ],
  deliverables=["Portal design system", "Production portal with custom widgets", "Search and knowledge tuning report", "Analytics dashboard", "Content governance guide"],
  faqs=[
    ("Service Portal or Employee Center?", "Employee Center for the unified-experience roadmap, Service Portal for controlled custom cases. We map your license and goals before recommending."),
    ("Can you match our brand exactly?", "Yes, within platform patterns that keep upgrades safe. Pixel fidelity without customization debt."),
    ("What deflection lift is realistic?", "Portals we rebuild typically cut simple ticket volume by twenty to thirty five percent within a quarter, and we instrument it so you can verify."),
  ],
  tech=["servicenow-app-engine"], related=["servicenow-hrsd-csm", "servicenow-virtual-agent-ai", "servicenow-itsm-implementation"],
),

"servicenow-virtual-agent-ai": dict(
  practice="servicenow", name="ServiceNow Virtual Agent & AI",
  short="Virtual Agent, Predictive Intelligence, and Now Assist enablement.",
  meta="ServiceNow AI services: Virtual Agent conversations, Predictive Intelligence models, and Now Assist enablement with measured outcomes.",
  hero="Platform AI that resolves tickets, not just greets users.",
  body=[
    "ServiceNow's AI features earn their license cost only when they are pointed at the right work. Syvora deploys Virtual Agent on your highest-volume intents, trains Predictive Intelligence on your own history, and enables Now Assist where generative summaries actually save agent minutes.",
    "Everything ships with baselines and dashboards, so the AI conversation with your leadership is about measured deflection and handle time, not demos."
  ],
  scope=[
    ("Intent mining.", "Contact driver analysis to pick the conversations worth automating first."),
    ("Virtual Agent.", "Conversation design and build with graceful live-agent handoff."),
    ("Predictive Intelligence.", "Categorization, routing, and similarity models trained and tuned on your data."),
    ("Now Assist.", "Generative summarization and resolution notes enabled with guardrails."),
    ("Knowledge readiness.", "Content structured so AI answers are grounded and current."),
    ("Measurement.", "Deflection, containment, and accuracy dashboards with monthly tuning."),
  ],
  deliverables=["Automation opportunity report", "Live Virtual Agent topics", "Trained PI models with accuracy baselines", "Now Assist configuration", "AI performance dashboard"],
  faqs=[
    ("Where should we start with platform AI?", "Virtual Agent on your top five intents. It is the fastest path to visible deflection and it funds everything after it."),
    ("How accurate does Predictive Intelligence get?", "With clean history, routing models commonly reach eighty five percent plus. We publish the confusion matrix, not just the headline."),
    ("Is Now Assist worth it?", "For high-volume agent teams, summarization alone often justifies it. We pilot on one queue and let the numbers decide."),
  ],
  tech=["servicenow-now-assist"], related=["servicenow-service-portal", "ai-agentic-automation", "servicenow-itsm-implementation"],
),

"servicenow-managed-services": dict(
  practice="servicenow", name="ServiceNow Managed Services",
  short="Instance health scans, upgrade cycles, and ongoing SLA-backed support.",
  meta="ServiceNow managed services: SLA-backed administration, enhancements, upgrade execution, and instance health from certified consultants.",
  hero="A platform team on tap, without the headcount.",
  body=[
    "ServiceNow keeps releasing whether or not you have capacity. Syvora's managed services keep your instance healthy, current, and improving: a certified team handling administration, enhancements, and twice-yearly upgrades under real SLAs.",
    "You get a monthly rhythm of delivered improvements and an instance health score trending the right way, instead of a backlog that only grows."
  ],
  scope=[
    ("Administration.", "User, group, and access management with documented change control."),
    ("Enhancements.", "A prioritized backlog delivered in monthly increments with demos."),
    ("Upgrades.", "Family release upgrades planned, tested with ATF, and executed on schedule."),
    ("Instance health.", "HealthScan-driven remediation of technical debt and performance issues."),
    ("Incident support.", "SLA-backed response for platform issues, with root cause follow-through."),
    ("Advisory.", "Quarterly roadmap reviews aligning platform investment to business priorities."),
  ],
  deliverables=["Service catalog and SLA definitions", "Monthly delivery reports", "Executed upgrade cycles", "Instance health scorecard", "Quarterly roadmap reviews"],
  faqs=[
    ("How is this priced?", "A flat monthly retainer sized by scope, not a ticket meter. Predictable cost is the point."),
    ("Can you take over from another partner?", "Yes. Transition includes a health scan, documentation recovery, and a stabilization sprint before the regular cadence starts."),
    ("Do we keep our own admin?", "Ideally yes. We multiply internal admins rather than replace them, and we document so knowledge stays in your house."),
  ],
  tech=["servicenow-itsm"], related=["servicenow-itsm-implementation", "servicenow-itom-cmdb", "servicenow-integrations"],
),

# ---------------------------------------------------------------- EXTENDED
"ai-agentic-automation": dict(
  practice="extended-capabilities", name="AI & Agentic Automation",
  short="LLM integration, RAG pipelines, and agent workflows for real business operations.",
  meta="AI automation services: LLM integration, RAG pipelines, and agentic workflows with n8n or custom orchestration, built for production.",
  hero="AI agents doing real work, with logs to prove it.",
  body=[
    "The distance between an AI demo and an AI system is error handling, evaluation, and cost control. Syvora builds automation that survives contact with production: retrieval pipelines grounded in your data, agents with explicit tool permissions, and orchestration in n8n or custom code with observability throughout.",
    "We target measurable operations: hours saved, tickets deflected, cycle time cut, and we instrument every workflow so the number is real."
  ],
  scope=[
    ("Opportunity mapping.", "Process mining to find automations with payback in weeks, not quarters."),
    ("RAG systems.", "Retrieval pipelines with chunking, evaluation sets, and grounded citations."),
    ("Agent workflows.", "Multi-step agents with tool access, approvals, and human-in-the-loop gates."),
    ("Orchestration.", "n8n or custom orchestration with retries, queues, and full run logs."),
    ("Evaluation.", "Golden datasets and regression checks so model changes cannot silently degrade output."),
    ("Cost & latency.", "Model routing, caching, and budgets that keep unit economics sane."),
  ],
  deliverables=["Automation opportunity report", "Production RAG or agent system", "Evaluation harness with baselines", "Run logs and monitoring dashboard", "Cost model per workflow"],
  faqs=[
    ("Which models do you use?", "Whatever the eval says: frontier APIs for reasoning-heavy steps, smaller or open models where they match quality at lower cost. Routing is part of the design."),
    ("How do you stop hallucinations in workflows?", "Grounded retrieval, constrained outputs, verification steps, and human approval on consequential actions. Agents get permissions, not free rein."),
    ("n8n or custom code?", "n8n for speed and visibility on integration-heavy flows, custom services when latency or complexity demands it. We run both in production."),
  ],
  tech=["python", "n8n", "typescript"], related=["api-backend-development", "data-engineering-analytics", "servicenow-virtual-agent-ai"],
),

"mobile-app-development": dict(
  practice="extended-capabilities", name="Mobile App Development",
  short="React Native and Flutter applications shipped to both app stores.",
  meta="Mobile app development services: React Native and Flutter apps shipped to the App Store and Google Play with native quality.",
  hero="One codebase, two stores, zero excuses on quality.",
  body=[
    "Cross-platform is a compounding advantage when it is engineered properly and a compounding liability when it is not. Syvora builds React Native and Flutter apps with native-feeling navigation, offline-first data, and release pipelines that make shipping weekly boring.",
    "From v1 launches to rescuing apps with two-star performance reviews, we treat mobile like the product surface it is."
  ],
  scope=[
    ("Product build.", "React Native or Flutter apps with platform-correct UX on iOS and Android."),
    ("Native integration.", "Camera, biometrics, payments, and background work via native modules when needed."),
    ("Offline & sync.", "Local-first storage with conflict-aware synchronization."),
    ("Performance.", "Startup time, frame rate, and bundle size treated as budgets in CI."),
    ("Release engineering.", "Fastlane pipelines, staged rollouts, OTA updates, and crash monitoring."),
    ("Store operations.", "Listings, review compliance, and phased launch management."),
  ],
  deliverables=["Published iOS and Android apps", "CI/CD with automated store deployment", "Crash and performance monitoring", "Offline sync architecture", "Release playbook"],
  faqs=[
    ("React Native or Flutter?", "React Native when you have a web React team to share code and people with; Flutter for heavy custom UI. We recommend per team, not per trend."),
    ("Can you rescue our existing app?", "Yes. A one-week audit covers crashes, performance, and architecture, then we fix in impact order. Ratings usually respond within two releases."),
    ("Do you handle app store review?", "End to end, including the rejection appeals. Compliance is designed in, which is why our submissions rarely bounce."),
  ],
  tech=["react-native", "flutter", "typescript"], related=["web-application-development", "api-backend-development", "product-design-ui-engineering"],
),

"data-engineering-analytics": dict(
  practice="extended-capabilities", name="Data Engineering & Analytics",
  short="Pipelines, warehouses, and dashboards that make product and on-chain data usable.",
  meta="Data engineering services: ELT pipelines, warehouse modeling with dbt, and analytics dashboards teams actually trust.",
  hero="From scattered data to numbers people trust.",
  body=[
    "Analytics fails socially before it fails technically: nobody trusts the dashboard, so nobody uses it. Syvora builds data platforms where trust is engineered in: tested pipelines, documented models, and metrics defined once instead of five slightly different ways.",
    "We handle product analytics, operational reporting, and the on-chain data workloads most data teams have never met."
  ],
  scope=[
    ("Pipeline engineering.", "ELT with orchestration, retries, and freshness monitoring."),
    ("Warehouse modeling.", "dbt models with tests and documentation, on BigQuery or Postgres."),
    ("Metrics layer.", "Single definitions for the numbers leadership argues about."),
    ("Dashboards.", "Focused reporting that answers decisions, not vanity walls."),
    ("On-chain analytics.", "Indexed chain data joined with product data for full-funnel views."),
    ("Data quality.", "Anomaly detection and contracts that catch breakage before Monday's meeting."),
  ],
  deliverables=["Pipeline and warehouse infrastructure", "dbt project with tests and docs", "Metrics definitions", "Executive and team dashboards", "Data quality monitors"],
  faqs=[
    ("Our dashboards disagree with each other. Fixable?", "Yes, and it is the most common ask. A metrics layer with single definitions ends the argument; migration takes weeks, not quarters."),
    ("Do we need a big warehouse?", "Usually not at first. Postgres plus dbt covers more scale than most products ever reach; we upgrade when data volume says so."),
    ("Can you join on-chain and product data?", "Yes. Our indexing practice lands chain data in the same warehouse, so wallets, users, and revenue live in one model."),
  ],
  tech=["python", "postgresql", "gcp"], related=["blockchain-indexing-data", "database-architecture", "ai-agentic-automation"],
),

"devops-platform-engineering": dict(
  practice="extended-capabilities", name="DevOps & Platform Engineering",
  short="Kubernetes, Terraform, GitHub Actions, and full environment automation.",
  meta="DevOps and platform engineering services: Kubernetes, Terraform, GitHub Actions, and golden-path automation that speeds every team.",
  hero="Deploys so smooth your engineers forget release day existed.",
  body=[
    "Platform engineering is leverage: every hour invested speeds every engineer after it. Syvora builds the golden path: templated services, one-command environments, pipelines with progressive delivery, and infrastructure that new hires can reason about in week one.",
    "We meet you where you are, from taming a hand-built cluster to designing a platform for a team of fifty."
  ],
  scope=[
    ("Platform design.", "Golden paths and paved roads that make the right way the easy way."),
    ("Kubernetes.", "Cluster architecture, GitOps with Argo CD, and workload standards."),
    ("Infrastructure as code.", "Terraform modules and policy checks with drift detection."),
    ("CI/CD.", "GitHub Actions pipelines with caching, preview environments, and canary deploys."),
    ("Developer experience.", "Local environments, service templates, and docs that stay true."),
    ("Security & secrets.", "Least-privilege access, secret management, and supply chain checks."),
  ],
  deliverables=["Platform architecture doc", "GitOps-managed clusters", "Reusable Terraform modules", "Golden-path service template", "Deployment metrics dashboard"],
  faqs=[
    ("Do we actually need Kubernetes?", "Maybe not, and we will say so. Below a certain scale, managed containers or the edge deliver the same outcomes with less ceremony."),
    ("What improves first?", "Deployment frequency and lead time. Teams typically go from weekly, nervous releases to daily, boring ones within the first month."),
    ("Can you work alongside our platform team?", "That is the default mode. We add capacity and patterns, then hand the paved road to your team with documentation."),
  ],
  tech=["kubernetes", "aws", "cloudflare", "go"], related=["cloud-infrastructure", "performance-reliability-engineering", "qa-test-automation"],
),

"qa-test-automation": dict(
  practice="extended-capabilities", name="QA & Test Automation",
  short="Playwright, Cypress, and API test suites wired directly into CI.",
  meta="QA and test automation services: Playwright and Cypress suites, API testing, and CI integration that catches bugs before users do.",
  hero="Test suites that catch bugs and keep your team's trust.",
  body=[
    "Bad test suites die of flakiness; teams stop believing them and start clicking merge anyway. Syvora builds automation engineered for trust: stable selectors, controlled test data, parallel execution, and a quarantine process so one flaky test never poisons the signal.",
    "Coverage follows risk: the money paths first, the edge cases when they earn it, and everything wired into CI so quality is a gate rather than a hope."
  ],
  scope=[
    ("Test strategy.", "Risk-based coverage mapping across UI, API, and integration layers."),
    ("E2E automation.", "Playwright or Cypress suites with resilient patterns and visual checks where they pay."),
    ("API testing.", "Contract and integration tests that catch breakage below the UI."),
    ("Test data.", "Seeded, isolated data management so tests never fight each other."),
    ("CI integration.", "Parallelized runs, flake quarantine, and readable failure reports."),
    ("Quality metrics.", "Escape rate, coverage of critical paths, and suite reliability tracked openly."),
  ],
  deliverables=["Test strategy document", "Automated suites in CI", "Test data management setup", "Flake quarantine process", "Quality metrics dashboard"],
  faqs=[
    ("Playwright or Cypress?", "Playwright for new builds: faster, better parallelism, first-class multi-browser. Cypress stays when a team already runs it well."),
    ("How do you handle flaky tests?", "Quarantine on first flake, root-cause within the sprint, and reliability tracked as a suite-level SLO. Flakiness is treated as a defect."),
    ("What coverage should we aim for?", "One hundred percent of revenue-critical journeys before breadth anywhere else. A hundred meaningful tests beat a thousand brittle ones."),
  ],
  tech=["typescript", "nodejs"], related=["performance-reliability-engineering", "web-application-development", "devops-platform-engineering"],
),

"technical-seo-growth": dict(
  practice="extended-capabilities", name="Technical SEO & Growth",
  short="Structured data, performance, and content architecture for organic acquisition.",
  meta="Technical SEO services: site architecture, structured data, Core Web Vitals, and programmatic SEO systems that compound organic growth.",
  hero="Organic growth treated as an engineering problem.",
  body=[
    "Most SEO fails at the architecture layer: pages that rank rotate away, internal links scatter authority, and templates ship without the markup crawlers reward. Syvora runs SEO as engineering: hub-and-spoke architecture, programmatic page systems, structured data, and Core Web Vitals enforced in CI.",
    "This is the discipline behind our own products and client programs: permanent hub pages capturing the demand that listing pages leak."
  ],
  scope=[
    ("Architecture.", "Hub-and-spoke information architecture with internal linking designed on purpose."),
    ("Programmatic SEO.", "Template systems generating hundreds of unique, indexable pages from structured data."),
    ("Structured data.", "Schema.org markup: Organization, Service, FAQ, Product, and Breadcrumb done correctly."),
    ("Performance.", "Core Web Vitals budgets and rendering strategy that crawlers and users both feel."),
    ("Indexation control.", "Canonical, robots, and sitemap discipline so crawl budget lands on money pages."),
    ("Measurement.", "Search Console mining that finds ranking pages leaking clicks and fixes them."),
  ],
  deliverables=["Technical SEO audit", "Site architecture and linking map", "Programmatic page system", "Structured data implementation", "Search performance dashboard"],
  faqs=[
    ("What is programmatic SEO exactly?", "Generating many high-quality pages from structured data: services by capability, locations, comparisons. This very website is built that way."),
    ("How long until results?", "Technical fixes show in weeks; architecture compounds over one to two quarters. We report leading indicators, impressions and coverage, from week one."),
    ("Do you write content too?", "We architect and template it, and produce technical content ourselves. For volume editorial we pair with your writers inside our structure."),
  ],
  tech=["nextjs", "cloudflare", "python"], related=["web-application-development", "shopify-commerce-engineering", "data-engineering-analytics"],
),
}
