from typing import Optional
import uvicorn as uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI()
contacts = []


class Contact(BaseModel):
    name: str
    mobile: str
    description: Optional[str] = None


class User(BaseModel):
    username: str
    display_name: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
def decode_token(token: str = Depends(oauth2_scheme)):
    return User(username=token + 'decoded', display_name='test')

def get_current_user(token: str = Depends(oauth2_scheme)):
    user = decode_token(token)
    return user

@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.password != '123':
        raise HTTPException(status_code=400, detail='Incorrect username of password')
    return {'access_token': form_data.username, 'token_type': 'bearer'}

@app.post('/contact/')
def create_contact(contact: Contact):
    contacts.append(contact)
    return "Contact was created"


@app.get('/contacts/')
def read_contacts(current_user: User = Depends(get_current_user)):
    return contacts


@app.get('/users/me')
def read_contacts(current_user: User = Depends(get_current_user)):
    user = current_user
    return user


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)