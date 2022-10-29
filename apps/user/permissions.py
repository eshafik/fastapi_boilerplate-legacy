from fastapi import Header, HTTPException


async def check_permission(x_token: str = Header()):
    # if token != "jessica":
    #     raise HTTPException(status_code=400, detail="No Jessica token provided")
    pass


async def get_query_token(token: str = Header()):
    # if token != "jessica":
    #     raise HTTPException(status_code=400, detail="No Jessica token provided")
    pass
