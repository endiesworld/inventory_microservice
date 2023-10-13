from typing import Callable

from fastapi import FastAPI


def mount(app: FastAPI) -> Callable:
    async def start_app() -> None:
        from app.routes import home_page
        # from payment_services.app.routes import payment
        
        # from app.routes.requester import auth_route as requester_auth_route
        
        

        app.include_router( home_page.router )
        # app.include_router( payment.router )
        

    return start_app
