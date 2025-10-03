# Tech Context

## Technologies Used

### Core Technologies
- **VS Code**: Code editor and development environment
- **Cline Extension**: AI agent and context management
- **OpenRouter**: LLM gateway and API provider
- **Markdown**: Documentation format
- **Git**: Version control

### AI/ML Technologies
- **Large Language Models**: Claude, GPT-4, Gemini, Llama, ZhipuAI GLM-4
- **Context Management**: Cline's Memory Bank system
- **Vector Operations**: Built into Cline (no external DB needed)
- **Prompt Engineering**: Optimized for coding tasks
- **Model Selection**: Free, budget, and premium options available

### Development Tools
- **VS Code Extensions**: Cline, Continue (optional)
- **API Integration**: OpenRouter REST API
- **File Management**: Local file system
- **Documentation**: Markdown with Mermaid diagrams
- **Learning Resources**: YouTube tutorials, OpenRouter model browser

## Development Setup

### Prerequisites
- VS Code (latest version)
- Internet connection (for LLM calls)
- OpenRouter account and API key
- Basic understanding of AI tools

### Installation Steps
1. Install VS Code from official website
2. Install Cline extension from marketplace
3. Create OpenRouter account
4. Generate API key
5. Configure Cline with API key and model

### Configuration Files
- **.vscode/settings.json**: VS Code configuration
- **.clinerules**: Project-specific rules
- **memory-bank/**: Context management files
- **.gitignore**: Version control exclusions

## Technical Constraints

### Performance Constraints
- **Context Window**: Limited by LLM model (1M tokens for Claude Sonnet 4.5)
- **Response Time**: Depends on OpenRouter and model performance
- **Memory Usage**: Minimal (no local LLM required)
- **Storage**: Only for project files and Memory Bank

### Network Constraints
- **Internet Required**: For LLM API calls
- **API Rate Limits**: Depends on OpenRouter plan
- **Latency**: Network-dependent response times
- **Reliability**: Depends on OpenRouter uptime

### Platform Constraints
- **VS Code Only**: Extension requires VS Code
- **Operating System**: Windows, macOS, Linux supported
- **Architecture**: x64, ARM64 supported
- **Browser**: Not applicable (desktop app)

## Dependencies

### Required Dependencies
- **VS Code**: >= 1.80.0
- **Cline Extension**: Latest version
- **OpenRouter API**: Active account
- **Internet Connection**: For API calls

### Optional Dependencies
- **Continue Extension**: For autocomplete
- **Ollama**: For local LLM models
- **Git**: For version control
- **Python/Node.js**: For project development

### External Services
- **OpenRouter**: Primary LLM provider
- **Anthropic**: Claude models
- **OpenAI**: GPT models
- **Google**: Gemini models
- **Meta**: Llama models
- **ZhipuAI**: GLM-4 models (Chinese, very cheap)
- **Microsoft**: Phi-3 models (free options available)

## Tool Usage Patterns

### Cline Commands
- **/memory-bank**: Update project memory
- **/deep-planning**: Plan complex features
- **/newtask**: Start fresh task
- **/smol**: Compress conversation

### Memory Bank Files
- **projectbrief.md**: Project foundation
- **productContext.md**: Product understanding
- **activeContext.md**: Current work focus
- **systemPatterns.md**: Technical architecture
- **techContext.md**: Technology details
- **progress.md**: Project status

### VS Code Integration
- **Sidebar**: Cline chat interface
- **File Operations**: Create, edit, delete files
- **Terminal**: Execute commands
- **Extensions**: Seamless integration

## Development Workflow

### Daily Workflow
1. Open VS Code with project
2. Start Cline conversation
3. Use Memory Bank context
4. Code with AI assistance
5. Update Memory Bank as needed

### Project Setup
1. Initialize Memory Bank
2. Configure .clinerules
3. Set up project structure
4. Test basic functionality
5. Document setup process

### Maintenance
1. Update Memory Bank regularly
2. Review and update documentation
3. Test with new features
4. Gather user feedback
5. Improve based on usage

## Performance Considerations

### Optimization Strategies
- **Context Management**: Use Memory Bank effectively
- **Model Selection**: Balance cost and performance
- **Prompt Engineering**: Optimize for specific tasks
- **File Organization**: Keep project structure clean

### Monitoring
- **Response Times**: Track AI response speed
- **Context Usage**: Monitor context window usage
- **Error Rates**: Track failed requests
- **User Satisfaction**: Gather feedback regularly

### Scaling Considerations
- **Team Usage**: Share Memory Bank files
- **Large Projects**: Use /smol and /newtask
- **Multiple Models**: Switch based on needs
- **Cost Management**: Monitor API usage
