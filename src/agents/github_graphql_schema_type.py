from langchain_core.tools import BaseTool, tool
from graphql import build_schema, OperationType
from graphql.utilities import print_schema, print_value, print_introspection_schema, print_type


with open('schema.docs.graphql', 'r', encoding='utf-8') as f:
    schema_content = f.read()

schema = build_schema(schema_content)
text = print_schema(schema)

query_type = schema.query_type


def type_root_docs2(type_name: str):
    """这是可以查询github GrahpQL schema 某个type具体文档的工具，你需要提供type_name
Args:
    type_name: 字段类型比如 `SecurityAdvisoryConnection`
Returns:
    str: 文档内容
"""
    type_1 = schema.get_type(type_name)
    return print_type(type_1)


GrahpQL_doc_type_tool: BaseTool = tool(type_root_docs2)
GrahpQL_doc_type_tool.name = "GrahpQL_doc_type"
