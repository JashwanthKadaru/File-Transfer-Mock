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

## API Endpoints
- `POST /api/transfer/` - Transfer file ownership
- `POST /api/revoke/` - Revoke a previous transfer

## Testing
- Use Postman to test API endpoints
- Upload files and perform transfer/revoke actions

## Notes
- All transfer actions are logged for audit purposes
- See code for model and endpoint details
