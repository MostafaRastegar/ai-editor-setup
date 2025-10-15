# Cline Smart Model Selection Rules

## 🎯 Model Selection Strategy

You are an AI coding assistant with access to multiple specialized models. Before responding to any request, you MUST analyze the task type and select the most appropriate model based on the criteria below.

---

## 📋 Available Free Models (Context >= 120K)

### Primary Models

1. **z-ai/glm-4.5-air:free**
   - Context: 131K tokens
   - Strengths: Balanced performance, high usage (1.18B tokens), optional reasoning
   - Best for: General coding, fullstack development, balanced tasks
   - Architecture: MoE (Mixture of Experts)
   - Tool calling: 142K successful calls

2. **deepseek/deepseek-chat-v3.1:free**
   - Context: 163K tokens
   - Strengths: Hybrid reasoning, most popular (3.44B tokens)
   - Best for: Complex logic, debugging, architecture discussions
   - Reasoning: Optional (can toggle on/off)

3. **tngtech/deepseek-r1t2-chimera:free**
   - Context: 163K tokens
   - Strengths: Strong reasoning (4.28B tokens usage), assembly of experts
   - Best for: Complex problem-solving, algorithm design, deep analysis
   - Reasoning: Always on (thinking mode)

4. **qwen/qwen3-coder-480b-a35b-07-25:free**
   - Context: 262K tokens (largest!)
   - Strengths: Code-specialized, huge context window
   - Best for: Large codebases, refactoring, code review
   - Note: No reasoning mode, pure coding

### Backup Models

5. **deepseek/deepseek-r1-0528:free**
   - Context: 163K tokens
   - Reasoning: Strong (900M tokens)
   - Use case: When primary reasoning models are unavailable

6. **tngtech/deepseek-r1t-chimera:free**
   - Context: 163K tokens
   - Reasoning: R1+V3 merge (596M tokens)
   - Use case: Alternative reasoning model

---

## 🔍 Task Detection & Model Selection Logic

### Rule 1: Code Writing & Implementation
**Keywords:** "write", "create", "implement", "build", "develop", "code"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Best balance between speed and quality for general coding tasks

**Example prompts:**
- "Create a React component for user authentication"
- "Implement a REST API endpoint in Python"
- "Build a TypeScript utility function"

---

### Rule 2: Debugging & Bug Fixes
**Keywords:** "debug", "fix", "error", "bug", "issue", "problem", "not working"
**Complexity:** Medium-High
**Selected Model:** `deepseek/deepseek-chat-v3.1:free`
**Reason:** Hybrid reasoning helps trace issues, large context for error logs

**Example prompts:**
- "Fix this error: TypeError..."
- "Debug why the API call is failing"
- "This function returns undefined, help me fix it"

---

### Rule 3: Architecture & Design
**Keywords:** "design", "architecture", "pattern", "structure", "organize", "best practice"
**Complexity:** High
**Selected Model:** `tngtech/deepseek-r1t2-chimera:free`
**Reason:** Strong reasoning for system design and architectural decisions

**Example prompts:**
- "Design a microservices architecture for..."
- "What's the best pattern for state management?"
- "How should I structure this Next.js project?"

---

### Rule 4: Algorithm & Complex Logic
**Keywords:** "algorithm", "optimize", "performance", "complexity", "efficient", "solve"
**Complexity:** High
**Selected Model:** `tngtech/deepseek-r1t2-chimera:free`
**Reason:** Deep reasoning for algorithmic challenges

**Example prompts:**
- "Optimize this sorting algorithm"
- "Find the most efficient way to..."
- "Solve this dynamic programming problem"

---

### Rule 5: Code Review & Refactoring
**Keywords:** "review", "refactor", "improve", "clean", "optimize code", "rewrite"
**Complexity:** Medium-High
**Selected Model:** `qwen/qwen3-coder-480b-a35b-07-25:free`
**Reason:** Largest context (262K) for handling large codebases

**Example prompts:**
- "Review this code and suggest improvements"
- "Refactor this legacy component"
- "How can I make this more maintainable?"

---

### Rule 6: Large Codebase Analysis
**Keywords:** "analyze", "understand", "explain", "codebase", "multiple files"
**Context needed:** > 160K tokens
**Selected Model:** `qwen/qwen3-coder-480b-a35b-07-25:free`
**Reason:** Largest context window (262K)

**Example prompts:**
- "Analyze this entire module structure"
- "Explain how these 10 files interact"
- "Review this large PR with multiple changes"

---

### Rule 7: Testing & Documentation
**Keywords:** "test", "unit test", "e2e", "documentation", "comment", "readme"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Fast, efficient, good for systematic tasks

**Example prompts:**
- "Write unit tests for this function"
- "Generate documentation for this API"
- "Create a README for this project"

---

### Rule 8: TypeScript/JavaScript Specific
**Keywords:** "typescript", "ts", "react", "nextjs", "node", "javascript"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Excellent fullstack support, high usage indicates strong performance

**Example prompts:**
- "Convert this JavaScript to TypeScript"
- "Create a Next.js API route"
- "Build a React custom hook"

---

### Rule 9: Python Specific
**Keywords:** "python", "django", "fastapi", "flask", "pandas", "numpy"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Strong general-purpose coding with Python support

**Example prompts:**
- "Create a FastAPI endpoint"
- "Write a Python script for data processing"
- "Build a Django model with relationships"

---

### Rule 10: Quick Questions & Explanations
**Keywords:** "what", "how", "why", "explain", "difference", "?", "quick question"
**Complexity:** Low
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Fast, efficient, no reasoning overhead needed

**Example prompts:**
- "What's the difference between let and const?"
- "How does async/await work?"
- "Explain this error message"

---

## 🎲 Fallback Strategy

If primary model is unavailable or fails:

```
1st: z-ai/glm-4.5-air:free (default fallback)
2nd: deepseek/deepseek-chat-v3.1:free (reasoning needed)
3rd: tngtech/deepseek-r1t2-chimera:free (complex tasks)
4th: qwen/qwen3-coder-480b-a35b-07-25:free (large context)
```

---

## 🚫 Models to AVOID for Programming

- `google/gemini-2.0-flash-exp:free` - Vision-focused
- `meta-llama/llama-3.2-3b-instruct:free` - Too small (3B)
- Models with context < 120K - Insufficient for modern development

---

## 📊 Decision Tree Summary

```
START
  ↓
Is context > 200K needed?
  ├─ YES → qwen/qwen3-coder-480b-a35b-07-25:free
  └─ NO → Continue
       ↓
Is deep reasoning required? (architecture/algorithms)
  ├─ YES → tngtech/deepseek-r1t2-chimera:free
  └─ NO → Continue
       ↓
Is it debugging/complex logic?
  ├─ YES → deepseek/deepseek-chat-v3.1:free
  └─ NO → z-ai/glm-4.5-air:free (default)
```

---

## 🔧 Usage in Cline

When you receive a prompt:

1. **Analyze** the task type using keywords above
2. **Select** the appropriate model based on rules
3. **Inform** the user: "Using [model-name] for [reason]"
4. **Execute** the task with selected model
5. **Fallback** if model fails

---

## 📝 Example Responses

**User:** "Create a React authentication component"
**Assistant:** "Using `z-ai/glm-4.5-air:free` - optimal for general React development with balanced performance."

**User:** "Design a scalable microservices architecture"
**Assistant:** "Using `tngtech/deepseek-r1t2-chimera:free` - strong reasoning capabilities for architectural decisions."

**User:** "Debug this 500-line legacy code"
**Assistant:** "Using `qwen/qwen3-coder-480b-a35b-07-25:free` - large context window (262K) handles extensive code review."

---

## ⚠️ Important Notes

1. **Always prefer quality over speed** - You specified quality is more important
2. **Context is king** - Use models with larger context for complex tasks
3. **Reasoning is optional** - Only use reasoning models when truly needed
4. **Monitor performance** - If a model consistently fails, escalate to next tier
5. **Stay updated** - This ruleset is based on current usage data; update when new models arrive

---

## 🎯 Your Priority Matrix

```
Priority 1: Code Quality
Priority 2: Speed/Performance
Priority 3: Context Length
Priority 4: Reasoning (optional)
```

**Final Default:** When in doubt, use `z-ai/glm-4.5-air:free` - it has the best balance and highest proven usage for general tasks.

---

*Last Updated: Based on usage data through 2025-10-11*
*Total Models Analyzed: 200+ | Free Models Selected: 6 | Context Range: 131K-262K*