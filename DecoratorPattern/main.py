from models.content import Content
from models.output_type import Output_type

b = Content("this is fun")
print(b.export_content())
print(Output_type.to_json(b.export_content()))
print(b.export_content_decorater())
