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


# Assignment : **Implement output guardrail functionality**

## Objective
Extend the guardrails.py example to add output guardrails using OpenAI’s Agent SDK.

 - Current code blocks non-math queries (input guardrails).

 - Add rules so agent responses avoid political topics and references to political figures.

code available at : `guardrails.py`


# Assignment : **Convert static instructions into dynamic instruction**

## objective
Convert static instructions into dynamic ones using OpenAI’s Agent SDK.

 - Base your work on the bilal_fareed_code example for hotel booking and information retrieval.

 - Update it so a single agent can store and retrieve details for multiple hotels.

- Use context to return the correct hotel information based on the user’s query.

code available at : `bilal_fareed_code/my_agent/hotel_assistant.py`

# Assignment : **Build a Smart Customer Support Bot using OpenAI Agent SDK**

## Objective
Create a customer support bot using OpenAI's Agent SDK that can handle basic FAQs, fetch order statuses, and escalate to a human agent when necessary. The bot should also implement guardrails to ensure positive interactions and showcase advanced features of the SDK.

## Requirements
You will build a bot that can assist customers with common queries and order tracking. The bot should be able to handle simple requests autonomously, use function tools to fetch data, and escalate to a human agent for complex queries or negative sentiment.

* **Answer basic product FAQs**
* **Fetch order status using a simulated API (function tool)**
* **Escalate to a human agent if the query is complex or sentiment is negative (handoff)**
* **Enforce a simple guardrail: block or rephrase negative/offensive user input**
* **Showcase usage of model\_settings (tool\_choice, metadata, etc.)**
* **Showcase advanced use of @function\_tool decorator, including is\_enabled and error\_function**

---

### **Breakdown of Required Elements**

#### 1. **Create Two Agents**

* **BotAgent**: Handles FAQs, order lookup (function tools).
* **HumanAgent**: For escalation (handoff).

#### 2. **Implement Function Tools**

* `@function_tool`: `get_order_status(order_id)`: Simulates fetching order status.

  * Use `is_enabled` to toggle the tool (e.g., only enabled for "order" queries).
  * Use `error_function` to return a friendly error if order\_id not found.

#### 3. **Guardrails**

* Use `@guardrail` to check for offensive or negative language. If detected, return a warning or rephrase the response.

#### 4. **Agent Handoff**

* If the bot detects a query it can’t handle or sentiment is negative, **handoff** to the HumanAgent.

#### 5. **ModelSettings Usage**

* Set `tool_choice="auto"` or `"required"` and pass custom `metadata` (e.g., store customer ID).
* Experiment with the effect of tool\_choice and metadata in responses.

#### 6. **Bonus: Logging**

* Log all tool invocations and handoffs for traceability.

---

### **What To Submit**

* Your full source code (with improvements or customizations)
* **Comments** on where you used: tool call, handoff, guardrail, ModelSettings options, function\_tool decorators.
* Screenshots or logs showing all scenarios working.

---

**Happy coding!** 🚀
