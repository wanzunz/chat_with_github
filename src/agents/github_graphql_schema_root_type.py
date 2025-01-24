from langchain_core.tools import BaseTool, tool
from graphql import build_schema, OperationType
from graphql.utilities import print_schema, print_value, print_introspection_schema, print_type  

with open('schema.docs.graphql', 'r', encoding='utf-8') as f:
    schema_content = f.read()

schema = build_schema(schema_content)
text = print_schema(schema)

query_type = schema.query_type


def type_root_docs2(type_name: str):
    """这是可以查询github GrahpQL schema 中 root type的工具，你需要提供root type 类型只有两个选择：QUERY/MUTATION
Args:
    type_name: root type 类型QUERY或者MUTATION
Returns:
    str: 文档内容
"""
    graphql_type = schema.get_root_type(OperationType[type_name])
    doc_str = (f"# Type Name: {graphql_type.name}\n")
    if hasattr(graphql_type, 'description') and graphql_type.description:
        doc_str += (f"Description: {graphql_type.description}\n")
    else:
        doc_str += ("No description provided.\n")

    if hasattr(graphql_type, 'fields'):
        doc_str += ("## Fields:\n")
        for field_name, field in graphql_type.fields.items():
            field_description = getattr(field, 'description', "No description\n\n")
            doc_str += (f"### {field_name} \n ```markdown\n{field_description}\n```\n ")
    return doc_str


GrahpQL_doc_root_type_tool: BaseTool = tool(type_root_docs2)
GrahpQL_doc_root_type_tool.name = "GrahpQL_doc_root_type"
