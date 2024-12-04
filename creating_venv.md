   If your project folder structure looks like this:
   ```
   /project/
       ├── src/
       ├── venv/
       ├── requirements.txt
   ```
   Then run the commands from the `/project` folder, **not inside `venv`**.


**To set up your virtual environment (`venv`) and `requirements.txt`, follow these steps:**

---

### **1. Setting Up the Virtual Environment**
Run the following commands to create and activate a virtual environment:

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

---

### **2. Installing Dependencies**
Install the required packages for your project:

1. **Flask**: A micro web framework for building APIs.
2. **sqlite3**: Python's built-in library for database operations (no installation required).
3. **Flask-CORS** (optional): To handle cross-origin requests if the API is accessed from a frontend running on a different domain.
4. **Any other libraries needed for your additional logic** (not necessary based on your shared code but can be extended later).

Run this command to install Flask and Flask-CORS:
```bash
pip install Flask Flask-CORS
```

---

### **3. Creating `requirements.txt`**
Generate the file automatically by running:
```bash
pip freeze > requirements.txt
```

Your `requirements.txt` should look similar to this:
```
Flask==2.3.2
Flask-Cors==3.0.10
```

If any additional libraries are added in the future, regenerate the file using `pip freeze > requirements.txt`.

---

### **4. Running the Project**
1. Activate the virtual environment (`source venv/bin/activate` or `venv\Scripts\activate`).
2. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python src/app.py
   ```

