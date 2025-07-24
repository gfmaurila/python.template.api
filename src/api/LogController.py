from fastapi import APIRouter, Query, HTTPException
from application.Log.queries.GetAllLogsQuery import GetAllLogsQuery
from application.Log.commands.DeleteLogsCommand import DeleteLogsCommand
from datetime import datetime
from loguru import logger

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/")
def get_all_logs(limit: int = Query(default=100, le=1000)):
    query = GetAllLogsQuery()
    logs = query.execute(limit)
    logger.info(f"Ação: GET /logs - Retornando {len(logs)} logs (limite: {limit})")
    for log in logs:
        log["_id"] = str(log["_id"])
    return logs

@router.delete("/")
def delete_logs(older_than: str = Query(default=None, description="Formato ISO 8601: YYYY-MM-DDTHH:MM:SS")):
    command = DeleteLogsCommand()

    if older_than:
        try:
            datetime.fromisoformat(older_than)
        except ValueError:
            logger.warning(f"Ação: DELETE /logs - Parâmetro 'older_than' inválido: {older_than}")
            raise HTTPException(
                status_code=400,
                detail="Parâmetro 'older_than' inválido. Use o formato ISO 8601: YYYY-MM-DDTHH:MM:SS"
            )
        deleted = command.delete_older_than(older_than)
        logger.info(f"Ação: DELETE /logs - Apagados {deleted} logs anteriores a {older_than}")
    else:
        deleted = command.delete_all()
        logger.info(f"Ação: DELETE /logs - Apagados {deleted} logs (todos)")

    return {"deleted": deleted}
