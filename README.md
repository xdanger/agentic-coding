# 面向 Agentic Coding 的软件工程

## 对于未来的判断

未来软件工程的组织方式，会从面向人类转变为面向 AI/Agent —— 所有软件工程中执行的部分：coding, documentation, testing, debugging, etc. 都会由 AI/Agent 来完成，而人类的重点将转移到设计面向 AI/Agent 的架构（管理好目录结构、文档、历史记录），以及 review AI/Agent 的输出。

## 什么是 Agentic Coding

之所以不叫做 AI Coding，是想更准确地定义不同事物、理解各自的职责和范围。

### LLMs

LLMs 本质是一个与 CPU 类似的数字化处理器，接收信息输入，处理后输出信息。区别是，CPU 输出的信息是基于确定的规则的，可重现的；而 LLMs 是一种神经网络处理器，输出的信息是基于概率的。因此，LLMs 就能用来处理原来再强大的 CPU 也无法处理的非结构化数据与模糊问题。

韦氏智商测试（Wechsler Intelligence Scale）会对这些方面的能力进行量化测试：语言理解（Verbal Comprehension）、 语言流畅（Language Fluency）、数字能力（Numerical Ability）、视觉空间/知觉推理（Visual Spatial / Perceptual Reasoning）、流体推理（Fluid Reasoning）、记忆（Working Memory）、处理速度（Processing Speed）、执行功能（Executive Function）。

可以说，LLMs 在所有这些方面的表现都会远远优于人类：

- **逻辑能力**（理解、计算、推理）会超过在领域内最尖端的人类，比如 2025 年内很可能出现比所有人类 coding 能力都强的 AI；
- **处理速度** 是人类的 100x。不仅编写代码快，而且设计、重构、测试、管理文档 …… 都很快；

但与人类不同的是，人类有刻在基因里的目标 —— 将基因延续下去，因此需要生存和繁衍。为了实现这些目标，需要个体以及群体合作，因此逐渐进化出情感、自我意识（分工与试错），于是也需要承载自我意识的长期记忆。

### Agentic Coding

而 Agent 的工作，或者说 Agentic Coding，就是想办法利用 LLMs 的这些长处，设计一套工作流程和规范来补足 LLMs 的局限，使得可以快速、高质量地完成我们的工程目标。

目前，AI/Agentic Coding 在实用性上受限于：

- LLMs 缺乏对整个项目全局的理解，往往只关注完成当前的任务；
- LLMs 缺乏对人类意图的理解，往往只能完成人类 prompt 的表面工作；
- LLMs 缺乏对仓库历史的长期记忆，因此缺乏长期维护的能力，往往只能完成短期任务；
- LLMs 缺乏为减少将来的工作而进行优化的意识 —— 不会整理仓库、删除不必要的文件、重构代码、优化算法、更新注释和文档 …… 等；
- 如果人工对于仓库手动做了修改，AI/Agent 很难获得这部分信息，因此对于项目的过程的记忆是不完整的。

使用 LLMs 来写代码，非常像雇佣了一群新认识的 freelancer。

- 是一个 24x7 可以响应的、劳动力带宽几乎无限的一群 freelancer；
- 这群 freelancer 的活不仅质量高、还非常便宜；
- 但是这群 freelancer 只关注完成你给的特定任务，如果没有具体的 prompt，他们不会想着需要在达成全局目标（或约束）的情况下完成任务，也不会想到我完成之后如何让其他人能方便地接手。

如何能让这群 freelancer 更好地完成任务，就是 Agentic Coding 要解决的问题。

## 解决办法：Agentic Coding 最佳实践框架

以下是一些 high level 的思路：

- `/docs/` 目录，由人类和 AI 共同维护，以传统方式存放项目的开发文档
  - `decisions/`，存放所有与项目相关的决策记录，包括决策的背景、理由、以及决策后的结果 —— 文件格式为 `YYYY/{THREE_DIGIT_SEQUENCE_NUMBER}_{DECISION_TITLE_SLUG}.md`；
  - `debt/` 目录，用于存放项目当前的技术债务以及重构的机会 —— 文件格式为 `{DEBT_TITLE_SLUG}.md`。
  - `metrics/` 目录，用于存放项目当前的各类技术指标，需要包括原因和潜在的解决方法，包括：
    - `performance-metrics.md`，性能指标；
    - `code-quality-metrics.md`，代码质量指标；
    - `test-coverage.md`，测试覆盖率指标；
  - `specs/`，存放所有与项目相关的技术规范，包括：
    - `architecture.md`，架构设计；
    - `coding-standards.md`：编码规范；
    - `db-schema.md`：数据库 schema；
    - `diagrams.md`，系统图表；
    - `documentation-standards.md`：文档格式规范；
    - `interfaces.md`：对外接口；
    - `testing-standards.md`：测试标准；
- 由 AI 维护一个 `/.agent/` 目录，用于存放所有 AI/Agent 生成、以及 AI/Agent 今后需要使用的相关文件：
  - `tasks/` 目录：每次执行的任务信息，时间、总结人类的 prompt 和 AI 执行的工作结果与反思信息 —— 文件格式为 `YYYY-MM/DD_{FOUR_DIGIT_SEQUENCE_NUMBER}.md`；
  - `experiences/` 目录：AI 执行任务时犯的错误、碰到的问题的总结与反思 —— 文件格式为 `YYYY-MM/{EXPERIENCE_TITLE_SLUG}.md`，类似的问题在一个文件中合并；
  - `releases/` 目录：每个版本的信息，包括发布日期、版本号、发布说明等 —— 文件格式为 `YYYY-MM/v{VERSION_NUMBER}.md`；
- 需要让 LLMs 对于全局目标和规范约束有充分的理解；
- 在开发过程中，需要让 LLMs 在 `/.agent/` 目录下留下可以给自己将来使用的记忆，并不断地思考和反思，更新相应的 `/.agent/` 和 `/docs/` 目录下的文件；
- 同时，还需要将相应的内容保存或更新到以下几个 agent 的目录，比如：
  - 在 `/.agent/rules/` 目录下，保存所有 [Cursor Editor](https://www.cursor.com/) 需要用到的规则；
  - 在 `/CLAUDE.md` 文件中，保存所有 [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) 需要用到的全局 prompt。
