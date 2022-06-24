# library-system
Library System

## API endpoints
1. '/api/books/' : OPTIONS['GET','POST']

    ```
    GET: to get all the book records
    POST: to add new book records
    ```
    
2. '/api/book/<book_id>/' : OPTIONS['GET','PATCH','DELETE']

    ```
    GET: to get record of a particular book based on book_id
    PATCH: to update any book record based on book_id
    DELETE: to delete any book record based on book_id
    ```

## Installation
1. Clone the project.
   ```
   git clone https://github.com/eknathyadav/Study-room.git
   ```
2. Install Django framework.
   ```
   pip install django
   ```
3. Access the Study-room folder.
4. Run the server.
   ```
   python manage.py runserver
   ```
5. Copy http://127.0.0.1:8000/ and paste it on your browser.


