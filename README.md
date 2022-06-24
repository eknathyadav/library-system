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

![main](https://user-images.githubusercontent.com/48616375/175518911-3ceb0167-827b-4a92-97cf-b5198e716840.PNG)

![addbook](https://user-images.githubusercontent.com/48616375/175518959-a2bc64ff-281c-4e3a-87d4-f5692d181507.PNG)

![bookedit](https://user-images.githubusercontent.com/48616375/175518970-c5873b55-a309-41e9-b371-386a5957f8af.PNG)


