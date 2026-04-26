# AI-Assistant-sturcture 


ai-study-assistant/
│
├── app/
│   ├── main.py                # Flask app entry point
│   │
│   ├── routes/               # API endpoints
│   │   ├── chat_routes.py    # ask doubts
│   │   ├── planner_routes.py # study plan
│   │   └── user_routes.py    # progress
│   │
│   ├── services/             # core logic (brain)
│   │   ├── llm_service.py    # OpenAI / local LLM
│   │   ├── doubt_solver.py   # Q&A logic
│   │   ├── planner_service.py# study plan generator
│   │   └── progress_service.py # track progress
│   │
│   ├── models/               # database tables
│   │   ├── user.py
│   │   ├── progress.py
│   │   └── chat_history.py
│   │
│   ├── db/                   # database setup
│   │   ├── database.py       # SQLite connection
│   │   └── init_db.py
│   │
│   ├── utils/                # helper functions
│   │   ├── prompts.py        # AI prompts
│   │   └── helpers.py
│
├── data/                     # optional notes/files
│
├── requirements.txt
├── .env
└── README.md
