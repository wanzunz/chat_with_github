import os

from langchain_core.tools import BaseTool, tool
import requests

# GitHub GraphQL API URL
GITHUB_API_URL = "https://api.github.com/graphql"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def call_github_graphql(graphql: str) -> str:
    """这是可以执行github GrahpQL open api 的工具。使用前尽量先使用文档查询工具,并且尽量返回字段带上id以便于后续操作
    Args:

        graphql: 具体的语句
    Returns:
        str: 执行执行结果
    """
    try:
        # 设置请求头，包括授权信息
        headers = {
            "Content-Type": "application/json"
        }
        if GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
        # 发起 POST 请求
        response = requests.post(GITHUB_API_URL, headers=headers, json={'query': graphql})

        # 检查响应状态
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"request failed: {response.status_code} - {response.text}")
    except Exception as e:
        return f'{e}.'


github_tool: BaseTool = tool(call_github_graphql)
github_tool.name = "github_tool"
