# AI Editor - Free Cursor Alternative

Transform VS Code into an AI-powered editor using Cline with built-in context management.

## What is this?

A complete, ready-to-use setup that turns VS Code into an AI Agent Editor similar to Cursor:
- **Cost-effective**: ~$1-3/month vs Cursor Pro's $20/month
- **Simple setup**: No Docker, no external databases
- **Built-in context**: Cline handles all context management
- **Same quality**: AI assistance as good as Cursor
- **Ready to use**: Clone, configure, and start coding

## Quick Start

### 1. Clone & Setup
```bash
git clone <repository-url>
cd ai-editor
code .
```

### 2. Install Cline Extension
- Open VS Code Extensions (Ctrl+Shift+X)
- Search for "Cline" 
- Install the extension by saoudrizwan

### 3. Get OpenRouter API Key
- Sign up at [OpenRouter](https://openrouter.ai)
- Create API key
- Choose your model (see [Free Models](https://openrouter.ai/models?max_price=0&order=context-high-to-low&q=free))

### 4. Configure Cline
- Click Cline icon in VS Code sidebar
- Set API Provider: OpenRouter
- Add your API key
- Select model (e.g., `google/gemini-2.0-flash-exp:free`)

### 5. Start Coding!
- Use `/memory-bank` to initialize project context
- Chat with AI to write code, fix bugs, refactor
- Enjoy 85-95% cost savings vs Cursor Pro!

## Stack

- **VS Code**: Code editor
- **Cline Extension**: AI Agent with built-in context management
- **OpenRouter**: LLM gateway (Claude, GPT-4, Gemini, etc.)

## Usage

1. Open VS Code
2. Click Cline icon in sidebar
3. Chat with AI to write code, fix bugs, refactor, etc.

## Features

- **Automatic Context Gathering**: Cline reads and understands your project
- **Memory Bank**: Built-in context storage system
- **Focus Chain**: Maintains task lists across sessions
- **Auto Compact**: Manages context window automatically
- **Multi-file Operations**: Create, edit, and manage files
- **Terminal Commands**: Execute commands directly
- **Project Understanding**: Analyzes code structure and patterns

## Cost Comparison

| Service | Cost/Month | Quality |
|---------|------------|---------|
| Cursor Pro | $20 | ⭐⭐⭐⭐⭐ |
| This Setup | $1-3 | ⭐⭐⭐⭐⭐ |

## Recommended Models

**Best Quality:**
- `anthropic/claude-3.5-sonnet`
- `openai/gpt-4-turbo`

**Budget-Friendly:**
- `zhipuai/glm-4-flash` (Chinese model, very cheap)
- `meta-llama/llama-3.3-70b-instruct`
- `anthropic/claude-3-haiku`

**Free Models:**
- `google/gemini-2.0-flash-exp:free` (completely free!)
- `microsoft/phi-3-medium-128k-instruct:free`
- `meta-llama/llama-3.1-8b-instruct:free`

**Browse all free models:** [OpenRouter Free Models](https://openrouter.ai/models?max_price=0&order=context-high-to-low&q=free)

## Memory Bank Setup (Optional)

For better context management across sessions:

1. Create `.clinerules` file in project root
2. Use `/memory-bank` command in Cline
3. Document project patterns and decisions

## Learning Resources

**Cline Tutorial:** [YouTube Video](https://www.youtube.com/watch?v=UBqh6ud5LqY) - Learn how to use Cline effectively

**Model Selection:**
- **Free models:** [OpenRouter Free Models](https://openrouter.ai/models?max_price=0&order=context-high-to-low&q=free)
- **Budget models:** ZhipuAI GLM-4 Flash (Chinese, very cheap)
- **Premium models:** Claude Sonnet, GPT-4 Turbo

## System Requirements

**Minimum:**
- RAM: 4GB
- CPU: 2 cores
- Disk: 1GB

**Recommended:**
- RAM: 8GB+
- CPU: 4 cores+
- Disk: 2GB+

## FAQ

**Why Cline?**
Best AI agent extension with built-in context management, no external databases needed.

**Do I need Docker?**
No! Cline handles everything internally.

**Do I need internet?**
Only for LLM calls (OpenRouter). Context management is local.

**Can I use local models?**
Yes! Install Ollama and configure Cline to use local models.

## Advanced Features

- **Deep Planning**: `/deep-planning` for complex features
- **New Task**: `/newtask` for fresh context
- **Smol**: `/smol` to compress conversation
- **Memory Bank**: Persistent project knowledge
- **Focus Chain**: Task management across sessions

## License

MIT