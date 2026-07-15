from sqlalchemy.orm import Session
from app import models
from app.weather_service import fetch_weather


def create_search(db: Session, location_query: str) -> models.SearchHistory:
    weather_result = fetch_weather(location_query)

    db_entry = models.SearchHistory(
        location_query=location_query,
        resolved_location=weather_result["resolved_location"],
        weather_data={
            "current": weather_result["current"],
            "forecast": weather_result["forecast"],
        },
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


def get_all_searches(db: Session):
    return db.query(models.SearchHistory).order_by(models.SearchHistory.created_at.desc()).all()


def get_search(db: Session, search_id: int):
    return db.query(models.SearchHistory).filter(models.SearchHistory.id == search_id).first()


def update_search(db: Session, search_id: int, new_location_query: str | None):
    db_entry = get_search(db, search_id)
    if not db_entry:
        return None

    query_to_use = new_location_query if new_location_query else db_entry.location_query
    weather_result = fetch_weather(query_to_use)

    db_entry.location_query = query_to_use
    db_entry.resolved_location = weather_result["resolved_location"]
    db_entry.weather_data = {
        "current": weather_result["current"],
        "forecast": weather_result["forecast"],
    }
    db.commit()
    db.refresh(db_entry)
    return db_entry


def delete_search(db: Session, search_id: int) -> bool:
    db_entry = get_search(db, search_id)
    if not db_entry:
        return False
    db.delete(db_entry)
    db.commit()
    return True