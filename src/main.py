"""Main application entry point for GeoSpy"""
import uvicorn
from fastapi import FastAPI
from src.api import routes
from src.config import settings

app = FastAPI(title="GeoSpy API", version="2.1.0")
app.include_router(routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
// Update 12 Jan 2026 13:51:56
// Update 12 Jan 2026 13:51:56
// Update 12 Jan 2026 13:51:57
// Update 12 Jan 2026 13:51:57
// Update 12 Jan 2026 13:51:58
// Update 12 Jan 2026 13:51:58
// Update 12 Jan 2026 13:51:58
// Update 12 Jan 2026 13:51:59
// Update 12 Jan 2026 13:51:59
// Update 12 Jan 2026 13:52:00
// Update 12 Jan 2026 13:52:00
// Update 12 Jan 2026 13:52:00
// Update 12 Jan 2026 13:52:01
// Update 12 Jan 2026 13:52:01
// Update 12 Jan 2026 13:52:02
// Update 12 Jan 2026 13:52:02
// Update 12 Jan 2026 13:52:02
// Update 12 Jan 2026 13:52:03
// Update 12 Jan 2026 13:52:03
// Update 12 Jan 2026 13:52:04
# Modified 2024-07-03
# Modified 2025-06-18
# Modified 2025-06-24
# Modified 2025-07-02
# Modified 2025-06-12
# Modified 2025-08-22
# Modified 2022-08-28
# Modified 2023-02-12
# Modified 2023-06-02
# Modified 2024-05-29
# Modified 2024-09-17
