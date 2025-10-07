from fastapi import APIRouter
from services.db_service import get_db

router = APIRouter(prefix="/data", tags=["data"])

@router.get("/test")
def test_db_connection():
    db = get_db()
    collections = db.list_collection_names()
    return {"status": "success", "collections": collections}