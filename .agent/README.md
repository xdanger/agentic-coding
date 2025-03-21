# `.agent`

这个目录由 agent 使用和维护，agent 可在没有人类授意的情况下依据自己的判断和工作流的要求而更新其中内容，用于存放所有 agent 生成、以及 agent 今后需要使用的相关文件；在开发过程中，需要让 LLM 在 `/.agent/` 下留下可以给自己将来使用的记忆，并不断地思考和反思，更新相应的 `/.agent/` 和 `/docs/` 目录下的文件

- `tasks/`：每次执行的任务信息，时间、总结人类的 prompt 和 agent 执行的工作结果与反思信息 —— 文件格式为 `YYYY-MM/DD_{TIMESTAMP}.md`
- `reflections/`：agent 执行任务时犯的错误、碰到的问题的总结与反思 —— 文件格式为 `YYYY-MM/{REFLECTION_TITLE_SLUG}.md`，类似的问题在一个文件中合并
- `releases/`：每个版本的信息，包括发布日期、版本号、发布说明等 —— 文件格式为 `YYYY-MM/v{VERSION_NUMBER}.md`
