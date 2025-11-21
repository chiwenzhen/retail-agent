import asyncio

from client import AgentClient
from core import settings
from schema import ChatMessage


# async def amain() -> None:
#     #### ASYNC ####
#     client = AgentClient('http://127.0.0.1:8080', agent='retail_agent')
#
#     print("Agent info:")
#     print(client.info)
#
#     print("Chat example:")
#     response = await client.ainvoke("中国第一个皇帝是谁?")
#     response.pretty_print()
#
#     print("\nStream example:")
#     async for message in client.astream("中国第一个皇帝是谁?"):
#         if isinstance(message, str):
#             print(message, flush=True, end="")
#         elif isinstance(message, ChatMessage):
#             print("\n", flush=True)
#             message.pretty_print()
#         else:
#             print(f"ERROR: Unknown type - {type(message)}")
#

def main() -> None:
    #### SYNC ####
    client = AgentClient('http://127.0.0.1:8080', agent='retail_agent')

    # print("Agent info:")
    # print(client.info)

    # print("Chat example:")
    # questions = [
    #     "中国第一个皇帝是谁",
    #     "他的父亲是谁",
    #     "请给我推荐一些存款产品",
    #     "请帮我介绍易方达基金",
    #     "请对比一下浙富宝7天301号和长赢14D002号"
    # ]
    # for question in questions:
    #     print("Human:", end="")
    #     print(question)
    #     print("AI:", end="")
    #     response = client.invoke(question, thread_id='user-123')
    #     print(response.content)


    # print("\nStream example:")
    questions = [
        "中国第一个皇帝是谁",
        # "他的父亲是谁",
        # "请给我推荐一些存款产品",
        # "请帮我介绍易方达基金",
        # "请对比一下浙富宝7天301号和长赢14D002号"
    ]
    for question in questions:
        print("Human:", end="")
        print(question)
        print("AI:", end="")
        for message in client.stream(question, thread_id='user-123'):
            if isinstance(message, str):
                print(message, flush=True, end="")
            elif isinstance(message, ChatMessage):
                print("\n", flush=True)
                message.pretty_print()
            else:
                print(f"ERROR: Unknown type - {type(message)}")


if __name__ == "__main__":
    print("Running in sync mode")
    main()
    print("\n\n\n\n\n")
    # print("Running in async mode")
    # asyncio.run(amain())
