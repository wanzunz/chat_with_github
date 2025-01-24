from langchain_core.tools import BaseTool, tool
from graphql import build_schema, OperationType
from graphql.utilities import print_schema, print_value, print_introspection_schema, print_type  


with open('schema.docs.graphql', 'r', encoding='utf-8') as f:
    schema_content = f.read()

schema = build_schema(schema_content)
text = print_schema(schema)

query_type = schema.query_type


def print_type_field(type_name: str, type_fields_name: str):
    """这是可以查询github GrahpQL schema 中 root type的工具，你需要提供root_type_name和type_fields_name
Args:
type_name: root type 类型`QUERY`或者`MUTATION`
type_fields_name: field 名称比如 `repository` 这个是根据root type文档来的
Returns:
str: 对应field的文档内容
"""
    object_type = schema.get_root_type(OperationType[type_name])
    if hasattr(object_type, "fields"):
        type_name_field = object_type.fields[type_fields_name]
        return print_type_field_docs(type_fields_name, type_name_field)
    else:
        print("没有fields字段")


def print_type_field_docs(name, field):
    doc_str = f"# {name}\n"
    if hasattr(field, 'description') and field.description:
        doc_str += f"{field.description}\n"
    else:
        doc_str += "No description provided."
    doc_str += "## Parameters \n"
    for arg_name, arg in field.args.items():
        doc_str += f"### `{arg_name}: {arg.type}`\n{arg.description}\n"

    doc_str += "## Return Type \n"
    # doc_str += f"### `{str(field.type)}`\n{field.type.of_type.description}\n"
    doc_str += f"### `{str(field.type)}`\n"
    return doc_str


GrahpQL_doc_field_tool: BaseTool = tool(print_type_field)
GrahpQL_doc_field_tool.name = "GrahpQL_doc_field"
