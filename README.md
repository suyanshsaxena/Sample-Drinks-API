# 🥤 Sample Drinks API

## 📖 Overview

This project is a **Flask-based REST API** for managing drinks. It demonstrates basic **CRUD operations** (Create, Read, Update, Delete) using **SQLite + SQLAlchemy**.

The API allows you to:

* ✅ List all drinks
* ✅ Retrieve a single drink by ID
* ✅ Add a new drink
* ✅ Update (patch) a drink
* ✅ Delete a drink

This is a beginner-friendly example of building REST APIs with Flask.

---

## ⚙️ Tech Stack

* **Flask** – Python web framework
* **Flask-SQLAlchemy** – ORM for database interactions
* **SQLite** – Lightweight relational database

---

## 📂 Project Structure

```
├── app.py           # Main Flask application
├── instance
|   ├──data.db         # SQLite database (auto-created on first run)
├── requirement.txt    # Python dependencies
└── README.md          # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/sample-drinks-api.git
cd sample-drinks-api
```

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirement.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

The API will be available at **`http://127.0.0.1:5000/`**

---

## 📊 API Endpoints

| Method | Endpoint       | Description              | Example Body (JSON)                                   |
| ------ | -------------- | ------------------------ | ----------------------------------------------------- |
| GET    | `/`            | Hello test route         | -                                                     |
| GET    | `/drinks`      | Get all drinks           | -                                                     |
| GET    | `/drinks/<id>` | Get a drink by ID        | -                                                     |
| POST   | `/drinks`      | Add a new drink          | `{"name": "Cola", "description": "Sweet soft drink"}` |
| PATCH  | `/drinks/<id>` | Update a drink (partial) | `{"name": "Diet Cola"}`                               |
| DELETE | `/drinks/<id>` | Delete a drink           | -                                                     |

---

## 🧪 Testing with Postman

You can test the API easily using **Postman**:

1. **Base URL:**

   ```
   http://127.0.0.1:5000
   ```

2. **Endpoints to Test:**

   * **Get All Drinks**

     * Method: `GET`
     * URL: `http://127.0.0.1:5000/drinks`

   * **Get a Single Drink**

     * Method: `GET`
     * URL: `http://127.0.0.1:5000/drinks/1`

   * **Add a Drink**

     * Method: `POST`
     * URL: `http://127.0.0.1:5000/drinks`
     * Body (JSON):

       ```json
       {
         "name": "Cola",
         "description": "Sweet soft drink"
       }
       ```

   * **Update a Drink**

     * Method: `PATCH`
     * URL: `http://127.0.0.1:5000/drinks/1`
     * Body (JSON):

       ```json
       {
         "description": "Zero sugar Cola"
       }
       ```

   * **Delete a Drink**

     * Method: `DELETE`
     * URL: `http://127.0.0.1:5000/drinks/1`


