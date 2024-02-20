from asteroids.entities.score import Score

from sqlite3 import connect

from typing import Optional

from datetime import datetime

class ScoresRepository:
    def __init__(self):
        self.database = "./scores.db"
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connect(self.database)
        self.cursor = self.connection.cursor()

        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                name TEXT PRIMARY KEY,
                value INT NOT NULL,
                updatedAt TEXT NOT NULL
            );
        """)
        self.connection.commit()

        return self
         
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cursor.close()
        self.connection.close()

    def create(self, name: str, newScore: int) -> None:
        score = self.findOne(name)

        if not score: 
            score = Score(name, newScore)

            self.cursor.execute(
                "INSERT INTO scores VALUES(?, ?, ?);",
                (score.name, score.value, score.updatedAt)
            )
            self.connection.commit()

            return
        
        score.value = newScore
        score.updatedAt = datetime.now()
        
        self.cursor.execute(
            """
                UPDATE scores 
                SET 
                    value = ?, 
                    updatedAt = ? 
                WHERE name = ?;
            """,
            (score.value, score.updatedAt, score.name)
        )
        self.connection.commit()

    def findOne(self, name: str) -> Optional[Score]:
        result = self.cursor.execute(
            "SELECT * FROM scores WHERE name = ?;", 
            (name,)
        )

        row = result.fetchone()

        if not row:
            return None
        
        return Score(row[0], row[1], row[2])

    def getRanking(self) -> list[Score]:
        ranking = []

        scores = self.cursor.execute(
            "SELECT * FROM scores LIMIT 10 ORDER BY value ASC;"
        )

        for score in scores:
            ranking.append(
                Score(
                    name = score[0], 
                    value = score[1], 
                    updatedAt = score[2]
                )
            )

        return ranking