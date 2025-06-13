# hackathon-agentic-ai-semantic-kernel
Hack project to play with Agentic AI using Semantic kernel

The source data is gathered from 9 different relation tables and combined to a single json input. 
Data is structured as below;
- Titles
- Amendments
- Details
- POs
    - EOs
        - Teaching Points
    - Tasks
- References

## Setup Instructions

1. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

Note: For trusted network: pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org semantic-kernel