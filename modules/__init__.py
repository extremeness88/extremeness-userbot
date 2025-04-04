def owner_only(func):
    async def wrapper(event):
        if event.sender_id != event.client.owner_id:
            return
        await func(event)
    return wrapper
