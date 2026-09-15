## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone git@github.com:AbdelatefOsama/Cybersecurity_Toolkit.git
cd Cybersecurity_Toolkit
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Verify the Installation

```bash
python -c "import cryptography; import argon2; import Crypto; import bcrypt; print('All required packages installed successfully!')"
```

If the installation is successful, you should see:

```text
All required packages installed successfully!
```

### 7. Run the Toolkit

```bash
python main.py
```

---

## 📦 Dependencies

The project uses the following Python packages:

* `cryptography` — Cryptographic operations
* `argon2-cffi` — Argon2 password hashing
* `pycryptodome` — Cryptographic algorithms and utilities
* `bcrypt` — Bcrypt password hashing
