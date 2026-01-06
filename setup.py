from setuptools import setup, find_packages

setup(
    name="agentic-rag-test-framework",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=6.0",
        "openai>=1.0.0",
        "anthropic>=0.5.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "tqdm>=4.62.0",
        "pyyaml>=6.0"
    ],
    entry_points={
        "console_scripts": [
            "rag-test=rag_test_framework.cli:main",
        ],
    },
    author="AI Engineer Community",
    description="CLI tool for automated evaluation of RAG agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/agentic-rag-test-framework",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)