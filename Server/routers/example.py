from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def func1():
    path = Path(r'C:\Users\Isaìas\Desktop\Scripy\FastAPI Model\static\index.html')
    return path.read_text()

@router.post("/path", response_class=HTMLResponse)
def func2():
    ...

@router.delete("/path", response_class=HTMLResponse)
def func3():
    ...

@router.websocket("/path")
def func4():
    ...