# Flow Explanation — Signal Mirror Tree

## 1. System Overview

The Signal Mirror Tree is implemented as a **deterministic state machine** that transforms user selections into structured behavioral signals.

At its core, the system performs three operations repeatedly:

1. **Capture** → constrained categorical input
2. **Transform** → map input to signals
3. **Transition** → route to the next node deterministically

This loop continues until a terminal summary state is reached.

---

## 2. Execution Model

The system operates as a **directed acyclic graph (DAG)** of nodes, where:

* Nodes = interaction or logic units
* Edges = predefined transitions
* Paths = complete reflection journeys

There are **no cycles, no randomness, and no dynamic branching**.

---

## 3. Interaction Pipeline

Each user interaction follows a strict pipeline:

### Stage 1: Input Capture

* User selects from a **closed set of options**
* Eliminates ambiguity and input variance

### Stage 2: Signal Encoding

* Each option maps to one or more **categorical signals**
* Example:

  ```text
  "Adapted fast" → control:internal, reaction:active
  ```

### Stage 3: State Update

* Signals are incrementally accumulated:

  ```text
  state.control.internal += 1
  ```

### Stage 4: Deterministic Routing

* Decision nodes evaluate:

  * last answer
  * or grouped answer categories
* Transition is resolved using **explicit rule matching**

---

## 4. Axis-Wise Flow Decomposition

### 4.1 Control Signal (Axis 1)

**Purpose:** Establish perceived agency

**Mechanism:**

* Initial classification of day context
* Branching based on perceived control vs constraint
* Secondary questions refine:

  * reaction type (active/passive)
  * energy direction (proactive/withdrawn)

**Output:**

* Reflection on how the user **engaged with events**, not just experienced them

---

### 4.2 Value Signal (Axis 2)

**Purpose:** Evaluate contribution behavior

**Mechanism:**

* Identify whether attention is on:

  * contribution (giving)
  * entitlement (expecting)
* Follow-up questions isolate:

  * motivation drivers
  * expectation gaps

**Output:**

* Reflection on **value creation vs value expectation**

---

### 4.3 Impact Signal (Axis 3)

**Purpose:** Measure scope of awareness

**Mechanism:**

* Classify focus into:

  * self-centric
  * other-oriented
* Expand through:

  * team awareness
  * empathy indicators
  * outcome orientation

**Output:**

* Reflection on **breadth of perspective**

---

## 5. State Architecture

The system maintains two synchronized layers of state:

### 5.1 Interaction State

Stores raw responses:

```text
node_id → selected_option
```

### 5.2 Signal State

Stores aggregated signals:

```text
control.internal = n
value.contribution = n
impact.other = n
```

This separation ensures:

* traceability (what user said)
* interpretability (what it means structurally)

---

## 6. Decision Engine

Decision nodes act as **rule evaluators**, not predictors.

### Routing Example:

```text
IF answer ∈ {Sharp, Uneven} → S1_HIGH
ELSE IF answer ∈ {Heavy, Blocked} → S1_LOW
```

Properties:

* deterministic
* exhaustive (no undefined paths)
* mutually exclusive conditions

---

## 7. Summary Computation

At termination, the system computes **dominant signals per axis**.

### Method:

* simple frequency comparison
* no weights, no thresholds, no probabilistic scoring

### Output:

```text
Control → internal
Value → contribution
Impact → other
```

### Key Insight:

The summary is not predictive—it is a **direct projection of accumulated signals**.

---

## 8. Determinism Guarantee

The system guarantees strict determinism through:

* finite and predefined input space
* explicit transition rules
* static output templates
* absence of runtime variability

### Formal Property:

> For any input sequence S, output O is invariant.

---

## 9. Constraint Handling

The system eliminates common failure modes:

| Risk                | Mitigation                   |
| ------------------- | ---------------------------- |
| Ambiguous input     | Closed option sets           |
| Missing data        | Mandatory selection per node |
| Hallucination       | No generative components     |
| Inconsistent output | Static templates             |
| Undefined states    | Fully enumerated transitions |

---

## 10. Cognitive Flow Design

The flow mirrors a natural reflective sequence:

1. **Experience Layer** → “What happened to me?”
2. **Action Layer** → “What did I do?”
3. **Perspective Layer** → “Who else was involved?”

This progression:

* reduces cognitive friction
* increases response clarity
* improves signal reliability

---

## 11. Analytical Interpretation

From a data perspective, the system:

* converts subjective experience into **structured categorical variables**
* enables **pattern recognition via signal aggregation**
* ensures **full auditability of every output**
* avoids bias introduced by probabilistic inference

---

## 12. System Boundaries

The system intentionally does NOT:

* infer intent
* interpret emotional nuance
* generate new insights dynamically
* adapt based on historical data

This constraint preserves:

* consistency
* explainability
* control

---

## 13. Conclusion

The Signal Mirror Tree functions as a **deterministic behavioral processing pipeline**.

It does not evaluate or predict.

Instead, it:

* captures structured inputs
* maps them to signals
* processes them through fixed logic
* reflects them back transparently

This ensures a system that is:

* reliable
* interpretable
* analytically grounded
