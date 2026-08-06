#!/usr/bin/env python3
# 对外官网（afafreight.com）中英双语文案表。
# 改文案只改这里，两个语言版本由 build_dist.py 用同一套 HTML 模板渲染。
# 口径来源：docs/02-business/全链条商业模式与Sigma融合.md、CLAUDE.md（公司名 / 用语规范）。
#
# 注意：
#   1. 公司名一律「非快达」/ AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED；
#   2. 不写未经核实的排名类表述（如「最大清关公司」），不写具体运价与财务数字——那些属于融资页；
#   3. 不宣称尚未注册的办公实体，只写业务覆盖城市。

MAIL = 'contact@afafreight.com'

ZH = {
    'lang': 'zh-CN',
    'locale': 'zh_CN',
    'title': '非快达 AFA · 中国—东非全链条物流与清关',
    'desc': '非快达 AFA（AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED）：中国—东非海空双通道全链条物流与清关服务，'
            '覆盖 FOB / CIF / DAP / DDP 全条款履约，蒙巴萨—内罗毕走廊门到门交付。',
    'keywords': '非快达,AFA,肯尼亚物流,东非货代,蒙巴萨清关,内罗毕,DDP,中国到肯尼亚,Africa Fast Arrival',

    'alt_href': '/en/', 'alt_label': 'EN',
    'nav': ['使命', '业务板块', '履约能力', '服务网络', '联系我们'],
    'nav_cta': '业务洽谈',
    'mail_subject': '非快达业务合作洽谈',

    'hero_kicker': 'Africa Fast Arrival',
    'hero_h1': '连接非洲<br>驱动未来',
    'hero_sub': '中国 — 东非全链条物流与清关服务',
    'hero_en': 'Fast Movement · Certain Arrival · Africa Connected',
    'hero_btn1': '业务洽谈',
    'hero_btn2': '了解业务板块',

    'mission_kicker': 'Our Mission',
    'mission_big': '让每一票货<br><em>确定地抵达</em>',
    'mission_p1': '非快达（AFRICA FAST ARRIVAL）取「非洲快速达到」之意。我们把中国到东非这条链路上分散的环节——'
                  '订舱、报关、干线、清关、内陆运输与末端交付——收进一张单子、一个责任方，'
                  '客户不必再在多个供应商之间反复协调与追问。',
    'mission_p2': '物流的价值不在报价单上最低的那个数字，而在于货真的到了、按时到了、成本是可预期的。',

    'svc_kicker': 'Business Segments',
    'svc_h2': '业务板块',
    'svc_lede': '围绕中国—东非贸易的完整链条布局，海空双通道、门到门交付。',
    'services': [
        ('sea', '海运', '整柜与拼箱，中国主要港口至蒙巴萨，含订舱、拖车、报关与目的港操作。'),
        ('air', '空运', '时效敏感与高价值货物，中国至内罗毕的空运通道与机场清关交付。'),
        ('customs', '清关', '本地清关团队处理申报、查验、税费与放行，以合规为前提。'),
        ('land', '内陆运输', '蒙巴萨—内罗毕走廊干线运输，车队资源与全程节点跟踪。'),
        ('warehouse', '仓储与集货', '国内集货与目的地仓储中转，拆并柜、暂存与分拨。'),
        ('lastmile', '末端派送', '内罗毕及周边城市送货到门，交付节点回传，签收可追溯。'),
        ('crossborder', '跨境延伸', '以肯尼亚为枢纽，向东非共同体（EAC）邻国延伸的跨境运输安排。'),
        ('platform', '数字平台', '下单、报价、单证与全程进度在线可查，AI 原生的运营与客服支撑。'),
    ],

    'cap_kicker': 'Full-Term Fulfillment',
    'cap_h2': '全条款履约<br>海空双通道',
    'cap_lede': '按客户实际需要承接 FOB / CIF / DAP / DDP 各类贸易条款，而不是只做其中最省事的一段。'
                'DDP 项下由我们统一安排运输、清关与税费代缴，客户拿到的是一个确定的到岸成本。',
    'cap_tags': ['FOB', 'CIF', 'DAP', 'DDP 门到门', '海运', '空运'],
    'cap_alt': '空运货物装载',

    'ops_kicker': 'Operations',
    'ops_h2': '把每个节点<br>握在自己手里',
    'ops_lede': '仓库、堆场、清关现场与调度中心，是同一套流程的不同环节。我们在关键节点上留人、留数据，'
                '让异常在发生时就被看见，而不是等客户来问。',
    'ops_tags': ['节点可视', '异常预警', '单证在线', '责任到人'],
    'ops_alt': '仓储作业现场',

    'net_kicker': 'Network',
    'net_h2': '服务网络',
    'net_lede': '以蒙巴萨—内罗毕走廊为主轴，向东非腹地延伸。',
    'network': [
        ('中国', '华南、华东主要港口与机场集货出运'),
        ('蒙巴萨', '东非门户港，海运到港、清关与拖车'),
        ('内罗毕', '业务与交付中心，空运清关、仓储与末端派送'),
        ('东非共同体', '向邻国延伸的跨境陆运安排'),
    ],
    'net_alt': '配送车队与场站',

    'con_kicker': 'Contact',
    'con_h2': '业务洽谈',
    'con_lede': '货量询价、线路方案、渠道与仓配合作，都可以直接写信给我们。',
    'con_lbl1': 'Business Enquiry', 'con_note1': '工作日 24 小时内回复',
    'con_lbl2': 'Company', 'con_note2': '非快达',
    'con_lbl3': 'Coverage', 'con_val3': '中国 · 蒙巴萨 · 内罗毕', 'con_note3': '东非共同体跨境延伸',
    'con_btn': '发送邮件',

    'foot_tagline': '非快达 · 连接非洲，驱动未来',
    'foot_note': '本站部分图片为品牌视觉应用效果图，仅用于形象展示。',
    'foot_copy': '© 2026 AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED. All rights reserved.',
}

EN = {
    'lang': 'en',
    'locale': 'en_US',
    'title': 'AFA · China–East Africa End-to-End Freight & Customs',
    'desc': 'AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED (AFA): end-to-end sea and air freight, customs clearance '
            'and door delivery between China and East Africa, across FOB / CIF / DAP / DDP terms on the '
            'Mombasa–Nairobi corridor.',
    'keywords': 'AFA, Africa Fast Arrival, Kenya freight forwarder, Mombasa customs clearance, Nairobi logistics, '
                'DDP China to Kenya, East Africa freight, air freight Kenya',

    'alt_href': '/', 'alt_label': '中文',
    'nav': ['Mission', 'Services', 'Capability', 'Network', 'Contact'],
    'nav_cta': 'Get in touch',
    'mail_subject': 'AFA business enquiry',

    'hero_kicker': 'Africa Fast Arrival',
    'hero_h1': 'Connecting Africa<br>Driving the Future',
    'hero_sub': 'End-to-end freight and customs between China and East Africa',
    'hero_en': 'Fast Movement · Certain Arrival · Africa Connected',
    'hero_btn1': 'Get in touch',
    'hero_btn2': 'Our services',

    'mission_kicker': 'Our Mission',
    'mission_big': 'Every shipment<br><em>arrives as promised</em>',
    'mission_p1': 'AFA stands for Africa Fast Arrival. We take the steps that are normally split across a chain of '
                  'suppliers — booking, export declaration, main leg, customs clearance, inland haulage and final '
                  'delivery — and put them on one order, under one accountable party. No more chasing four vendors '
                  'for one container.',
    'mission_p2': 'The value of logistics is not the lowest number on a quotation. It is that the cargo actually '
                  'arrives, arrives on time, and costs what you were told it would cost.',

    'svc_kicker': 'Business Segments',
    'svc_h2': 'What we do',
    'svc_lede': 'Built around the full China–East Africa trade lane: sea and air, door to door.',
    'services': [
        ('sea', 'Sea Freight', 'FCL and LCL from major Chinese ports to Mombasa, including booking, haulage, export '
                               'declaration and destination handling.'),
        ('air', 'Air Freight', 'Time-critical and high-value cargo from China to Nairobi, with airport clearance and '
                               'delivery.'),
        ('customs', 'Customs Clearance', 'A local clearance team handles declaration, inspection, duties and release '
                                         '— compliance first.'),
        ('land', 'Inland Transport', 'Line-haul along the Mombasa–Nairobi corridor, with fleet capacity and '
                                     'milestone tracking.'),
        ('warehouse', 'Warehousing', 'Consolidation in China and transit storage at destination: stuffing, '
                                     'de-stuffing, short-term storage and distribution.'),
        ('lastmile', 'Last-mile Delivery', 'Door delivery in Nairobi and surrounding towns, with delivery milestones '
                                           'and traceable proof of receipt.'),
        ('crossborder', 'Cross-border', 'Onward movement from the Kenyan hub into neighbouring East African '
                                        'Community (EAC) markets.'),
        ('platform', 'Digital Platform', 'Orders, quotes, documents and live status online — supported by an '
                                         'AI-native operations and service team.'),
    ],

    'cap_kicker': 'Full-Term Fulfillment',
    'cap_h2': 'Every Incoterm<br>Sea and air',
    'cap_lede': 'We take on FOB, CIF, DAP and DDP as the customer actually needs them, not just the easiest leg. '
                'Under DDP we arrange transport, clearance and duty payment ourselves, so what you get is a landed '
                'cost you can rely on.',
    'cap_tags': ['FOB', 'CIF', 'DAP', 'DDP door-to-door', 'Sea', 'Air'],
    'cap_alt': 'Air cargo loading',

    'ops_kicker': 'Operations',
    'ops_h2': 'Every node<br>in our own hands',
    'ops_lede': 'Warehouse, yard, clearance desk and control room are stages of one process, not separate companies. '
                'We keep people and data at the nodes that matter, so exceptions surface when they happen — not when '
                'the customer asks.',
    'ops_tags': ['Milestone visibility', 'Exception alerts', 'Documents online', 'Named ownership'],
    'ops_alt': 'Warehouse operations',

    'net_kicker': 'Network',
    'net_h2': 'Where we operate',
    'net_lede': 'Anchored on the Mombasa–Nairobi corridor, extending into the East African interior.',
    'network': [
        ('China', 'Consolidation and departure via major South and East China ports and airports'),
        ('Mombasa', 'East Africa gateway port: arrival, clearance and haulage'),
        ('Nairobi', 'Operations and delivery hub: air clearance, warehousing and last-mile'),
        ('EAC', 'Cross-border road movement into neighbouring markets'),
    ],
    'net_alt': 'Delivery fleet and depot',

    'con_kicker': 'Contact',
    'con_h2': 'Talk to us',
    'con_lede': 'Rate enquiries, lane solutions, agency and warehousing partnerships — write to us directly.',
    'con_lbl1': 'Business Enquiry', 'con_note1': 'We reply within one business day',
    'con_lbl2': 'Company', 'con_note2': 'AFA',
    'con_lbl3': 'Coverage', 'con_val3': 'China · Mombasa · Nairobi', 'con_note3': 'Extending across the EAC',
    'con_btn': 'Send email',

    'foot_tagline': 'AFA · Connecting Africa, Driving the Future',
    'foot_note': 'Some images on this site are brand application mock-ups, shown for identity purposes only.',
    'foot_copy': '© 2026 AFRICA FAST ARRIVAL DIGITAL TECHNOLOGY LIMITED. All rights reserved.',
}

LOCALES = {'zh': ZH, 'en': EN}
