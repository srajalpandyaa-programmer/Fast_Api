from fastapi import FastAPI, status, HTTPException, Request, Depends, Header, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# import os
# import shutil
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# # from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# # import sqlite3
# from sqlalchemy import create_engine,Column, Integer, String, Boolean
# from sqlalchemy.orm import declarative_base, sessionmaker, Session
# import time
# import asyncio
# from jose import jwt,JWTError
# from passlib.context import CryptContext
# from datetime import datetime, timedelta, timezone
# from dotenv import load_dotenv
# from config import settings
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)


@app.get("/news")
def get_news(page: int = 1,limit: int = 5):
    url = "https://indianexpress.com/"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    title = []
    for item in soup.find_all("a",class_ = "topblockNews__sidebarTitle"):
        title.append(item.text)

    #Pagination
    start = (page -1)* limit
    end = start + limit
    return {
        "page":page,
        "limit":limit,
        "total": len(title),
        "data":title[start:end]
    }









# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# print(data)

# # Get All Data
# @app.get("/posts")
# def get_posts():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#     return response.json()


# @app.get("/posts/{post_id}")
# def get_post(post_id:int):
#     url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()
#     return response.json()




# @app.get("/")
# def home():
#     return {"message": "Hello Srajal!"}


# @app.get("/add")
# def add(a: int, b: int):
#     return {"result": a + b}







# load_dotenv()
#Allowed Origins(Front-End URl)
# origins = settings.origins



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins, # Allow front end
#     allow_credentials= True,
#     allow_methods=["*"],#Get,put,post,delete
#     allow_headers=["*"]
# )


# @app.get("/")
# def home():
#     return{
#         "message":"Hello Srajal!"
#     }


# @app.get("/add")
# def add(a: int, b:int):
#     return{
#         "result": a + b
#     }


# app = FastAPI()


# #Step 1: Ensure Upload Folder Exist
# UPLOAD_DIR = "uploads"
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)


# #Step 2: Static File Setup
# app.mount("/files/",StaticFiles(directory=UPLOAD_DIR), name="files")


# #Step 3: Upload File API
# @app.post("/upload")
# def upload_file(file: UploadFile = File(...)):
#     filename = file.filename

#     if not filename:
#         raise HTTPException(status_code=400, detail="File not Selected")

#     filename = os.path.basename(filename)
#     file_path = os.path.join(UPLOAD_DIR,filename)

#     with open(file_path,"wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#         return{
#             "message": "File Uploaded Successfully",
#             "Filename":filename,
#             "File_Url": f"http://127.0.0.1:8000/files/{filename}"
#         }

# #Step 4: Get File URL API
# @app.get("/files/{filename}")
# def get_file(filename: str):
#     filename = os.path.basename(filename)
#     file_path = os.path.join(UPLOAD_DIR,filename)

#     if not os.path.exists(file_path):
#         raise HTTPException(status_code= 404,detail="File not Found" )

#     return{
#         "File_Url": f"http://127.0.0.1:8000/files/{filename}"
#     }


# @app.get("/")
# def home():
#     return{
#         "message":"File Uploaded Api Running."
#     }




# app = FastAPI()

# #JWT Config
# SECRET_KEY = "mysecret"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# #PASSWORD HASHING SETUP
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


# #Oauth Setup
# oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


# #Dummy user db
# fake_user_db = {

#     "admin":{
#         "username":"admin",
#         "hashed_password":pwd_context.hash("1234")
#     }

# }


# #Hash password
# def hash_password(password:str):
#     return pwd_context.hash(password)


# #verify password
# def verify_password(plain_password,hashed_password):
#     return pwd_context.verify(plain_password,hashed_password)


# # Create Token
# def create_token(data:dict):
#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + timedelta(minutes=60)
#     to_encode.update({
#         "exp":expire
#     })
#     token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

#     return token

# #Login API(OAuth2 form)
# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = fake_user_db.get(form_data.username)
#     if not user or not verify_password(form_data.password,user["hashed_password"]):
#         raise HTTPException(
#               status_code=400,
#               detail="Invalid Username and Password"
#           )
#     access_token = create_token({"sub":form_data.username})
#     return{
#         "access_token":access_token,
#         "token_type":"bearer"
#     }

# #token verification
# def token_verify(token: str = Depends(oauth2_schema)):
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(
#                         status_code=401,
#                         detail="Invalid or Expired Token"
#                     )
#         return username
#     except JWTError:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or Expired Token"
#         )



# #protected route
# @app.get("/protected")
# def protected_route(username: str = Depends(token_verify)):
#     return{
#         "message":"Hello you have access to this protected route!",
#         "user": username
#     }





# #Login API(Token Generate)
# @app.post("/login")
# def login(username:str,password:str):
#     if username != "admin" or password != "1234":
#         raise HTTPException(
#             status_code=404,
#             detail="Invalid Username and Password"
#         )

#     token = create_token({
#         "sub": username
#     })
#     return {
#         "access_toke":token
#     }

# #token verification
# def token_verify(token: str = Header(None)):

#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
#         return payload
#     except:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid or Expired Token"
#         )

# #protected route
# @app.get("/secure")
# def secure_data(user = Depends(token_verify)):
#     return{
#         "message":"Secure Data Accessed",
#         "user": user
#     }




# @app.get("/")
# async def home():
#     await asyncio.sleep(3)  # Simulate a time-consuming task
#     return {"message": "Hello World from FastAPI!"}




# async def async_task():
#     print("Starting async task...")
#     await asyncio.sleep(2)  # Simulate a time-consuming task
#     print("Async task completed!")


# DATABASE_URL = "sqlite:///./mydatabase16.db"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

# Base = declarative_base()

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )




# # 1. SQLAlchemy model: database table
# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     completed = Column(Boolean, default=False)


# # 2. Pydantic model: incoming request data
# class TodoCreate(BaseModel):
#     title: str
#     description: str
#     completed: bool = False


# Base.metadata.create_all(bind=engine)


# # 3. Database dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # 4. Create a todo
# @app.post("/todos")
# def create_todo(
#     todo: TodoCreate,
#     db: Session = Depends(get_db)
# ):
#     new_todo = Todo(
#         title=todo.title,
#         description=todo.description,
#         completed=todo.completed
#     )

#     db.add(new_todo)
#     db.commit()
#     db.refresh(new_todo)

#     return {
#         "message": "Todo created successfully",
#         "todo": {
#             "id": new_todo.id,
#             "title": new_todo.title,
#             "description": new_todo.description,
#             "completed": new_todo.completed
#         }
#     }



# @app.get("/todos")
# def read_todos(db: Session = Depends(get_db)):
#     todos = db.query(Todo).all()
#     return {
#         "total": len(todos),
#         "Data": todos
#     }

# @app.get("/todos/{todo_id}")
# def read_todo(todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(Todo).filter(Todo.id == todo_id).first()
#     if not todo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
#     return {
#         "todo": {
#             "id": todo.id,
#             "title": todo.title,
#             "description": todo.description,
#             "completed": todo.completed
#         }
#     }


# @app.put("/todos/{todo_id}")
# def update_todo(
#     todo_id: int,
#     updated_todo: TodoCreate,
#     db: Session = Depends(get_db)
# ):
#     todo = db.query(Todo).filter(Todo.id == todo_id).first()
#     if not todo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

#     todo.title = updated_todo.title
#     todo.description = updated_todo.description
#     todo.completed = updated_todo.completed

#     db.commit()
#     db.refresh(todo)

#     return {
#         "message": "Todo updated successfully",
#         "todo": {
#             "id": todo.id,
#             "title": todo.title,
#             "description": todo.description,
#             "completed": todo.completed
#         }
#     }


# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     todo = db.query(Todo).filter(Todo.id == todo_id).first()
#     if not todo:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

#     db.delete(todo)
#     db.commit()

#     return {
#         "message": "Todo deleted successfully",
#         "todo": {
#             "id": todo.id,
#             "title": todo.title,
#             "description": todo.description,
#             "completed": todo.completed
#         }
#     }




# DATABASE_URL = "sqlite:///./mydatabase56.db"
# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()


# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     completed = Column(String, default=False)


# Base.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/todos")
# def create_todo(todo: Todo, db: Session = Depends(get_db)):
#     todo = Todo(title=todo.title, completed=todo.completed)
#     db.add(todo)
#     db.commit()
#     db.refresh(todo)
#     return {"message": "Todo created successfully", "todo": todo}


# @app.get("/todos")
# def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     todos = db.query(Todo).offset(skip).limit(limit).all()
#     return todos    


# # Home Route
# @app.get("/")
# def home():
#     return {"message":"Hello world from FastAPI VENV"}

# # About Route
# @app.get("/about")
# def about():
#     return {"message":"This is a FastAPI application."} 

# # Users Route
# @app.get("/users")
# def users():
#     return {
#         "users": [
#         {"id": 1, "name": "John Doe"},  
#         {"id": 2, "name": "Jane Smith"},
#         {"id": 3, "name": "Alice Johnson"}
#     ]
#     }

# # Users Route
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     users = {
#         1: {"id": 1, "name": "John Doe"},
#         2: {"id": 2, "name": "Jane Smith"},
#         3: {"id": 3, "name": "Alice Johnson"}
#     }
#     user = users.get(user_id)
#     if user:
#         return user
#     else:
#         return {"error": "User not found"}


# @app.get("/users/")
# def get_users(name: str = None):
#     return {name: f"Hello, {name}!" if name else "Hello, World!"}

# @app.get("/products/")
# def get_products(limit: int = 10, offset: int = 0):
#     return {"limit": limit, "offset": offset}

# @app.post("/create-user")
# def create_user(name: str, age: int):
#     return {"name": name, "age": age}


# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/create-user")
# def create_user(user: User):
#     return {"Message": "User created successfully", "user": user}






# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# @app.post("/create-user")
# def create_user(user: User):
#     return {"message": "User created successfully", "user": user}







# class Address(BaseModel):
#     city: str
#     pincode: int

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     address: Address

# @app.post("/create-user")
# def create_user(user: User):
#     return {"message": "User created successfully", "user": user}



# todos = []

# class Todo(BaseModel):
#     id: int
#     title: str
#     description: str
#     completed: bool = False

# @app.post("/todos")
# def create_todo(todo: Todo):
#     todos.append(todo)
#     return {"message": "Todo created successfully", "todo": todo}

# @app.get("/todos")
# def get_todos():
#     return {"todos": todos}

# @app.get("/todos/{todo_id}")
# def get_todo(todo_id: int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return {"todo": todo}
#     return {"error": "Todo not found"}

# @app.put("/todos/{todo_id}")
# def update_todo(todo_id: int, updated_todo: Todo):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[index] = updated_todo
#             return {"message": "Todo updated successfully", "todo": updated_todo}
#     return {"error": "Todo not found"}

# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: int):  
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             deleted_todo = todos.pop(index)
#             return {"message": "Todo deleted successfully", "todo": deleted_todo}
#     return {"error": "Todo not found"}


# users = []
# class User(BaseModel):
#     name:str
#     age:int

# @app.post("/users")
# def create_user(user:User):
#     users.append(user)
#     return{
#         "message":"User Created.",
#         "data":user
#     }


# @app.put("/users/{user_id}")
# def update_user(user_id:int,user:User,notify:bool=False):
#     if user_id < len(users):
#         users[user_id] = user


#         return{
#             "message":"User Updated.",
#             "notify":notify,
#             "data":user
#         }

#     return{
#         "error":"User not Found"
#     }


# @app.post("/create_user", status_code=status.HTTP_201_CREATED)
# def create_user():
#     return {"message": "User created successfully"}


# @app.get("/users")
# def get_users():
#     return {
#         "Stauts": "Success",
#         "message": "Users retrieved successfully",
#         "data": [
#             {"id": 1, "name": "John Doe"},
#             {"id": 2, "name": "Jane Smith"},
#             {"id": 3, "name": "Alice Johnson"}
#         ]

#     }

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     users = {
#         1: {"id": 1, "name": "John Doe"},
#         2: {"id": 2, "name": "Jane Smith"},
#         3: {"id": 3, "name": "Alice Johnson"}
#     }
#     user = users.get(user_id)
#     if user:
#         return {
#             "Stauts": "Success",
#             "message": "User retrieved successfully",
#             "data": user
#         }
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found") 
    

# class UserNotFoundException(HTTPException):
#     def __init__(self, user_id: int):
#         super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")


# @app.exception_handler(UserNotFoundException)
# def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.detail}
#     )

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     users = {
#         1: {"id": 1, "name": "John Doe"},
#         2: {"id": 2, "name": "Jane Smith"},
#         3: {"id": 3, "name": "Alice Johnson"}
#     }
#     user = users.get(user_id)
#     if user:
#         return {
#             "Status": "Success",
#             "message": "User retrieved successfully",
#             "data": user
#         }
#     else:
#         raise UserNotFoundException(user_id)


# def common_logic():
#     # Common logic that can be reused in multiple routes
#     return {"message": "This is common logic"}  

# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data


# def get_current_user():
#     # Simulating user authentication
#     return {"id": 1, "name": "John Doe"}


# @app.get("/profile")
# def get_profile(current_user: dict = Depends(get_current_user)):
#     return {
#         "message": "User profile retrieved successfully",
#         "user": current_user
#     }

# @app.get("/dashboard")
# def get_dashboard(current_user: dict = Depends(get_current_user)):
#     return {
#         "message": "Dashboard data retrieved successfully",
#         "user": current_user
#     }



# def verify_token(x_token: str = Header(None)):
#     if x_token != "mysecrettoken":
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
#     return x_token


# @app.get("/secure-data")
# def get_secure_data(token: str = Depends(verify_token)):
#     return {
#         "message": "Secure data retrieved successfully",
#         "token": token
#     }


# @app.middleware("http")
# async def log_requests(request: Request, call_next):    
#     # Log the request details
#     print(f"Request: {request.method} {request.url}")

#     # Process the request and get the response
#     response = await call_next(request)

#     # Log the response details
#     print(f"Response: {response.status_code}")

#     return response

# @app.middleware("http")
# async def log_middleware(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     print(f"Request: {request.method} {request.url} completed in {process_time:.4f} seconds")
#     return response


# conn = sqlite3.connect('mydatabase.db', check_same_thread=False)
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL,
#                     completed Text
#                 )''')
# conn.commit()

# @app.get("/home")
# def home():
#     return {"message": "Sqlite database connection established successfully"}