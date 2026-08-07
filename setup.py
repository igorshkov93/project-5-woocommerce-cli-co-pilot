from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="woo-copilot",
    version="0.1.0",
    author="Igor",
    author_email="your.email@example.com",
    description="CLI Co-pilot for WooCommerce powered by Gemini AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/woo-copilot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10",
    install_requires=[
        "google-generativeai>=0.8.0",
        "woocommerce>=3.0.0",
        "click>=8.1.7",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "pandas>=2.1.0",
        "colorlog>=6.8.0",
        "pydantic>=2.5.0",
    ],
    entry_points={
        "console_scripts": [
            "woo-copilot=src.cli.main:cli",
        ],
    },
)
