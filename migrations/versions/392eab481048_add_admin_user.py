"""Add Admin user

Revision ID: 392eab481048
Revises: ba3b652ed3f0
Create Date: 2024-01-14 14:50:29.554369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "392eab481048"
down_revision = "ba3b652ed3f0"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        " INSERT INTO users (id, username, email, name, last_name) VALUES (1, 'admin', 'admin@admin.com', 'Admin', 'Admin')"
    )


def downgrade():
    op.execute(" DELETE FROM users WHERE username = 'admin' ")
