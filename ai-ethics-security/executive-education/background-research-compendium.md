# Executive MBA GenAI Curriculum: Background Research Compendium

> **Research Compiled**: December 2024
> **Purpose**: Evidence-based background research to inform Executive MBA curriculum development on Generative AI ethics, data governance, security, and product implementation.

---

## Table of Contents

1. [AI Ethics Frameworks and Principles](#1-ai-ethics-frameworks-and-principles)
2. [Regulatory Landscape](#2-regulatory-landscape)
3. [AI Security Threats and Best Practices](#3-ai-security-threats-and-best-practices)
4. [Data Governance and Privacy](#4-data-governance-and-privacy)
5. [AI Bias and Fairness Research](#5-ai-bias-and-fairness-research)
6. [Enterprise AI Governance](#6-enterprise-ai-governance)
7. [AI Product Development Methodologies](#7-ai-product-development-methodologies)
8. [Technical Foundations: RAG, Hallucination Mitigation, XAI](#8-technical-foundations)
9. [Human Oversight Research](#9-human-oversight-research)
10. [Workforce Impact and Change Management](#10-workforce-impact-and-change-management)
11. [AI Incidents and Case Studies](#11-ai-incidents-and-case-studies)
12. [Sources and References](#12-sources-and-references)

---

## 1. AI Ethics Frameworks and Principles

### 1.1 NIST AI Risk Management Framework (AI RMF)

**Source**: [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

The AI RMF is a voluntary framework designed to improve the ability to incorporate trustworthiness considerations into AI design, development, use, and evaluation.

**Key 2024-2025 Updates**:

- **AI RMF 2.0** (February 2024): First major update building on early adoption experiences and adapting to evolved AI paradigms including generative AI
- **Generative AI Profile** (July 2024): Tailors the framework specifically for content-creating systems, describing risks unique to or exacerbated by GAI
- **Dioptra Testing Platform**: Open-source security testbed for adversarial evaluations, benchmarking models against evasion, poisoning, and extraction attacks
- **March 2025 Updates**: Emphasis on model provenance, data integrity, and third-party model assessment

**Four Core Functions**:
1. **Govern**: Organizational structures and policies
2. **Map**: Context and risk identification
3. **Measure**: Risk assessment and analysis
4. **Manage**: Risk treatment and monitoring

**Source**: [NIST AI RMF 2025 Updates](https://www.ispartnersllc.com/blog/nist-ai-rmf-2025-updates-what-you-need-to-know-about-the-latest-framework-changes/)

---

### 1.2 OECD AI Principles (2024 Update)

**Source**: [OECD Updates AI Principles](https://www.oecd.org/en/about/news/press-releases/2024/05/oecd-updates-ai-principles-to-stay-abreast-of-rapid-technological-developments.html)

The OECD AI Principles were revised at the May 2024 Ministerial Council Meeting, representing the first update since their 2019 adoption.

**The Five Value-Based Principles**:
1. Inclusive growth, sustainable development, and human well-being
2. Respect for the rule of law, human rights, and democratic values
3. Transparency and explainability
4. Robustness, security, and safety
5. Accountability

**Key 2024 Revisions**:
- Enhanced focus on **safety**, **privacy**, **intellectual property rights**, and **information integrity**
- New provisions addressing **misinformation and disinformation** amplified by AI
- Emphasis on **responsible business conduct** throughout the AI lifecycle
- Explicit reference to **environmental sustainability**
- Requirement for information on AI decision-making now relates to *challenging*, rather than just understanding, AI outcomes

**Adoption**: Now endorsed by **47 jurisdictions** including the European Union.

**Source**: [Evolving with Innovation: The 2024 OECD AI Principles Update](https://oecd.ai/en/wonk/evolving-with-innovation-the-2024-oecd-ai-principles-update)

---

### 1.3 IEEE Ethically Aligned Design (EAD)

**Source**: [IEEE Ethically Aligned Design](https://standards.ieee.org/wp-content/uploads/import/documents/other/ead_v2.pdf)

A comprehensive vision for the development of autonomous and intelligent systems (A/IS) that prioritizes human well-being.

**Five General Principles**:
1. **Human Well-being**: Primary success criterion for development
2. **Accountability**: Evidence of effectiveness and fitness for purpose
3. **Transparency**: Unambiguous rationale for all decisions
4. **Awareness of Misuse**: Guard against potential misuses and risks
5. **Data Agency**: Individuals' rights to control their personal data

**Related Standards**:
- **IEEE 7000**: Model Process for Addressing Ethical Concerns During System Design
- **IEEE 7010**: Wellbeing Metrics Standard for Ethical Artificial Intelligence
- **IEEE CertifAIEd**: Certification mark for responsible AI systems

**Source**: [IEEE Ethics In Action](https://ethicsinaction.ieee.org/)

---

### 1.4 ISO/IEC 42001:2023 - AI Management Systems

**Source**: [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)

Published December 2023, ISO 42001 is the **first international certifiable management system standard for AI**.

**Key Features**:
- Specifies requirements for establishing, implementing, maintaining, and improving an AI Management System (AIMS)
- Applicable to all organization types and industries
- Facilitates compliance with regulations like the EU AI Act
- Promotes development and use of trustworthy, transparent, and accountable AI systems

**2024 Adoption**:
- ANAB launched the ISO 42001 certification program in January 2024
- 15 certification bodies have applied for accreditation
- Microsoft achieved ISO 42001 certification in 2024
- Infosys received ISO 42001:2023 certification in 2024

**Source**: [ISO/IEC 42001 - AI Management Systems (ANAB)](https://blog.ansi.org/anab/iso-iec-42001-ai-management-systems/)

---

## 2. Regulatory Landscape

### 2.1 EU AI Act (Regulation 2024/1689)

**Source**: [EU AI Act - Shaping Europe's Digital Future](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

The **first comprehensive legal framework on AI worldwide**, entered into force August 1, 2024.

**Implementation Timeline**:
| Date | Milestone |
|------|-----------|
| August 1, 2024 | Entry into force |
| February 2, 2025 | Prohibited AI practices and AI literacy obligations |
| August 2, 2025 | Governance rules and GPAI model obligations |
| August 2, 2026 | Full applicability |
| August 2, 2027 | Extended transition for high-risk AI in regulated products |

**Risk Classification**:

| Risk Level | Examples | Requirements |
|------------|----------|--------------|
| **Unacceptable** | Social scoring, real-time biometric surveillance | Prohibited |
| **High Risk** | Hiring, credit, healthcare, law enforcement | Conformity assessment, registration, monitoring |
| **Limited Risk** | Chatbots, emotion recognition | Transparency obligations |
| **Minimal Risk** | Spam filters, recommendations | No specific requirements |

**High-Risk AI Provider Obligations**:
1. Quality Management System
2. Risk Management System (iterative, throughout lifecycle)
3. Documentation & Recordkeeping (technical documentation, automatic logging)
4. Transparency and Human Oversight
5. CE marking and registration
6. Accuracy, robustness, and cybersecurity design

**Source**: [High-level Summary of the AI Act](https://artificialintelligenceact.eu/high-level-summary/)

---

### 2.2 Colorado AI Act (SB24-205)

**Source**: [Colorado AI Act - General Assembly](https://leg.colorado.gov/bills/sb24-205)

Signed May 17, 2024, the **first comprehensive U.S. state law regulating high-risk AI systems**. Effective February 1, 2026.

**Scope**: Developers and deployers of high-risk AI systems in employment, housing, financial services, insurance, and healthcare in Colorado.

**Core Focus**: Mitigate risk of **algorithmic discrimination** - "any condition in which the use of an AI system results in an unlawful differential treatment or impact that disfavors an individual or group."

**Protected Characteristics**: Age, color, disability, ethnicity, genetic information, limited English proficiency, national origin, race, religion, reproductive health, sex, veteran status.

**Compliance Requirements**:
- Developers must publish statements on algorithmic discrimination risk management
- Deployers must implement risk management policy aligned with NIST AI RMF and ISO 42001
- Attorney general has exclusive enforcement authority

**Source**: [Colorado's Landmark AI Act (Skadden)](https://www.skadden.com/insights/publications/2024/06/colorados-landmark-ai-act)

---

### 2.3 Emerging U.S. State Regulations

| State | Legislation | Status | Focus |
|-------|-------------|--------|-------|
| Colorado | SB 24-205 | Enacted (2024) | Algorithmic discrimination |
| Utah | AI Policy Act | Enacted (2024) | Disclosure requirements |
| NYC | Local Law 144 | Enacted (2023) | Bias audits for employment AI |
| Georgia | AI Bill | Proposed | Modeled on Colorado |
| Illinois | AI Bill | Proposed | Modeled on Colorado |

---

## 3. AI Security Threats and Best Practices

### 3.1 OWASP Top 10 for LLM Applications

**Source**: [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

**LLM01:2025 - Prompt Injection** remains the #1 vulnerability:

**Types**:
- **Direct Prompt Injection** ("jailbreaking"): Malicious user overwrites system prompt
- **Indirect Prompt Injection**: Malicious content in external sources (websites, documents, emails) manipulates model behavior

**Attack Patterns Identified**:
- Instructions hidden in images/documents via steganography or invisible characters
- Malicious instructions in document metadata
- Poisoning documents in vector databases (RAG attacks)
- Thought/Observation Injection (forging agent reasoning steps)
- Tool manipulation in LLM agents

**2024-2025 Incidents**:
- **CVE-2024-5184**: LLM email assistant vulnerability allowing access to sensitive information
- **December 2024**: OpenAI ChatGPT search tool vulnerable to indirect injection (The Guardian)
- **January 2025**: DeepSeek-R1 ranked 17th of 19 models in prompt injection resistance

**Mitigations** (OWASP):
- Least privilege access enforcement
- Human oversight for sensitive operations
- External content isolation
- Adversarial testing

**Key Finding**: "Prompt injection remains a persistent challenge" - no complete technical solution exists.

**Source**: [OWASP LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)

---

### 3.2 MITRE ATLAS Framework

**Source**: [MITRE ATLAS](https://atlas.mitre.org/)

ATLAS (Adversarial Threat Landscape for AI Systems) is a knowledge base of adversary tactics and techniques for AI systems, modeled after MITRE ATT&CK.

**Framework Structure**:
- **14 tactics** (adversary goals)
- **82 techniques** (methods to achieve goals)
- Real-world case studies

**Key Attack Types**:
| Attack | Description |
|--------|-------------|
| Data Poisoning | Corrupting training data |
| Model Extraction | Stealing model parameters |
| Model Inversion | Extracting training data |
| Membership Inference | Determining if data was used in training |
| Evasion Attacks | Adversarial inputs causing misclassification |
| Backdoor Attacks | Hidden malicious behaviors |

**AI-Specific Tactics** (not in ATT&CK):
- ML Model Access
- ML Attack Staging

**Source**: [MITRE ATLAS Framework Guide (Practical DevSecOps)](https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/)

---

### 3.3 Defense Techniques

**SmoothLLM (2024)**:
- Randomly perturbs input text and aggregates outputs
- Drives success rate of many jailbreak attacks "down to almost 0%"

**Defense in Depth**:
- Input sanitization (low effectiveness - easily bypassed)
- Output filtering (medium - reduces impact)
- Privilege separation (high - reduces blast radius)
- Human approval workflows (high - catches attacks)
- Canary tokens for detection

---

## 4. Data Governance and Privacy

### 4.1 GDPR and AI Training Data

**Source**: [EDPB Opinion 28/2024](https://www.dataprotectionreport.com/2025/01/the-edpb-opinion-on-training-ai-models-using-personal-data-and-recent-garante-fine-lawful-deployment-of-llms/)

The European Data Protection Board (EDPB) published Opinion 28/2024 in late 2024, addressing AI training with personal data.

**Key Findings**:
- GDPR regularly applies to AI models trained with personal data
- **Legitimate interest** (Article 6(1)(f)) is a practicable alternative to consent
- Three-part test: legitimate purpose + necessity + rights balance

**2024 Enforcement Actions**:
- **OpenAI**: €15 million fine by Italian Garante
- **X (Twitter)**: Agreed to suspend processing EU/EEA user data for LLM training
- **Meta, Google**: Irish DPC inquiries on personal data use for LLMs

**AI Act and GDPR Complementarity**:
Per EDPB March 2024 statement: "the AI Act and the Union data protection legislation...need to be...considered as complementary and mutually reinforcing instruments."

**Source**: [Top 10 Operational Impacts of the EU AI Act (IAPP)](https://iapp.org/resources/article/top-impacts-eu-ai-act-leveraging-gdpr-compliance/)

---

### 4.2 Data Governance Best Practices

**Essential Elements**:
1. Clear data governance standards for AI projects
2. Comprehensive AI governance programme with triage processes
3. Defined purposes for personal data use
4. Data lineage and provenance tracking
5. Training data transparency requirements

**Source**: [Data Protection in 2024: The Era of AI Clauses](https://gdprlocal.com/data-protection-in-2024-the-era-of-ai-clauses/)

---

## 5. AI Bias and Fairness Research

### 5.1 Sources of Bias

**Source**: [Fairness and Bias in AI: A Brief Survey (MDPI)](https://www.mdpi.com/2413-4155/6/1/3)

| Bias Type | Source | Example |
|-----------|--------|---------|
| Historical | Training data reflects past discrimination | Hiring AI favors historically hired demographics |
| Representation | Under/over-representation in data | Medical AI trained mostly on one demographic |
| Measurement | Proxies for protected characteristics | ZIP code as proxy for race |
| Aggregation | Single model for diverse populations | Same credit model across cultures |
| Amplification | AI exacerbates learned biases | 2024 UCL study findings |

### 5.2 Key 2024 Research

**Amplification Bias (UCL 2024)**:
AI not only learns human biases but exacerbates them, creating feedback loops where users of biased AI become more biased themselves.

**MIT Debiasing Technique (December 2024)**:
"Specific points in our dataset are contributing to this bias, and we can find those data points, remove them, and get better performance."

**Source**: [MIT Researchers Reduce Bias While Preserving Accuracy](https://news.mit.edu/2024/researchers-reduce-bias-ai-models-while-preserving-improving-accuracy-1211)

### 5.3 Inherent Limitations

**Source**: [Inherent Limitations of AI Fairness (ACM)](https://cacm.acm.org/research/inherent-limitations-of-ai-fairness/)

"AI fairness methods can only make guarantees about fairness based on strong assumptions that are unrealistic in practice...AI fairness suffers from inherent limitations that prevent the field from accomplishing its goal on its own."

### 5.4 Tools and Frameworks

- **IBM AI Fairness 360**: Open-source toolkit with fairness metrics and bias mitigation algorithms
- **Google What-If Tool**: Visualize and compare model predictions across demographics
- **Blueprint for an AI Bill of Rights** (White House): Principles emphasizing fairness, privacy, transparency

### 5.5 Documented Bias Examples

- **Facial Recognition**: Error rates for dark-skinned women reached 35% vs. <1% for light-skinned men

---

## 6. Enterprise AI Governance

### 6.1 McKinsey Research Findings

**Source**: [A Generative AI Reset (McKinsey)](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/a-generative-ai-reset-rewiring-to-turn-potential-into-value-in-2024)

**Governance Gap Statistics**:
- Only **18%** of organizations have an enterprise-wide AI governance council
- Only **one-third** require AI risk mitigation as a technical skill set

**High Performer Characteristics**:
- Nearly twice as likely to involve legal function and embed risk reviews early ("shift left")
- More likely to employ wide range of best practices from strategy to scaling

**Recommendations**:
- Establish governance structure balancing expertise with rapid decision-making
- Embed governance in operating model with cross-organizational expertise
- Launch sprint to understand inbound AI risk exposures
- Develop comprehensive view of risk materiality across use cases

**Source**: [Implementing GenAI with Speed and Safety (McKinsey)](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/implementing-generative-ai-with-speed-and-safety)

---

### 6.2 Gartner Findings

**Source**: [Gartner Enterprise Guide to Generative AI](https://www.gartner.com/en/topics/generative-ai)

**Key Statistics**:
- GenAI is now the **most frequently deployed AI solution** in organizations (2024)
- AI leaders face challenges demonstrating ROI, identifying use cases, managing expectations

**Four Foundational Capabilities for AI Maturity**:
1. Scalable AI operating model (centralized + distributed)
2. AI engineering focus
3. Systematic approach to building and deploying AI
4. Change management investment

**Recommendation**: "Focus on augmentation, not replacement: Prioritize using GenAI to augment employee productivity rather than focusing solely on cost savings."

---

## 7. AI Product Development Methodologies

### 7.1 Responsible AI Lifecycle Approaches

**Google (2024)**:

**Source**: [Google Responsible AI 2024 Report](https://blog.google/technology/ai/responsible-ai-2024-report-ongoing-work/)

- 6th annual Responsible AI Progress Report
- Govern, map, measure, manage AI risk throughout lifecycle
- **Frontier Safety Framework** (2024): Protocols to address risks from powerful frontier models
- Published AI principles in 2018; annual transparency reports since 2019

**Microsoft**:

**Six Dimensions of Responsible AI**:
1. Fairness
2. Reliability and safety
3. Privacy and security
4. Inclusiveness
5. Transparency
6. Accountability

Provides tools, processes, and best practices throughout AI lifecycle.

**Frontier Model Forum** (Google, Microsoft, Anthropic, OpenAI):

**Source**: [Frontier Model Forum Announcement](https://blog.google/outreach-initiatives/public-policy/google-microsoft-openai-anthropic-frontier-model-forum/)

Industry body focused on:
- Advancing AI safety research
- Identifying best practices for responsible development
- Collaborating with policymakers, academics, civil society
- Supporting applications addressing societal challenges

---

### 7.2 Model Cards and Documentation

**Source**: [Systematic Analysis of 32K AI Model Cards (Nature Machine Intelligence)](https://www.nature.com/articles/s42256-024-00857-z)

**Key Findings from Analysis of 32,111 Model Cards**:
- Sections on **environmental impact**, **limitations**, and **evaluation** have lowest fill-out rates
- **Training section** most consistently completed
- Adding model cards correlates with increased download rates

**Industry Adoption**:
- Meta: Model Cards with fairness dashboards
- Hugging Face: Model card for every Hub model
- OpenAI: Internal Model Card-like documentation
- Stanford CRFM: Detailed datasheets for HELM benchmark models

**Best Practices**:
- Allocate efforts to documenting dataset-related ethical issues
- Focus on data curation and distribution transparency
- Use checklists/tools to raise awareness of ethical documentation needs

---

## 8. Technical Foundations

### 8.1 Retrieval-Augmented Generation (RAG)

**Source**: [RAG Comprehensive Survey (arXiv)](https://arxiv.org/abs/2410.12837)

**2024 Market Statistics**:
- Large Enterprise segment: **72.2%** market share
- Cloud segment: **75.9%** market share
- Over **1,200 RAG-related papers** on arXiv in 2024 (vs. <100 in 2023)

**Key 2024 Developments**:
- **GraphRAG** (Microsoft): Open-sourced mid-2024, addresses semantic gap issues
- **RAPTOR**: Recursive Abstractive Processing for Tree-Organized Retrieval
- RAG + Agents integration accelerating in late 2024

**Effectiveness**:
- Reduces hallucinations by **42-68%**
- Medical AI with trusted sources: up to **89%** factual accuracy
- Stanford 2024 study: RAG + RLHF + guardrails = **96%** hallucination reduction

**Source**: [What is RAG (McKinsey)](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-retrieval-augmented-generation-rag)

---

### 8.2 Hallucination Mitigation

**Source**: [Comprehensive Survey of Hallucination Mitigation Techniques (arXiv)](https://arxiv.org/abs/2401.01313)

**Identified Techniques**: Over 32 methods including:
- Retrieval Augmented Generation
- Knowledge Retrieval
- Chain-of-Verification (CoVe)
- Self-consistency checking

**Hallucination Rates by Domain**:
| Domain | Hallucination Rate |
|--------|-------------------|
| Speech Recognition | 1.4% |
| Medical Reporting | Reduced 38% with domain grounding |
| Legal Text Generation | >16% |

**Key Approaches**:
1. **RAG**: Grounding in external knowledge
2. **Prompt Engineering**: Designing prompts to reduce hallucinations
3. **Fine-tuning**: Domain-specific training
4. **Multi-model Systems**: Cross-validation
5. **Human-in-the-loop**: Oversight and verification

---

### 8.3 Explainable AI (XAI)

**Source**: [XAI 2024: Algorithmic Transparency and EU AI Act](https://www.swiftask.ai/blog/explainable-ai-xai)

**Four Essential Pillars**:
1. **Transparency**: Understanding internal workings
2. **Interpretability**: Explaining decisions in understandable terms
3. **Justifiability**: Demonstrating reasoning
4. **Auditability**: Complete traceability

**Regulatory Requirements**:
- EU AI Act requires explanations for certain AI systems
- NIST AI RMF emphasizes voluntary explainability guidelines

**Key Techniques**:
- Feature attribution
- Rule-based explanations
- Surrogate models
- Saliency maps
- Counterfactual explanations
- SHAP, LIME

**Challenges**:
- Balance between performance and transparency (8-12% accuracy trade-off)
- Cognitive overload from too many explanations

**Impact Example**: Major European bank reduced credit decision disputes by **30%** using SHAP models.

---

## 9. Human Oversight Research

### 9.1 Feasibility of Human Oversight

**Source**: [Is Human Oversight to AI Systems Still Possible? (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1871678424005636)

**Key Finding** (Holzinger et al., December 2024):
"While complete oversight may no longer be viable in certain contexts, strategic interventions leveraging human-AI collaboration and trustworthy AI design principles can preserve accountability and safety."

**Challenges**:
- Algorithms operate as black boxes
- Constant algorithmic modification impedes oversight
- Humans tend to overtrust computer systems

---

### 9.2 Effective Human Oversight (ACM FAccT 2024)

**Source**: [On the Quest for Effectiveness in Human Oversight (ACM)](https://dl.acm.org/doi/10.1145/3630106.3659051)

**Three Domains Affecting Effectiveness**:
1. Technical design of the system
2. Individual factors of oversight persons
3. Environmental circumstances

**EU AI Act Article 14 Analysis**:
Framework scrutinized as exemplary regulatory approach to human oversight requirements.

---

### 9.3 Risk-Based Framework

**Oversight Levels by Context**:

| Context | Oversight Level | Example |
|---------|-----------------|---------|
| Low-stakes, routine | Automated with audits | Spam filtering |
| High-volume, clear criteria | Automation with exception handling | Insurance claims |
| High-stakes, safety-critical | Human-in-the-loop | Collision avoidance in AVs |
| Complex judgment | Human-in-command | Medical diagnosis |

**Future Prediction**: By 2027, ~15% of new applications will be AI-generated without human-in-the-loop.

---

## 10. Workforce Impact and Change Management

### 10.1 WEF Future of Jobs Report 2025

**Source**: [WEF Future of Jobs Report](https://technologymagazine.com/articles/wef-report-the-impact-of-ai-driving-170m-new-jobs-by-2030)

**Key Statistics**:
- AI and automation will transform **86%** of businesses by 2030
- **170 million new jobs** created, **92 million** displaced
- **40%** of employers expect to reduce workforce where AI can automate tasks
- **39%** of existing skill sets will become outdated 2025-2030
- **85%** of employers plan to prioritize workforce upskilling
- **77%** plan to prioritize reskilling for AI collaboration by 2030
- **63%** identify skills gaps as primary barrier to transformation

**Fastest Growing Roles**:
- Big data specialists
- Fintech engineers
- AI specialists
- Autonomous vehicle specialists
- Renewable energy engineers

**At-Risk Roles**:
- Market research analysts: 53% tasks automatable
- Sales representatives: 67% tasks automatable

**Source**: [WEF Leveraging GenAI for Workforce Productivity (PDF)](https://reports.weforum.org/docs/WEF_Leveraging_Generative_AI_for_Job_Augmentation_and_Workforce_Productivity_2024.pdf)

---

## 11. AI Incidents and Case Studies

### 11.1 Incident Databases

**AI Incident Database (AIID)**:
- Source: [incidentdatabase.ai](https://incidentdatabase.ai/)
- Sponsored by Partnership on AI
- Corporate product managers, risk officers, engineers as primary users

**MIT AI Incident Tracker**:
- Source: [MIT AI Risk](https://airisk.mit.edu/ai-incident-tracker)
- Classifies incidents using EU AI Act risk levels
- Detailed severity analysis across 10 harm categories

**2024 Statistics**:
- Documented AI safety incidents: **233** (up from 149 in 2023)
- **56.4%** increase year-over-year

---

### 11.2 Notable 2024 Enterprise AI Failures

| Incident | Organization | Impact | Key Lesson |
|----------|--------------|--------|------------|
| **Chatbot Misinformation** | Air Canada | Damages paid to passenger; tribunal ruling | Companies liable for AI-generated customer communications |
| **Drive-Thru AI** | McDonald's/IBM | Partnership ended after 3 years | AI reliability in customer-facing roles |
| **MyCity Chatbot** | NYC Government | False legal/business guidance | Government AI requires rigorous validation |
| **AI-Generated Reports** | Deloitte | False citations, fabricated papers in $1.6M Canadian healthcare report | AI content requires human verification |
| **API Breach** | T-Mobile | Customer data accessed via AI-equipped API | AI-enabled attack vectors |
| **ChatGPT Search** | OpenAI | Vulnerable to indirect prompt injection (Guardian, Dec 2024) | Even leading models have security gaps |

**Cost Data**:
- Global average data breach cost (IBM 2024): **$4.88 million**
- Single hallucinated chatbot answer: **$100 billion** shareholder value erased (within hours)

**Source**: [AI Safety Incidents 2024 (Responsible AI Labs)](https://responsibleailabs.ai/knowledge-hub/articles/ai-safety-incidents-2024)

---

## 12. Sources and References

### Regulatory and Framework Sources

1. [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
2. [NIST AI RMF 2025 Updates](https://www.ispartnersllc.com/blog/nist-ai-rmf-2025-updates-what-you-need-to-know-about-the-latest-framework-changes/)
3. [EU AI Act - European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
4. [EU AI Act High-Level Summary](https://artificialintelligenceact.eu/high-level-summary/)
5. [Colorado AI Act](https://leg.colorado.gov/bills/sb24-205)
6. [Colorado AI Act Analysis (Skadden)](https://www.skadden.com/insights/publications/2024/06/colorados-landmark-ai-act)
7. [OECD AI Principles Update](https://www.oecd.org/en/about/news/press-releases/2024/05/oecd-updates-ai-principles-to-stay-abreast-of-rapid-technological-developments.html)
8. [IEEE Ethically Aligned Design](https://standards.ieee.org/wp-content/uploads/import/documents/other/ead_v2.pdf)
9. [ISO/IEC 42001:2023](https://www.iso.org/standard/42001)

### Security Sources

10. [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
11. [OWASP Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
12. [MITRE ATLAS](https://atlas.mitre.org/)

### Data Governance Sources

13. [EDPB Opinion on AI Training Data](https://www.dataprotectionreport.com/2025/01/the-edpb-opinion-on-training-ai-models-using-personal-data-and-recent-garante-fine-lawful-deployment-of-llms/)
14. [AI Act and GDPR Complementarity (IAPP)](https://iapp.org/resources/article/top-impacts-eu-ai-act-leveraging-gdpr-compliance/)

### Research Sources

15. [AI Bias Survey (MDPI)](https://www.mdpi.com/2413-4155/6/1/3)
16. [MIT Bias Reduction Research](https://news.mit.edu/2024/researchers-reduce-bias-ai-models-while-preserving-improving-accuracy-1211)
17. [Inherent Limitations of AI Fairness (ACM)](https://cacm.acm.org/research/inherent-limitations-of-ai-fairness/)
18. [Hallucination Mitigation Survey (arXiv)](https://arxiv.org/abs/2401.01313)
19. [RAG Comprehensive Survey (arXiv)](https://arxiv.org/abs/2410.12837)
20. [Human Oversight Research (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1871678424005636)
21. [Human Oversight Effectiveness (ACM FAccT)](https://dl.acm.org/doi/10.1145/3630106.3659051)
22. [Model Cards Analysis (Nature Machine Intelligence)](https://www.nature.com/articles/s42256-024-00857-z)

### Industry Sources

23. [McKinsey GenAI Reset 2024](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/a-generative-ai-reset-rewiring-to-turn-potential-into-value-in-2024)
24. [McKinsey GenAI Safety Implementation](https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/implementing-generative-ai-with-speed-and-safety)
25. [Gartner GenAI Guide](https://www.gartner.com/en/topics/generative-ai)
26. [Google Responsible AI 2024 Report](https://blog.google/technology/ai/responsible-ai-2024-report-ongoing-work/)
27. [Frontier Model Forum](https://blog.google/outreach-initiatives/public-policy/google-microsoft-openai-anthropic-frontier-model-forum/)

### Workforce Impact Sources

28. [WEF Future of Jobs Report](https://technologymagazine.com/articles/wef-report-the-impact-of-ai-driving-170m-new-jobs-by-2030)
29. [WEF GenAI Workforce Productivity](https://reports.weforum.org/docs/WEF_Leveraging_Generative_AI_for_Job_Augmentation_and_Workforce_Productivity_2024.pdf)

### Incident Sources

30. [AI Incident Database](https://incidentdatabase.ai/)
31. [MIT AI Incident Tracker](https://airisk.mit.edu/ai-incident-tracker)
32. [AI Safety Incidents 2024](https://responsibleailabs.ai/knowledge-hub/articles/ai-safety-incidents-2024)

---

*This research compendium serves as the evidence base for Executive MBA curriculum development on Generative AI. All sources are from 2024-2025 where available, representing the current state of research, regulation, and industry practice.*
