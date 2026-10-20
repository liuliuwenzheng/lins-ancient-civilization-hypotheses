# 条目详情呈现（v1）

[English](entry-detail-ui.md) | 中文

> 在 `/ui` **解锁已有档案深度**。优先露出已登记的 Markdown 分栏报告，而不是新写空话。相关：[`entry-depth.zh.md`](entry-depth.zh.md) · [`design-taste.zh.md`](design-taste.zh.md) · [`council.zh.md`](council.zh.md) · 决策 **D-2026-10-13-09**、**D-2026-10-13-10**。

---

## 问题

此前在 `/ui` 打开文明时，默认是**主张一行字**，遗址/分期只有**名称 + 短摘要**。`data/civilizations/civ-*.md` 里已有丰富双语分栏（摘要、地理、分期、关键遗址、城市与制度、文字与行政、经济与手工业、物质文化、对外接触、研究史、来源），`markdown_path` 已挂上，但**没有送到浏览界面**。档案其实厚，屏幕却显得薄。

## 目标

打开文明时，**主视图**是 entry-depth 已写好的**分栏报告**，不是主张列表。主张、遗址、分期作为次级档案页签保留。

## 主视图：分栏报告 / Report columns

| 规则 | 说明 |
|------|------|
| 真源 | `civilization.json` → `markdown_path` → 解析该文件的 `##` 栏目 |
| 栏目集合 | 有什么 `##` 就显示什么；已知标题映射到 entry-depth id；**不虚构**缺失栏目 |
| 空栏 | 诚实省略，不注水 |
| 语言 | UI 为中文且解析到中文块时优先 `body_zh`；否则展示完整 `body_md`（多数条目本就中英并列）。英文 UI 同理优先 `body_en` |
| 渲染 | 轻量 Markdown：段落、列表、简单表格；高亮 `` `src-*` ``。不上伪造图 |
| 研究史 | Markdown 里有则必须可见——发现脉络的诚实落点 |

已知标题 → id（未列标题仍以 slug 出现）：

| id | en | zh |
|----|----|----|
| `summary` | Summary | 摘要 |
| `geography-environment` | Geography & environment | 地理与环境 |
| `chronology-periodization` | Chronology / periodization | 年代与分期 |
| `key-sites` | Key sites | 关键遗址 |
| `urbanism-architecture-institutions` | Urbanism, architecture & institutions | 城市、建筑与制度 |
| `writing-language-administration` | Writing, language & administration | 文字、语言与行政 |
| `economy-subsistence-craft` | Economy, subsistence & craft | 经济、生计与手工业 |
| `material-culture` | Material culture | 物质文化 |
| `external-contacts` | External contacts | 对外接触 |
| `research-history` | Research history | 研究史 |
| `sources` | Sources | 来源 |
| `related-civilizations` | Related civilizations | 相关文明 |
| `notes` | Notes | 备注 |

## 考察办法 / 发现脉络

| 做 | 不做 |
|----|------|
| 原样展示 **研究史** 栏目正文 | 编造发掘故事 |
| 将已登记 `src-*`（尤其档次 **P** 的发掘报告）标为 **已登记来源脉络** | 宣称该列表等于完整田野史 |
| 遗址卡片展开来源 + 包内关联主张 | 伪造方法说明、坐标或页码 |

界面短注：脉络条仅为**已登记来源**，不能代替阅读原报告。

## 次级页签

1. **遗址** — 名称、摘要、区域；坐标**仅当** JSON 已核验存在；可展开来源；同包内引用该遗址的主张。
2. **分期** — 按年代排序（`approx_from_bce` 降序，空值靠后）；展示 `time.label`（及可选起讫 BCE）与淡化的 `scheme_note`；摘要（空则省略）。跨度是引证方案，不是唯一历法。
3. **主张** — 不再作默认首页；保留 kind 徽章、来源展开、事实/假说筛选。
4. **媒体** — 仅已登记外链：标题、`media_type`、权利状态/署名、外链按钮、展开来源。`outbound-link-only` 标为外链资料/目录/图库页——**不当**可嵌图片，不伪造缩略图。无记录时诚实空态。

## API 形状（v1）

**优先**独立只读端点，避免列表/详情过重：

```
GET /api/v1/civilizations/{id}/report
```

响应草图见英文版。`markdown_path` 缺失或文件不存在时 `available: false` 且 `sections: []`——**不发明正文**。`body_zh` / `body_en` 尽力从双语段落拆分；始终保留 `body_md`。

## UI 默认

- 语言默认中文（除非用户切到 EN）。
- 打开文明默认页签：**档案报告**。
- 主张 kind 筛选仅在「主张」页签生效。
- 品味：一强调色、字体、诚实空态——见 [`design-taste.zh.md`](design-taste.zh.md)。

## 配图闸门

仅当下列**全部**满足时登记媒体：

| 闸门 | 要求 |
|------|------|
| URL | 稳定公开地址（WHC 页、博物馆目录、数字化落地页、已引证开放 PDF） |
| 权利 | 外链清晰，或未来热链/嵌入所需的开放许可 |
| 出处 | 标题/说明 + 至少一条 `src-*` |
| 诚实 | 无 AI/伪造文物图；无装饰性图库；`local_path` 保持 null |
| 优先 | 遗址图、发掘报告数字化本、博物馆开放目录、教科文组织图库 |

**不要**把受版权二进制下载进仓库。在核验到可视化 URL 之前，包内可仅保留文档外链媒体。

### 页内嵌图（D-2026-10-20-01）

通过**嵌入闸门**（`export_check` 强制）的记录可热链真实图片：

| 字段 | 规则 |
|------|------|
| `media_type` | `embedded-image` |
| `image_url` / `thumb_url` | 仅官方主机：`upload.wikimedia.org`、`thumb.wikimedia.org`、`images.metmuseum.org`（schema 正则）。仓内不存二进制。 |
| `rights` | `status: rights-cleared`；`license` 仅限公有领域 / CC0 / CC BY / CC BY-SA；必须有 `license_url`、`attribution`（照抄来源署名）、`upstream_url` |
| `external_url` | Commons 文件页或博物馆藏品页 |
| `caption` | 中英双语、只写事实：是什么、来源给出的收藏机构与馆藏号；石膏模型/复制品/摹本必须注明（本次试点未收） |
| 关联 | ≥1 条 `src-*`（每图一条 T 档记录）+ ≥1 个包内存在的 `object_ids`/`site_ids` |

逐图核验：Commons API `imageinfo`/`extmetadata`；大都会 Collection API `isPublicDomain=true`；目视核对缩略图与说明一致；`python3 tools/check_media_images.py <包名>`（HEAD → 200 `image/*`）。

界面：媒体页签先列已核验图片（懒加载、`alt` = 说明、许可 + 署名 + 来源页），外链资料仍为链接卡片；档案报告顶部 ≤4 张图带，点击跳到媒体页签；遗址卡按 `site_ids` 显示缩略图；图片失效时移除 `<img>`，保留说明与链接。

试点：埃及 12 张、两河 9 张——见 [`decisions.zh.md#d-2026-10-20-01`](decisions.zh.md)。

## 非目标（v1）

- 在 API 里生成新百科散文
- 自动补译缺失的中/英半边
- 装饰性「博物馆」配图或伪造缩略图
- 把假说升格写进报告分栏
- 在无权利清理时嵌入第三方图片（见上方嵌入闸门）

## 校验

- `export_check` 仍通过（报告解析只读呈现）。
- Curl 埃及、两河 `/report` → 栏目非空；Markdown 含研究史则响应含该栏。
- Curl `/periods?civilization=civ-ancient-egypt` → 旧石器/巴达里早于纳盖达早于古王国（按 `approx_from_bce`）。
- Curl `/media?civilization=…` → 有登记媒体的包非空；UI 媒体页签外链卡片无假缩略图；仅通过嵌入闸门的记录显示图片（埃及/两河含 `image_url`；`tools/check_media_images.py` 全部 OK）。
