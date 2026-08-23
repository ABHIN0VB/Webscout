from pydantic import BaseModel
from typing import Any

class AnalyticsResponse(BaseModel):
    total_runs: int
    successful_runs: int
    failed_runs: int
    healed_runs: int
    total_records: int
    records_recovered: int
    avg_recovery_time_seconds: float
    run_history: list[dict[str, Any]]
    healing_history: list[dict[str, Any]]
