# AI Modules Development Outline
## Executive MBA: Introduction to GenAI (3 Hours Total)

> **Development Plan**: December 2025
> **Target Audience**: C-suite executives, board members, senior VPs, Executive MBA students
> **No technical AI background required**

---

## Overview

This outline proposes an approach for developing the two AI modules based on the existing research. The goal is to transform comprehensive research into engaging, actionable executive education that balances strategic depth with practical applicability.

---

## Module 1: Data and Project Management (1 Hour)

### Recommended Structure

| Section | Duration | Primary Focus |
|---------|----------|---------------|
| Opening & Context Setting | 5 min | Why this matters now |
| Part 1: Data Foundation | 20 min | Data as the foundation of AI success |
| Part 2: Project Management | 25 min | How AI projects differ and succeed |
| Part 3: Strategic Considerations | 10 min | Maturity model & resource allocation |

### Content Development Priorities

**Part 1: Data Foundation (20 min)**
- The Data Hierarchy of Needs (visual framework)
- Three categories of enterprise GenAI data (Training, Context, Operational)
- Data quality dimensions with real consequences
- The "hidden costs" case study (4 months → 15 months)
- Data governance minimum requirements

**Key Update from 2025 Research**: Integrate IP/Copyright considerations around training data rights (from Section 2 of supplement)

**Part 2: Project Management (25 min)**
- Why traditional PM fails for AI (comparison table)
- The 6-phase AI Project Lifecycle
- Success metrics that matter (business outcomes, not vanity metrics)
- Five common failure modes with mitigation strategies
- Build vs. Buy vs. Partner decision framework

**Key Update from 2025 Research**:
- MIT finding: 67% success rate for purchase/partner vs. 22% for internal builds
- Vendor evaluation framework from Section 5 of supplement
- ROI timeline expectations (6-48 months depending on use case)

**Part 3: Strategic Considerations (10 min)**
- GenAI Maturity Model (5 levels)
- Portfolio approach to AI investment
- Change management imperatives

---

### Module 1 In-Class Activities

#### Activity 1: Data Readiness Assessment (8-10 min)
**Format**: Individual reflection → Table discussion → Report out

**Exercise**: Participants complete a rapid self-assessment of their organization's data readiness across 5 dimensions:
1. Data accessibility (Can your teams access the data they need?)
2. Data quality (Is your data accurate, complete, consistent?)
3. Data governance (Do you have clear ownership, lineage, controls?)
4. Data rights (Do you have legal rights to use your data for AI?)
5. Data advantage (What data do you have that competitors don't?)

**Materials**: One-page scorecard (1-5 scale per dimension)

**Discussion Prompt**: "Where are your organization's biggest data gaps? What would it take to close them?"

---

#### Activity 2: AI Project Autopsy (10-12 min)
**Format**: Small groups (3-4 people) analyze a case

**Exercise**: Groups receive a brief (half-page) description of a failed AI project. They must:
1. Identify which of the 5 failure modes caused the failure
2. Determine at which project phase the failure was seeded
3. Propose what should have been done differently

**Case Options** (rotate among groups):
- **Case A**: "The Perfect PoC" - A model that worked brilliantly in testing but failed in production
- **Case B**: "Scope Tsunami" - A customer service AI that kept expanding until it collapsed
- **Case C**: "Data Mirage" - A predictive model built on data that didn't exist at the quality assumed

**Debrief**: Each group shares their diagnosis in 1-2 minutes

---

#### Activity 3: Build vs. Buy Decision (5-7 min)
**Format**: Quick polling + discussion

**Exercise**: Present a specific AI use case scenario (e.g., "AI-powered contract review for legal team"). Participants vote:
- Build from scratch
- Fine-tune existing model
- RAG implementation
- Buy SaaS solution
- Partner with specialist

**Discussion**: Why did you choose that approach? What factors were decisive?

---

## Module 2: Ethics, Security, and Implementation (2 Hours)

### Recommended Structure

| Section | Duration | Primary Focus |
|---------|----------|---------------|
| Opening & Transition | 5 min | From strategy to responsibility |
| Section 1: AI Ethics | 45 min | Business imperative, core challenges, governance |
| Section 2: Data Security | 35 min | Threat landscape, controls, compliance |
| Section 3: Product Implementation | 35 min | Lifecycle, patterns, UX, monitoring |

### Content Development Priorities

**Section 1: AI Ethics (45 min)**
- The business case for ethical AI (risk/reward table)
- Cost of getting it wrong (case studies: Amazon, Microsoft, Apple, Clearview, COMPAS)
- Four core ethical challenges:
  1. Bias and Fairness
  2. Transparency and Explainability
  3. Human Oversight and Control
  4. Privacy and Consent
- Governance frameworks (Three Lines of Defense, Ethics Board structure)
- Risk classification (EU AI Act aligned)

**Key Updates from 2025 Research**:
- China's comprehensive regulatory framework (Section 1 of supplement)
- PIPL integration requirements for China operations
- Board governance shift (48% now disclose AI oversight vs. 16% in 2024)
- Environmental/ESG considerations (Section 7)

**Section 2: Data Security (35 min)**
- Why GenAI security is different (new attack surfaces)
- Threat landscape (data attacks, model attacks, system attacks)
- Deep dive: Prompt injection (the critical threat)
- Data security controls (training data, models, inference)
- Compliance frameworks (SOC 2, ISO 27001/42001, NIST AI RMF)
- Incident response for AI systems

**Key Updates from 2025 Research**:
- Agentic AI governance and security (Section 3 of supplement)
- OWASP's 15 agentic threat categories
- Non-Human Identity (NHI) challenges (45 billion NHIs by end of 2025)
- AWS Agentic Security Scoping Matrix

**Section 3: Product Implementation (35 min)**
- Phase-gate model for GenAI products (6 gates)
- Kill criteria (establish before emotional investment)
- Implementation patterns (Co-pilot, Automation with exceptions, Full automation, Internal tool)
- Build vs. Buy vs. Fine-tune vs. Prompt decision framework
- API vs. Self-hosted considerations
- UX design for AI products (setting expectations, handling errors, building trust)
- Monitoring and continuous improvement

**Key Updates from 2025 Research**:
- ROI/TCO frameworks (Section 4 of supplement)
- Vendor evaluation and due diligence (Section 5)
- Industry-specific case studies (Section 9)
- Talent strategy integration (Section 8)

---

### Module 2 In-Class Activities

#### Activity 4: Ethics Dilemma Discussion (12-15 min)
**Format**: Structured debate with assigned positions

**Exercise**: Present a realistic ethical dilemma. Assign different roles to different tables:
- **Table A**: The CEO (business pressure to launch)
- **Table B**: The Chief Ethics Officer (risk concerns)
- **Table C**: The General Counsel (legal exposure)
- **Table D**: The CTO (technical limitations)

**Scenario Options**:
1. "Your company discovers subtle bias in a production AI system affecting thousands. No complaints yet. What do you do?"
2. "A competitor launches an AI feature your team deprioritized due to ethical concerns. How do you respond?"
3. "An employee used unauthorized AI tools with customer data and achieved significant productivity gains. How do you handle it?"

**Format**:
- 5 min: Groups prepare their position
- 5 min: Cross-table discussion/debate
- 3 min: Facilitator synthesis and key takeaways

---

#### Activity 5: Security Threat Mapping (10 min)
**Format**: Interactive exercise with physical/digital cards

**Exercise**: Participants receive cards describing different AI attack types:
- Data poisoning
- Prompt injection (direct)
- Prompt injection (indirect)
- Model extraction
- Adversarial examples
- Memory poisoning (agentic)
- Tool misuse (agentic)

**Task**: Map each attack to:
1. Most vulnerable AI system type (customer-facing chatbot, internal copilot, autonomous agent, etc.)
2. Most appropriate mitigation strategy
3. Detection difficulty (easy, medium, hard)

**Debrief**: Reveal the "answers" and discuss where participants' intuitions were right/wrong

---

#### Activity 6: Responsible Launch Checklist (10-12 min)
**Format**: Table groups work through a case

**Exercise**: Groups receive a scenario: "MegaCorp Financial Services wants to deploy a GenAI assistant for customer service reps that suggests responses to customer inquiries."

Using the provided checklist framework, groups must:
1. Identify the top 3 ethical risks
2. Determine the appropriate risk classification (EU AI Act tiers)
3. Specify what human oversight model is needed
4. List 3 "kill criteria" that would stop the project

**Materials**: Condensed version of the Executive AI Ethics Checklist from Module 2

---

#### Activity 7: Vendor Evaluation Simulation (12-15 min)
**Format**: Role-play negotiation

**Exercise**: Half the room plays "AI Vendor Sales Team," half plays "Enterprise Procurement/Risk Team."

**Vendor Team receives**: Marketing materials with impressive claims, some red flags buried in fine print

**Procurement Team receives**: Due diligence checklist, list of critical questions to ask

**Task**: 8-minute "sales meeting" where procurement tries to uncover:
- Training data provenance
- Security certifications
- Indemnification terms
- Data handling practices

**Debrief**: What did procurement uncover? What did vendors try to hide? What would be deal-breakers?

---

#### Activity 8: ROI Reality Check (8-10 min)
**Format**: Quick calculation exercise

**Exercise**: Present a real AI investment scenario with costs and projected benefits. Participants must:
1. Calculate the simple ROI
2. Identify 3 "hidden costs" likely missing from the projection
3. Assess whether the 18-month timeline is realistic
4. Determine what success metrics should be tracked

**Discussion**: How would you present this to your board? What questions would they ask?

---

## Cross-Module Integration Points

### Themes to Reinforce Throughout

1. **Data is foundational** - Appears in Module 1 (Data Foundation) and Module 2 (Training data security, privacy)

2. **Governance enables speed** - Module 1 (Project governance) → Module 2 (Ethics governance, compliance)

3. **Realistic expectations** - Module 1 (Project timelines, metrics) → Module 2 (ROI, kill criteria)

4. **Human oversight as default** - Module 1 (Team structure) → Module 2 (Human-in-loop, ethics)

5. **Global considerations** - Module 1 (Build vs. buy) → Module 2 (China/APAC regulations, cross-border data)

---

## Materials to Develop

### For Module 1
- [ ] Data Readiness Scorecard (1-page)
- [ ] AI Project Autopsy case studies (3 x half-page)
- [ ] Build vs. Buy polling scenarios (2-3)
- [ ] GenAI Maturity Model visual
- [ ] Data Hierarchy of Needs visual

### For Module 2
- [ ] Ethics Dilemma scenarios (3 fully developed)
- [ ] Security Threat Cards (7-10 cards with descriptions)
- [ ] Responsible Launch Checklist (condensed 1-page)
- [ ] Vendor Evaluation role-play materials (2 packet types)
- [ ] ROI calculation scenario

### Supporting Materials (Both Modules)
- [ ] Executive glossary (existing, may need updates)
- [ ] Pre-reading list (existing, confirm currency)
- [ ] Post-session resources/reading list
- [ ] One-page summary "cheat sheets" for each module

---

## Content Integration: 2025 Research Supplement

### Priority Additions by Section

| Supplement Section | Integrate Into | Priority |
|-------------------|----------------|----------|
| 1. China/APAC Regulations | Module 2, Ethics (global regulatory) | High |
| 2. IP/Copyright | Module 1, Data Foundation | High |
| 3. Agentic AI Security | Module 2, Security (new threat types) | High |
| 4. ROI/TCO Frameworks | Module 2, Implementation | High |
| 5. Vendor Evaluation | Module 2, Implementation | Medium |
| 6. Board Communications | Module 2, Governance | Medium |
| 7. Environmental/ESG | Module 2, Ethics | Medium |
| 8. Talent Strategy | Module 1, Team Structure | Low-Medium |
| 9. Industry Case Studies | Both modules (examples) | High |

### Suggested Approach

**Option A: Integrate into Main Modules**
- Weave 2025 updates directly into existing module structure
- Pros: Seamless, comprehensive
- Cons: May lengthen content, harder to update

**Option B: Create "2025 Update" Addendum Sections**
- Mark specific sections as "2025 Updates" within modules
- Pros: Easy to update, clear what's new
- Cons: May feel fragmented

**Option C: Selective Integration + Reference to Supplement**
- Integrate highest-priority updates; reference supplement for depth
- Pros: Balanced, respects time constraints
- Cons: Requires participants to do additional reading

**Recommendation**: Option C - Selective integration with reference to supplement for executives who want deeper dives.

---

## Presentation Development

### Slide Development Priorities

For the existing HDX Beamer template, prioritize:

1. **Visual frameworks** - Data Hierarchy, Maturity Model, Phase Gates
2. **Comparison tables** - Traditional vs. AI projects, Build vs. Buy
3. **Case study summaries** - Real failures and successes
4. **Decision frameworks** - Risk classification, human oversight levels
5. **Checklists** - Governance, security controls, launch readiness

### Recommended Slide Count

| Section | Estimated Slides |
|---------|-----------------|
| Module 1 Opening | 3-4 |
| Module 1 Part 1 (Data) | 12-15 |
| Module 1 Part 2 (PM) | 15-18 |
| Module 1 Part 3 (Strategy) | 8-10 |
| Module 2 Opening | 2-3 |
| Module 2 Section 1 (Ethics) | 25-30 |
| Module 2 Section 2 (Security) | 20-25 |
| Module 2 Section 3 (Implementation) | 20-25 |
| **Total** | **105-130 slides** |

---

## Next Steps

### Phase 1: Content Finalization
1. Review and approve this outline
2. Decide on 2025 supplement integration approach
3. Finalize activity selection (recommend 2 per module minimum)
4. Identify any additional case studies needed

### Phase 2: Materials Development
1. Develop activity materials (scorecards, cases, role-play packets)
2. Create slide deck following HDX Beamer template
3. Write facilitator notes for activities
4. Develop pre/post reading lists

### Phase 3: Review & Refinement
1. Internal review of all materials
2. Pilot test activities with sample audience if possible
3. Refine based on feedback
4. Final production of materials

---

*Development Outline v1.0 | December 2025*
