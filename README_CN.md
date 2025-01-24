# 🧰 Github AI Assistant


一个ai助手同时支持github中一系列的能力，比如查询/修改仓库、组织、Issue、PR等。理论上支持 [GitHub GraphQL API documentation](https://docs.github.com/en/graphql) 中的大部分能力。

项目源于对[JoshuaC215/agent-service-toolkit](https://github.com/JoshuaC215/agent-service-toolkit)的修改。 

一个完整的工具包，用于运行使用 LangGraph、FastAPI 和 Streamlit 构建的 AI 代理服务。

它包括一个 [LangGraph](https://langchain-ai.github.io/langgraph/) 代理、一个 [FastAPI](https://fastapi.tiangolo.com/) 服务来提供代理服务、一个与服务交互的客户端，以及一个使用客户端提供聊天界面的 [Streamlit](https://streamlit.io/) 应用程序。数据结构和设置使用 [Pydantic](https://github.com/pydantic/pydantic) 构建。

这个项目为您提供了一个模板，可以轻松构建和运行您自己的代理，使用 LangGraph 框架。 它展示了一个完整的设置，从代理定义到用户界面，通过提供一个完整、强大的工具包，使您更容易开始使用基于 LangGraph 的项目。


## 概述

<a href="https://agent-service-toolkit.streamlit.app/"><img src="media/app_screenshot.png" width="600"></a>


### 可以做哪些事情？
#### 例子1: 自动生成仓库描述并且修改它
![](media/zh/modify_description.png)
#### 例子2: 结合文档回复issue
![](media/zh/comment_issue.png)
#### 例子3: 查询仓库
![](media/zh/hot_repo.png)

### 更多

- 多种查询操作

![img.png](media/zh/query.png)


- 支持多种修改操作

![img.png](media/zh/mutation.png)

### 快速入门
直接在 python 中运行

```sh
# At least one LLM API key is required
echo 'GITHUB_TOKEN = your_github_token' >> .env
echo 'OPENAI_API_KEY=your_openai_api_key' >> .env

# uv is recommended but "pip install ." also works
pip install uv
uv sync --frozen
# "uv sync" creates .venv automatically
source .venv/bin/activate
python src/run_service.py

# In another shell
source .venv/bin/activate
streamlit run src/streamlit_app.py
```


使用 Docker 运行

```sh
echo 'GITHUB_TOKEN = your_github_token' >> .env
echo 'OPENAI_API_KEY=your_openai_api_key' >> .env
docker compose watch
```


### 架构图

<img src="media/agent_architecture.png" width="600">

### 主要特性
1. **LangGraph 代理**: 使用 LangGraph 框架构建的可定制代理。
2. **FastAPI 服务**: 通过流式和非流式端点提供代理服务。
3. **高级流式传输**: 一种新颖的方法，支持基于标记和基于消息的流式传输。
4. **内容审核**: 实现 LlamaGuard 进行内容审核（需要 Groq API 密钥）。
5. **Streamlit 界面**: 提供一个用户友好的聊天界面，用于与代理交互。
6. **支持多个代理**: 运行服务中的多个代理并通过 URL 路径调用它们
7. **异步设计**: 使用 async/await 有效处理并发请求。
8. **反馈机制**: 包含一个与 LangSmith 集成的基于星级的反馈系统。
9. **动态元数据**: `/info` 端点提供有关服务和可用代理和模型的动态配置元数据。
10. **Docker 支持**: 包括 Dockerfile 和 docker compose 文件，方便开发和部署。
11. **测试**: 包括整个存储库的强大单元测试和集成测试。

### 主要文件
存储库的结构如下：

- `src/agents/`: 定义具有不同功能的多个代理
- `src/schema/`: 定义协议模式
- `src/core/`: 核心模块，包括 LLM 定义和设置
- `src/service/service.py`: FastAPI 服务，用于提供代理服务
- `src/client/client.py`: 与代理服务交互的客户端
- `src/streamlit_app.py`: 提供聊天界面的 Streamlit 应用程序
- `tests/`: 单元测试和集成测试

## 为什么选择 LangGraph？

AI 代理越来越多的构建在结构更明确、控制更严格的 [复合 AI 系统](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) 上，对 [认知架构](https://blog.langchain.dev/what-is-a-cognitive-architecture/) 进行了仔细的关注。 在创建此存储库时，LangGraph 似乎是最先进的开源框架，用于构建这样的系统，它具有高度的控制能力以及对并发执行、图形中的循环、流式结果、内置可观察性以及 LangChain 周围的丰富生态系统等功能的支持。

在过去一年中，我花了不少时间使用 LangChain 进行构建，并体验了一些常见的痛点。 在使用 LangGraph 进行构建时，我发现了一些类似的问题，但总体而言，我喜欢它的方向，并且我对选择它感到满意。

话虽如此，这个领域还有其他几个有趣的项目值得一提，我希望很快能花更多时间使用它们：

- [LlamaIndex 工作流](https://www.llamaindex.ai/blog/introducing-workflows-beta-a-new-way-to-create-complex-ai-applications-with-llamaindex) 和 [llama-agents](https://github.com/run-llama/llama-agents)：LlamaIndex 工作流在我开始工作的那天发布。 我一直很喜欢使用 LlamaIndex 的体验，这看起来很有希望。
- [DSPy](https://github.com/stanfordnlp/dspy)：DSPy 优化器和方法也似乎非常有趣且有前途。 但创建者 [已经表示](https://github.com/stanfordnlp/dspy/issues/703#issuecomment-2016598529) 他们还没有专注于代理。 我将来可能会尝试使用 DSPy 构建更复杂的代理中的某些特定节点。
- 我知道还有很多不断涌现的项目，例如最近我遇到了 [Prefect ControlFlow](https://github.com/PrefectHQ/ControlFlow)。

## 设置和使用

1. 克隆存储库：

   ```sh
   git clone https://github.com/JoshuaC215/agent-service-toolkit.git
   cd agent-service-toolkit
   ```

2. 设置环境变量：
   在根目录中创建一个 `.env` 文件。 至少需要一个 LLM API 密钥或配置。 请参阅 [`.env.example` 文件](./.env.example) 以获取所有可用环境变量的完整列表，包括各种模型提供程序 API 密钥、基于标头的身份验证、LangSmith 跟踪、测试和开发模式以及 OpenWeatherMap API 密钥。

3. 现在，您可以本地运行代理服务和 Streamlit 应用程序，无论是使用 Docker 还是仅使用 Python。 建议使用 Docker 进行更简单的环境设置和在更改代码时立即重新加载服务。

### Docker 设置
此项目包含一个 Docker 设置，用于方便的开发和部署。 `compose.yaml` 文件定义了两个服务：`agent_service` 和 `streamlit_app`。 每个服务的 `Dockerfile` 位于其各自的目录中。

对于本地开发，建议使用 [docker compose watch](https://docs.docker.com/compose/file-watch/)。 此功能通过在检测到源代码中的更改时自动更新容器，从而实现更流畅的开发体验。

1. 确保您的系统已安装 Docker 和 Docker Compose (>=[2.23.0](https://docs.docker.com/compose/release-notes/#2230))。

2. 构建并以监视模式启动服务：

   ```sh
   docker compose watch
   ```

3. 现在服务会在您更改代码时自动更新：
   - 相关 python 文件和目录中的更改将触发相关服务的更新。
   - 注意：如果更改了 `pyproject.toml` 或 `uv.lock` 文件，则需要通过运行 `docker compose up --build` 来重新构建服务。

4. 通过在 Web 浏览器中导航到 `http://localhost:8501` 来访问 Streamlit 应用程序。

5. 代理服务 API 将通过 `http://localhost:80` 可用。 您还可以使用 OpenAPI 文档访问 `http://localhost:80/redoc`。

6. 使用 `docker compose down` 停止服务。

此设置使您可以实时开发和测试更改，而无需手动重新启动服务。

###  无需 Docker 的本地开发

您也可以仅使用 Python 虚拟环境在本地运行代理服务和 Streamlit 应用程序，而无需 Docker。

1. 创建虚拟环境并安装依赖项：

   ```sh
   pip install uv
   uv sync --frozen
   source .venv/bin/activate
   ```

2. 运行 FastAPI 服务器：

   ```sh
   python src/run_service.py
   ```

3. 在另一个终端中，运行 Streamlit 应用程序：

   ```sh
   streamlit run src/streamlit_app.py
   ```

4. 打开浏览器并导航到 Streamlit 提供的 URL（通常是 `http://localhost:8501`）。

### 使用 LangGraph Studio 进行开发
该代理支持 [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio)，这是一个用于在 LangGraph 中开发代理的新 IDE。

您只需安装 LangGraph Studio，将您的 `.env` 文件添加到上述根目录，然后启动指向根目录的 LangGraph studio。根据需要自定义 `langgraph.json`。

###  贡献

目前，测试需要使用无需 Docker 的本地开发设置来运行。要运行代理服务的测试：

1. 确保您位于项目根目录，并已激活您的虚拟环境。

2. 安装开发依赖项和预提交钩子：

   ```sh
   pip install uv
   uv sync --frozen
   pre-commit install
   ```

3. 使用 pytest 运行测试：

   ```sh
   pytest
   ```

##  定制

要根据您的用例自定义代理：

1. 将您的新代理添加到 `src/agents` 目录。您可以复制 `research_assistant.py` 或 `chatbot.py` 并修改它以更改代理的行为和工具。
2. 将您的新代理导入并添加到 `src/agents/agents.py` 中的 `agents` 字典中。您的代理可以通过 `/<your_agent_name>/invoke` 或 `/<your_agent_name>/stream` 来调用。
3. 调整 `src/streamlit_app.py` 中的 Streamlit 界面以匹配您的代理的功能。

##  在 AgentClient 上构建其他应用程序

该存储库包含一个通用的 `src/client/client.AgentClient`，可用于与代理服务交互。该客户端设计灵活，可用于在代理之上构建其他应用程序。它支持同步和异步调用以及流式和非流式请求。

有关如何使用 `AgentClient` 的完整示例，请参见 `src/run_client.py` 文件。一个快速示例：

```python
from client import AgentClient
client = AgentClient()

response = client.invoke("Tell me a brief joke?")
response.pretty_print()
# ================================== Ai Message ==================================
#
# A man walked into a library and asked the librarian, "Do you have any books on Pavlov's dogs and Schrödinger's cat?"
# The librarian replied, "It rings a bell, but I'm not sure if it's here or not."

```


## 贡献

欢迎贡献！请随时提交拉取请求。

## 许可证

该项目采用 MIT 许可证 - 有关详细信息，请参阅 LICENSE 文件。 




