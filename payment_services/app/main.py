import uuid

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# USE THIS PIECE TO CONNECT TO AN EXTERNAL DATABASE
from app.core import (
    create_start_app_handler,
    create_redis_refund_consumer
    # create_stop_app_handler,
)


from app.core.global_config import app_config
from app.logger import setup_logging

from app.models.exceptions.crud_exception import (
    BadRequestError,
    InvalidStateError,
    DuplicateAccountError,
    DuplicateAccountException,
    DuplicateDataError,
    DuplicateDataException,
    InvalidUserAccountStateException,
    MissingParametersException,
    NotFoundError,
    NotFoundException,
)

from app.modules import application_module

global consumer

app = FastAPI(
    title="Payment API",
    version=app_config.API_VERSION,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inject Request Ids
@app.middleware("http")
async def request_middleware(request: Request, call_next):
    request.state.request_id = uuid.uuid4().hex
    request.state.request_ip = request.client.host
    request.state.request_method = request.method
    # add record here.!
    response = await call_next(request)
    return response


@app.exception_handler(DuplicateAccountException)
async def duplicate_account_exception(request: Request, exc: DuplicateAccountException):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=jsonable_encoder(
            DuplicateAccountError(
                current_record_id=exc.current_record_id,
                code=exc.error_code,
                message=exc.message,
            )
        ),
    )


@app.exception_handler(DuplicateDataException)
async def duplicate_data_exception(request: Request, exc: DuplicateDataException):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=jsonable_encoder(
            DuplicateDataError(
                current_record_id=exc.current_record_id,
                code=exc.error_code,
                message=exc.message,
            )
        ),
    )


@app.exception_handler(NotFoundException)
async def not_found_exception(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder(
            NotFoundError(
                code=exc.error_code,
                message=exc.message,
                details=exc.details,
            )
        ),
    )


@app.exception_handler(MissingParametersException)
async def missing_parameters_exception(
    request: Request, exc: MissingParametersException
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            BadRequestError(
                code=exc.error_code,
                message=exc.message,
                details=exc.details,
            )
        ),
    )


@app.exception_handler(InvalidUserAccountStateException)
async def invalid_account_user_state_exception(
    request: Request, exc: InvalidUserAccountStateException
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=jsonable_encoder(
            InvalidStateError(
                code=exc.error_code,
                message=exc.message,
            )
        ),
    )


app.add_event_handler("startup", setup_logging)

# Database Connection
app.add_event_handler("startup", create_start_app_handler(app))
# app.add_event_handler("shutdown", create_stop_app_handler(app))

app.add_event_handler("startup", create_redis_refund_consumer)

app.add_event_handler("startup", application_module.mount(app))
