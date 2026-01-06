# Agentic RAG Test Framework

![License](https://img.shields.io/github/license/ai-engineer-community/agentic-rag-test-framework)
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![CLI](https://img.shields.io/badge/CLI-Tool-green)

CLI tool + GitHub Actions integration for automated evaluation of RAG agents against knowledge bases, vector DB quality metrics, tool hallucination detection, and context relevance scoring.

## Features

- Automated RAG evaluation against knowledge bases
- Vector database quality metrics
- Tool hallucination detection
- Context relevance scoring
- GitHub Actions integration
- Support for multiple RAG frameworks

## Installation

```bash
pip install agentic-rag-test-framework
```

Or for development:

```bash
git clone https://github.com/your-username/agentic-rag-test-framework.git
cd agentic-rag-test-framework
pip install -e .
```

## Usage

```bash
rag-test --config config.yaml --eval dataset.json
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT