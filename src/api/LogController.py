from fastapi import APIRouter, Query, HTTPException
from application.Log.queries.GetAllLogsQuery import GetAllLogsQuery
from application.Log.commands.DeleteLogsCommand import DeleteLogsCommand
from datetime import datetime

router = APIRouter(prefix="/logs", tags=["Logs"])

@router.get("/")
def get_all_logs(limit: int = Query(default=100, le=1000)):
    query = GetAllLogsQuery()
    logs = query.execute(limit)
    for log in logs:
        log["_id"] = str(log["_id"])
    return logs

@router.delete("/")
def delete_logs(older_than: str = Query(default=None, description="Formato ISO 8601: YYYY-MM-DDTHH:MM:SS")):
    command = DeleteLogsCommand()

    if older_than:
        try:
            # Tenta converter a string em datetime para validar o formato ISO
            datetime.fromisoformat(older_than)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Parâmetro 'older_than' inválido. Use o formato ISO 8601: YYYY-MM-DDTHH:MM:SS"
            )
        deleted = command.delete_older_than(older_than)
    else:
        deleted = command.delete_all()

    return {"deleted": deleted}
