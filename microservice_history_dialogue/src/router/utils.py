from uuid import UUID


async def replace_uuid(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, UUID):
                data[key] = str(value)
            else:
                data[key] = replace_uuid(value)
    elif isinstance(data, list):
        for item in data:
            replace_uuid(item)
    return await data
