# LABFAT

Below is an example of a GitHub Actions workflow that implements a CI/CD pipeline for your Python script. This workflow will run on a push to the `main` branch, install dependencies using `pip`, and run `pylint` for code quality checks.

```yaml name=.github/workflows/python-ci.yml
name: Python CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout the repository
      - name: Checkout code
        uses: actions/checkout@v3

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      # Step 4: Run pylint
      - name: Lint with pylint
        run: |
          pip install pylint
          pylint **/*.py
```

### Explanation:
1. **Trigger (`on`)**:
   - The workflow is triggered on a push to the `main` branch.

2. **Job (`lint`)**:
   - The job runs on the latest Ubuntu environment (`ubuntu-latest`).

3. **Steps**:
   - **Checkout code**: Uses the `actions/checkout` action to clone the repository.
   - **Set up Python**: Configures the Python environment with `actions/setup-python`.
   - **Install dependencies**: Installs Python dependencies from `requirements.txt`, if it exists.
   - **Run pylint**: Installs `pylint` and then runs it on all Python files in the repository using the glob pattern `**/*.py`.

4. **Linting**:
   - The `pylint` tool checks the code quality of Python scripts.

This workflow ensures that every push to `main` maintains code quality and that dependencies are installed correctly. Let me know if you need further adjustments or additional features!







Here is the complete code for implementing the CI/CD pipeline for your Python script using GitHub Actions.

````yaml name=.github/workflows/python-ci.yml
name: Python CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout the repository
      - name: Checkout code
        uses: actions/checkout@v3

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      # Step 4: Run pylint
      - name: Lint with pylint
        run: |
          pip install pylint
          pylint **/*.py
````

### File Structure
Ensure your project repository has the following structure:
```
project-root/
├── .github/
│   └── workflows/
│       └── python-ci.yml  # The workflow file
├── script.py              # Your Python script
└── requirements.txt       # Your dependencies (if any)
```

### Example `requirements.txt`
If your project has dependencies, list them in the `requirements.txt` file. For example:
````plaintext name=requirements.txt
pylint
requests
````

### Example `script.py`
Here’s a simple Python script to demonstrate:
````python name=script.py
import requests

def main():
    response = requests.get("https://api.github.com")
    print(response.json())

if __name__ == "__main__":
    main()
````

This setup will:
1. Trigger the CI pipeline on every push to the `main` branch.
2. Install the dependencies listed in `requirements.txt`.
3. Run `pylint` on all `.py` files to ensure code quality.
