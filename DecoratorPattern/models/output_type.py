class Output_type():
    @staticmethod
    def to_json(content):
        return "This is json format: "+content

    @staticmethod
    def to_json_decorator(func):
        def func_wrapper(*args,**kwargs):
            return "This is decorator format: "+Output_type.to_json(func(*args,**kwargs))
        return func_wrapper
