import logging.config

from fastapi import FastAPI, Request, responses, status
from fastapi.exceptions import HTTPException
from utils import configure_logging, is_valid

configure_logging()
log = logging.getLogger("direktor")
app = FastAPI()


@app.get("/health")
async def health_check():
    return {"healthy": True}


@app.get("/{path:path}")
async def oauth_redirect(request: Request, path: str, state: str = ""):
    target_domain, _, _ = state.partition("|")
    path = f"/{path}"
    if not is_valid(target_domain, path):
        log.info("unauthorized domain=%s path=%s", target_domain, path)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    full_url = f"https://{target_domain}{path}"
    return responses.RedirectResponse(full_url, status_code=302)


@app.exception_handler(Exception)
async def exception(request: Request, exc: Exception):
    log.exception(exc)
    return responses.JSONResponse(
        status_code=500, content={"message": "An error occurred. Please try again later."}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9050)
