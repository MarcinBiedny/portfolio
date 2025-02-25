"""Add 'password' column to 'users'

Revision ID: c2aaf46febc3
Revises: 392eab481048
Create Date: 2024-07-14 10:28:58.369095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c2aaf46febc3"
down_revision = "ba3b652ed3f0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("password", sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("password")

    # ### end Alembic commands ###
