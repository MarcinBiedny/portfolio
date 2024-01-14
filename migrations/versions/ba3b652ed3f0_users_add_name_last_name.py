"""Users add name, last_name

Revision ID: ba3b652ed3f0
Revises: ed298897b06c
Create Date: 2024-01-14 11:54:53.115685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ba3b652ed3f0"
down_revision = "ed298897b06c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("name", sa.String(length=80), nullable=False))
        batch_op.add_column(
            sa.Column("last_name", sa.String(length=80), nullable=False)
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_column("last_name")
        batch_op.drop_column("name")

    # ### end Alembic commands ###
