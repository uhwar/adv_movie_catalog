import aiosqlite
import time

DB_PATH = "movies.db"

async def setup_db():
    try:
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    tconst TEXT PRIMARY KEY,
                    title_type TEXT NOT NULL,
                    primary_title TEXT NOT NULL,
                    original_title TEXT,
                    is_adult INTEGER DEFAULT 0,
                    start_year INTEGER,
                    end_year INTEGER,
                    runtime_minutes INTEGER,
                    genres TEXT,
                    average_rating REAL,
                    num_votes INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            await db.commit()