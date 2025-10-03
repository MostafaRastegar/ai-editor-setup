# Setup Guide

Simple step-by-step setup for AI Editor using Cline.

## Step 1: Install VS Code

Download and install VS Code from: https://code.visualstudio.com/

## Step 2: Install Cline Extension

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for **Cline**
4. Install the extension by saoudrizwan

Direct link: https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev

## Step 3: Get OpenRouter API Key

1. Go to https://openrouter.ai
2. Sign up for an account
3. Go to API Keys section
4. Create a new API key
5. Copy the key (you'll need it for Cline)

## Step 4: Configure Cline

1. Click Cline button in VS Code sidebar
2. Click the settings/gear icon
3. Set the following:
   - **API Provider**: OpenRouter
   - **API Key**: Your OpenRouter key
   - **Model**: anthropic/claude-3.5-sonnet (or your preferred model)

## Step 5: Test Cline

1. Open any project folder in VS Code
2. Click Cline icon in sidebar
3. Try this test prompt:
   ```
   Can you see the files in this project? List them and explain what this project does.
   ```

## Done!

You can now use Cline like Cursor:
- Write and edit code
- Create new files
- Fix bugs and refactor
- Execute terminal commands
- Understand entire codebase

---

## Recommended Models

**Best Quality:**
- anthropic/claude-3.5-sonnet
- openai/gpt-4-turbo

**Budget-Friendly:**
- zhipuai/glm-4-flash (Chinese model, very cheap)
- meta-llama/llama-3.3-70b-instruct
- anthropic/claude-3-haiku

**Free Models:**
- google/gemini-2.0-flash-exp:free (completely free!)
- microsoft/phi-3-medium-128k-instruct:free
- meta-llama/llama-3.1-8b-instruct:free

**Browse all free models:** [OpenRouter Free Models](https://openrouter.ai/models?max_price=0&order=context-high-to-low&q=free)

## Memory Bank Setup (Optional)

For better context management across sessions:

1. **Create .clinerules file** in your project root:
   ```markdown
   # Project Rules
   - Use Python 3.9+
   - Follow PEP 8 style guide
   - Add type hints to functions
   - Write docstrings for all functions
   ```

2. **Use Memory Bank commands** in Cline:
   - `/memory-bank` - Create or update project memory
   - `/deep-planning` - Plan complex features
   - `/newtask` - Start fresh task with context

## Troubleshooting

**Cline can't write files:**
- Enable "Allow File Operations" in Cline Settings

**API Error:**
- Check OpenRouter API key
- Verify internet connection
- Ensure model name is correct

**Cline not responding:**
- Restart VS Code
- Check Cline extension is enabled
- Verify API key is valid

## Advanced Features

- **Focus Chain**: Automatic task management
- **Auto Compact**: Context window management
- **Memory Bank**: Persistent project knowledge
- **Deep Planning**: Complex feature planning
- **Slash Commands**: Quick actions

## Learning Resources

**Cline Tutorial:** [YouTube Video](https://www.youtube.com/watch?v=UBqh6ud5LqY) - Learn how to use Cline effectively

**Model Selection Guide:**
- **Free models:** [OpenRouter Free Models](https://openrouter.ai/models?max_price=0&order=context-high-to-low&q=free)
- **Budget models:** ZhipuAI GLM-4 Flash (Chinese, very cheap)
- **Premium models:** Claude Sonnet, GPT-4 Turbo

## Optional Enhancements

- **Continue Extension**: Add autocomplete
- **Ollama**: Run local LLM models
- **Custom .clinerules**: Project-specific instructions