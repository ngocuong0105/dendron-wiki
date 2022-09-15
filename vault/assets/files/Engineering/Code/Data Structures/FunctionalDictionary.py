def make_dict():
    container = []
    def get_item(key):
        for k,v in container:
            if k == key:
                return v
        return -1

    def set_item(key,val):
        for i in range(len(container)):
            if container[i][0] == key:
                container[i][1] = val
                return
        container.append((key,val))

    def dispatch(message,key=None,val=None):
        if message == 'get_item':
            return get_item(key)
        elif message == 'set_item':
            set_item(key,val)
        elif message == 'keys':
            return tuple(key for key,_ in container)
        elif message == 'values':
            return tuple(val for _,val in container)
        elif message == 'items':
            return tuple((key,val) for key,val in container)

    return dispatch