from .output_type import Output_type  

class Content():
    def __init__(self,content):
        self._content = content
    def export_content(self):
        return self._content

    @Output_type.to_json_decorator
    def export_content_decorater(self):
        return self._content
