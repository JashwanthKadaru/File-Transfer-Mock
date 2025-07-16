# File Transfer API

This project is a Django REST API system for transferring and revoking file ownership between users, with full audit history.

## Features
- File upload and ownership management
- Transfer file ownership between users
- Revoke file transfers (return ownership to original owner)
- All actions logged in transfer history

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install django djangorestframework
   ```
3. Run migrations:
   ```powershell
   python manage.py migrate
   ```
4. Create a superuser:
   ```powershell
   python manage.py createsuperuser
   ```
5. Start the server:
   ```powershell
   python manage.py runserver
   ```

## API Endpoints & Usage

### 1. Upload File
- **POST** `/api/files/`
- **Body (form-data):**
  - `name`: string (file name)
  - `file`: file (upload)
- **Auth:** Basic Auth (username & password)
- **Response:** File details (including `id`)

### 2. List Files
- **GET** `/api/files/`
- **Auth:** Basic Auth
- **Response:** List of files

### 3. Transfer File Ownership
- **POST** `/api/transfer/`
- **Body (JSON):**
  ```json
  { "file_id": <file id>, "to_user_id": <user id> }
  ```
- **Auth:** Only current owner can transfer
- **Response:** Success message

### 4. Revoke File Transfer
- **POST** `/api/revoke/`
- **Body (JSON):**
  ```json
  { "file_id": <file id> }
  ```
- **Auth:** Only original owner can revoke
- **Response:** Success message

### 5. Transfer History
- **GET** `/api/history/`
- **Auth:** Basic Auth
- **Response:** List of all transfer/revoke actions

## Working Screenshots

Add screenshots for each stage below after testing with Postman:

### 1. Upload File (`/api/files/`)
- _Screenshot: File upload request and response_ 

(check images/Screenshot 2025-07-16 084910.png)

### 2. Transfer File Ownership (`/api/transfer/`)
- _Screenshot: Transfer request and response_

(check images/Screenshot 2025-07-16 085514.png)

### 3. Revoke File Transfer (`/api/revoke/`)
- _Screenshot: Revoke request and response_

(check images/Screenshot 2025-07-16 090155.png)

### 4. Transfer History (`/api/history/`)
- _Screenshot: History response_

(check images/Screenshot 2025-07-16 090220.png)

### 5. Django Admin (Database State)
- _Screenshot: Admin panel showing Users, Files, and TransferHistory_

(check images/Screenshot 2025-07-16 090611.png)

(check images/Screenshot 2025-07-16 090621.png)

---

## Notes
- All transfer actions are logged for audit purposes
- See code for model and endpoint details
