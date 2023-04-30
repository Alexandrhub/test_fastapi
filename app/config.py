from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    @property
    def DATABASE_URL(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:"
                f"{self.DB_PASS}@{self.DB_HOST}:"
                f"{self.DB_PORT}/{self.DB_NAME}"
                )
    

    class Config:
        env_file = '.env'

settings = Settings()

