# ERC-4337 Documentation

This repository contains the official documentation for ERC-4337 (Account Abstraction).

## 🚀 Quick Start

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eth-infinitism/aa-mkdocs.git
   cd aa-mkdocs
   ```

2. **Set up Python virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Serve locally:**
   ```bash
   mkdocs serve
   ```
   
   Open http://127.0.0.1:8000 in your browser.

### Building

To build the static site:

```bash
mkdocs build
```

The built site will be in the `site/` directory.

## 🏗️ Build & Deploy

This documentation is automatically built and deployed using:

- **Cloudflare Pages** for hosting
- **GitHub Actions** for CI/CD
- **MkDocs Material** for the documentation framework

### Cloudflare Pages Settings

- **Build command:** `pip install -r requirements.txt && mkdocs build`
- **Output directory:** `site`
- **Python version:** 3.11
- **PR Previews:** Enabled (automatic preview deployments for pull requests)

### CI/CD

The repository includes GitHub Actions workflow (`.github/workflows/mkdocs-ci.yml`) that:
- Runs on every pull request to `main`
- Installs dependencies
- Builds the documentation with strict mode
- Blocks PRs if build fails

## 🤝 Contributing

### Development Workflow

1. **Fork the repository** and create a feature branch
2. **Make your changes** to the documentation
3. **Test locally** with `mkdocs serve`
4. **Create a pull request** - this will trigger:
   - CI build validation
   - Cloudflare Pages preview deployment
5. **Review and merge** - changes will be automatically deployed to production

### Guidelines

- **No web editor** - all changes must be made via pull requests
- **Test locally** before submitting PRs
- **Follow Markdown best practices**
- **Update navigation** in `mkdocs.yml` if adding new sections
- **Use descriptive commit messages**

## 🔗 Links

- **Production site:** https://docs.erc4337.io
- **Repository:** https://github.com/eth-infinitism/aa-mkdocs
- **Issues:** https://github.com/eth-infinitism/aa-mkdocs/issues


## 🛠️ Technology Stack

- **MkDocs** - Static site generator
- **Material for MkDocs** - Theme and features
- **Python 3.11** - Runtime environment
- **Cloudflare Pages** - Hosting and CDN
- **GitHub Actions** - CI/CD pipeline

---

[![Build Status](https://github.com/eth-infinitism/aa-mkdocs/workflows/Build%20Docs/badge.svg)](https://github.com/eth-infinitism/aa-mkdocs/actions)

