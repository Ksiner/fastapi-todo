"""uniq emails on users table

Revision ID: 0170694074d9
Revises: 370d17c54516
Create Date: 2023-04-27 17:53:09.312719

"""
from alembic import op
import sqlalchemy as sa
from db.sql.core import TableNames


# revision identifiers, used by Alembic.
revision = "0170694074d9"
down_revision = "370d17c54516"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("uniq_emails", TableNames.USERS.value, ["email"])


def downgrade() -> None:
    op.drop_constraint("uniq_emails", TableNames.USERS.value)
