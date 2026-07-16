Nivi/
├── main.py                 # (Orchestrator) حلقة التشغيل الرئيسية ومدير العمليات
├── router.py               # (Brain Router) موجه المهام (يقرر من يفعل ماذا)
├── registry.py             # (Tool Registry) تسجيل الأدوات والإضافات ديناميكياً
├── config.json             # الإعدادات العامة للنظام
├── .env                    # المتغيرات السرية (API Keys, Tokens)
├── requirements.txt        # المكتبات المطلوبة
├── README.md               # توثيق المشروع
├── .gitignore              # ملفات تجاهل الـ Git
│
├── data/                   # (Data Storage)
│   ├── nivi.db             # قاعدة بيانات SQLite (الذاكرة طويلة المدى)
│   ├── cache/              # ملفات مؤقتة
│   ├── models/             # ملفات النماذج المحلية (Ollama GGUF)
│   └── uploads/            # الملفات المرفوعة من المستخدم
│
├── logs/                   # (System Logs) سجلات الأخطاء والعمليات
│
├── events/                 # (Event Bus) نظام الأحداث (المراسلات بين الأجزاء)
│   ├── __init__.py
│   └── bus.py              # الموزع المركزي للأحداث (Pub/Sub)
│
├── scheduler/              # (Automation) المهام المجدولة
│   ├── __init__.py
│   └── tasks.py            # المهام التي تعمل في الخلفية (Cron jobs)
│
├── memory/                 # (Memory Unit) العقل المستمر
│   ├── __init__.py
│   ├── core.py             # الذاكرة الأساسية (الهوية والقواعد)
│   ├── short_term.py       # الذاكرة القصيرة (سياق المحادثة)
│   └── long_term.py        # الذاكرة الطويلة (SQLite Interface)
│
├── modules/                # (Core Logic) الذكاء والمنطق
│   ├── __init__.py
│   ├── ai.py               # المحرك المفكر (Ollama/LLM Integration)
│   ├── voice.py            # محرك تحويل النص لصوت والعكس
│   └── social.py           # منطق التواصل الاجتماعي
│
├── devices/                # (Hardware/External Tools) الأدوات والأجهزة
│   ├── __init__.py
│   ├── linux.py            # أوامر النظام
│   ├── browser.py          # أدوات المتصفح
│   ├── files.py            # التعامل مع الملفات
│   ├── screenshot.py       # تصوير الشاشة
│   └── terminal.py         # تنفيذ أوامر التيرمينال
│
├── plugins/                # (Dynamic Extensibility) الإضافات الخارجية
│   ├── __init__.py
│   ├── loader.py           # محمل الإضافات
│   ├── manifest.py         # تعريف الإضافات
│   └── installed/          # الإضافات المثبتة
│
├── network/                # (API & Communication)
│   ├── __init__.py
│   ├── websocket.py        # للتواصل اللحظي (Real-time)
│   ├── protocol.py         # بروتوكولات الاتصال
│   └── auth.py             # التحقق من الهوية والأمان
│
└── frontend/               # (UI Layer) الواجهة (مستقبلية)
    └── README.md           # توثيق تقنيات الواجهة (Next.js + TS + Tailwind)
