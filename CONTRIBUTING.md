# Contributing to PDF Watermark API

Thank you for considering contributing to **PDF Watermark API**.
Contributions of all kinds are welcome — whether it is fixing a bug, adding a feature, improving the documentation, or sharing feedback.

This document outlines the guidelines and workflow to ensure smooth collaboration.

---

## 🛠 Contribution Areas

You can contribute in the following ways:

* Fixing bugs and issues
* Implementing new features
* Improving code readability and maintainability
* Enhancing test coverage
* Improving documentation and examples
* Reporting issues or suggesting improvements

---

## ⚡ Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/vasantharan/PDF_Watermark_API.git
   cd PDF_Watermark_API
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python main.py
   ```

The server should now be running at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Workflow

1. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature
   ```

2. **Implement your changes**

   * Follow [PEP8](https://peps.python.org/pep-0008/) coding style.
   * Write clear, maintainable, and well-documented code.
   * Add tests where appropriate.

3. **Commit changes**
   Use conventional commit messages to maintain a clean history:

   ```
   feat: add support for custom watermark color
   fix: resolve crash when pdf_file is missing
   docs: update usage examples
   ```

4. **Push and open a Pull Request (PR)**

   ```bash
   git push origin feature/your-feature
   ```

   In your PR description, please include:

   * A summary of the changes
   * The motivation or issue reference
   * Any additional notes for review

---

## ✅ Pull Request Guidelines

* Keep each PR focused on a single feature or fix.
* Ensure existing functionality is not broken.
* Update relevant documentation if your changes affect usage.
* Be respectful and constructive during code reviews.

---

## 🐞 Reporting Issues

When reporting issues, please include:

* A clear and descriptive title
* Steps to reproduce the problem
* Expected vs actual behavior
* Logs, screenshots, or code snippets if possible

---

## 🤝 Final Note

This project values contributions of all sizes. Your effort — whether small or large — helps improve the project and benefits the community.

Thank you for taking the time to contribute.

---
