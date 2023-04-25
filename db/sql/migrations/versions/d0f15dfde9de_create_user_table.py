"""create user table

Revision ID: d0f15dfde9de
Revises: 
Create Date: 2023-04-25 15:25:31.868333

"""
from alembic import op
import sqlalchemy as sa
from db.sql.models import TableNames


# revision identifiers, used by Alembic.
revision = "d0f15dfde9de"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        TableNames.USERS.value,
        sa.Column("id", sa.UUID, primary_key=True),
        sa.Column("email", sa.Text, index=True),
        sa.Column("password", sa.Text, index=True),
        sa.Column("first_name", sa.Text),
        sa.Column("last_name", sa.Text),
        sa.Column("created_at", sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table(TableNames.USERS.value)
