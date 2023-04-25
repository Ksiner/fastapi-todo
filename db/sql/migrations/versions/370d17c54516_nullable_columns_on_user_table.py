"""nullable columns on user table

Revision ID: 370d17c54516
Revises: d0f15dfde9de
Create Date: 2023-04-25 16:05:44.492430

"""
from alembic import op
import sqlalchemy as sa
from db.sql.core import TableNames


# revision identifiers, used by Alembic.
revision = "370d17c54516"
down_revision = "d0f15dfde9de"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(TableNames.USERS.value, "id", nullable=False)
    op.alter_column(TableNames.USERS.value, "email", nullable=False)
    op.alter_column(TableNames.USERS.value, "password", nullable=False)
    op.alter_column(TableNames.USERS.value, "first_name", nullable=True)
    op.alter_column(TableNames.USERS.value, "last_name", nullable=True)
    op.alter_column(TableNames.USERS.value, "created_at", nullable=False)


def downgrade() -> None:
    pass
