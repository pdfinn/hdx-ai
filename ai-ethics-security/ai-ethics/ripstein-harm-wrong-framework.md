# Ripstein's Harm/Wrong Distinction: A Framework for AI Safety vs. Ethics

## Overview

Arthur Ripstein's *Private Wrongs* (Harvard University Press, 2016) provides a Kantian framework for understanding tort law that offers valuable conceptual tools for distinguishing AI safety from AI ethics. This document explores how Ripstein's distinction between "harm" and "wrong" can sharpen executive understanding of AI governance.

## Ripstein's Core Distinction

### Harm vs. Wrong

Ripstein argues that **not all harms are wrongs, and not all wrongs involve harm**:

- **Harm**: Factual damage or injury to a person's interests (economic loss, physical injury, etc.)
- **Wrong**: Violation of someone's right to be "in charge of" their own person, property, and purposes

**Key insight**: What makes conduct tortious is not that it causes harm, but that it *wrongs* someone by violating their rights. The harm may trigger the need for compensation, but the wrong is what creates the legal and moral obligation.

### Two Categories of Wrong

Ripstein identifies two types of wrongful interference:

1. **Use-based wrongs**: Direct misuse of another's body or property (e.g., battery, trespass). These are wrongs *even if no damage occurs*. A harmless trespass is still a wrong.

2. **Damage-based wrongs**: Harming another's means through negligent conduct (e.g., car accidents). Here, both wrongful conduct *and* damage are required.

### The "In Charge Of" Principle

The foundation of Ripstein's framework is the Kantian principle that rational agents are entitled to be "in charge of" the means they use to pursue their purposes—their bodies, their property, their reputation. Wrongs occur when someone interferes with this entitlement, regardless of whether harm results.

## Application to AI: Safety vs. Ethics

### Mapping the Distinction

| Ripstein's Framework | AI Safety | AI Ethics |
|---------------------|-----------|-----------|
| **Focus** | Preventing harm | Preventing wrong |
| **Question** | Does the system malfunction and cause damage? | Does the system violate rights, even when working as designed? |
| **Nature** | Engineering/technical problem | Governance/values problem |
| **Remedy** | Fix the system | Constrain or redesign the system's *purpose* |

### Concrete Examples

#### Example 1: Self-Driving Vehicle Crash (Safety Issue)

A sensor malfunction causes an autonomous vehicle to collide with a pedestrian.

- **Harm**: Physical injury, economic damages
- **Wrong?**: If due to negligent design/testing, yes (damage-based wrong). If genuinely unforeseeable, potentially no wrong—just tragic harm.
- **Category**: Primarily a **safety** issue. Better engineering, testing, and fail-safes are the remedy.

#### Example 2: Discriminatory Hiring Algorithm (Ethics Issue)

An AI hiring system systematically rates candidates from certain demographic groups lower, even when equally qualified. The system is working exactly as trained.

- **Harm**: Lost job opportunities, economic damage to affected individuals
- **Wrong**: Yes—the system *uses* protected characteristics to make decisions about people's life prospects, violating their right to be evaluated as individuals
- **Category**: Primarily an **ethics** issue. The system isn't malfunctioning; it's *wronging* people by design.

**Critical point**: This case involves *both* harm and wrong, but what makes it ethically objectionable is the wrong, not the harm. A candidate might not get a job for many legitimate reasons (harm without wrong). What makes algorithmic discrimination different is that it wrongs people by treating their characteristics as something to be used against them.

#### Example 3: Data Collection Without Consent (Ethics Issue)

A company collects behavioral data from users without meaningful disclosure, then uses it to build predictive models.

- **Harm**: Potentially none—the user may never experience tangible damage
- **Wrong**: Yes—a "use-based" wrong. The company is using the person's digital footprint (an extension of their means) without authorization
- **Category**: **Ethics** issue. The absence of harm doesn't eliminate the wrong.

#### Example 4: AI Hallucination Causing Bad Decision (Safety Issue)

A large language model generates a confident but false statement about medication interactions. A user relies on it and suffers adverse effects.

- **Harm**: Physical injury, potential medical costs
- **Wrong**: Depends on how the system was presented. If marketed as reliable medical advice, potentially a damage-based wrong through negligent deployment.
- **Category**: Primarily **safety**—the system failed to perform reliably.

### The Matrix: Harm, Wrong, and AI Governance

|  | **No Wrong** | **Wrong Present** |
|--|--------------|-------------------|
| **No Harm** | Acceptable operation | Ethics violation (e.g., unauthorized data use with no tangible impact) |
| **Harm Present** | Unfortunate but not tortious (e.g., competitor's better AI takes market share) | Full liability—both safety and ethics failure (e.g., discriminatory algorithm causing denied opportunities) |

## Business Implications

### Why This Distinction Matters for Executives

1. **Different remediation paths**: Safety failures call for engineering solutions (better testing, monitoring, fail-safes). Ethics failures require governance interventions (redesigning purposes, constraining applications, human oversight).

2. **Different risk profiles**: Safety failures are often insurable and fixable. Ethics failures raise existential questions about whether the product *should exist* in its current form.

3. **Regulatory implications**: The EU AI Act and similar frameworks distinguish between technical requirements (safety) and fundamental rights protections (ethics). Understanding the distinction helps with compliance strategy.

4. **Reputational asymmetry**: Safety failures ("the system broke") generate different public response than ethics failures ("the system was designed to do this"). Ethics failures suggest organizational values problems.

### Questions for AI Governance

Ripstein's framework suggests key questions for AI projects:

1. **Safety questions**: Could this system malfunction in ways that cause harm? What are our testing and monitoring protocols?

2. **Ethics questions**: Even if this system works perfectly as designed, does it *wrong* anyone? Does it:
   - Use people's data/identity without proper authorization?
   - Make decisions that violate individual autonomy or dignity?
   - Treat people as means rather than ends?

## Limitations of the Framework

### 1. Individual vs. Systemic Wrongs

Ripstein's framework addresses bilateral relationships (wrongdoer → victim). AI systems often create diffuse, statistical harms that don't map neatly to identifiable victims:
- Amplification of societal bias
- Erosion of democratic discourse
- Environmental costs of training

These may require supplementary frameworks focused on collective or systemic wrongs.

### 2. Attribution Complexity

Ripstein assumes an identifiable wrongdoer. AI development involves distributed responsibility:
- Data providers
- Model developers
- Fine-tuners
- Deployers
- End users

The framework helps identify *what* the wrong is but doesn't resolve *who* bears responsibility.

### 3. Abstraction Level

For executive audiences, the philosophical precision requires translation into concrete business scenarios. The framework is a starting point for analysis, not a complete decision procedure.

## Conclusion

Ripstein's distinction between harm and wrong provides a valuable conceptual tool for AI governance:

- **AI Safety** focuses on preventing systems from *harming* through malfunction
- **AI Ethics** focuses on preventing systems from *wronging* through their intended operation

The hiring algorithm example illustrates why this matters: a system can work perfectly while still being fundamentally objectionable. Safety asks "does it work?" Ethics asks "should it exist?"

For executives, the practical takeaway is that safety and ethics require different governance mechanisms, different expertise, and different remediation strategies. Conflating them leads to inadequate responses to both.

## References

- Ripstein, Arthur. *Private Wrongs*. Harvard University Press, 2016.
- Notre Dame Philosophical Reviews. "Private Wrongs." https://ndpr.nd.edu/reviews/private-wrongs/
- Stanford Encyclopedia of Philosophy. "Ethics of Artificial Intelligence and Robotics." https://plato.stanford.edu/entries/ethics-ai/
- Leslie, David. "Understanding Artificial Intelligence Ethics and Safety." The Alan Turing Institute, 2019. https://www.turing.ac.uk/sites/default/files/2019-06/understanding_artificial_intelligence_ethics_and_safety.pdf

## Suggested Further Reading

- Weinrib, Ernest. *The Idea of Private Law*. Oxford University Press, 2012.
- Floridi, Luciano, and Josh Cowls. "A Unified Framework of Five Principles for AI in Society." *Harvard Data Science Review*, 2019.
- Mittelstadt, Brent. "Principles Alone Cannot Guarantee Ethical AI." *Nature Machine Intelligence*, 2019.

---

*Document prepared for HDX Executive Education: Introduction to GenAI*
*Part of the AI Ethics research collection*
