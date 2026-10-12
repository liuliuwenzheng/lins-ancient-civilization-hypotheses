"""Wave-3 pack definitions for generate_wave3.py (D-2026-10-12-15).

Integrity: real P/S/T sources only; abstract/TOC-level claims; no invented
finds, page numbers, coordinates, or media art. Site ids must not collide
with existing packs.
"""
from __future__ import annotations
import json

PACKS = json.loads(r"""
[
  {
    "pack": "cahokia",
    "civ_id": "civ-cahokia",
    "names": {
      "zh": "卡霍基亚（密西西比文化）",
      "en": "Cahokia (Mississippian)",
      "native": "Cahokia"
    },
    "region": "North America / American Bottom (Illinois; Mississippi River floodplain)",
    "time_span": "Mississippian florescence ca. 1050–1350 CE (Pauketat / Emerson frames)",
    "summary": {
      "zh": "卡霍基亚档案壳（library-seed）：Pauketat 综合 + 教科文；北美密西西比大型中心。",
      "en": "Cahokia archive shell (library-seed): Pauketat synthesis + UNESCO; major Mississippian centre."
    },
    "related_ids": [
      "civ-ancestral-pueblo"
    ],
    "sources": [
      {
        "id": "src-cahokia-unesco-198",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Cahokia Mounds State Historic Site. Inscribed 1982. https://whc.unesco.org/en/list/198/",
        "url": "https://whc.unesco.org/en/list/198/",
        "notes": "WHC orientation for Cahokia Mounds; tier T."
      },
      {
        "id": "src-cahokia-pauketat-2009",
        "type": "monograph",
        "tier": "S",
        "citation": "Pauketat, Timothy R. 2009. Cahokia: Ancient America's Great City on the Mississippi. New York: Viking / Penguin.",
        "url": null,
        "notes": "Accessible synthesis of Cahokia urbanism; print; shell uses TOC-level scope."
      },
      {
        "id": "src-cahokia-emerson-1997",
        "type": "monograph",
        "tier": "S",
        "citation": "Emerson, Thomas E. 1997. Cahokia and the Archaeology of Power. Tuscaloosa: University of Alabama Press.",
        "url": null,
        "notes": "Political archaeology synthesis; print orientation."
      },
      {
        "id": "src-cahokia-milner-1998",
        "type": "monograph",
        "tier": "S",
        "citation": "Milner, George R. 1998. The Cahokia Chiefdom: The Archaeology of a Mississippian Society. Washington, DC: Smithsonian Institution Press.",
        "url": null,
        "notes": "Mississippian chiefdom synthesis; print."
      },
      {
        "id": "src-cahokia-fowler-1997",
        "type": "excavation-report",
        "tier": "P",
        "citation": "Fowler, Melvin L. 1997. The Cahokia Atlas: A Historical Atlas of Cahokia Archaeology. Revised edition. Illinois Transportation Archaeological Research Program / University of Illinois.",
        "url": null,
        "notes": "Atlas of mounds and excavations; P-tradition pointer."
      }
    ],
    "sites": [
      {
        "id": "site-cahokia-monks-mound",
        "names": {
          "zh": "卡霍基亚（修士丘）",
          "en": "Cahokia (Monks Mound)",
          "native": "Cahokia"
        },
        "kind_note": "Mississippian ceremonial–urban centre; UNESCO WH",
        "region": "Collinsville area, Illinois, USA",
        "coords": null,
        "summary": {
          "zh": "密西西比河洪泛平原大型土墩中心；教科文名录。",
          "en": "Large earthen-mound centre on the Mississippi floodplain; UNESCO listed."
        },
        "sources": [
          "src-cahokia-unesco-198",
          "src-cahokia-pauketat-2009",
          "src-cahokia-fowler-1997"
        ]
      },
      {
        "id": "site-cahokia-east-st-louis-orientation",
        "names": {
          "zh": "东圣路易斯相关组群（指针）",
          "en": "East St. Louis related cluster (orientation)",
          "native": null
        },
        "kind_note": "American Bottom related Mississippian precincts",
        "region": "American Bottom, Illinois",
        "coords": null,
        "summary": {
          "zh": "美底区相关密西西比组群指针；细节待加厚。",
          "en": "Related Mississippian precinct orientation in the American Bottom; details deferred."
        },
        "sources": [
          "src-cahokia-pauketat-2009",
          "src-cahokia-emerson-1997"
        ]
      }
    ],
    "period": {
      "id": "period-cahokia-mississippian-floruit",
      "names": {
        "zh": "卡霍基亚密西西比繁荣窗",
        "en": "Cahokia Mississippian floruit"
      },
      "time": {
        "label": "ca. 1050–1350 CE (Pauketat / Emerson working frame)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "CE span; Lohmann–Stirling–Moorehead phase tables deferred."
      },
      "summary": {
        "zh": "壳级密西西比繁荣窗。",
        "en": "Shell Mississippian floruit window."
      },
      "sources": [
        "src-cahokia-pauketat-2009",
        "src-cahokia-milner-1998"
      ]
    },
    "object": {
      "id": "asm-cahokia-mound-plaza-frame",
      "names": {
        "zh": "卡霍基亚土墩—广场框架组合",
        "en": "Cahokia mound–plaza frame assemblage"
      },
      "summary": {
        "zh": "壳级土墩与广场规划指针；无伪造馆藏号。",
        "en": "Shell mound-and-plaza planning pointer; no forged catalog numbers."
      },
      "site_ids": [
        "site-cahokia-monks-mound"
      ],
      "sources": [
        "src-cahokia-unesco-198",
        "src-cahokia-fowler-1997"
      ]
    },
    "claim": {
      "id": "claim-cahokia-mississippian-centre",
      "statement": {
        "zh": "教科文与学术综合将卡霍基亚土墩群表述为北美密西西比文化的大型仪礼—城市中心（UNESCO 198；Pauketat 2009）。",
        "en": "UNESCO and scholarly syntheses frame Cahokia Mounds as a major Mississippian ceremonial–urban centre in North America (UNESCO 198; Pauketat 2009)."
      },
      "site_ids": [
        "site-cahokia-monks-mound"
      ],
      "sources": [
        "src-cahokia-unesco-198",
        "src-cahokia-pauketat-2009"
      ]
    }
  },
  {
    "pack": "ancestral-pueblo",
    "civ_id": "civ-ancestral-pueblo",
    "names": {
      "zh": "先祖普韦布洛",
      "en": "Ancestral Puebloan",
      "native": "Ancestral Puebloan / Hisatsinom (Hopi preference varies)"
    },
    "region": "North America / Colorado Plateau (Four Corners: NM, AZ, CO, UT)",
    "time_span": "Basketmaker–Pueblo florescence broadly 1st–13th centuries CE (Pecos Classification / Lekson frames)",
    "summary": {
      "zh": "先祖普韦布洛档案壳：Lekson/Plog 综合 + 查科/梅萨维德教科文；library-seed。",
      "en": "Ancestral Puebloan archive shell: Lekson/Plog synthesis + Chaco/Mesa Verde UNESCO; library-seed."
    },
    "related_ids": [
      "civ-cahokia"
    ],
    "sources": [
      {
        "id": "src-pueblo-unesco-chaco-353",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Chaco Culture. Inscribed 1987. https://whc.unesco.org/en/list/353/",
        "url": "https://whc.unesco.org/en/list/353/",
        "notes": "WHC orientation for Chaco Culture; tier T."
      },
      {
        "id": "src-pueblo-unesco-mesa-verde-27",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Mesa Verde National Park. Inscribed 1978. https://whc.unesco.org/en/list/27/",
        "url": "https://whc.unesco.org/en/list/27/",
        "notes": "WHC orientation for Mesa Verde cliff dwellings; tier T."
      },
      {
        "id": "src-pueblo-lekson-2009",
        "type": "monograph",
        "tier": "S",
        "citation": "Lekson, Stephen H. 2009. A History of the Ancient Southwest. Santa Fe: School for Advanced Research Press.",
        "url": null,
        "notes": "Regional synthesis of Southwest archaeology; print; TOC-level for shell."
      },
      {
        "id": "src-pueblo-plog-2008",
        "type": "monograph",
        "tier": "S",
        "citation": "Plog, Stephen. 2008. Ancient Peoples of the American Southwest. 2nd ed. London: Thames and Hudson.",
        "url": null,
        "notes": "Accessible Southwest overview; print."
      },
      {
        "id": "src-pueblo-nps-chaco-orientation",
        "type": "web",
        "tier": "T",
        "citation": "U.S. National Park Service. Chaco Culture National Historical Park — archaeology orientation pages.",
        "url": "https://www.nps.gov/chcu/learn/historyculture/index.htm",
        "notes": "NPS institutional orientation; tier T."
      }
    ],
    "sites": [
      {
        "id": "site-chaco-canyon",
        "names": {
          "zh": "查科峡谷",
          "en": "Chaco Canyon",
          "native": "Chaco"
        },
        "kind_note": "Great-house canyon centre; UNESCO WH",
        "region": "Northwestern New Mexico, USA",
        "coords": null,
        "summary": {
          "zh": "大屋与道路体系著名的峡谷中心；教科文名录。",
          "en": "Canyon centre famous for great houses and road systems; UNESCO listed."
        },
        "sources": [
          "src-pueblo-unesco-chaco-353",
          "src-pueblo-lekson-2009",
          "src-pueblo-nps-chaco-orientation"
        ]
      },
      {
        "id": "site-mesa-verde",
        "names": {
          "zh": "梅萨维德",
          "en": "Mesa Verde",
          "native": null
        },
        "kind_note": "Cliff-dwelling mesa landscape; UNESCO WH",
        "region": "Southwestern Colorado, USA",
        "coords": null,
        "summary": {
          "zh": "悬崖居所与台地聚落景观；教科文名录。",
          "en": "Cliff-dwelling and mesa settlement landscape; UNESCO listed."
        },
        "sources": [
          "src-pueblo-unesco-mesa-verde-27",
          "src-pueblo-plog-2008"
        ]
      }
    ],
    "period": {
      "id": "period-ancestral-pueblo-floruit",
      "names": {
        "zh": "先祖普韦布洛繁荣窗",
        "en": "Ancestral Puebloan floruit"
      },
      "time": {
        "label": "broadly 1st–13th centuries CE (Pecos / Lekson working labels)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Basketmaker–Pueblo II/III phase tables deferred to densify."
      },
      "summary": {
        "zh": "壳级先祖普韦布洛窗。",
        "en": "Shell Ancestral Puebloan window."
      },
      "sources": [
        "src-pueblo-lekson-2009",
        "src-pueblo-plog-2008"
      ]
    },
    "object": {
      "id": "asm-pueblo-great-house-frame",
      "names": {
        "zh": "先祖普韦布洛大屋—崖居框架组合",
        "en": "Ancestral Puebloan great-house / cliff-dwelling frame"
      },
      "summary": {
        "zh": "壳级大屋与崖居建筑指针。",
        "en": "Shell great-house and cliff-dwelling architecture pointer."
      },
      "site_ids": [
        "site-chaco-canyon",
        "site-mesa-verde"
      ],
      "sources": [
        "src-pueblo-unesco-chaco-353",
        "src-pueblo-unesco-mesa-verde-27"
      ]
    },
    "claim": {
      "id": "claim-pueblo-chaco-mesa-verde",
      "statement": {
        "zh": "教科文将查科文化与梅萨维德表述为美国西南部先祖普韦布洛建筑与聚落传统的代表性景观（UNESCO 353、27）。",
        "en": "UNESCO frames Chaco Culture and Mesa Verde as representative landscapes of Ancestral Puebloan architecture and settlement in the U.S. Southwest (UNESCO 353, 27)."
      },
      "site_ids": [
        "site-chaco-canyon",
        "site-mesa-verde"
      ],
      "sources": [
        "src-pueblo-unesco-chaco-353",
        "src-pueblo-unesco-mesa-verde-27"
      ]
    }
  },
  {
    "pack": "great-zimbabwe",
    "civ_id": "civ-great-zimbabwe",
    "names": {
      "zh": "大津巴布韦",
      "en": "Great Zimbabwe",
      "native": "Great Zimbabwe"
    },
    "region": "Southern Africa / Zimbabwe plateau (Masvingo region)",
    "time_span": "Stone-walled capital floruit broadly 11th–15th centuries CE (Pikirayi / Huffman frames)",
    "summary": {
      "zh": "大津巴布韦档案壳：Pikirayi/Huffman 综合 + 教科文；library-seed。",
      "en": "Great Zimbabwe archive shell: Pikirayi/Huffman synthesis + UNESCO; library-seed."
    },
    "related_ids": [
      "civ-west-africa-medieval"
    ],
    "sources": [
      {
        "id": "src-zimbabwe-unesco-364",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Great Zimbabwe National Monument. Inscribed 1986. https://whc.unesco.org/en/list/364/",
        "url": "https://whc.unesco.org/en/list/364/",
        "notes": "WHC orientation; tier T."
      },
      {
        "id": "src-zimbabwe-pikirayi-2001",
        "type": "monograph",
        "tier": "S",
        "citation": "Pikirayi, Innocent. 2001. The Zimbabwe Culture: Origins and Decline of Southern Zambezian States. Walnut Creek, CA: AltaMira Press.",
        "url": null,
        "notes": "Major synthesis of Zimbabwe Culture; print."
      },
      {
        "id": "src-zimbabwe-huffman-2007",
        "type": "monograph",
        "tier": "S",
        "citation": "Huffman, Thomas N. 2007. Handbook to the Iron Age: The Archaeology of Pre-Colonial Farming Societies in Southern Africa. Pietermaritzburg: University of KwaZulu-Natal Press.",
        "url": null,
        "notes": "Iron Age handbook including Zimbabwe Culture; print; contested models noted in densify."
      },
      {
        "id": "src-zimbabwe-garlake-1973",
        "type": "monograph",
        "tier": "S",
        "citation": "Garlake, Peter S. 1973. Great Zimbabwe. London: Thames and Hudson.",
        "url": null,
        "notes": "Classic accessible monograph; print; shell TOC-level."
      },
      {
        "id": "src-zimbabwe-ndoro-2001",
        "type": "monograph",
        "tier": "S",
        "citation": "Ndoro, Webber. 2001. Your Monument Our Shrine: The Preservation of Great Zimbabwe. Uppsala: Department of Archaeology and Ancient History, Uppsala University.",
        "url": null,
        "notes": "Heritage management and local meaning study; print orientation."
      }
    ],
    "sites": [
      {
        "id": "site-great-zimbabwe-monument",
        "names": {
          "zh": "大津巴布韦国家纪念地",
          "en": "Great Zimbabwe National Monument",
          "native": "Great Zimbabwe"
        },
        "kind_note": "Dry-stone walled capital; UNESCO WH",
        "region": "Masvingo Province, Zimbabwe",
        "coords": null,
        "summary": {
          "zh": "干石墙都城与山丘建筑群；教科文名录。",
          "en": "Dry-stone walled capital and hill complex; UNESCO listed."
        },
        "sources": [
          "src-zimbabwe-unesco-364",
          "src-zimbabwe-pikirayi-2001",
          "src-zimbabwe-garlake-1973"
        ]
      },
      {
        "id": "site-zimbabwe-culture-orientation",
        "names": {
          "zh": "津巴布韦文化相关遗址（指针）",
          "en": "Zimbabwe Culture related sites (orientation)",
          "native": null
        },
        "kind_note": "Regional Zimbabwe Culture stonewall tradition",
        "region": "Southern Zambezian plateau",
        "coords": null,
        "summary": {
          "zh": "区域石墙传统指针；非单一点。",
          "en": "Regional stonewall tradition pointer; not a single point."
        },
        "sources": [
          "src-zimbabwe-pikirayi-2001",
          "src-zimbabwe-huffman-2007"
        ]
      }
    ],
    "period": {
      "id": "period-great-zimbabwe-floruit",
      "names": {
        "zh": "大津巴布韦繁荣窗",
        "en": "Great Zimbabwe floruit"
      },
      "time": {
        "label": "broadly 11th–15th centuries CE (Pikirayi working frame)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Absolute phase debates open; shell window only."
      },
      "summary": {
        "zh": "壳级大津巴布韦窗。",
        "en": "Shell Great Zimbabwe window."
      },
      "sources": [
        "src-zimbabwe-pikirayi-2001",
        "src-zimbabwe-huffman-2007"
      ]
    },
    "object": {
      "id": "asm-zimbabwe-dry-stone-frame",
      "names": {
        "zh": "大津巴布韦干石墙框架组合",
        "en": "Great Zimbabwe dry-stone architecture frame"
      },
      "summary": {
        "zh": "壳级干石墙建筑指针。",
        "en": "Shell dry-stone architecture pointer."
      },
      "site_ids": [
        "site-great-zimbabwe-monument"
      ],
      "sources": [
        "src-zimbabwe-unesco-364",
        "src-zimbabwe-garlake-1973"
      ]
    },
    "claim": {
      "id": "claim-great-zimbabwe-stone-capital",
      "statement": {
        "zh": "教科文与学术综合将大津巴布韦表述为南部非洲铁器时代重要的干石墙都城与津巴布韦文化中心（UNESCO 364；Pikirayi 2001）。",
        "en": "UNESCO and scholarly syntheses frame Great Zimbabwe as a major dry-stone capital and Zimbabwe Culture centre of the southern African Iron Age (UNESCO 364; Pikirayi 2001)."
      },
      "site_ids": [
        "site-great-zimbabwe-monument"
      ],
      "sources": [
        "src-zimbabwe-unesco-364",
        "src-zimbabwe-pikirayi-2001"
      ]
    }
  },
  {
    "pack": "west-africa-medieval",
    "civ_id": "civ-west-africa-medieval",
    "names": {
      "zh": "西非中世纪诸国（加纳–马里–桑海）",
      "en": "West African medieval empires (Ghana–Mali–Songhai)",
      "native": "Ghāna / Mālī / Songhay"
    },
    "region": "West Africa / Sahel–Savanna (Senegal–Niger bend; Middle Niger)",
    "time_span": "Sahelian empire floruit broadly 8th–16th centuries CE (Levtzion / McIntosh frames)",
    "summary": {
      "zh": "西非中世纪诸国档案壳：Levtzion/McIntosh + 廷巴克图/杰内教科文；library-seed。",
      "en": "West African medieval empires shell: Levtzion/McIntosh + Timbuktu/Djenné UNESCO; library-seed."
    },
    "related_ids": [
      "civ-nok-west-africa",
      "civ-great-zimbabwe"
    ],
    "sources": [
      {
        "id": "src-waf-unesco-timbuktu-119",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Timbuktu. Inscribed 1988. https://whc.unesco.org/en/list/119/",
        "url": "https://whc.unesco.org/en/list/119/",
        "notes": "WHC orientation for Timbuktu; Mali empire–era scholarly centre; tier T."
      },
      {
        "id": "src-waf-unesco-djenne-116",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Old Towns of Djenné. Inscribed 1988. https://whc.unesco.org/en/list/116/",
        "url": "https://whc.unesco.org/en/list/116/",
        "notes": "WHC orientation for Djenné; Middle Niger urbanism; tier T."
      },
      {
        "id": "src-waf-levtzion-hopkins-2000",
        "type": "monograph",
        "tier": "S",
        "citation": "Levtzion, Nehemia, and J. F. P. Hopkins, eds. 2000. Corpus of Early Arabic Sources for West African History. Princeton: Markus Wiener. (Reprint of 1981 Cambridge edition.)",
        "url": null,
        "notes": "Arabic-source corpus for Ghana/Mali/Songhai; print; shell uses corpus orientation only."
      },
      {
        "id": "src-waf-mcintosh-2005",
        "type": "monograph",
        "tier": "S",
        "citation": "McIntosh, Roderick J. 2005. Ancient Middle Niger: Urbanism and the Self-Organizing Landscape. Cambridge: Cambridge University Press.",
        "url": null,
        "notes": "Middle Niger urbanism synthesis; print."
      },
      {
        "id": "src-waf-hunwick-timbuktu-orientation",
        "type": "monograph",
        "tier": "S",
        "citation": "Hunwick, John O. — Timbuktu and the Songhay Empire / Arabic chronicle translations and studies (Brill tradition).",
        "url": null,
        "notes": "Songhay chronicle and Timbuktu scholarship pointer; deepen with specific edition citations."
      }
    ],
    "sites": [
      {
        "id": "site-timbuktu-medieval",
        "names": {
          "zh": "廷巴克图",
          "en": "Timbuktu",
          "native": "Timbuktu / Tombouctou"
        },
        "kind_note": "Sahelian scholarly–commercial city; UNESCO WH",
        "region": "Timbuktu Region, Mali",
        "coords": null,
        "summary": {
          "zh": "萨赫勒学术—商业城市；教科文名录。",
          "en": "Sahelian scholarly–commercial city; UNESCO listed."
        },
        "sources": [
          "src-waf-unesco-timbuktu-119",
          "src-waf-hunwick-timbuktu-orientation"
        ]
      },
      {
        "id": "site-djenne-old-towns",
        "names": {
          "zh": "杰内老城",
          "en": "Old Towns of Djenné",
          "native": "Djenné"
        },
        "kind_note": "Middle Niger urban mudbrick tradition; UNESCO WH",
        "region": "Mopti Region, Mali",
        "coords": null,
        "summary": {
          "zh": "中尼日尔泥砖城市传统；教科文名录。",
          "en": "Middle Niger mudbrick urban tradition; UNESCO listed."
        },
        "sources": [
          "src-waf-unesco-djenne-116",
          "src-waf-mcintosh-2005"
        ]
      },
      {
        "id": "site-koumbi-saleh-orientation",
        "names": {
          "zh": "昆比萨利赫（指针）",
          "en": "Koumbi Saleh (orientation)",
          "native": "Koumbi Saleh"
        },
        "kind_note": "Often identified with medieval Ghana capital in Arabic sources",
        "region": "Southeast Mauritania / Mali border zone",
        "coords": null,
        "summary": {
          "zh": "阿拉伯文献中常与加纳都城相联系的遗址指针；鉴定讨论开放。",
          "en": "Site orientation often linked to medieval Ghana's capital in Arabic sources; identification debates open."
        },
        "sources": [
          "src-waf-levtzion-hopkins-2000",
          "src-waf-mcintosh-2005"
        ]
      }
    ],
    "period": {
      "id": "period-west-africa-sahelian-empires",
      "names": {
        "zh": "萨赫勒帝国繁荣窗",
        "en": "Sahelian empire floruit"
      },
      "time": {
        "label": "broadly 8th–16th centuries CE (Ghana–Mali–Songhai working sequence)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Empire sequence labels only; absolute reign tables deferred."
      },
      "summary": {
        "zh": "壳级萨赫勒帝国窗。",
        "en": "Shell Sahelian empire window."
      },
      "sources": [
        "src-waf-levtzion-hopkins-2000",
        "src-waf-hunwick-timbuktu-orientation"
      ]
    },
    "object": {
      "id": "asm-waf-sahel-urban-manuscript-frame",
      "names": {
        "zh": "萨赫勒城市—手稿传统框架组合",
        "en": "Sahel urban–manuscript tradition frame"
      },
      "summary": {
        "zh": "壳级城市与手稿传统指针；无伪造馆藏号。",
        "en": "Shell urban and manuscript-tradition pointer; no forged catalog numbers."
      },
      "site_ids": [
        "site-timbuktu-medieval",
        "site-djenne-old-towns"
      ],
      "sources": [
        "src-waf-unesco-timbuktu-119",
        "src-waf-unesco-djenne-116"
      ]
    },
    "claim": {
      "id": "claim-waf-sahelian-urban-centres",
      "statement": {
        "zh": "教科文与学术综合将廷巴克图、杰内等表述为西非萨赫勒中世纪商业—学术—城市网络的关键节点（UNESCO 119、116；Levtzion & Hopkins 2000）。",
        "en": "UNESCO and scholarly syntheses frame Timbuktu, Djenné, and related nodes as key centres in West Africa's medieval Sahelian commercial–scholarly–urban networks (UNESCO 119, 116; Levtzion & Hopkins 2000)."
      },
      "site_ids": [
        "site-timbuktu-medieval",
        "site-djenne-old-towns"
      ],
      "sources": [
        "src-waf-unesco-timbuktu-119",
        "src-waf-unesco-djenne-116",
        "src-waf-levtzion-hopkins-2000"
      ]
    }
  },
  {
    "pack": "hallstatt-celtic",
    "civ_id": "civ-hallstatt-celtic",
    "names": {
      "zh": "哈尔施塔特—早期凯尔特",
      "en": "Hallstatt / early Celtic",
      "native": "Hallstatt"
    },
    "region": "Europe / Alpine–Danubian zone (Austria; south Germany; Bohemia contacts)",
    "time_span": "Hallstatt C–D / early La Tène broadly 8th–5th centuries BCE (Cunliffe / Kristiansen frames)",
    "summary": {
      "zh": "哈尔施塔特档案壳：Cunliffe 综合 + 哈尔施塔特–达赫施泰因教科文；library-seed。",
      "en": "Hallstatt archive shell: Cunliffe synthesis + Hallstatt–Dachstein UNESCO; library-seed."
    },
    "related_ids": [
      "civ-aegean",
      "civ-nuragic-sardinia"
    ],
    "sources": [
      {
        "id": "src-hallstatt-unesco-806",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Hallstatt-Dachstein / Salzkammergut Cultural Landscape. Inscribed 1997. https://whc.unesco.org/en/list/806/",
        "url": "https://whc.unesco.org/en/list/806/",
        "notes": "WHC cultural landscape including Hallstatt salt-mining heritage; tier T."
      },
      {
        "id": "src-hallstatt-cunliffe-1997",
        "type": "monograph",
        "tier": "S",
        "citation": "Cunliffe, Barry. 1997. The Ancient Celts. Oxford: Oxford University Press.",
        "url": null,
        "notes": "Major Celtic archaeology synthesis including Hallstatt/La Tène; print."
      },
      {
        "id": "src-hallstatt-kristiansen-larsson-2005",
        "type": "monograph",
        "tier": "S",
        "citation": "Kristiansen, Kristian, and Thomas B. Larsson. 2005. The Rise of Bronze Age Society: Travels, Transmissions and Transformations. Cambridge: Cambridge University Press.",
        "url": null,
        "notes": "European Bronze–Iron transition synthesis; print orientation."
      },
      {
        "id": "src-hallstatt-collis-2003",
        "type": "monograph",
        "tier": "S",
        "citation": "Collis, John. 2003. The Celts: Origins, Myths and Inventions. Stroud: Tempus.",
        "url": null,
        "notes": "Critical overview of Celtic labels; print; shell avoids ethnicity overclaim."
      },
      {
        "id": "src-hallstatt-nhm-vienna-orientation",
        "type": "web",
        "tier": "T",
        "citation": "Natural History Museum Vienna / Hallstatt research tradition — salt-mine and cemetery archaeology orientation.",
        "url": "https://www.nhm-wien.ac.at/en/research/prehistory",
        "notes": "Institutional orientation for Hallstatt research; tier T."
      }
    ],
    "sites": [
      {
        "id": "site-hallstatt-type",
        "names": {
          "zh": "哈尔施塔特（类型址）",
          "en": "Hallstatt (type site)",
          "native": "Hallstatt"
        },
        "kind_note": "Salt-mining and cemetery type site; UNESCO cultural landscape",
        "region": "Salzkammergut, Upper Austria",
        "coords": null,
        "summary": {
          "zh": "盐矿与墓地类型址；教科文文化景观组成部分。",
          "en": "Salt-mine and cemetery type site; part of UNESCO cultural landscape."
        },
        "sources": [
          "src-hallstatt-unesco-806",
          "src-hallstatt-nhm-vienna-orientation",
          "src-hallstatt-cunliffe-1997"
        ]
      },
      {
        "id": "site-hallstatt-princely-orientation",
        "names": {
          "zh": "哈尔施塔特“王侯”中心（指针）",
          "en": "Hallstatt princely centres (orientation)",
          "native": null
        },
        "kind_note": "Regional fortified/elite centres of Hallstatt D / early La Tène",
        "region": "West-central Europe",
        "coords": null,
        "summary": {
          "zh": "区域设防/精英中心指针；非单一点。",
          "en": "Regional fortified/elite-centre orientation; not a single point."
        },
        "sources": [
          "src-hallstatt-cunliffe-1997",
          "src-hallstatt-collis-2003"
        ]
      }
    ],
    "period": {
      "id": "period-hallstatt-cd-early-latene",
      "names": {
        "zh": "哈尔施塔特 C–D / 早期拉坦诺窗",
        "en": "Hallstatt C–D / early La Tène window"
      },
      "time": {
        "label": "ca. 8th–5th centuries BCE (Cunliffe working frame)",
        "approx_from_bce": 800,
        "approx_to_bce": 400,
        "scheme_note": "Absolute phase tables vary by region; shell window only."
      },
      "summary": {
        "zh": "壳级哈尔施塔特—早期拉坦诺窗。",
        "en": "Shell Hallstatt–early La Tène window."
      },
      "sources": [
        "src-hallstatt-cunliffe-1997",
        "src-hallstatt-kristiansen-larsson-2005"
      ]
    },
    "object": {
      "id": "asm-hallstatt-salt-burial-frame",
      "names": {
        "zh": "哈尔施塔特盐矿—墓葬框架组合",
        "en": "Hallstatt salt-mine / burial frame"
      },
      "summary": {
        "zh": "壳级盐矿与墓葬传统指针。",
        "en": "Shell salt-mine and burial-tradition pointer."
      },
      "site_ids": [
        "site-hallstatt-type"
      ],
      "sources": [
        "src-hallstatt-unesco-806",
        "src-hallstatt-nhm-vienna-orientation"
      ]
    },
    "claim": {
      "id": "claim-hallstatt-type-salt-landscape",
      "statement": {
        "zh": "教科文与学术综合将哈尔施塔特表述为阿尔卑斯盐矿与铁器时代早期精英墓葬传统的类型景观（UNESCO 806；Cunliffe 1997）。",
        "en": "UNESCO and scholarly syntheses frame Hallstatt as a type landscape of Alpine salt mining and Early Iron Age elite burial traditions (UNESCO 806; Cunliffe 1997)."
      },
      "site_ids": [
        "site-hallstatt-type"
      ],
      "sources": [
        "src-hallstatt-unesco-806",
        "src-hallstatt-cunliffe-1997"
      ]
    }
  },
  {
    "pack": "nuragic-sardinia",
    "civ_id": "civ-nuragic-sardinia",
    "names": {
      "zh": "努拉吉（撒丁）",
      "en": "Nuragic Sardinia",
      "native": "Nuragic / Nuraghe"
    },
    "region": "Europe / Sardinia (Mediterranean island)",
    "time_span": "Nuragic florescence broadly Mid–Late Bronze to Early Iron Age (Lilliu / Webster frames)",
    "summary": {
      "zh": "努拉吉档案壳：Lilliu/Webster + 巴鲁米尼苏努拉西教科文；library-seed。",
      "en": "Nuragic archive shell: Lilliu/Webster + Su Nuraxi di Barumini UNESCO; library-seed."
    },
    "related_ids": [
      "civ-aegean",
      "civ-phoenician",
      "civ-hallstatt-celtic"
    ],
    "sources": [
      {
        "id": "src-nuragic-unesco-833",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Su Nuraxi di Barumini. Inscribed 1997. https://whc.unesco.org/en/list/833/",
        "url": "https://whc.unesco.org/en/list/833/",
        "notes": "WHC orientation for Su Nuraxi; tier T."
      },
      {
        "id": "src-nuragic-lilliu-1988",
        "type": "monograph",
        "tier": "S",
        "citation": "Lilliu, Giovanni. 1988. La civiltà nuragica. Sassari: Carlo Delfino. (And related Lilliu syntheses of Nuragic civilization.)",
        "url": null,
        "notes": "Foundational Italian synthesis; print; shell TOC-level."
      },
      {
        "id": "src-nuragic-webster-1996",
        "type": "monograph",
        "tier": "S",
        "citation": "Webster, Gary S. 1996. A Prehistory of Sardinia 2300–500 BC. Sheffield: Sheffield Academic Press.",
        "url": null,
        "notes": "English-language Sardinia prehistory synthesis; print."
      },
      {
        "id": "src-nuragic-blake-1999",
        "type": "article",
        "tier": "S",
        "citation": "Blake, Emma. 1999. Identity-Mapping in the Sardinian Bronze Age. European Journal of Archaeology 2(1): 35–55.",
        "url": null,
        "notes": "Identity and landscape discussion; article orientation."
      },
      {
        "id": "src-nuragic-trump-orientation",
        "type": "monograph",
        "tier": "S",
        "citation": "Trump, David H. — Nuraghe and Sardinian prehistory field guides / excavation notes tradition.",
        "url": null,
        "notes": "Field-guide and excavation orientation pointer."
      }
    ],
    "sites": [
      {
        "id": "site-su-nuraxi-barumini",
        "names": {
          "zh": "巴鲁米尼苏努拉西",
          "en": "Su Nuraxi di Barumini",
          "native": "Su Nuraxi"
        },
        "kind_note": "Nuraghe complex type site; UNESCO WH",
        "region": "Medio Campidano, Sardinia, Italy",
        "coords": null,
        "summary": {
          "zh": "努拉吉石塔聚落类型址；教科文名录。",
          "en": "Nuraghe stone-tower settlement type site; UNESCO listed."
        },
        "sources": [
          "src-nuragic-unesco-833",
          "src-nuragic-lilliu-1988",
          "src-nuragic-webster-1996"
        ]
      },
      {
        "id": "site-nuragic-landscape-orientation",
        "names": {
          "zh": "撒丁努拉吉景观（指针）",
          "en": "Sardinian Nuragic landscape (orientation)",
          "native": null
        },
        "kind_note": "Island-wide nuraghe distribution frame",
        "region": "Sardinia",
        "coords": null,
        "summary": {
          "zh": "全岛努拉吉分布指针；非单一点。",
          "en": "Island-wide nuraghe distribution pointer; not a single point."
        },
        "sources": [
          "src-nuragic-webster-1996",
          "src-nuragic-blake-1999"
        ]
      }
    ],
    "period": {
      "id": "period-nuragic-bronze-iron",
      "names": {
        "zh": "努拉吉青铜—早期铁器窗",
        "en": "Nuragic Bronze–Early Iron window"
      },
      "time": {
        "label": "Mid–Late Bronze to Early Iron Age (Webster / Lilliu working labels)",
        "approx_from_bce": 1700,
        "approx_to_bce": 700,
        "scheme_note": "Absolute subdivision deferred; shell window only."
      },
      "summary": {
        "zh": "壳级努拉吉窗。",
        "en": "Shell Nuragic window."
      },
      "sources": [
        "src-nuragic-webster-1996",
        "src-nuragic-lilliu-1988"
      ]
    },
    "object": {
      "id": "asm-nuragic-tower-village-frame",
      "names": {
        "zh": "努拉吉石塔—村落框架组合",
        "en": "Nuragic tower–village frame"
      },
      "summary": {
        "zh": "壳级石塔与环绕村落指针。",
        "en": "Shell tower-and-village architecture pointer."
      },
      "site_ids": [
        "site-su-nuraxi-barumini"
      ],
      "sources": [
        "src-nuragic-unesco-833",
        "src-nuragic-lilliu-1988"
      ]
    },
    "claim": {
      "id": "claim-nuragic-su-nuraxi-type",
      "statement": {
        "zh": "教科文将巴鲁米尼苏努拉西表述为撒丁努拉吉文明石塔建筑最完整的例证之一（UNESCO 833）。",
        "en": "UNESCO frames Su Nuraxi di Barumini as one of the most complete examples of Nuragic stone-tower architecture on Sardinia (UNESCO 833)."
      },
      "site_ids": [
        "site-su-nuraxi-barumini"
      ],
      "sources": [
        "src-nuragic-unesco-833",
        "src-nuragic-webster-1996"
      ]
    }
  },
  {
    "pack": "rapa-nui",
    "civ_id": "civ-rapa-nui",
    "names": {
      "zh": "拉帕努伊（复活节岛）",
      "en": "Rapa Nui (Easter Island)",
      "native": "Rapa Nui"
    },
    "region": "Oceania / southeastern Pacific (Chilean Polynesia)",
    "time_span": "Polynesian settlement to monumental moai florescence broadly late 1st–early 2nd millennium CE (Hunt–Lipo / Martinsson-Wallin frames; ethics-first)",
    "summary": {
      "zh": "拉帕努伊档案壳：伦理优先；Hunt–Lipo/Martinsson-Wallin + 教科文；library-seed。",
      "en": "Rapa Nui archive shell: ethics-first; Hunt–Lipo/Martinsson-Wallin + UNESCO; library-seed."
    },
    "related_ids": [
      "civ-lapita-pacific"
    ],
    "sources": [
      {
        "id": "src-rapanui-unesco-715",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Rapa Nui National Park. Inscribed 1995. https://whc.unesco.org/en/list/715/",
        "url": "https://whc.unesco.org/en/list/715/",
        "notes": "WHC orientation; tier T; ethics: community and heritage protocols apply."
      },
      {
        "id": "src-rapanui-hunt-lipo-2011",
        "type": "monograph",
        "tier": "S",
        "citation": "Hunt, Terry L., and Carl P. Lipo. 2011. The Statues That Walked: Unraveling the Mystery of Easter Island. New York: Free Press.",
        "url": null,
        "notes": "Revisionist synthesis; contested models — shell cites as S, not settled fact."
      },
      {
        "id": "src-rapanui-martinsson-wallin-orientation",
        "type": "monograph",
        "tier": "S",
        "citation": "Martinsson-Wallin, Helene, and Paul Wallin, eds. — Rapa Nui archaeology collected studies / Uppsala–Gotland research tradition.",
        "url": null,
        "notes": "Field research tradition pointer; deepen with specific volume citations."
      },
      {
        "id": "src-rapanui-van-tilburg-1994",
        "type": "monograph",
        "tier": "S",
        "citation": "Van Tilburg, Jo Anne. 1994. Easter Island: Archaeology, Ecology and Culture. London: British Museum Press.",
        "url": null,
        "notes": "BM Press synthesis; print; moai research orientation."
      },
      {
        "id": "src-rapanui-stevenson-orientation",
        "type": "article",
        "tier": "S",
        "citation": "Stevenson, Christopher M., and collaborators — Rapa Nui chronology and settlement studies (journal tradition).",
        "url": null,
        "notes": "Chronology/settlement orientation; no invented dates."
      }
    ],
    "sites": [
      {
        "id": "site-rapa-nui-national-park",
        "names": {
          "zh": "拉帕努伊国家公园",
          "en": "Rapa Nui National Park",
          "native": "Rapa Nui"
        },
        "kind_note": "Island ceremonial landscape with moai / ahu; UNESCO WH",
        "region": "Easter Island, Chile",
        "coords": null,
        "summary": {
          "zh": "摩艾与阿胡仪礼景观；教科文名录；伦理优先。",
          "en": "Moai and ahu ceremonial landscape; UNESCO listed; ethics-first packing."
        },
        "sources": [
          "src-rapanui-unesco-715",
          "src-rapanui-van-tilburg-1994"
        ]
      },
      {
        "id": "site-rapanui-orongo-orientation",
        "names": {
          "zh": "奥龙戈（指针）",
          "en": "Orongo (orientation)",
          "native": "Orongo"
        },
        "kind_note": "Ceremonial village associated with birdman cult narratives",
        "region": "Southwestern Rapa Nui",
        "coords": null,
        "summary": {
          "zh": "与鸟人仪礼叙述相关的仪礼村指针。",
          "en": "Ceremonial-village orientation linked to birdman-cult narratives."
        },
        "sources": [
          "src-rapanui-unesco-715",
          "src-rapanui-martinsson-wallin-orientation"
        ]
      }
    ],
    "period": {
      "id": "period-rapa-nui-monumental",
      "names": {
        "zh": "拉帕努伊纪念建筑繁荣窗",
        "en": "Rapa Nui monumental floruit"
      },
      "time": {
        "label": "late 1st–early 2nd millennium CE working window (debated)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Settlement and collapse models contested; shell window only."
      },
      "summary": {
        "zh": "壳级拉帕努伊窗；年代争论开放。",
        "en": "Shell Rapa Nui window; chronological debates open."
      },
      "sources": [
        "src-rapanui-hunt-lipo-2011",
        "src-rapanui-stevenson-orientation"
      ]
    },
    "object": {
      "id": "asm-rapanui-moai-ahu-frame",
      "names": {
        "zh": "摩艾—阿胡框架组合",
        "en": "Moai–ahu frame assemblage"
      },
      "summary": {
        "zh": "壳级摩艾与阿胡指针；无伪造图像或馆藏号。",
        "en": "Shell moai–ahu pointer; no forged images or catalog numbers."
      },
      "site_ids": [
        "site-rapa-nui-national-park"
      ],
      "sources": [
        "src-rapanui-unesco-715",
        "src-rapanui-van-tilburg-1994"
      ]
    },
    "claim": {
      "id": "claim-rapanui-moai-landscape",
      "statement": {
        "zh": "教科文将拉帕努伊国家公园表述为以摩艾石像与阿胡平台为标志的波利尼西亚仪礼景观（UNESCO 715）。",
        "en": "UNESCO frames Rapa Nui National Park as a Polynesian ceremonial landscape marked by moai statues and ahu platforms (UNESCO 715)."
      },
      "site_ids": [
        "site-rapa-nui-national-park"
      ],
      "sources": [
        "src-rapanui-unesco-715",
        "src-rapanui-van-tilburg-1994"
      ]
    }
  },
  {
    "pack": "inca",
    "civ_id": "civ-inca",
    "names": {
      "zh": "印加",
      "en": "Inca (Tawantinsuyu)",
      "native": "Tawantinsuyu"
    },
    "region": "South America / Andean highlands and coast (Cusco heartland; empire span)",
    "time_span": "Late Horizon empire floruit broadly 15th–early 16th centuries CE (D'Altroy / McEwan frames)",
    "summary": {
      "zh": "印加档案壳：D'Altroy/McEwan + 库斯科/马丘比丘教科文；library-seed。",
      "en": "Inca archive shell: D'Altroy/McEwan + Cusco/Machu Picchu UNESCO; library-seed."
    },
    "related_ids": [
      "civ-andes",
      "civ-wari",
      "civ-tiwanaku",
      "civ-moche"
    ],
    "sources": [
      {
        "id": "src-inca-unesco-cusco-273",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. City of Cuzco. Inscribed 1983. https://whc.unesco.org/en/list/273/",
        "url": "https://whc.unesco.org/en/list/273/",
        "notes": "WHC orientation for Cusco; tier T."
      },
      {
        "id": "src-inca-unesco-machu-picchu-274",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Historic Sanctuary of Machu Picchu. Inscribed 1983. https://whc.unesco.org/en/list/274/",
        "url": "https://whc.unesco.org/en/list/274/",
        "notes": "WHC orientation for Machu Picchu; tier T."
      },
      {
        "id": "src-inca-daltroy-2014",
        "type": "monograph",
        "tier": "S",
        "citation": "D'Altroy, Terence N. 2014. The Incas. 2nd ed. The Peoples of America. Chichester: Wiley-Blackwell.",
        "url": null,
        "notes": "Standard English synthesis; print; shell TOC-level."
      },
      {
        "id": "src-inca-mcewan-2006",
        "type": "monograph",
        "tier": "S",
        "citation": "McEwan, Gordon F. 2006. The Incas: New Perspectives. Santa Barbara: ABC-CLIO / Norton.",
        "url": null,
        "notes": "Accessible synthesis; print."
      },
      {
        "id": "src-inca-hyslop-1990",
        "type": "monograph",
        "tier": "S",
        "citation": "Hyslop, John. 1990. Inka Settlement Planning. Austin: University of Texas Press.",
        "url": null,
        "notes": "Settlement planning monograph; print orientation."
      }
    ],
    "sites": [
      {
        "id": "site-cusco-inca",
        "names": {
          "zh": "库斯科",
          "en": "Cusco (Cuzco)",
          "native": "Qosqo"
        },
        "kind_note": "Inca imperial capital; UNESCO WH",
        "region": "Cusco Region, Peru",
        "coords": null,
        "summary": {
          "zh": "印加帝国都城；教科文名录。",
          "en": "Inca imperial capital; UNESCO listed."
        },
        "sources": [
          "src-inca-unesco-cusco-273",
          "src-inca-daltroy-2014"
        ]
      },
      {
        "id": "site-machu-picchu",
        "names": {
          "zh": "马丘比丘",
          "en": "Machu Picchu",
          "native": "Machu Picchu"
        },
        "kind_note": "Royal estate / ceremonial complex; UNESCO WH",
        "region": "Cusco Region, Peru",
        "coords": null,
        "summary": {
          "zh": "皇家庄园/仪礼建筑群；教科文名录。",
          "en": "Royal estate / ceremonial complex; UNESCO listed."
        },
        "sources": [
          "src-inca-unesco-machu-picchu-274",
          "src-inca-mcewan-2006"
        ]
      }
    ],
    "period": {
      "id": "period-inca-late-horizon",
      "names": {
        "zh": "印加晚地平线繁荣窗",
        "en": "Inca Late Horizon floruit"
      },
      "time": {
        "label": "broadly 15th–early 16th centuries CE (D'Altroy working frame)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Expansion chronology debated; shell window only."
      },
      "summary": {
        "zh": "壳级晚地平线窗。",
        "en": "Shell Late Horizon window."
      },
      "sources": [
        "src-inca-daltroy-2014",
        "src-inca-mcewan-2006"
      ]
    },
    "object": {
      "id": "asm-inca-masonry-road-frame",
      "names": {
        "zh": "印加石工—道路框架组合",
        "en": "Inca masonry–road frame"
      },
      "summary": {
        "zh": "壳级精细石工与道路网指针。",
        "en": "Shell fine masonry and road-network pointer."
      },
      "site_ids": [
        "site-cusco-inca",
        "site-machu-picchu"
      ],
      "sources": [
        "src-inca-unesco-cusco-273",
        "src-inca-hyslop-1990"
      ]
    },
    "claim": {
      "id": "claim-inca-cusco-machu-picchu",
      "statement": {
        "zh": "教科文与学术综合将库斯科与马丘比丘表述为印加（Tawantinsuyu）晚期帝国高地建筑与政治中心的代表（UNESCO 273、274；D'Altroy 2014）。",
        "en": "UNESCO and scholarly syntheses frame Cusco and Machu Picchu as representative highland architectural and political centres of the late Inca (Tawantinsuyu) empire (UNESCO 273, 274; D'Altroy 2014)."
      },
      "site_ids": [
        "site-cusco-inca",
        "site-machu-picchu"
      ],
      "sources": [
        "src-inca-unesco-cusco-273",
        "src-inca-unesco-machu-picchu-274",
        "src-inca-daltroy-2014"
      ]
    }
  },
  {
    "pack": "moche",
    "civ_id": "civ-moche",
    "names": {
      "zh": "莫切",
      "en": "Moche",
      "native": "Moche / Mochica"
    },
    "region": "South America / north coast Peru (Moche–Chicama–Lambayeque valleys)",
    "time_span": "Early Intermediate / Moche florescence broadly 1st–8th centuries CE (Quilter / Castillo frames)",
    "summary": {
      "zh": "莫切档案壳：Quilter/Castillo + 太阳/月亮金字塔发掘传统；library-seed。",
      "en": "Moche archive shell: Quilter/Castillo + Huacas de Moche excavation tradition; library-seed."
    },
    "related_ids": [
      "civ-andes",
      "civ-chavin",
      "civ-inca"
    ],
    "sources": [
      {
        "id": "src-moche-quilter-2010",
        "type": "monograph",
        "tier": "S",
        "citation": "Quilter, Jeffrey. 2010. The Moche of Ancient Peru: Media and Messages. Cambridge, MA: Peabody Museum Press / Harvard University.",
        "url": null,
        "notes": "Accessible Moche synthesis; print."
      },
      {
        "id": "src-moche-castillo-uceda-orientation",
        "type": "excavation-report",
        "tier": "P",
        "citation": "Castillo Butters, Luis Jaime, and Santiago Uceda Castillo — Huaca de la Luna / Huacas de Moche excavation program publications.",
        "url": null,
        "notes": "Primary excavation tradition pointer; no invented inventories."
      },
      {
        "id": "src-moche-donnan-mcclelland-1999",
        "type": "monograph",
        "tier": "S",
        "citation": "Donnan, Christopher B., and Donna McClelland. 1999. Moche Fineline Painting: Its Evolution and Its Artists. Los Angeles: UCLA Fowler Museum.",
        "url": null,
        "notes": "Fineline ceramic iconography corpus; print."
      },
      {
        "id": "src-moche-bourget-2006",
        "type": "monograph",
        "tier": "S",
        "citation": "Bourget, Steve. 2006. Sex, Death, and Sacrifice in Moche Religion and Visual Culture. Austin: University of Texas Press.",
        "url": null,
        "notes": "Religion and visual culture study; print; contested interpretations noted."
      },
      {
        "id": "src-moche-huacas-project-web",
        "type": "web",
        "tier": "T",
        "citation": "Proyecto Huacas del Sol y de la Luna / Universidad Nacional de Trujillo — institutional project orientation.",
        "url": "https://www.huacasdemoche.pe/",
        "notes": "Project portal orientation; tier T; deepen with peer-reviewed reports."
      }
    ],
    "sites": [
      {
        "id": "site-huacas-de-moche",
        "names": {
          "zh": "莫切太阳与月亮金字塔",
          "en": "Huacas de Moche (Sol y Luna)",
          "native": "Huacas de Moche"
        },
        "kind_note": "Moche ceremonial–urban capital complex",
        "region": "La Libertad, Peru",
        "coords": null,
        "summary": {
          "zh": "莫切仪礼—城市核心建筑群；长期发掘项目。",
          "en": "Moche ceremonial–urban core complex; long-term excavation project."
        },
        "sources": [
          "src-moche-castillo-uceda-orientation",
          "src-moche-huacas-project-web",
          "src-moche-quilter-2010"
        ]
      },
      {
        "id": "site-sipan-orientation",
        "names": {
          "zh": "西潘（指针）",
          "en": "Sipán (orientation)",
          "native": "Sipán"
        },
        "kind_note": "Elite Moche burial complex (Lambayeque)",
        "region": "Lambayeque, Peru",
        "coords": null,
        "summary": {
          "zh": "莫切精英墓葬发现指针；与皇家陵墓博物馆传统相关。",
          "en": "Elite Moche burial discovery orientation; linked to Museo Tumbas Reales tradition."
        },
        "sources": [
          "src-moche-quilter-2010",
          "src-moche-donnan-mcclelland-1999"
        ]
      }
    ],
    "period": {
      "id": "period-moche-eip-floruit",
      "names": {
        "zh": "莫切早期中间期繁荣窗",
        "en": "Moche Early Intermediate floruit"
      },
      "time": {
        "label": "broadly 1st–8th centuries CE (Quilter / Castillo working frame)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Phase I–V debates open; shell window only."
      },
      "summary": {
        "zh": "壳级莫切窗。",
        "en": "Shell Moche window."
      },
      "sources": [
        "src-moche-quilter-2010",
        "src-moche-castillo-uceda-orientation"
      ]
    },
    "object": {
      "id": "asm-moche-fineline-ceramic-frame",
      "names": {
        "zh": "莫切细线彩陶框架组合",
        "en": "Moche fineline ceramic frame"
      },
      "summary": {
        "zh": "壳级细线彩陶与肖像指针；无伪造馆藏号。",
        "en": "Shell fineline ceramic and portraiture pointer; no forged catalog numbers."
      },
      "site_ids": [
        "site-huacas-de-moche"
      ],
      "sources": [
        "src-moche-donnan-mcclelland-1999",
        "src-moche-quilter-2010"
      ]
    },
    "claim": {
      "id": "claim-moche-north-coast-polities",
      "statement": {
        "zh": "学术综合将莫切表述为秘鲁北部海岸早期中间期以大型金字塔神庙与细线彩陶为标志的复杂社会（Quilter 2010；Huacas de Moche 发掘传统）。",
        "en": "Scholarly syntheses frame Moche as Early Intermediate complex societies of Peru's north coast marked by monumental huacas and fineline ceramics (Quilter 2010; Huacas de Moche excavation tradition)."
      },
      "site_ids": [
        "site-huacas-de-moche"
      ],
      "sources": [
        "src-moche-quilter-2010",
        "src-moche-castillo-uceda-orientation"
      ]
    }
  },
  {
    "pack": "aztec",
    "civ_id": "civ-aztec",
    "names": {
      "zh": "阿兹特克（墨西卡）",
      "en": "Aztec (Mexica)",
      "native": "Mexica / Triple Alliance"
    },
    "region": "Mesoamerica / Basin of Mexico (Tenochtitlan–Tlatelolco)",
    "time_span": "Late Postclassic Triple Alliance floruit broadly 14th–early 16th centuries CE (Smith / Matos Moctezuma frames)",
    "summary": {
      "zh": "阿兹特克档案壳：Smith/Matos + 大神庙发掘；library-seed。",
      "en": "Aztec archive shell: Smith/Matos + Templo Mayor excavations; library-seed."
    },
    "related_ids": [
      "civ-teotihuacan",
      "civ-classic-maya",
      "civ-zapotec"
    ],
    "sources": [
      {
        "id": "src-aztec-smith-2012",
        "type": "monograph",
        "tier": "S",
        "citation": "Smith, Michael E. 2012. The Aztecs. 3rd ed. The Peoples of America. Chichester: Wiley-Blackwell.",
        "url": null,
        "notes": "Standard English synthesis; print; shell TOC-level."
      },
      {
        "id": "src-aztec-matos-templo-mayor",
        "type": "excavation-report",
        "tier": "P",
        "citation": "Matos Moctezuma, Eduardo — Templo Mayor Project excavation reports and syntheses (INAH / Mexico City).",
        "url": null,
        "notes": "Primary excavation tradition for Tenochtitlan ceremonial centre."
      },
      {
        "id": "src-aztec-unesco-mexico-city-412",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Historic Centre of Mexico City and Xochimilco. Inscribed 1987. https://whc.unesco.org/en/list/412/",
        "url": "https://whc.unesco.org/en/list/412/",
        "notes": "WHC includes historic centre overlying Tenochtitlan; tier T orientation."
      },
      {
        "id": "src-aztec-lopez-austin-lopez-lujan",
        "type": "monograph",
        "tier": "S",
        "citation": "López Austin, Alfredo, and Leonardo López Luján — Mexica religion, cosmology, and Templo Mayor studies.",
        "url": null,
        "notes": "Religion and Templo Mayor scholarship pointer."
      },
      {
        "id": "src-aztec-inah-templo-mayor-web",
        "type": "web",
        "tier": "T",
        "citation": "INAH / Museo del Templo Mayor — institutional orientation for Templo Mayor archaeology.",
        "url": "https://www.templomayor.inah.gob.mx/",
        "notes": "Museum/project portal; tier T."
      }
    ],
    "sites": [
      {
        "id": "site-templo-mayor-tenochtitlan",
        "names": {
          "zh": "特诺奇蒂特兰大神庙",
          "en": "Templo Mayor (Tenochtitlan)",
          "native": "Huey Teocalli"
        },
        "kind_note": "Mexica twin-temple ceremonial centre",
        "region": "Mexico City, Mexico",
        "coords": null,
        "summary": {
          "zh": "墨西卡双神庙仪礼中心；INAH 长期发掘。",
          "en": "Mexica twin-temple ceremonial centre; long-term INAH excavations."
        },
        "sources": [
          "src-aztec-matos-templo-mayor",
          "src-aztec-inah-templo-mayor-web",
          "src-aztec-smith-2012"
        ]
      },
      {
        "id": "site-tlatelolco-orientation",
        "names": {
          "zh": "特拉特洛尔科（指针）",
          "en": "Tlatelolco (orientation)",
          "native": "Tlatelolco"
        },
        "kind_note": "Sister city / market centre of the Mexica capital zone",
        "region": "Mexico City, Mexico",
        "coords": null,
        "summary": {
          "zh": "墨西卡都城区姊妹城/市场中心指针。",
          "en": "Sister-city / market-centre orientation in the Mexica capital zone."
        },
        "sources": [
          "src-aztec-smith-2012",
          "src-aztec-unesco-mexico-city-412"
        ]
      }
    ],
    "period": {
      "id": "period-aztec-late-postclassic",
      "names": {
        "zh": "阿兹特克晚后经典繁荣窗",
        "en": "Aztec Late Postclassic floruit"
      },
      "time": {
        "label": "broadly 14th–early 16th centuries CE (Smith working frame)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Triple Alliance chronology; Spanish contact endpoint noted but not moralized."
      },
      "summary": {
        "zh": "壳级晚后经典窗。",
        "en": "Shell Late Postclassic window."
      },
      "sources": [
        "src-aztec-smith-2012",
        "src-aztec-matos-templo-mayor"
      ]
    },
    "object": {
      "id": "asm-aztec-templo-mayor-offerings-frame",
      "names": {
        "zh": "大神庙祭献框架组合",
        "en": "Templo Mayor offerings frame"
      },
      "summary": {
        "zh": "壳级祭献与双神庙建筑指针；无伪造馆藏号。",
        "en": "Shell offerings and twin-temple architecture pointer; no forged catalog numbers."
      },
      "site_ids": [
        "site-templo-mayor-tenochtitlan"
      ],
      "sources": [
        "src-aztec-matos-templo-mayor",
        "src-aztec-lopez-austin-lopez-lujan"
      ]
    },
    "claim": {
      "id": "claim-aztec-templo-mayor-centre",
      "statement": {
        "zh": "学术与博物馆综合将大神庙表述为特诺奇蒂特兰墨西卡三重同盟都城的核心仪礼建筑（Matos Moctezuma 发掘传统；Smith 2012）。",
        "en": "Scholarly and museum syntheses frame the Templo Mayor as the central ceremonial architecture of Mexica Triple Alliance Tenochtitlan (Matos Moctezuma excavation tradition; Smith 2012)."
      },
      "site_ids": [
        "site-templo-mayor-tenochtitlan"
      ],
      "sources": [
        "src-aztec-matos-templo-mayor",
        "src-aztec-smith-2012"
      ]
    }
  },
  {
    "pack": "angkor",
    "civ_id": "civ-angkor",
    "names": {
      "zh": "吴哥（高棉）",
      "en": "Angkor (Khmer)",
      "native": "Yasodharapura / Angkor"
    },
    "region": "Southeast Asia / Cambodia (Tonlé Sap basin; Khmer empire heartland)",
    "time_span": "Angkorian florescence broadly 9th–15th centuries CE (Coe–Evans / Jacques frames)",
    "summary": {
      "zh": "吴哥档案壳：Coe–Evans/Jacques + 教科文；library-seed。",
      "en": "Angkor archive shell: Coe–Evans/Jacques + UNESCO; library-seed."
    },
    "related_ids": [
      "civ-dong-son",
      "civ-ban-chiang"
    ],
    "sources": [
      {
        "id": "src-angkor-unesco-668",
        "type": "web",
        "tier": "T",
        "citation": "UNESCO World Heritage Centre. Angkor. Inscribed 1992. https://whc.unesco.org/en/list/668/",
        "url": "https://whc.unesco.org/en/list/668/",
        "notes": "WHC orientation for Angkor; tier T."
      },
      {
        "id": "src-angkor-coe-evans-2018",
        "type": "monograph",
        "tier": "S",
        "citation": "Coe, Michael D., and Damian Evans. 2018. Angkor and the Khmer Civilization. 2nd ed. London: Thames and Hudson.",
        "url": null,
        "notes": "Updated synthesis including lidar landscape results; print."
      },
      {
        "id": "src-angkor-jacques-lafond-2007",
        "type": "monograph",
        "tier": "S",
        "citation": "Jacques, Claude, and Philippe Lafond. 2007. The Khmer Empire: Cities and Sanctuaries from the 5th to the 13th Century. Bangkok: River Books.",
        "url": null,
        "notes": "Cities and sanctuaries overview; print."
      },
      {
        "id": "src-angkor-evans-lidar-orientation",
        "type": "article",
        "tier": "S",
        "citation": "Evans, Damian, et al. — Angkor lidar landscape archaeology publications (PNAS / Antiquity tradition).",
        "url": null,
        "notes": "Lidar urban-landscape orientation; deepen with specific article citations."
      },
      {
        "id": "src-angkor-apsara-orientation",
        "type": "web",
        "tier": "T",
        "citation": "APSARA National Authority — Angkor heritage management institutional orientation.",
        "url": "https://apsaraauthority.gov.kh/",
        "notes": "Heritage authority portal; tier T."
      }
    ],
    "sites": [
      {
        "id": "site-angkor-wat",
        "names": {
          "zh": "吴哥窟",
          "en": "Angkor Wat",
          "native": "Angkor Wat"
        },
        "kind_note": "State temple / temple-mountain; UNESCO WH component",
        "region": "Siem Reap Province, Cambodia",
        "coords": null,
        "summary": {
          "zh": "国家庙山；教科文吴哥名录核心组成部分。",
          "en": "State temple-mountain; core component of UNESCO Angkor listing."
        },
        "sources": [
          "src-angkor-unesco-668",
          "src-angkor-coe-evans-2018"
        ]
      },
      {
        "id": "site-angkor-thom",
        "names": {
          "zh": "吴哥城",
          "en": "Angkor Thom",
          "native": "Angkor Thom"
        },
        "kind_note": "Late Angkorian fortified urban core",
        "region": "Siem Reap Province, Cambodia",
        "coords": null,
        "summary": {
          "zh": "晚期吴哥设防城市核心。",
          "en": "Late Angkorian fortified urban core."
        },
        "sources": [
          "src-angkor-unesco-668",
          "src-angkor-jacques-lafond-2007"
        ]
      },
      {
        "id": "site-angkor-hydraulic-orientation",
        "names": {
          "zh": "吴哥水利景观（指针）",
          "en": "Angkor hydraulic landscape (orientation)",
          "native": null
        },
        "kind_note": "Baray / canal urban-agrarian landscape frame",
        "region": "Greater Angkor region",
        "coords": null,
        "summary": {
          "zh": "巴莱与运河城市—农业景观指针；激光雷达研究相关。",
          "en": "Baray and canal urban–agrarian landscape pointer; lidar research related."
        },
        "sources": [
          "src-angkor-evans-lidar-orientation",
          "src-angkor-coe-evans-2018"
        ]
      }
    ],
    "period": {
      "id": "period-angkorian-floruit",
      "names": {
        "zh": "吴哥繁荣窗",
        "en": "Angkorian floruit"
      },
      "time": {
        "label": "broadly 9th–15th centuries CE (Coe–Evans working frame)",
        "approx_from_bce": null,
        "approx_to_bce": null,
        "scheme_note": "Reign and temple chronologies deferred to densify."
      },
      "summary": {
        "zh": "壳级吴哥窗。",
        "en": "Shell Angkorian window."
      },
      "sources": [
        "src-angkor-coe-evans-2018",
        "src-angkor-jacques-lafond-2007"
      ]
    },
    "object": {
      "id": "asm-angkor-temple-mountain-frame",
      "names": {
        "zh": "吴哥庙山—水利框架组合",
        "en": "Angkor temple-mountain / hydraulic frame"
      },
      "summary": {
        "zh": "壳级庙山与水利景观指针。",
        "en": "Shell temple-mountain and hydraulic-landscape pointer."
      },
      "site_ids": [
        "site-angkor-wat",
        "site-angkor-thom"
      ],
      "sources": [
        "src-angkor-unesco-668",
        "src-angkor-coe-evans-2018"
      ]
    },
    "claim": {
      "id": "claim-angkor-khmer-capital-landscape",
      "statement": {
        "zh": "教科文与学术综合将吴哥表述为高棉帝国以庙山与大型水利景观为标志的首都区域（UNESCO 668；Coe & Evans 2018）。",
        "en": "UNESCO and scholarly syntheses frame Angkor as the Khmer imperial capital region marked by temple-mountains and large-scale hydraulic landscapes (UNESCO 668; Coe & Evans 2018)."
      },
      "site_ids": [
        "site-angkor-wat",
        "site-angkor-thom"
      ],
      "sources": [
        "src-angkor-unesco-668",
        "src-angkor-coe-evans-2018"
      ]
    }
  }
]
""")
