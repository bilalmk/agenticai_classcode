### **Read the following links**
 - Anthropic Design Patterns [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
 - Exceptions [https://openai.github.io/openai-agents-python/running_agents/](https://openai.github.io/openai-agents-python/running_agents/)
 - Handoffs [https://openai.github.io/openai-agents-python/handoffs/](https://openai.github.io/openai-agents-python/handoffs/)
 - Guardrails [https://openai.github.io/openai-agents-python/guardrails/](https://openai.github.io/openai-agents-python/guardrails/)
 - Guardrails reference [https://openai.github.io/openai-agents-python/ref/guardrail/](https://openai.github.io/openai-agents-python/ref/guardrail/)
 - Life Cycle [https://openai.github.io/openai-agents-python/ref/lifecycle/](https://openai.github.io/openai-agents-python/ref/lifecycle/)
 - Agents Reference [https://openai.github.io/openai-agents-python/ref/agent/](https://openai.github.io/openai-agents-python/ref/agent/)
 - Model Settings [https://openai.github.io/openai-agents-python/ref/model_settings/#agents.model_settings.ModelSettings](https://openai.github.io/openai-agents-python/ref/model_settings/#agents.model_settings.ModelSettings)

---

### **Please review all the examples below**
 - Examples [https://openai.github.io/openai-agents-python/examples/](https://openai.github.io/openai-agents-python/examples/)
 - Agent Patterns [https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns](https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns)
 - Basic Examples [https://github.com/openai/openai-agents-python/tree/main/examples/basic](https://github.com/openai/openai-agents-python/tree/main/examples/basic)
 - Tools [https://github.com/openai/openai-agents-python/tree/main/examples/tools](https://github.com/openai/openai-agents-python/tree/main/examples/tools)
 - Handoffs [https://github.com/openai/openai-agents-python/tree/main/examples/handoffs](https://github.com/openai/openai-agents-python/tree/main/examples/handoffs)

---

### **Watch the following video playlist**
 - OpenAI Agents SDK - Open Source [https://www.youtube.com/watch?v=83l01nAHG6E&list=PL0vKVrkG4hWovpr0FX6Gs-06hfsPDEUe6](https://www.youtube.com/watch?v=83l01nAHG6E&list=PL0vKVrkG4hWovpr0FX6Gs-06hfsPDEUe6)
 - Quiz Preparation - OpenAI Agents SDK [https://www.youtube.com/watch?v=bDPiXVRjqF8&list=PL0vKVrkG4hWr4V2I4P6GaDzMG_LijlGTm](https://www.youtube.com/watch?v=bDPiXVRjqF8&list=PL0vKVrkG4hWr4V2I4P6GaDzMG_LijlGTm)
 - OpenAI Agents SDK - Crash Course [https://www.youtube.com/watch?v=iziGVjl8Fs4&list=PL0vKVrkG4hWpQJfc8as3tD4CClyIsZcag&pp=0gcJCWUEOCosWNin](https://www.youtube.com/watch?v=iziGVjl8Fs4&list=PL0vKVrkG4hWpQJfc8as3tD4CClyIsZcag&pp=0gcJCWUEOCosWNin)


---

# **Assignment**: Implement Input & Output Guardrail Functionality

## **Objective**

Enhance the existing **handoff example** using **OpenAI’s Agent SDK** by adding **input** and **output guardrails** at both the **agent level** and **run level**.
This assignment will help you understand how to **restrict queries**, **filter responses**, and **enforce compliance rules** while working with multiple agents.

---

## **Scenario**

You are working on a **multi-agent setup** where three agents are available:

* **Weather Agent** – provides weather information
* **Flight Agent** – provides flight schedules and fares
* **Hotel Agent** – provides hotel availability and bookings

We need to apply **guardrails** to control **what users can ask** and **what responses agents can give**.

---

## **Requirements**

### **1. Input Guardrails** *(Before agent processes a query)*

Users **must not** be able to ask **India-related queries**.

* **Weather Agent** → Must reject queries about **Indian cities**.
* **Flight Agent** → Must reject queries about **Indian cities**.
* **Hotel Agent** → Must reject queries about **Indian cities**.

> **Example:**

* ❌ User: “What’s the weather in Delhi?” → **Should be blocked**
* ✅ User: “What’s the weather in Dubai?” → **Allowed**

---

### **2. Output Guardrails** *(After agent generates a response)*

The final output of agent should be blocked if having **Cities** from **USA**:

* **Weather Agent** → Must **not** respond with **any U.S. city weather**.
* **Flight Agent** → Must **not** return any flight result containing **U.S. cities**.
* **Hotel Agent** → Must **not** show hotel availability for **U.S. cities**.

> **Example:**

* ❌ User: “Show me weather for New York.” → **Blocked Output**
* ✅ User: “Show me weather for Dubai.” → **Allowed Output**

---

### **3. Guardrail Levels**

You must implement **both agent-level** and **run-level** guardrails:

#### **a) Agent-Level Guardrails**

* Applied **before the first agent executes**.
* If invalid **inputs** then terminate the execution of loop.

#### **b) Run-Level Guardrails**

* Applied at the **workflow level**, controlling inputs **before any agent runs** and outputs **after all agents complete**.
* Ensures the **final response** is clean, compliant, and follows business rules.

---

### **4. Expected Behavior**

* **Input Guardrails** → Should be triggered **only once** for the **first agent**.
* **Output Guardrails** → Should be applied at the **final response stage** after all agents complete their tasks.

---

## **Instructions**

### **Step 1 — Extend Existing Handoff Code**

* Start with your **handoff example code** from OpenAI’s Agent SDK.
* Extend **hotel agent** and add tool for hotel booking.
* Add **input guardrails** for all three agents.
* Add **output guardrails** for all three agents.

---

### **Step 2 — Implement Agent-Level Guardrails**

* Use **filters** or **custom validation logic** in each agent.
* Block responses **before the first agent executes**.

---

### **Step 3 — Implement Run-Level Guardrails**

* Apply input and output guardrail in RunConfig.
* Input guardrail should executed before first agent and terminate the execution if break the guardrail rules.
* Output guardrail should executed after final result generated and terminate the execution if output is not align with **compliance rules**

---

### **Step 4 — Testing Checklist**

Perform tests for the following scenarios:

| **Test Case**                     | **Input**                      | **Expected Result**            |
| --------------------------------- | ------------------------------ | -----------------------------  |
| Weather agent - India input block | “Weather in Mumbai”            | ❌ Reject query                |
| Flight agent - India input block  | “Flights from Delhi to Dubai”  | ❌ Reject query                |
| Hotel agent - India input block   | “Hotels in Bangalore”          | ❌ Reject query                |
| Weather agent - US output filter  | “Weather in London”            | ✅ result returned             |
| Weather agent - US output filter  | “Weather in New York”          | ❌ No output for U.S. city     |
| Flight agent - US flight removal  | “Flights from Dubai to KHI”    | ✅ result returned             |
| Hotel agent - US hotels filter    | “Hotels in Los Angeles”        | ❌ No output for U.S. hotel    |

