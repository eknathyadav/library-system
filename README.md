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
   git clone https://github.com/eknathyadav/library-system.git
   ```
2. Install Django framework.
   ```
   pip install django
   ```
3. Access the library-system folder.
4. Run the server.
   ```
   python manage.py runserver
   ```
5. Copy http://127.0.0.1:8000/ and paste it on your browser.

## Screenshots
    ```
    ![main](https://user-images.githubusercontent.com/48616375/175518649-5361b057-58d2-4507-bcb7-5926a68888f1.PNG)
    ```
    ```
    ![addbook](https://user-images.githubusercontent.com/48616375/175518665-a0da7de0-38dd-4939-a413-5cfba0164d4a.PNG)
    ```
    ```
    ![bookedit](https://user-images.githubusercontent.com/48616375/175518691-828713c3-3cc3-4ba3-97c9-63da8a6dbe4b.PNG)
    ```




