# Web-sources thicken pass (2026-10-12)

English | [中文](pass-2026-10-12-web-sources.zh.md)

> Decision **D-2026-10-12-11**. Integrity over completeness: no invented coordinates, finds, page numbers, or archaeology.

## Goal

Find **more reliable open-web** gazetteer / heritage / project landings to thicken packs still weak after D-2026-10-12-10 — especially `sanxingdui` (0 coords), `china-bronze`, `andes`, `indus`, `olmec`, `early-maya`, plus remaining egypt / aegean empties where gazetteers hit cleanly.

## Method

1. Re-pull repo; inventory null-coordinate sites (skip survey / frame / pointer / intra-site loci unless a gazetteer publishes a **named** place for that unit).
2. Match only against: **UNESCO WHC** published DMS (inscribed + tentative), **Pleiades** places CSV representative points, **GeoNames** `S.ANS` / `S.RUIN` (country-locked; reject `P.PPL` town centroids and ambiguous multi-hits).
3. Register new Sources with stable URLs; attach UNESCO Chavín source to `site-chavin-de-huantar`; fill open PDF URLs on already-registered Sanxingdui briefs where found.
4. Add **outbound-link-only** Media (no forged images; `local_path` null).
5. Fuzzy hits → skip + log. Slack search for “hermes / 嘻嘻” returned **no** usable contact in this workspace.

## Coordinate fills this pass (**+26**; prior 84 → **110**)

| Pack | New fills | Still null (approx.) | New fill ids |
|------|----------:|---------------------:|--------------|
| sanxingdui | **2** | 34 | `site-sanxingdui`, `site-jinsha-comparative` (UNESCO Tentative **5816** DMS) |
| china-bronze | **1** | 37 | `site-wucheng` (GeoNames ANS) |
| andes | **1** | 39 | `site-chavin-de-huantar` (UNESCO **330** DMS) |
| indus | **1** | 34 | `site-lothal` (GeoNames RUIN) |
| olmec | **2** | 33 | `site-san-lorenzo`, `site-teopantecuanitlan` |
| early-maya | **11** | 23 | Cival, Lamanai, Colha, Nakbe, Cahal Pech, Altar de Sacrificios, Pacbitun, Kaminaljuyú, Yaxuná, Cerros (BZ), Holmul |
| egypt | **3** | 18 | Bubastis, Buto, Tell el-Farkha |
| aegean | **5** | 15 | Agia Triada, Palaikastro, Chania Kastelli (Kydonia), Mycenae Grave Circle B, Lefkandi Toumba/Heroon |
| mesopotamia | **0** | 14 | No clean new Pleiades hit for remaining empties (survey zones / loci left null) |

**Skipped (examples):** Aguada Fénix (no ANS hit); Naranjo-Belize (only Petén Naranjo in GeoNames); Tres Zapotes / El Manatí / Cascajal as modern `P.PPL` only; Aspero / Bandurria / Kotosh / Mehrgarh without ANS|RUIN|UNESCO decimal; Erlitou / Baodun / Sanxingdui pit loci; troy-VI/VIIa strata of already-filled Hisarlık.

## Sources registered / URL-filled

| Id | Action |
|----|--------|
| `src-andes-unesco-chavin-1985` | **New** WHC 330 listing (tier T) |
| `src-sanxingdui-npj-jade-2023` | **New** OA npj Heritage Science jade article (tier S) |
| `src-sanxingdui-qingguanshan-brief` | **URL filled** → open sckg.com PDF |
| `src-sanxingdui-hei-ma-sen-pit4-c14` | **URL filled** → open sckg.com PDF |

## Media added (**+11**; total **58 → 69**)

Outbound only: UNESCO Chavín; PEACS Caral values PDF; Sanxingdui Qingguanshan + Pit 4 PDFs; npj jade OA; Zhao NSR PMC mirror; UNESCO Moenjodaro maps; UNESCO Yinxu maps; INAH Teopantecuanitlán; FAMSI Hansen Nakbe + Freidel Yaxuná PDFs.

## Still blocked

- **Chinese gazetteer gap:** GeoNames ANS coverage for Erlitou, Baodun cluster, Zhengzhou Shang City, Yanshi Shang City, etc. is thin; Wikipedia/Wikidata alone not used.
- **Andean coastal Archaic:** Aspero, Bandurria, Sechín, Kotosh lack clean ANS/UNESCO decimal points in this pass (UTM-only PEACS PDFs not converted without datum verification).
- **Indus secondary centers:** Kalibangan, Rakhigarhi, Mehrgarh, Kot Diji — no GeoNames ANS/RUIN hit under country lock.
- **Olmec:** Tres Zapotes / El Manatí / Cascajal Block still null (no ANS; Cascajal ANS hit was Peru false positive).
- **Paywalled substance** (title-only notes; **not** fake-cited as full-text): Jinsha multi-volume sacrificial-area report; many CASS print monographs; Burger *Chavin* Thames & Hudson; Thorp Erlitou/Xia *Early China* body; Broodbank *Cyclades* Cambridge body; Campbell / Liu & Chen handbook chapters beyond open abstracts.

## Gate

`export_check` **OK** (9 packs; citation gate green).

## Hermes / 嘻嘻

User asked to ask Hermes’s 嘻嘻 for clues. Slack user/channel search for `hermes` / `嘻嘻` in this workspace returned **no results**. Proceeded with open-web gazetteers only; no third-party agent consulted.
