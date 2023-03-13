"""Feat: Added genre column

Revision ID: 2bb5e4d53495
Revises: d1320367b78c
Create Date: 2023-03-13 09:39:34.738074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bb5e4d53495'
down_revision = 'd1320367b78c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genre', sa.String(length=255), nullable=True))
        batch_op.alter_column('release_date',
               existing_type=sa.DATE(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.alter_column('release_date',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.drop_column('genre')

    # ### end Alembic commands ###