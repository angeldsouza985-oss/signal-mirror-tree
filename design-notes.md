# Design Notes — Signal Mirror Tree

## 1. Problem Framing

The objective was to design a **deterministic decision system** that enables structured self-reflection while eliminating ambiguity, inconsistency, and AI hallucination.

Traditional AI-driven reflection systems introduce:

* probabilistic outputs
* lack of traceability
* inconsistent interpretations

This solution replaces those with a **fully deterministic, rule-based architecture** that ensures:

* repeatability
* interpretability
* controlled outcomes

---

## 2. Conceptual Model

The system is built as a **“Signal Mirror”**, where user responses are translated into measurable behavioral signals across three dimensions:

| Dimension          | Description                 | Behavioral Question            |
| ------------------ | --------------------------- | ------------------------------ |
| **Control Signal** | Degree of perceived agency  | “Did I influence outcomes?”    |
| **Value Signal**   | Contribution vs expectation | “Did I give or expect?”        |
| **Impact Signal**  | Breadth of perspective      | “Was my focus self or others?” |

This abstraction converts qualitative reflection into **structured, analyzable data signals**.

---

## 3. System Architecture

The solution follows a **tree-based deterministic architecture** composed of discrete node types:

* **Start Node** → Initializes session
* **Question Nodes** → Capture structured input (fixed options only)
* **Decision Nodes** → Route flow using explicit conditions
* **Reflection Nodes** → Deliver pre-defined insights
* **Bridge Nodes** → Maintain logical continuity between axes
* **Summary Node** → Aggregate and present dominant signals

### Key Property:

Every node transition is **predefined and non-probabilistic**, ensuring complete control over system behavior.

---

## 4. Data Modeling Approach

User interaction is captured as **categorical signals**, not free text.

### Primary Signals:

* `control: internal | external`
* `value: contribution | entitlement`
* `impact: self | other`

### Secondary (Micro) Signals:

* `reaction: active | passive`
* `energy: proactive | withdrawn`

These signals are:

* **incrementally accumulated**
* **non-weighted (simple tally system)**
* used for **dominance detection** in summary

---

## 5. Deterministic Logic Design

The system enforces determinism through:

* Fixed input space (closed set of options)
* Explicit routing rules in decision nodes
* No conditional ambiguity
* No dynamic content generation

### Example Logic:

* Input selection → mapped to signal
* Signal → contributes to axis state
* Axis state → determines summary output

This design ensures:

> Same input sequence → identical output every time

---

## 6. Anti-Hallucination Strategy

A key constraint was eliminating AI hallucination. This was addressed through system design, not post-processing.

### Guardrails Implemented:

* No free-text inputs (removes ambiguity)
* No inference layer (no interpretation of intent)
* No generative outputs (all responses predefined)
* No missing-data assumptions
* No probabilistic branching

### Result:

The system is **fully explainable and auditable**, with zero reliance on AI-generated reasoning.

---

## 7. Interaction Design & Language

The system adopts a **neutral, reflective tone** to avoid bias or judgment.

### Design Choices:

* Questions framed as observations, not evaluations
* Avoidance of leading or emotionally charged language
* Consistent phrasing across nodes

### Example:

* Instead of: “Did you perform well?”
* Used: “What drove things forward?”

This improves:

* user comfort
* response honesty
* data reliability

---

## 8. Reflection Generation Strategy

Reflections are:

* pre-authored templates
* mapped to specific signal paths
* designed to highlight patterns, not assign labels

They do not:

* score users
* classify behavior as good/bad
* generate new interpretations

This ensures consistency and prevents narrative drift.

---

## 9. Flow Design Logic

The system enforces a strict progression:

1. **Control Signal (Axis 1)**
   → Establishes perceived agency

2. **Value Signal (Axis 2)**
   → Evaluates contribution behavior

3. **Impact Signal (Axis 3)**
   → Expands perspective beyond self

This sequential structure:

* reduces cognitive load
* builds reflection depth progressively
* ensures logical continuity

---

## 10. Trade-off Analysis

| Strength              | Limitation                        |
| --------------------- | --------------------------------- |
| Fully deterministic   | Limited flexibility               |
| Zero hallucination    | Cannot process unstructured input |
| High interpretability | Requires manual design effort     |
| Consistent outputs    | No adaptive learning              |

---

## 11. Scalability Considerations

The current system is modular and can be extended by:

* adding more nodes per axis
* introducing weighted signals
* integrating external dashboards for analytics
* exporting interaction logs for pattern analysis

Despite scalability potential, determinism is preserved as a core constraint.

---

## 12. Alignment with Data Analytics Principles

This system aligns with core data analytics practices:

* **Structured Data Collection** → categorical inputs
* **Feature Engineering** → signal creation
* **Rule-Based Modeling** → deterministic logic
* **Explainability** → full traceability of outputs
* **Reproducibility** → identical outcomes for identical inputs

---

## 13. Design Rationale

The system intentionally avoids AI-driven approaches because:

* interpretability is prioritized over flexibility
* consistency is prioritized over personalization
* control is prioritized over generation

---

## 14. Conclusion

The Signal Mirror Tree transforms subjective reflection into a **structured, rule-based analytical process**.

It does not attempt to predict or evaluate.

Instead, it:

* captures behavior as signals
* organizes them deterministically
* reflects them back with clarity

This approach ensures reliability, transparency, and analytical rigor.
