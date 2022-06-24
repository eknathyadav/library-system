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

1. ![main](https://user-images.githubusercontent.com/48616375/175518291-d5320ddd-91d1-4e40-b974-d2233acd6e7c.PNG)

2. ![addbook](https://user-images.githubusercontent.com/48616375/175518322-cbfd2020-2f89-40bf-b31e-73f40e433cb1.PNG)

3. ![bookedit](https://user-images.githubusercontent.com/48616375/175518355-11b10945-7c8b-43d6-bd45-9cf2e1218e05.PNG)




