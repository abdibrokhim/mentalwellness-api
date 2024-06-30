# MeWellAI Backend Service (API)

`Note:` Make sure you have already checked MeWellAI app [here](https://github.com/abdibrokhim/mentalwellness). if you haven't, please check it first then come back here again.

## 🚀 Getting Started

### 📋 Pre-requisites

- 🛜 Internet
- 💻 Mac (kidding, any laptop)
* Python
* FastAPI


### 📦 Clone the repository

```bash
git clone https://github.com/abdibrokhim/mentalwellness-api
```

### 📂 Go to the project directory
```
cd mentalwellness-api
```

### 🌐 Create a virtual environment

```bash
python3 -m venv .venv
```

### 🔓 Activate the virtual environment

```bash
# Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate.bat
```

### 📚 Install dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Set environment variables

```bash
cp .env.example .env
```
`Note`: You need to set the environment variables in the `.env` file.

### 🏃‍♂️ Run the app

```bash
python3 api.py
```

### 🚀 Run with bash script
    
```bash
bash run.sh
```

### 👀 Run with gunicorn
    
```bash
gunicorn api:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80
```

Back to [README.md]() file.

## New to API development? 🙃
Check the [FASTAPI.md]() file for helpful resources on how to get started with Python and FastAPI.

## Contact 📨
Message me at [abdibrokhim@gmail.com](mailto:abdibrokhim@gmail.com) or [Contact](https://abdibrokhim.vercel.app/contact)