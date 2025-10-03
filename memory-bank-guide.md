# Cline Memory Bank Guide

Learn how to use Cline's professional Memory Bank system for perfect context management.

## What is Memory Bank?

Memory Bank is Cline's sophisticated system for maintaining project context across sessions. Cline has a unique characteristic: **memory resets completely between sessions**. This isn't a limitation - it's what drives perfect documentation. After each reset, Cline relies ENTIRELY on the Memory Bank to understand the project and continue work effectively.

## Memory Bank Structure

The Memory Bank consists of core files and optional context files, all in Markdown format. Files build upon each other in a clear hierarchy:

```
projectbrief.md → productContext.md → activeContext.md
                ↘ systemPatterns.md ↗
                ↘ techContext.md ↗
```

### Core Files (Required)

#### 1. `projectbrief.md`
- **Foundation document** that shapes all other files
- Created at project start if it doesn't exist
- Defines core requirements and goals
- Source of truth for project scope

#### 2. `productContext.md`
- Why this project exists
- Problems it solves
- How it should work
- User experience goals

#### 3. `activeContext.md`
- Current work focus
- Recent changes
- Next steps
- Active decisions and considerations
- Important patterns and preferences
- Learnings and project insights

#### 4. `systemPatterns.md`
- System architecture
- Key technical decisions
- Design patterns in use
- Component relationships
- Critical implementation paths

#### 5. `techContext.md`
- Technologies used
- Development setup
- Technical constraints
- Dependencies
- Tool usage patterns

#### 6. `progress.md`
- What works
- What's left to build
- Current status
- Known issues
- Evolution of project decisions

### Additional Context
Create additional files/folders within `memory-bank/` when they help organize:
- Complex feature documentation
- Integration specifications
- API documentation
- Testing strategies
- Deployment procedures

## Setting Up Memory Bank

### 1. Create Memory Bank Directory

```bash
mkdir memory-bank
cd memory-bank
```

### 2. Create Core Files

Start with `projectbrief.md`:

```markdown
# Project Brief

## Project Name
AI Editor - Free Cursor Alternative

## Core Purpose
Transform VS Code into an AI-powered editor using Cline with built-in context management.

## Key Requirements
- Cost-effective: ~$1-3/month vs Cursor Pro's $20/month
- Simple setup: No Docker, no external databases
- Built-in context: Cline handles all context management
- Same quality: AI assistance as good as Cursor

## Success Criteria
- Easy installation and setup
- Reliable AI assistance
- Good documentation
- Active community support
```

### 3. Use Memory Bank Commands

In Cline chat, use these commands:

```
/memory-bank
```
Creates or updates project memory with current context.

```
/deep-planning
```
For complex features - analyzes codebase and creates implementation plan.

```
/newtask
```
Starts fresh task with distilled context from memory bank.

```
/smol
```
Compresses current conversation to keep momentum.

## Core Workflows

### Plan Mode
1. **Read Memory Bank** - Cline reads ALL memory bank files
2. **Check Completeness** - Verify all required files exist
3. **Create Plan** - If files incomplete, create missing ones
4. **Document Strategy** - Present approach in chat

### Act Mode
1. **Check Memory Bank** - Review current context
2. **Update Documentation** - Keep files current
3. **Execute Task** - Implement changes
4. **Document Changes** - Update progress

## Documentation Updates

Memory Bank updates occur when:
1. Discovering new project patterns
2. After implementing significant changes
3. When user requests with **update memory bank** (MUST review ALL files)
4. When context needs clarification

**Important**: When triggered by **update memory bank**, Cline MUST review every memory bank file, even if some don't require updates. Focus particularly on `activeContext.md` and `progress.md` as they track current state.

## Best Practices

### 1. Maintain File Hierarchy
- Keep `projectbrief.md` as foundation
- Build other files on top of it
- Update `activeContext.md` frequently
- Keep `progress.md` current

### 2. Use Clear Structure
- Use consistent Markdown formatting
- Include clear headings and sections
- Add examples and code snippets
- Link related concepts

### 3. Regular Updates
- Update after major changes
- Review all files periodically
- Remove outdated information
- Document key decisions

### 4. Team Collaboration
- Share memory bank files
- Use version control
- Document team decisions
- Keep files synchronized

## Example Memory Bank Files

### projectbrief.md
```markdown
# Project Brief

## Project Name
AI Editor

## Core Purpose
Transform VS Code into AI-powered editor

## Key Requirements
- Cost-effective
- Simple setup
- Built-in context management

## Success Criteria
- Easy installation
- Reliable AI assistance
- Good documentation
```

### activeContext.md
```markdown
# Active Context

## Current Focus
Setting up Memory Bank system for better context management

## Recent Changes
- Removed Qdrant dependency
- Updated to Cline-only setup
- Created Memory Bank guide

## Next Steps
- Test Memory Bank functionality
- Create sample memory bank files
- Document workflows

## Key Patterns
- Use .clinerules for project rules
- Maintain memory-bank/ directory
- Update files after major changes
```

## Troubleshooting

**Memory Bank not working:**
- Check memory-bank/ directory exists
- Ensure core files are present
- Verify Cline extension is active

**Context getting lost:**
- Use `/smol` to compress conversation
- Run `/memory-bank` more frequently
- Check file completeness

**Files not updating:**
- Use **update memory bank** command
- Review all files manually
- Check file permissions

## Learning Resources

**Cline Tutorial:** [YouTube Video](https://www.youtube.com/watch?v=UBqh6ud5LqY) - Learn how to use Cline effectively

**Model Selection:**
- **Free models:** [OpenRouter Free Models](https://openrouter.ai/models?max_price=0&order=context-high-to-low&q=free)
- **Budget models:** ZhipuAI GLM-4 Flash (Chinese, very cheap)
- **Premium models:** Claude Sonnet, GPT-4 Turbo

## Advanced Tips

- Use `@` mentions to add web content
- Screenshots for image-capable models
- MCP servers for external knowledge
- Combine with Continue Extension

## Memory Bank vs External Databases

| Feature | Memory Bank | External DB |
|---------|-------------|-------------|
| Setup | ✅ Built-in | ❌ Complex |
| Maintenance | ✅ Minimal | ❌ Required |
| Performance | ✅ Fast | ⚠️ Network |
| Context Quality | ✅ Excellent | ⚠️ Depends |
| Team Sharing | ✅ Files | ❌ Server needed |

**Conclusion**: Memory Bank is simpler, faster, and more effective for most projects.

---

**REMEMBER**: After every memory reset, Cline begins completely fresh. The Memory Bank is the only link to previous work. It must be maintained with precision and clarity, as effectiveness depends entirely on its accuracy.
