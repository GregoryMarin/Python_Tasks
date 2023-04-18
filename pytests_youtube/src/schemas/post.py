POST_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'tytle': {'type': 'string', 'enum': ['POST']}
    },
    'required': ["id"]
}




# {'id': 1, 'title': 'Post 1'}