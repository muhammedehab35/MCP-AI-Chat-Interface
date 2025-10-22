# MCP AI Chat Interface

🤖 Interactive CLI chat application with AI models (Claude/OpenAI) using Model Control Protocol (MCP) for document management and tool integration.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-1.8.0-green.svg)](https://github.com/modelcontextprotocol)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

MCP AI Chat Interface is a command-line interface application that enables interactive chat capabilities with AI models (Claude or OpenAI). The application supports document retrieval, command-based prompts, and extensible tool integrations via the MCP (Model Control Protocol) architecture.

## ✨ Features

- 🤖 **Multi-Provider Support**: Works with both Claude (Anthropic) and OpenAI models
- 📄 **Document Management**: Read and edit documents via MCP tools
- 🔧 **MCP Integration**: Full support for Model Control Protocol
- 💬 **Interactive CLI**: Auto-completion and command suggestions
- 🏷️ **@Mentions**: Reference documents directly in your queries
- ⚡ **Fast & Lightweight**: Built with Python and async I/O

## Prerequisites

- Python 3.10+
- Anthropic API Key (for Claude) or OpenAI API Key

## Project Structure

```
MCP-AI-Chat-Interface/
├── src/
│   └── mcp_chat/           # Main application package
│       ├── core/           # Core functionality
│       │   ├── chat.py     # Base chat class
│       │   ├── claude.py   # Claude AI provider
│       │   ├── openai_provider.py  # OpenAI provider
│       │   ├── cli.py      # CLI interface
│       │   ├── cli_chat.py # CLI chat implementation
│       │   └── tools.py    # Tool manager
│       ├── mcp_client.py   # MCP client
│       ├── mcp_server.py   # MCP server (document tools)
│       └── main.py         # Application entry point
├── main.py                 # Launcher script
├── pyproject.toml          # Project configuration
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
└── README.md
```

## Setup

### Step 1: Configure the environment variables

1. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

2. Edit `.env` and configure your settings:

```env
# Choose your provider: "claude" or "openai"
PROVIDER=openai

# If using Claude
CLAUDE_MODEL=claude-3-5-sonnet-20241022
ANTHROPIC_API_KEY=your_key_here

# If using OpenAI
OPENAI_MODEL=gpt-4o
OPENAI_API_KEY=your_key_here

# Use UV (1) or regular Python (0)
USE_UV=1
```

### Step 2: Install dependencies

#### Option 1: Setup with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. Install uv, if not already installed:

```bash
pip install uv
```

2. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
uv pip install -e .
```

4. Run the project

```bash
uv run main.py
```

#### Option 2: Setup without uv

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

## Usage

### Basic Interaction

Simply type your message and press Enter to chat with the model.

### Document Retrieval

Use the @ symbol followed by a document ID to include document content in your query:

```
> Tell me about @deposition.md
```

### Commands (Prompts)

Use the / prefix to execute commands defined in the MCP server:

**Available commands:**
```bash
# Summarize a document
> /summarize deposition.md

# Rewrite a document in clean markdown format
> /rewrite_markdown report.pdf
```

Commands will auto-complete when you press Tab.

## Development

### Adding New Documents

Edit the `src/mcp_chat/mcp_server.py` file to add new documents to the `docs` dictionary.

### Project Features

✅ **Fully Implemented:**
- **MCP Tools:**
  - Document reading and editing via MCP tools
  - Resources for listing and accessing documents
- **AI Provider Support:**
  - Support for both Claude (Anthropic) and OpenAI models
- **CLI Features:**
  - Interactive CLI with autocompletion
  - Document mention system (@doc_id)
  - Command suggestions with Tab completion
- **Prompts System:**
  - `/summarize` - Generate concise document summaries
  - `/rewrite_markdown` - Reformat documents in clean markdown
- **MCP Client:**
  - `list_prompts()` - List available prompts from server
  - `get_prompt()` - Get prompt by name with arguments
  - Full MCP protocol implementation

### Available MCP Tools

- `read_doc(doc_name: str)` - Read document content
- `edit_doc(doc_name: str, old_string: str, new_string: str)` - Edit document

### Available MCP Resources

- `docs://documents` - List all document IDs
- `docs://documents/{doc_id}` - Get specific document content

### Available MCP Prompts

- `summarize` - Generate a concise summary of a document
- `rewrite_markdown` - Rewrite a document in clean markdown format

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [MCP (Model Context Protocol)](https://github.com/modelcontextprotocol)
- Supports [Anthropic Claude](https://www.anthropic.com/) and [OpenAI](https://openai.com/) models
