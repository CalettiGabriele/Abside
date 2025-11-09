<div align="center">

  # Abside

  **Architectural Blueprint System for IDEs**
  
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Apse.png" alt="Abside Logo" width="450"/>
  
  A modular MCP (Model Context Protocol) ecosystem that helps developers and LLMs apply design patterns and write better code.
  
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
  [![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![MCP](https://img.shields.io/badge/MCP-compatible-green.svg)](https://modelcontextprotocol.io)
</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [MCP Servers](#mcp-servers)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Abside is a family of MCP (Model Context Protocol) servers designed to enhance the development experience by providing intelligent architectural guidance, design pattern recommendations, and code quality improvements directly within your IDE.

### Key Features

- **🏗️ Modular Architecture**: Each server focuses on a specific aspect of software development
- **🔌 MCP Protocol**: Seamless integration with AI-powered IDEs and tools
- **📚 Pattern Library**: Comprehensive collection of design patterns and best practices
- **🤖 AI-Native**: Built specifically for LLM-assisted development workflows
- **🔧 Extensible**: Easy to add new servers and capabilities

## 🏛️ Architecture

Abside follows a microservices-inspired architecture where each MCP server is an independent, specialized component:

```
┌─────────────────────────────────────────────────────────┐
│                      IDE / Client                        │
└─────────────────────────────────────────────────────────┘
                           │
                           │ MCP Protocol
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼────────┐ ┌──────▼───────┐ ┌───────▼────────┐
│  Pattern       │ │  Architecture │ │   Quality      │
│  Server        │ │  Server       │ │   Server       │
└────────────────┘ └──────────────┘ └────────────────┘
        │                  │                  │
        └──────────────────┴──────────────────┘
                           │
                    Shared Libraries
```

## 🖥️ MCP Servers

### Available Servers

| Server | Description | Status |
|--------|-------------|--------|
| **Pattern Server** | Design patterns, SOLID principles, architectural patterns | 🚧 In Development |
| **Architecture Server** | System design, component relationships, dependency analysis | 📋 Planned |
| **Quality Server** | Code quality metrics, refactoring suggestions, best practices | 📋 Planned |
| **Documentation Server** | Auto-documentation, API specs, inline comments | 📋 Planned |

### Server Capabilities

Each MCP server provides:
- **Resources**: Access to pattern libraries, documentation, and knowledge bases
- **Tools**: Executable functions for code analysis and transformation
- **Prompts**: Pre-configured prompts for common development tasks

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip or uv package manager
- An MCP-compatible IDE or client

### Install from Source

```bash
# Clone the repository
git clone https://github.com/CalettiGabriele/Abside.git
cd Abside

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

### Install with uv

```bash
uv pip install -e .
```

## 🚀 Quick Start

### 1. Configure Your IDE

Add Abside servers to your MCP client configuration (e.g., `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "abside-pattern": {
      "command": "python",
      "args": ["-m", "abside.servers.pattern"],
      "cwd": "/path/to/Abside"
    }
  }
}
```

### 2. Start Using Abside

Once configured, you can interact with Abside through your AI assistant:

```
"Show me the Singleton pattern implementation"
"Analyze this code for SOLID principle violations"
"Suggest an architectural pattern for this microservice"
```

## ⚙️ Configuration

Each server can be configured through environment variables or configuration files:

```bash
# .env file
ABSIDE_PATTERN_LIBRARY_PATH=/path/to/patterns
ABSIDE_LOG_LEVEL=INFO
ABSIDE_CACHE_ENABLED=true
```

See individual server documentation for specific configuration options.

## 🛠️ Development

### Project Structure

```
Abside/
├── src/
│   └── abside/
│       ├── servers/          # Individual MCP servers
│       │   ├── pattern/
│       │   ├── architecture/
│       │   └── quality/
│       ├── common/           # Shared utilities
│       └── patterns/         # Pattern library
├── tests/                    # Test suite
├── docs/                     # Documentation
├── examples/                 # Usage examples
└── README.md
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=abside --cov-report=html
```

### Adding a New Server

1. Create a new directory under `src/abside/servers/`
2. Implement the MCP server interface
3. Add server configuration
4. Write tests
5. Update documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting PRs.

### Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run linting
ruff check .

# Format code
ruff format .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io) for the MCP specification
- The open-source community for inspiration and support

## 📞 Contact

- **Author**: Gabriele Caletti
- **Repository**: [github.com/CalettiGabriele/Abside](https://github.com/CalettiGabriele/Abside)
- **Issues**: [github.com/CalettiGabriele/Abside/issues](https://github.com/CalettiGabriele/Abside/issues)

---
