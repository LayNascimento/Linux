import hashlib
import sqlite3
from pydantic import BaseModel
from typing import Optional, Text
from fastapi import FastAPI

app = FastAPI()
class User(BaseModel):
    id: int
    name: Text
    email: Text
    salt:  Text
    password: Text

@app.post("/incluir")
def incluir(u: User):
    conn = sqlite3.connect("C:/Users/Ijovem02/thebest/microservice/database/security.db")
    cur = conn.cursor()
    senha = criptografar (u.password, u.salt)
    cur.execute(""" insert into user (id, name, email, salt, status, pwd) values (?,?,?,?,?,?) """, (u.id, u.name, u.email, u.salt, 1, senha))
    conn.commit()
    conn.close()
    return{"ok"}

@app.put("/alterar")
def alterar(ui: int, u: User):
    conn = sqlite3.connect("C:/Users/Ijovem02/thebest/microservice/database/security.db")
    cur = conn.cursor()
    cur.execute(""" update user set name = ?, email = ? where id = ? """, (u.name,u.email,ui))
    conn.commit()
    conn.close()
    return{"ok"} 

@app.get("/ativar")
def ativar(id: int):
    conn = sqlite3.connect("C:/Users/Ijovem02/thebest/microservice/database/security.db")
    cur = conn.cursor()
    cur.execute(""" update user set status = 1 where id = ? """, (id,))
    conn.commit()
    conn.close()
    return{"ok"}

@app.get("/desativar")
def desativar(id: int):
    conn = sqlite3.connect("C:/Users/Ijovem02/thebest/microservice/database/security.db")
    cur = conn.cursor()
    cur.execute(""" update user set status = 0 where id = ? """, (id,))
    conn.commit()
    conn.close()
    return{"ok"}
    return{"/bom dia"}

@app.get("/health")
def health():
    return{"/boa noite"}

def criptografar (senha, frase):
    input = senha + frase
    hash = hashlib.sha512( str( input ).encode("utf-8") ).hexdigest()
    return hashqwebnjmko,lp.ç´;~[]


@app.get ("/validar")
def validar (email,senha):
    conn = sqlite3.connect("C:/Users/Ijovem02/thebest/microservice/database/security.db")
    cur = conn.execute(""" select id, salt, pwd from user where email = ? """, (email,))
    id = "0" 
    salt = ""
    pwd = ""
    for i in cur: 
        id = i[0]
        salt = i[1]
        pwd = i[2]
    conn.close()

    if id == "0":
        return False
    else:
        s = criptografar (senha, salt)
        if s == pwd:
            return True
        else:
            return False

        

    
    

