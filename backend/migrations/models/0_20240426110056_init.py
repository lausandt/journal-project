from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "email" VARCHAR(128) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "creadate" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "modate" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "entry" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "description" TEXT NOT NULL,
    "creadate" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "modate" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "regularentry" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(64) NOT NULL,
    "description" TEXT NOT NULL,
    "creadate" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "modate" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP,
    "period" VARCHAR(11) NOT NULL,
    "author_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "regularentry"."period" IS 'weekly: Weekly\nfourweekly: Four weekly\nmonthly: Montly\nquarterly: Quarterly\nyearly: Yearly';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
