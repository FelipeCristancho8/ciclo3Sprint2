from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
async def user():
    return {"message": "Rutas para usuarios"}