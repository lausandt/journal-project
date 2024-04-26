from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "active" BOOL NOT NULL  DEFAULT True;
        ALTER TABLE "user" ADD "superuser" BOOL NOT NULL  DEFAULT False;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "active";
        ALTER TABLE "user" DROP COLUMN "superuser";"""
