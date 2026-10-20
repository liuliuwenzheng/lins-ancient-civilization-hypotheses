# 林的古文明猜想

[English](README.md) | 中文

> 广收材料，事实与假说分栏，每条必有出处——绝不编造故事。

## 使命

**林的古文明猜想**（英文名：Lin's Ancient Civilization Hypotheses）是一个面向全球古文明的开放**档案 + 只读 API**——人类可读文案是呈现层，不是产品本身。

范围刻意**尽量广**：各大洲、各地区、各类文明——不限于单一遗址或单一河域。我们收集已发表证据、登记来源、把联想记为**明确标注的假说**，并以显式不确定性归档还原与因果说明。

本项目**不是**幻想故事、伪造文物图、或无法核验的「失落文明」虚构之地。每条记录必须有出处。假说就是假说——绝不以定论口吻呈现。

工艺标准：[设计品味](docs/design-taste.zh.md) · [English](docs/design-taste.md)——看见的与看不见的都要过关。

## 为何不是维基百科？

维基在**覆盖面**与大众协作上无可替代。本仓库做的是另一件事：

| | 维基百科 | 本项目 |
|--|----------|--------|
| 真值单元 | 叙述性词条 | 结构化档案实体（来源、遗址、分期、器物、主张、媒体） |
| 事实 vs 猜测 | 常揉进同一文风 | **硬分栏** — `kind: fact` / `kind: hypothesis`，API 与 `/ui` 都可见 |
| 机器使用 | 抓取 / 转储 | 一等公民**只读 API** + 出处失败即关闭 |
| 影像 | 社区媒体 | **不上伪造文物图**；权利清楚时媒体仅为外链元数据 |

此处覆盖仍窄。优势只有在密度、闸门与诚实持续加深时才成立。

## 试用 API / UI

```bash
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/export_check.py
.venv/bin/python -m api.serve
```

然后打开：

- **浏览 UI：** [http://127.0.0.1:8080/ui](http://127.0.0.1:8080/ui) — **默认中文**；博物馆级克制；可切 EN；事实/假说徽章
- **接口根：** [http://127.0.0.1:8080/api/v1/](http://127.0.0.1:8080/api/v1/) — 原则优先的服务卡片
- **OpenAPI：** [http://127.0.0.1:8080/api/v1/docs](http://127.0.0.1:8080/api/v1/docs)

## 四阶段方法

| 阶段 | 名称 | 做什么 |
|------|------|--------|
| 1 | **收集** | 把发掘报告、铭文/语料、博物馆图录、同行评议综述等登记进 `sources/` |
| 2 | **建库** | 在 `data/civilizations/` 维护文明条目，作为**事实库**（有年代、有出处；事实栏不写臆测） |
| 3 | **发现联想** | 在 `hypotheses/` 假说板上记录跨文明关联与待检验模式——每条必须标注 **HYPOTHESIS / 假说** |
| 4 | **还原与归档因果** | 在 `reconstructions/` 写还原稿，链接事实与假说，谨慎陈述因果，并标明不确定之处 |

**硬规矩：** 事实栏与假说栏严格分开，禁止混写进同一段不加区分的叙述。

**审议圆桌：** 材料固化前，可选多透镜审核（主持 + 选自 [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives) 的席位），产出 FACT_NOTES / HYPOTHESIS_CHALLENGES / OPEN_QUESTIONS / FUTURE_WINDOW。透镜是 AI 视角（`perspective: true`，`person_endorsement: false`）——不是具名人物背书。对话式审核优先走云端接口；已发布会话落在 `deliberations/`。

详见：[`docs/methodology.md`](docs/methodology.md) · 圆桌：[`docs/council.zh.md`](docs/council.zh.md)

## 结构化档案

产品核心是**档案 + 只读 API**。JSON Schema：[`schemas/`](schemas/)。结构化包：[`data/structured/`](data/structured/)。模型：[`docs/archive-data-model.zh.md`](docs/archive-data-model.zh.md)。校验：`.venv/bin/python tools/export_check.py`。设计：[`docs/design-taste.zh.md`](docs/design-taste.zh.md)。

## 来源分级

每条来源都要登记并分级。大致档次：

| 档 | 标签 | 典型例子 |
|----|------|----------|
| **P** | 一手 / Primary | 发掘报告、铭文、经策展的博物馆器物图录 |
| **S** | 二手 / Secondary | 同行评议综述、手册、学术专著 |
| **T** | 三手 / Tertiary | 百科、教材、可靠通论 |
| **U** | 存疑 / Uncertain | 出处不全、仅摘要可及、归属有争议 |

引用与分级细则：[`docs/source-grading.md`](docs/source-grading.md)

## 仓库目录

```
lins-ancient-civilization-hypotheses/
├── README.md / README.zh.md
├── LICENSE
├── api/                      # 只读 FastAPI + /ui（api/static/ui.html）
├── schemas/                  # 档案实体 JSON Schema
├── data/
│   ├── civilizations/        # 人类可读事实库 Markdown
│   └── structured/           # 机读档案包（JSON）
├── docs/                     # 方法、架构、接口、设计品味、决策
├── sources/                  # 来源登记
├── hypotheses/               # 假说板 — 标注 HYPOTHESIS
├── deliberations/            # 圆桌会话 — 视角透镜
├── reconstructions/          # 因果与不确定性
└── tools/export_check.py     # 出处失败即关闭闸门
```

模板已明确标为模板；**不会**预填虚构案例。

**资料库状态（2026-10-13）：** `data/structured/` 下 **40** 个结构化包 — **9 个密档**（`fact-library`，约 68–76 源）+ **31 个加厚中**（`library-seed-rich`，约 71 源级）。合计约 **2800+** 来源登记、**1600+** 遗址、**2600+** 主张（以 `export_check` / 结构化计数为准）。覆盖图：[`docs/coverage-map.zh.md`](docs/coverage-map.zh.md) · [English](docs/coverage-map.md)。深度：[`docs/entry-depth.zh.md`](docs/entry-depth.zh.md)。决策：[`docs/decisions.zh.md`](docs/decisions.zh.md)（含 D-2026-10-13-08 等）。

**密档（9）：** mesopotamia · egypt · andes · indus · china-bronze · sanxingdui · aegean · olmec · early-maya

**加厚中（31，约 71 源）：** 热门十包（teotihuacan · classic-maya · inca · angkor · aksum · aztec · phoenician · anatolia-hittite · nubia-kush · elam-iran）与其余二十一包（含 Wave-1/2/3 种子）均已加厚到同密度带；**尚未升 `fact-library`**——升档卡在有出处坐标与壳状遗址清理，不凑标签。

**浏览 UI：** `/ui` **默认中文**（可一键切 EN）。博物馆级克制；事实/假说徽章；不上伪造文物图。

- **设计品味** — 创作者原则 + UI/API/README 清单：[`docs/design-taste.zh.md`](docs/design-taste.zh.md) · [English](docs/design-taste.md)
- **条目深度** — 必填栏目、来源下限、状态阶梯：[`docs/entry-depth.zh.md`](docs/entry-depth.zh.md) · [English](docs/entry-depth.md)
- **条目详情 UI** — 分栏报告为主视图：[`docs/entry-detail-ui.zh.md`](docs/entry-detail-ui.zh.md) · [English](docs/entry-detail-ui.md)
- **决策记录** — 有日期的范围选择：[`docs/decisions.zh.md`](docs/decisions.zh.md) · [English](docs/decisions.md)
- **架构** — 分层、实体、不变量、存储路径：[`docs/architecture.zh.md`](docs/architecture.zh.md) · [English](docs/architecture.md)
- **审议圆桌** — 多透镜审核；面向未来窗口：[`docs/council.zh.md`](docs/council.zh.md) · [English](docs/council.md) · [`deliberations/`](deliberations/)
- **视角透镜（仅引用）** — AI 思维技能，非真人背书：[FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)
- **开放接口** — 资料库只读 v0 + 云端优先审议（规范）：[`docs/api.zh.md`](docs/api.zh.md) · [English](docs/api.md) · [`openapi.v0.yaml`](docs/openapi.v0.yaml)

## 贡献规范

1. **每条必有出处。** 没有来源 → 不要写入该主张。
2. **事实与假说分开。** 用模板；如实填写状态字段。
3. **不编造故事。** 不写虚构对话、不上伪造文物图、不引用无法核验的「秘密档案」。
4. **客户 / 成本 / 私密商务数据不上仓。**
5. **发布或删除本仓库** 须经所有者明确批准。
6. 优先可开放获取或可明确引用的文献；URL 请注明访问日期。
7. **设计工艺** — 遵循 [`docs/design-taste.zh.md`](docs/design-taste.zh.md)；勿用装饰掩盖薄档案。

完整说明：[`docs/contributing.md`](docs/contributing.md)

## 免责声明

**本仓库中的假说≠既定历史或考古结论。**

`hypotheses/` 下的条目，以及 `reconstructions/` 中的推测部分，是供讨论与进一步核验的工作假说。读者与贡献者不得将其当作已证实事实。证据冲突时两侧都记；证据薄弱时如实写明。

事实库力求审慎、有出处的摘要——仍是活文档，可能有误。欢迎用更好来源纠正。

圆桌席位名称指向 FHLS-perspectives 中的 **AI 生成思维透镜**。**不表示**那些人物背书本仓库或任何一场审议。

## 许可

代码与文档：**MIT** — 见 [`LICENSE`](LICENSE)。

所引第三方文本、图像与数据仍属原权利人。勿整篇粘贴受版权保护材料；请链接并引用。勿上传伪造或错标的文物影像。

**图片文件：** `data/media-files/` 存放开放许可图片（公有领域 / CC0 / CC BY / CC BY-SA）的网页尺寸副本。MIT 许可**不**适用于这些图片；每张图保留自身许可，作者、许可链接与来源页见 `data/media-files/<包名>/ATTRIBUTION.md`。CC BY-SA 图片按相同方式共享。详见 [`data/media-files/README.md`](data/media-files/README.md)。
