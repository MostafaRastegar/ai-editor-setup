# Cline Smart Model Selection Rules

## 🎯 Model Selection Strategy

You are an AI coding assistant with access to multiple FREE models optimized for fullstack development (Python, TypeScript, React, Next.js).

CRITICAL: Before responding to ANY request, you MUST:
1. Analyze the task type using keywords (both English and Persian)
2. Select the most appropriate model from the list below
3. Announce your selection: "🤖 Using [model] for [reason]"
4. **STOP** and ask the user for confirmation.
5. If the user confirms ('y'), proceed with the task. Otherwise, ask for clarification or choose a different approach.
6. **DO NOT proceed with the task until the user confirms.**

DO NOT skip model selection. DO NOT use default model without analysis.
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
**English Keywords:** "write", "create", "implement", "build", "develop", "code"
**Persian Keywords:** "نوشتن", "ایجاد", "پیاده‌سازی", "ساخت", "توسعه", "کدنویسی", "برنامه‌نویسی"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Best balance between speed and quality for general coding tasks

**Example prompts:**
- "Create a React component for user authentication"
- "یک کامپوننت ری‌اکت برای احراز هویت کاربر بساز"
- "Implement a REST API endpoint in Python"
- "یک endpoint API REST در پایتون پیاده‌سازی کن"
- "Build a TypeScript utility function"
- "یک تابع کمکی TypeScript بساز"

---

### Rule 2: Debugging & Bug Fixes
**English Keywords:** "debug", "fix", "error", "bug", "issue", "problem", "not working"
**Persian Keywords:** "دیباگ", "رفع خطا", "اشکال‌زدایی", "خطا", "باگ", "مشکل", "ایssue", "problem", "کار نمی‌کند"
**Complexity:** Medium-High
**Selected Model:** `deepseek/deepseek-chat-v3.1:free`
**Reason:** Hybrid reasoning helps trace issues, large context for error logs

**Example prompts:**
- "Fix this error: TypeError..."
- "این خطا را رفع کن: TypeError..."
- "Debug why the API call is failing"
- "دیباگ کن ببین چرا فراخوانی API شکست می‌خورد"
- "This function returns undefined, help me fix it"
- "این تابع undefined برمی‌گردونه، کمک کن درستش کنم"

---

### Rule 3: Architecture & Design
**English Keywords:** "design", "architecture", "pattern", "structure", "organize", "best practice"
**Persian Keywords:** "طراحی", "معماری", "الگو", "ساختار", "سازماندهی", "بهترین روش", "best practice"
**Complexity:** High
**Selected Model:** `tngtech/deepseek-r1t2-chimera:free`
**Reason:** Strong reasoning for system design and architectural decisions

**Example prompts:**
- "Design a microservices architecture for..."
- "یک معماری میکروسرویس برای ... طراحی کن"
- "What's the best pattern for state management?"
- "بهترین الگو برای مدیریت状态 چیه؟"
- "How should I structure this Next.js project?"
- "این پروژه Next.js رو چطور باید سازماندهی کنم؟"

---

### Rule 4: Algorithm & Complex Logic
**English Keywords:** "algorithm", "optimize", "performance", "complexity", "efficient", "solve"
**Persian Keywords:** "الگوریتم", "بهینه‌سازی", "کارایی", "پیچیدگی", "بهینه", "حل کردن", "solve"
**Complexity:** High
**Selected Model:** `tngtech/deepseek-r1t2-chimera:free`
**Reason:** Deep reasoning for algorithmic challenges

**Example prompts:**
- "Optimize this sorting algorithm"
- "این الگوریتم مرتب‌سازی را بهینه‌سازی کن"
- "Find the most efficient way to..."
- "کارآمدترین راه برای ... پیدا کن"
- "Solve this dynamic programming problem"
- "این مسئله برنامه‌نویسی پویا را حل کن"

---

### Rule 5: Code Review & Refactoring
**English Keywords:** "review", "refactor", "improve", "clean", "optimize code", "rewrite"
**Persian Keywords:** "بررسی", "بازنویسی", "بهبود", "تمیز کردن", "بهینه‌سازی کد", "refactor"
**Complexity:** Medium-High
**Selected Model:** `qwen/qwen3-coder-480b-a35b-07-25:free`
**Reason:** Largest context (262K) for handling large codebases

**Example prompts:**
- "Review this code and suggest improvements"
- "این کد را بررسی کن و پیشنهادات بهبودی بده"
- "Refactor this legacy component"
- "این کامپوننت قدیمی را بازنویسی کن"
- "How can I make this more maintainable?"
- "چطور می‌تونم این رو نگهداری‌پذیرتر کنم؟"

---

### Rule 6: Large Codebase Analysis
**English Keywords:** "analyze", "understand", "explain", "codebase", "multiple files"
**Persian Keywords:** "تحلیل", "درک", "توضیح", "کدبیس", "چندین فایل", "codebase"
**Context needed:** > 160K tokens
**Selected Model:** `qwen/qwen3-coder-480b-a35b-07-25:free`
**Reason:** Largest context window (262K)

**Example prompts:**
- "Analyze this entire module structure"
- "کل ساختار ماژول را تحلیل کن"
- "Explain how these 10 files interact"
- "توضیح بده این 10 فایل چطور با هم تعامل دارن"
- "Review this large PR with multiple changes"
- "این PR بزرگ با چندین تغییر را بررسی کن"

---

### Rule 7: Testing & Documentation
**English Keywords:** "test", "unit test", "e2e", "documentation", "comment", "readme"
**Persian Keywords:** "تست", "تست واحد", "تست انتها به انتها", "مستندات", "توضیح", "readme"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Fast, efficient, good for systematic tasks

**Example prompts:**
- "Write unit tests for this function"
- "برای این تابع تست‌های واحد بنویس"
- "Generate documentation for this API"
- "مستندات این API را تولید کن"
- "Create a README for this project"
- "یک README برای این پروژه بساز"

---

### Rule 8: TypeScript/JavaScript Specific
**English Keywords:** "typescript", "ts", "react", "nextjs", "node", "javascript"
**Persian Keywords:** "تایپ‌اسکریپت", "ری‌اکت", "نکست جی‌اس", "نود", "جاوا اسکریپت"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Excellent fullstack support, high usage indicates strong performance

**Example prompts:**
- "Convert this JavaScript to TypeScript"
- "این جاوا اسکریپت را به تایپ‌اسکریپت تبدیل کن"
- "Create a Next.js API route"
- "یک روت API در Next.js بساز"
- "Build a React custom hook"
- "یک هوک سفارشی ری‌اکت بساز"

---

### Rule 9: Python Specific
**English Keywords:** "python", "django", "fastapi", "flask", "pandas", "numpy"
**Persian Keywords:** "پایتون", "جنگو", "فاست‌ایپی‌آی", "فلسک", "پانداس", "نامپای"
**Complexity:** Medium
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Strong general-purpose coding with Python support

**Example prompts:**
- "Create a FastAPI endpoint"
- "یک endpoint FastAPI بساز"
- "Write a Python script for data processing"
- "یک اسکریپت پایتون برای پردازش داده بنویس"
- "Build a Django model with relationships"
- "یک مدل جنگو با رابطه‌ها بساز"

---

### Rule 10: Quick Questions & Explanations
**English Keywords:** "what", "how", "why", "explain", "difference", "?", "quick question"
**Persian Keywords:** "چیست", "چگونه", "چرا", "توضیح", "تفاوت", "سوال سریع", "؟"
**Complexity:** Low
**Selected Model:** `z-ai/glm-4.5-air:free`
**Reason:** Fast, efficient, no reasoning overhead needed

**Example prompts:**
- "What's the difference between let and const?"
- "تفاوت let و const چیه؟"
- "How does async/await work?"
- "async/await چطور کار می‌کنه؟"
- "Explain this error message"
- "این پیام خطا را توضیح بده"

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

1. **Analyze** the task type using keywords above (both English and Persian)
2. **Select** the appropriate model based on rules
3. **Inform** the user: "🤖 Using [model-name] for [reason]"
4. **STOP** and ask the user for confirmation: "are you select model? (y/n)"
5. **WAIT for the user's response.**
6. If the user confirms ('y'), proceed with the task. Otherwise, ask for clarification or choose a different approach.
7. **Fallback** if model fails

---

## 📝 Example Responses

**User:** "Create a React component for user authentication"
**Assistant:** "🤖 Using `z-ai/glm-4.5-air:free` - optimal for general React development with balanced performance.
are you select model? (y/n)"

**User:** "یک کامپوننت ری‌اکت برای احراز هویت کاربر بساز"
**Assistant:** "🤖 Using `z-ai/glm-4.5-air:free` - optimal for general React development with balanced performance.
are you select model? (y/n)"

**User:** "Design a scalable microservices architecture"
**Assistant:** "🤖 Using `tngtech/deepseek-r1t2-chimera:free` - strong reasoning capabilities for architectural decisions.
are you select model? (y/n)"

**User:** "یک معماری میکروسرویس برای ... طراحی کن"
**Assistant:** "🤖 Using `tngtech/deepseek-r1t2-chimera:free` - strong reasoning capabilities for architectural decisions.
are you select model? (y/n)"

**User:** "Debug this 500-line legacy code"
**Assistant:** "🤖 Using `qwen/qwen3-coder-480b-a35b-07-25:free` - large context window (262K) handles extensive code review.
are you select model? (y/n)"

**User:** "این کد 500 خطی قدیمی را دیباگ کن"
**Assistant:** "🤖 Using `qwen/qwen3-coder-480b-a35b-07-25:free` - large context window (262K) handles extensive code review.
are you select model? (y/n)"

---

## ⚠️ Important Notes

1. **Always prefer quality over speed** - You specified quality is more important
2. **Context is king** - Use models with larger context for complex tasks
3. **Reasoning is optional** - Only use reasoning models when truly needed
4. **Monitor performance** - If a model consistently fails, escalate to next tier
5. **Stay updated** - This ruleset is based on current usage data; update when new models arrive
6. **User confirmation is required** - Always stop and ask for confirmation before proceeding with a task after model selection.
7. **WAIT for user confirmation** - Do not proceed with the task until the user explicitly confirms with 'y'.

---

## 🎯 Your Priority Matrix

```
Priority 1: Code Quality
Priority 2: Speed/Performance
Priority 3: Context Length
Priority 4: Reasoning (optional)
```

**Final Default:**
<!-- befor start task : -->
<!-- Announce the proposed model to the user and only say:  -->
<!-- are you select model? (y/n) -->
---

*Last Updated: Based on usage data through 2025-10-11*
*Total Models Analyzed: 200+ | Free Models Selected: 6 | Context Range: 131K-262K*
