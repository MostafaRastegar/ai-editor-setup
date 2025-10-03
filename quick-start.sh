#!/bin/bash

# Quick Start Script for AI Editor

echo "🚀 AI Editor Quick Start"
echo "========================"
echo ""

# Check VS Code
echo "1. Checking VS Code..."
if command -v code &> /dev/null; then
    echo "   ✅ VS Code is installed"
else
    echo "   ❌ VS Code not found!"
    echo "   Please install VS Code from: https://code.visualstudio.com/"
    exit 1
fi

# Check Cline Extension
echo "2. Checking Cline Extension..."
if code --list-extensions | grep -q "saoudrizwan.claude-dev"; then
    echo "   ✅ Cline extension is installed"
else
    echo "   ⚠️  Cline extension not found"
    echo "   Please install from VS Code Extensions (Ctrl+Shift+X)"
    echo "   Search for: Cline"
fi

# Check for OpenRouter API Key
echo "3. Checking configuration..."
echo "   📝 Make sure you have:"
echo "   - OpenRouter API key from https://openrouter.ai"
echo "   - Cline configured with OpenRouter"
echo "   - Model selected (e.g., anthropic/claude-3.5-sonnet)"

# Create sample .clinerules
echo "4. Creating sample .clinerules file..."
cat > .clinerules << 'EOF'
# Project Rules

## Code Style
- Use clear, readable code
- Add comments for complex logic
- Follow language-specific conventions

## Testing
- Write tests for new features
- Test edge cases
- Keep tests up to date

## Documentation
- Update README for major changes
- Document API endpoints
- Keep code comments current
EOF

echo "   ✅ Created .clinerules file"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Open VS Code: code ."
echo "2. Install Cline extension if not already installed"
echo "3. Configure Cline with your OpenRouter API key"
echo "4. Start coding with AI assistance!"
echo ""
echo "📚 For detailed setup: see setup-guide.md"
echo "🧠 For Memory Bank: see memory-bank-guide.md"
echo ""
echo "Test Cline with: 'Can you see the files in this project?'"