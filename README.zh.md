# 林的古文明猜想

[English](README.md) | 中文

> 广收材料，事实与假说分栏，每条必有出处——绝不编造故事。

## 使命

**林的古文明猜想**（英文名：Lin's Ancient Civilization Hypotheses）是一个面向全球古文明的开放资料库与假说板。

范围刻意**尽量广**：各大洲、各地区、各类文明——不限于单一遗址或单一河域。我们收集已发表证据、登记来源、把联想记为**明确标注的假说**，并以显式不确定性归档还原与因果说明。

本项目**不是**幻想故事、伪造文物图、或无法核验的「失落文明」虚构之地。每条记录必须有出处。假说就是假说——绝不以定论口吻呈现。

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
├── README.md                 # 英文
├── README.zh.md              # 中文（本文件）
├── LICENSE                   # MIT
├── docs/
│   ├── methodology.md        # 四阶段 + 事实/假说分栏
│   ├── source-grading.md     # 来源分级与引用
│   ├── contributing.md       # 贡献规范
│   ├── architecture.md       # System layers & entity model (EN)
│   ├── architecture.zh.md    # 架构说明（中文）
│   ├── council.md            # Deliberation Council (EN)
│   ├── council.zh.md         # 审议圆桌（中文）
│   ├── api.md                # Public API design v0 (EN)
│   ├── api.zh.md             # 开放接口设计 v0（中文）
│   ├── openapi.v0.yaml       # OpenAPI 草稿（资料库 + 审议）
│   ├── decisions.md          # Dated project decisions (EN)
│   ├── decisions.zh.md       # 项目决策记录（中文）
│   ├── entry-depth.md        # Fact-library depth standard (EN)
│   └── entry-depth.zh.md     # 事实库条目深度标准（中文）
├── data/civilizations/       # 事实库条目（含种子空壳、_template.md）
├── sources/                  # 来源登记（含 _template.md）
├── hypotheses/               # 假说板（含 _template.md）— 标注 HYPOTHESIS
├── deliberations/            # 圆桌会话（含 _template.md）— 视角透镜
└── reconstructions/          # 还原稿（含因果与不确定性，含 _template.md）
```

模板已明确标为模板；**不会**预填虚构案例。

**资料库状态（2026-10-11）：** `data/civilizations/` 下已有九个文明条目。两河（`civ-mesopotamia`）为深度试点，状态 **`fact-library`**（新加厚模板）；其余仍为 **`library-seed`**，待同等加厚。深度标准：[`docs/entry-depth.zh.md`](docs/entry-depth.zh.md)。有日期的拍板见 [`docs/decisions.zh.md`](docs/decisions.zh.md)。

- **条目深度** — 必填栏目、来源下限、状态阶梯：[`docs/entry-depth.zh.md`](docs/entry-depth.zh.md) · [English](docs/entry-depth.md)
- **决策记录** — 有日期的范围选择（席位、云端先规范、种子区域、加厚种子）：[`docs/decisions.zh.md`](docs/decisions.zh.md) · [English](docs/decisions.md)
- **架构** — 分层、实体、不变量、存储路径：[`docs/architecture.zh.md`](docs/architecture.zh.md) · [English](docs/architecture.md)
- **审议圆桌** — 条目固化前的多透镜审核；对话式面向未来窗口：[`docs/council.zh.md`](docs/council.zh.md) · [English](docs/council.md) · 会话见 [`deliberations/`](deliberations/)
- **视角透镜（仅引用）** — AI 思维技能，非真人背书：[FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)
- **开放接口（设计）** — 资料库只读 v0 + 云端优先审议：[`docs/api.zh.md`](docs/api.zh.md) · [English](docs/api.md) · [`openapi.v0.yaml`](docs/openapi.v0.yaml)

## 贡献规范

1. **每条必有出处。** 没有来源 → 不要写入该主张。
2. **事实与假说分开。** 用模板；如实填写状态字段。
3. **不编造故事。** 不写虚构对话、不上伪造文物图、不引用无法核验的「秘密档案」。
4. **客户 / 成本 / 私密商务数据不上仓。**
5. **发布或删除本仓库** 须经所有者明确批准。
6. 优先可开放获取或可明确引用的文献；URL 请注明访问日期。

完整说明：[`docs/contributing.md`](docs/contributing.md)

## 免责声明

**本仓库中的假说≠既定历史或考古结论。**

`hypotheses/` 下的条目，以及 `reconstructions/` 中的推测部分，是供讨论与进一步核验的工作假说。读者与贡献者不得将其当作已证实事实。证据冲突时两侧都记；证据薄弱时如实写明。

事实库力求审慎、有出处的摘要——仍是活文档，可能有误。欢迎用更好来源纠正。

圆桌席位名称指向 FHLS-perspectives 中的 **AI 生成思维透镜**。**不表示**那些人物背书本仓库或任何一场审议。

## 许可

代码与文档：**MIT** — 见 [`LICENSE`](LICENSE)。

所引第三方文本、图像与数据仍属原权利人。勿整篇粘贴受版权保护材料；请链接并引用。勿上传伪造或错标的文物影像。
